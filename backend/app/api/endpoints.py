from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List, Dict

from app.core.database import get_db
from app.models import models
from app.scanner.nmap_scanner import run_scan

router = APIRouter()

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    assets_count = db.query(models.Asset).count()
    services_count = db.query(models.Service).count()
    scans_count = db.query(models.ScanJob).count()
    return {
        "total_assets": assets_count,
        "total_services": services_count,
        "total_scans": scans_count
    }

@router.get("/assets")
def list_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Asset).offset(skip).limit(limit).all()

@router.post("/scans")
def trigger_scan(target: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # Basic validation to ensure they are scanning a valid internal subnet/IP
    # For now, we trust the input per the defensive MVP agreement.
    job = models.ScanJob(target=target, status="pending")
    db.add(job)
    db.commit()
    db.refresh(job)
    
    # Run scan in background
    background_tasks.add_task(run_scan, job.id, target)
    return {"message": "Scan triggered", "job_id": job.id}

@router.get("/scans")
def list_scans(db: Session = Depends(get_db)):
    return db.query(models.ScanJob).order_by(models.ScanJob.id.desc()).all()

@router.get("/search")
def search_services(query: str, db: Session = Depends(get_db)):
    # Basic Shodan-like search (e.g. "port:80" or "service:http")
    # For a real implementation, we'd parse the DSL. Here we do a basic LIKE.
    results = db.query(models.Service).join(models.Asset)
    
    if "port:" in query:
        port = query.split("port:")[1].split(" ")[0]
        try:
            results = results.filter(models.Service.port == int(port))
        except ValueError:
            pass
            
    if "service:" in query:
        proto = query.split("service:")[1].split(" ")[0]
        results = results.filter(models.Service.product.ilike(f"%{proto}%"))
        
    return results.limit(100).all()
