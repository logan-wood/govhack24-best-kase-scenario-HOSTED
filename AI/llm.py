import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_batch_report(context_data):
    prompt = """Role: You are an expert on road crash data, based in Victoria, Austrlia, with over 15 years of experience. You excel at making insights that are not obvious to other people.
     
    Task: Your task is to analyze provided data, and make links between events with similar contributing factors. You should provide recommendations on how to minimize the chances of similar events occuring in the future, with reasonings and evidence behind each recommendation. 

    Example: If the data provided shows a strong trend of collisions with animals, outline this, and recommend that more measures are taken to keep animals off the road.

    Example: If the data provided shows a strong trend of events during night time, outline this, and recommend to check street lighting conditions in the area, and recommend to focus on campaigns against fatigued driving.

    Your response should be concise and easy to read. At the start of your response, please summarize your recommendations to decrease probability of similar events occuring in two sentences.

    Please rank the key information you provide from most important to least important. Please identify costs, and take public relations risks into consideration with any recommendations.
    
    Contextual data provided here:

    """

    prompt = str(prompt) + "\n" + str(context_data)

    response = model.generate_content(prompt)
    print(response.text)
    return response.text

