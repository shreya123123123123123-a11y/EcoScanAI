from gemini import generate_explanation


product = {

"name":"Coca Cola",

"health_score":60,

"eco_score":85

}


answer = generate_explanation(product)


print(answer)