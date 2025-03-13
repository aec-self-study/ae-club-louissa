import uuid
import random
import datetime
import csv
import os
from faker import Faker
import pandas as pd
import numpy as np

faker = Faker()

N_VISITORS = 870242


# Reusable function to remove files
def rm_file(filename):
    try:
        os.remove(filename)
    except OSError:
        pass


# Function to create CSV files with headers
def create_csv(file_path, header):
    with open(file_path, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        writer.writerow(header)


# Initialize the CSV files
def initialize_csv_files():
    files = {
        "data/orders.csv": ["id", "created_at", "customer_id", "total", "address", "state", "zip"],
        "data/order_items.csv": ["id", "order_id", "product_id"],
        "data/customers.csv": ["id", "name", "email"],
        "data/pageviews.csv": ["id", "visitor_id", "device_type", "timestamp", "page", "customer_id"]
    }

    if not os.path.exists("data"):
        os.makedirs("data")

    for file_path, header in files.items():
        rm_file(file_path)
        create_csv(file_path, header)


# Prepare products data
products = pd.read_csv("products_seed.csv")
products["created_at"] = datetime.datetime(2021, 1, 1)
product_pages = ["product-" + str(i) for i in products["id"]]
pages = ["/", "about", "shopping-cart"] + product_pages
products.to_csv(
    "data/products.csv",
    columns=["id", "name", "category", "created_at"],
    index=False,
    sep="\t",
)


# Function to get price at a specific time for a product
def price_at_time(product_id, dtime, product_prices):
    id_prices = product_prices[product_prices["product_id"] == product_id]
    row = id_prices[(dtime >= id_prices["created_at"]) & (dtime < id_prices["ended_at"])]
    return row["price"].values[0]


# Function to generate random timestamp between two dates
def rand_timestamp(start_date, end_date):
    visit_date = start_date + datetime.timedelta(
        np.random.randint(0, (end_date - start_date).days)
    )
    rtime = int(random.random() * 86400)
    visit_timestamp = visit_date + datetime.timedelta(seconds=rtime)
    return visit_timestamp


# Function to generate a fake address
def get_fake_address():
    sa = faker.street_address()
    state = faker.state()
    zc = faker.zipcode()
    return {"street": sa, "state": state, "zc": zc}


# Function to record a page view
def record_pageview(visitor_id, device_type, timestamp, page, customer_id=None):
    with open("data/pageviews.csv", "a") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        writer.writerow(
            [uuid.uuid4(), visitor_id, device_type, timestamp, page, customer_id]
        )


# Function to record a new customer
def record_customer(customer_id):
    with open("data/customers.csv", "a") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        writer.writerow(
            [
                customer_id,
                faker.name(),
                faker.email(),
            ]
        )


# Function to record an order
def record_order(order_id, timestamp, customer_id, address, order_total):
    with open("data/orders.csv", "a") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        writer.writerow(
            [
                order_id,
                timestamp,
                customer_id,
                order_total,
                address["street"],
                address["state"],
                address["zc"],
            ]
        )


# Function to record an order item
def record_order_item(order_id, product_id):
    with open("data/order_items.csv", "a") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        writer.writerow([uuid.uuid4(), order_id, product_id])


# Function to create product prices
def generate_product_prices(products, start_date, end_date):
    product_prices_array = []

    for index, row in products.iterrows():
        product_id = row["id"]
        price = row["starting_price"]
        price_change_date = start_date

        while price_change_date <= end_date:
            price += random.randint(-3, 3)

            price_change_record = {
                "product_id": product_id,
                "price": price,
                "created_at": price_change_date,
                "ended_at": None,
            }

            price_change_date = rand_timestamp(
                start_date=price_change_date,
                end_date=price_change_date + datetime.timedelta(days=300),
            )

            price_change_record["ended_at"] = min(price_change_date, end_date)

            product_prices_array.append(price_change_record)

    product_prices = pd.DataFrame(product_prices_array)
    product_prices.insert(0, "id", None)
    product_prices["id"] = product_prices.index + 1

    product_prices.to_csv("data/product_prices.csv", index=False, sep="\t")

    return product_prices


# Function to process visits for visitors
def process_visits(products, pages, product_prices):
    for i in range(N_VISITORS):
        device_visitor_d = {}
        num_visits = np.random.poisson(2) + 1
        customer_device = random.sample(device_os, len(device_os))

        for j in range(num_visits):
            num_pages = np.random.poisson() + 1
            visit_start = rand_timestamp(start_date, end_date)
            visit_id = uuid.uuid4()

            device_type = np.random.choice(customer_device, p=device_p)
            visitor_id = device_visitor_d.get(device_type, uuid.uuid4())
            device_visitor_d[device_type] = visitor_id

            for k in range(num_pages):
                timestamp = visit_start + datetime.timedelta(seconds=np.random.poisson(15))
                page = random.sample(pages, 1)[0]
                record_pageview(visitor_id, device_type, timestamp, page, customer_id)

            checkout = np.random.choice([True, False], p=[cvr, 1 - cvr])
            if checkout:
                if not customer_id:
                    customer_id = uuid.uuid4()
                    record_customer(customer_id)

                timestamp = timestamp + datetime.timedelta(seconds=np.random.poisson(15))
                page = "shopping-cart"
                record_pageview(visitor_id, device_type, timestamp, page, customer_id)
                timestamp = timestamp + datetime.timedelta(seconds=np.random.poisson(15))
                page = "checkout"
                record_pageview(visitor_id, device_type, timestamp, page, customer_id)
                timestamp = timestamp + datetime.timedelta(seconds=np.random.poisson(15))
                page = "order-confirmation"
                record_pageview(visitor_id, device_type, timestamp, page, customer_id)

                items_purchased = np.random.poisson() + 1
                items = np.random.choice(products["id"], items_purchased)

                order_id = uuid.uuid4()
                order_total = 0
                for it in items:
                    order_total += price_at_time(it, visit_start, product_prices)
                    record_order_item(order_id, it)

                if address:
                    if random.random() < p_change_address:
                        address = get_fake_address()
                else:
                    address = get_fake_address()

                record_order(order_id, timestamp, customer_id, address, order_total)
