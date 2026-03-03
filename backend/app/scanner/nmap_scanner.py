import nmap
import json
from datetime import datetime
from app.core.database import SessionLocal
from app.models.models import ScanJob, Asset, Service

def run_scan(job_id: int, target: str):
    db = SessionLocal()
    job = db.query(ScanJob).filter_by(id=job_id).first()
    if not job:
        db.close()
        return

    job.status = "running"
    db.commit()

    try:
        nm = nmap.PortScanner()
        # Ping sweep + fast port scan for defensive footprinting
        nm.scan(hosts=target, arguments='-sn')
        
        # After finding live hosts, do a quick port scan
        live_hosts = nm.all_hosts()
        if live_hosts:
            host_list = " ".join(live_hosts)
            # basic service detection on top ports
            nm.scan(hosts=host_list, arguments='-sV --top-ports 100')
        
        for host in nm.all_hosts():
            asset = db.query(Asset).filter_by(ip=host).first()
            if not asset:
                asset = Asset(
                    ip=host,
                    hostname=nm[host].hostname() if nm[host].hostname() else "",
                    first_seen=datetime.utcnow()
                )
                db.add(asset)
                db.commit()
                db.refresh(asset)
            else:
                asset.last_seen = datetime.utcnow()
                db.commit()

            # Add services
            if 'tcp' in nm[host]:
                for port, data in nm[host]['tcp'].items():
                    svc = db.query(Service).filter_by(asset_id=asset.id, port=port, protocol="tcp").first()
                    if not svc:
                        svc = Service(
                            asset_id=asset.id,
                            port=port,
                            protocol="tcp",
                            product=data.get('product', ''),
                            version=data.get('version', ''),
                            banner=data.get('extrainfo', ''),
                            first_seen=datetime.utcnow()
                        )
                        db.add(svc)
                    else:
                        svc.product = data.get('product', '')
                        svc.version = data.get('version', '')
                        svc.banner = data.get('extrainfo', '')
                        svc.last_seen = datetime.utcnow()
                db.commit()

        job.status = "completed"
        job.stats_json = json.dumps({"hosts_scanned": len(nm.all_hosts())})
        
    except Exception as e:
        job.status = "failed"
        job.stats_json = json.dumps({"error": str(e)})
        
    finally:
        job.finished_at = datetime.utcnow()
        db.commit()
        db.close()
