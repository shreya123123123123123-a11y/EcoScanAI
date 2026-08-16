import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.ensemble import RandomForestClassifier

import joblib



# Load dataset

data = pd.read_csv("dataset.csv")



# Features and target

X = data.drop("eco_class", axis=1)

y = data["eco_class"]



# Categorical and numerical columns

categorical_features = [
    "packaging"
]


numeric_features = [
    "carbon",
    "water",
    "sugar",
    "protein"
]



# Convert text columns into numbers

preprocessor = ColumnTransformer(

    transformers=[

        (
            "category",
            OneHotEncoder(),
            categorical_features
        )

    ],

    remainder="passthrough"

)



# Random Forest Model

model = Pipeline(

    steps=[

        (
            "preprocessor",
            preprocessor
        ),

        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
        )

    ]

)



# Train model

model.fit(X, y)



# Save model

joblib.dump(
    model,
    "model.pkl"
)



print("Model trained successfully")