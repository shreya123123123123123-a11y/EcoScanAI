import csv

from database import SessionLocal
from models import Product



db = SessionLocal()



with open("../datasets/products.csv","r") as file:

    reader = csv.DictReader(file)


    for row in reader:


        product = Product(

    barcode=row["barcode"],

    name=row["name"],

    category=row["category"],

    carbon=row["carbon"],

    water=row["water"],

    packaging=row["packaging"],

    sugar=row["sugar"],

    protein=row["protein"],
    price=row["price"]

)


        db.add(product)



db.commit()


db.close()


print("Products imported successfully")