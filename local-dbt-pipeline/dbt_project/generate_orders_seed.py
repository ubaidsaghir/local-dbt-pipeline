import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# Output folder and file
seed_folder = Path("seeds")
seed_folder.mkdir(exist_ok=True)

output_file = seed_folder / "orders.csv"

# Sample values
customer_names = [
    "Ali", "Sara", "Ahmed", "Ayesha", "Bilal", "Hina", "Usman", "Fatima",
    "Zain", "Maham", "Hamza", "Iqra", "Danish", "Sana", "Omar", "Noor",
    "Taha", "Laiba", "Hassan", "Kiran"
]

product_categories = [
    "Electronics",
    "Clothing",
    "Home",
    "Beauty",
    "Sports",
    "Books",
    "Toys",
    "Groceries"
]

statuses = [
    "Completed",
    "Pending",
    "Cancelled",
    "Returned"
]

start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 4, 30)

date_range_days = (end_date - start_date).days

total_rows = 10000

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow([
        "order_id",
        "customer_id",
        "customer_name",
        "product_category",
        "quantity",
        "unit_price",
        "order_date",
        "status"
    ])

    for order_id in range(1, total_rows + 1):
        customer_id = random.randint(1001, 3000)
        customer_name = random.choice(customer_names)
        product_category = random.choice(product_categories)
        quantity = random.randint(1, 10)
        unit_price = round(random.uniform(50, 2000), 2)
        random_days = random.randint(0, date_range_days)
        order_date = (start_date + timedelta(days=random_days)).date()
        status = random.choice(statuses)

        writer.writerow([
            order_id,
            customer_id,
            customer_name,
            product_category,
            quantity,
            unit_price,
            order_date,
            status
        ])

print(f"Successfully generated {total_rows} rows in {output_file}")