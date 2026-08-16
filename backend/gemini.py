from google import genai
import os

from dotenv import load_dotenv


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



def generate_explanation(product):


    prompt = f"""

You are EcoScan AI, a sustainability and health assistant.

Analyze this product:

Product Name:
{product["name"]}

Health Score:
{product["health_score"]}/100

Eco Score:
{product["eco_score"]}/100


Explain:

1. Health impact
2. Environmental impact
3. Better alternatives

Give a short consumer-friendly answer.

"""


    response = client.models.generate_content(

    model="gemini-3.5-flash",

    contents=prompt

)


    return response.text