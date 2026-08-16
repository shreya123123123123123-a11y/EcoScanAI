def calculate_eco_score(carbon, water, packaging):

    score = 100


    # Carbon impact
    if carbon > 5:
        score -= 30

    elif carbon > 2:
        score -= 15



    # Water impact
    if water > 1000:
        score -= 20

    elif water > 500:
        score -= 10



    # Packaging impact
    if packaging == "Plastic":
        score -= 15



    if score < 0:
        score = 0


    return score
