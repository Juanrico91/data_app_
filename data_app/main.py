from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from database import engine
from models import User, Store, Customer, Log, Country, Campaign, Target, CustomerLayout

app = FastAPI()

# Temporary storage for data (in-memory)
users_db = []
stores_db = []
customers_db = []
logs_db = []
countries_db = []
campaigns_db = []
targets_db = []
layouts_db = []
market_share_db = []

session = Session(engine)


class User(BaseModel):
    User_ID: int
    creation_time: datetime
    email: str

class MarketShare(BaseModel):
    customer_id: int
    market_share_percentage: bool

class Store(BaseModel):
    id: int
    customer_sold_to: str
    original_store_code: str
    store_name: str
    channel: str
    ktz: bool
    state: str
    city: str

class Customer(BaseModel):
    id: int
    customer_sold_to: str
    group_name: str
    banner_name: str
    business_model: str
    customer_channel: str
    customer_segmentation: str
    whs_channel: str

class Log(BaseModel):
    log_id: int
    event_name: str
    time_stamp: datetime

class Country(BaseModel):
    country_id: int
    country_name: str

class Campaign(BaseModel):
    campaign_id: int
    campaign_name: str
    campaign_start_date: datetime
    campaign_end_date: datetime
    article_code: str

class Target(BaseModel):
    target_id: int
    customer_sold_to: str
    begin_date: datetime
    end_date: datetime
    target_local_currency: str

class CustomerLayout(BaseModel):
    customer_layout_id: int
    date: datetime
    store_code: str
    article_code: str
    size: str
    net_sales: float
    total_markdown: float
    net_quantity: int
    stock_quantity: int
    whs_price: float
    invoice_value: float

@app.post("/create_user/")
def create_user(user: User):
    # Generate a unique User_ID (you might want to implement a more robust method)
    user.User_ID = len(users_db) + 1
    user.creation_time = datetime.now()

    users_db.append(user)
    return user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id <= 0 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    
    return users_db[user_id - 1]

@app.put("/update_user/{user_id}")
def update_user(user_id: int, updated_user: User):
    if user_id <= 0 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")

    users_db[user_id - 1] = updated_user
    return updated_user

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    if user_id <= 0 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = users_db.pop(user_id - 1)
    return {"message": f"User with User_ID {user_id} deleted", "deleted_user": deleted_user}

@app.post("/create_store/")
def create_store(store: Store):
    stores_db.append(store)
    return store

@app.get("/stores/{store_id}")
def get_store(store_id: int):
    if store_id <= 0 or store_id > len(stores_db):
        raise HTTPException(status_code=404, detail="Store not found")
    
    return stores_db[store_id - 1]

@app.post("/create_customer/")
def create_customer(customer: Customer):
    customers_db.append(customer)
    return customer

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    if customer_id <= 0 or customer_id > len(customers_db):
        raise HTTPException(status_code=404, detail="Customer not found")
    
    return customers_db[customer_id - 1]

@app.post("/create_log/")
def create_log(log: Log):
    logs_db.append(log)
    return log

@app.get("/logs/{log_id}")
def get_log(log_id: int):
    if log_id <= 0 or log_id > len(logs_db):
        raise HTTPException(status_code=404, detail="Log not found")

    return logs_db[log_id - 1]

@app.post("/create_country/")
def create_country(country: Country):
    countries_db.append(country)
    return country

@app.get("/countries/{country_id}")
def get_country(country_id: int):
    if country_id <= 0 or country_id > len(countries_db):
        raise HTTPException(status_code=404, detail="Country not found")

    return countries_db[country_id - 1]

@app.post("/create_campaign/")
def create_campaign(campaign: Campaign):
    campaigns_db.append(campaign)
    return campaign

@app.get("/campaigns/{campaign_id}")
def get_campaign(campaign_id: int):
    if campaign_id <= 0 or campaign_id > len(campaigns_db):
        raise HTTPException(status_code=404, detail="Campaign not found")

    return campaigns_db[campaign_id - 1]

@app.post("/create_target/")
def create_target(target: Target):
    targets_db.append(target)
    return target

@app.get("/targets/{target_id}")
def get_target(target_id: int):
    if target_id <= 0 or target_id > len(targets_db):
        raise HTTPException(status_code=404, detail="Target not found")

    return targets_db[target_id - 1]

@app.post("/create_layout/")
def create_layout(layout: CustomerLayout):
    layouts_db.append(layout)
    return layout

@app.get("/layouts/{layout_id}")
def get_layout(layout_id: int):
    if layout_id <= 0 or layout_id > len(layouts_db):
        raise HTTPException(status_code=404, detail="Customer Layout not found")

    return layouts_db[layout_id - 1]

@app.post("/create_market_share/")
def create_target(market_share: MarketShare):
    targets_db.append(market_share)
    return market_share

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)