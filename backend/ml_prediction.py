import joblib
import pandas as pd
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model.pkl"
)


model = joblib.load(MODEL_PATH)



def predict_eco_category(
        carbon,
        water,
        packaging,
        sugar,
        protein
):


    data = pd.DataFrame(
        [
            {
                "carbon": carbon,
                "water": water,
                "packaging": packaging,
                "sugar": sugar,
                "protein": protein
            }
        ]
    )


    prediction = model.predict(data)


    return prediction[0]