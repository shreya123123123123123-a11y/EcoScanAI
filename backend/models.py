from sqlalchemy import Column, Integer, String, Float

from database import Base



class Product(Base):

    __tablename__ = "products"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    barcode = Column(
        String,
        unique=True,
        index=True
    )


    name = Column(
        String
    )


    carbon = Column(
        Float
    )
    category = Column(
        String
    )


    water = Column(
        Float
    )


    packaging = Column(
        String
    )


    sugar = Column(
        Float
    )


    protein = Column(
        Float
    )


    price = Column(
        Float
    )

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    barcode = Column(String, unique=True)

    name = Column(String)

    carbon = Column(Float)
    category = Column(String)

    water = Column(Float)

    packaging = Column(String)

    sugar = Column(Float)

    protein = Column(Float)

    price = Column(Float)