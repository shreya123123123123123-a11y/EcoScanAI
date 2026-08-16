from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal

from models import Product

from eco_score import calculate_eco_score

from health_score import calculate_health_score

from recommendation import get_recommendation, get_alternatives

from gemini import generate_explanation

from ml_prediction import predict_eco_category



app = FastAPI()
app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)



@app.get("/")
def home():

    return {
        "message": "EcoScan AI API Running"
    }





@app.get("/product/{barcode}")
def get_product(barcode: str):


    db = SessionLocal()



    # Find product using barcode

    product = db.query(Product).filter(
        Product.barcode == barcode
    ).first()



    if product is None:

        db.close()

        return {
            "message": "Product not found"
        }




    # -----------------------------
    # Calculate Eco Score
    # -----------------------------

    eco_score = calculate_eco_score(

        product.carbon,

        product.water,

        product.packaging

    )





    # -----------------------------
    # Calculate Health Score
    # -----------------------------

    health_score = calculate_health_score(

        product.sugar,

        product.protein

    )





    # -----------------------------
    # ML Eco Category Prediction
    # -----------------------------

    eco_category = predict_eco_category(

        product.carbon,

        product.water,

        product.packaging,

        product.sugar,

        product.protein

    )





    # -----------------------------
    # Recommendation
    # -----------------------------

    recommendation = get_recommendation(

        health_score,

        eco_score

    )





    # -----------------------------
    # Find Alternative Products
    # -----------------------------

    all_products = db.query(Product).all()



    alternatives = get_alternatives(

        product,

        all_products

    )





    # -----------------------------
    # Gemini AI Explanation
    # -----------------------------

    product_data = {


        "name": product.name,


        "health_score": health_score,


        "eco_score": eco_score,


        "eco_category": eco_category


    }




    ai_explanation = generate_explanation(

        product_data

    )





    db.close()





    return {


        "name": product.name,


        "barcode": product.barcode,


        "category": product.category,


        "eco_score": eco_score,


        "health_score": health_score,


        "eco_category": eco_category,


        "recommendation": recommendation,


        "alternatives": alternatives,


        "ai_explanation": ai_explanation

    }