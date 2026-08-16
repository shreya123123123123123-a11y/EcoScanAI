def get_recommendation(health_score, eco_score):


    if health_score >= 80 and eco_score >= 80:

        return "Excellent choice! Healthy and sustainable product."


    elif health_score >= 80:

        return "Healthy product but consider a more eco-friendly option."


    elif eco_score >= 80:

        return "Environment friendly but nutrition can improve."


    else:

        return "Consider choosing a healthier and sustainable alternative."





def get_alternatives(current_product, products):


    alternatives = []


    for product in products:


        if product.category == current_product.category:


            if product.name != current_product.name:

                alternatives.append(product)



    # Better nutrition first

    alternatives.sort(
        key=lambda x: (
            x.sugar,
            -x.protein
        )
    )



    result = []


    for product in alternatives[:3]:


        result.append({

            "name": product.name,

            "price": product.price,

            "category": product.category,

            "carbon": product.carbon,

            "water": product.water

        })


    return result