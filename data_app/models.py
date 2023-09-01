from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    creation_time = Column(DateTime)
    email = Column(String)

# Store model
class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    customer_sold_to = Column(String)
    original_store_code = Column(String)
    store_name = Column(String)
    channel = Column(String)
    ktz = Column(Boolean)
    state = Column(String)
    city = Column(String)

# Customer model
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    customer_sold_to = Column(String)
    group_name = Column(String)
    banner_name = Column(String)
    business_model = Column(String)
    customer_channel = Column(String)
    customer_segmentation = Column(String)
    whs_channel = Column(String)

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    event_name = Column(String)
    time_stamp = Column(DateTime)

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    country_name = Column(String)

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True)
    campaign_name = Column(String)
    campaign_start_date = Column(DateTime)
    campaign_end_date = Column(DateTime)
    article_code = Column(String)

class Target(Base):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True)
    customer_sold_to = Column(String)
    begin_date = Column(DateTime)
    end_date = Column(DateTime)
    target_local_currency = Column(String)

class CustomerLayout(Base):
    __tablename__ = "customer_layouts"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    store_code = Column(String)
    article_code = Column(String)
    size = Column(String)
    net_sales = Column(Float)
    total_markdown = Column(Float)
    net_quantity = Column(Integer)
    stock_quantity = Column(Integer)
    whs_price = Column(Float)
    invoice_value = Column(Float)