import csv

from eco_score import calculate_eco_score
from health_score import calculate_health_score
from recommendation import recommend


products = []


with open("../datasets/products.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        products.append(row)



processed_products = []


for product in products:


    eco = calculate_eco_score(
        float(product["carbon"]),
        float(product["water"]),
        product["packaging"]
    )


    health = calculate_health_score(
        float(product["sugar"]),
        float(product["protein"])
    )


    processed_products.append({

        "name": product["name"],

        "eco_score": eco,

        "health_score": health

    })



result = recommend(processed_products)



print("\nBest Products:\n")

for product in result:

    print(product)