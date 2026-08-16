from database import SessionLocal
from models import Product


db = SessionLocal()


products = db.query(Product).all()


for product in products:

    print(
        product.name,
        "----",
        product.category
    )


db.close()