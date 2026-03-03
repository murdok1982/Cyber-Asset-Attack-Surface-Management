from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True, index=True)
    hostname = Column(String, nullable=True)
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)
    tags = Column(String, default="")  # Comma separated
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=True)
    
    services = relationship("Service", back_populates="asset")

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    port = Column(Integer)
    protocol = Column(String)  # tcp/udp
    product = Column(String, nullable=True)
    version = Column(String, nullable=True)
    banner = Column(Text, nullable=True)
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)
    
    asset = relationship("Asset", back_populates="services")
    images = relationship("ImageCapture", back_populates="service")

class ScanJob(Base):
    __tablename__ = "scan_jobs"

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String)
    status = Column(String, default="pending")  # pending, running, completed, failed
    started_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)
    stats_json = Column(Text, nullable=True)

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lat = Column(String)
    lon = Column(String)
    notes = Column(Text, nullable=True)

class ImageCapture(Base):
    __tablename__ = "image_captures"
    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey("services.id"))
    path = Column(String)  # Local file path
    labels_json = Column(Text, nullable=True)  # Output from ViT
    created_at = Column(DateTime, default=datetime.utcnow)

    service = relationship("Service", back_populates="images")
