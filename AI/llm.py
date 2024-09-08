import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_batch_report(context_data):
    prompt = "You are an export on transport and road crash data, based in Victoria, Australia. Using the provided data, offer insights into any information the data tells us on why the crashes occured. If any insights are found, offer solutions to state government on ways to minimize the probability of similar car crashes occuring, with explanations behind each suggestion."

    prompt = str(prompt) + "\n" + str(context_data)

    response = model.generate_content(prompt)
    print(response.text)
    return response.text

