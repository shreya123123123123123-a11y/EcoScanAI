def calculate_health_score(sugar, protein):

    score = 100


    if sugar > 30:
        score -= 40

    elif sugar > 15:
        score -= 20



    if protein > 10:
        score += 10



    if score > 100:
        score = 100


    return score