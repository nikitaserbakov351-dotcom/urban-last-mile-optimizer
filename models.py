from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    plate_number = Column(String, unique=True, nullable=False)
    capacity = Column(Float, nullable=False)
    vehicle_type = Column(String)  # truck, van, bike
    status = Column(String, default='available') # available, in_transit, maintenance
    
    orders = relationship('Order', back_populates='vehicle')
    routes = relationship('Route', back_populates='vehicle')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    address = Column(String)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    time_window_start = Column(DateTime)
    time_window_end = Column(DateTime)
    status = Column(String, default='pending') # pending, assigned, delivered, cancelled
    
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship('Vehicle', back_populates='orders')

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    location_type = Column(String) # warehouse, terminal, office

class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    date = Column(DateTime, default=datetime.utcnow)
    total_distance = Column(Float)
    optimized_order_ids = Column(String) # Store as comma-separated IDs or JSON
    
    vehicle = relationship('Vehicle', back_populates='routes')

# Database connection setup
engine = create_engine('sqlite:///logistics.db')
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
