from database import SessionLocal
from models import Product


db = SessionLocal()


products = db.query(Product).all()


for p in products:

    print(
        p.name,
        "----",
        p.category,
        "----",
        p.price
    )


db.close()