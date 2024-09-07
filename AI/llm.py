import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "You are an export on transport and road crash data, based in Victoria, Australia. Using the provided data, offer insights into any information the data tells us on why the crashes occured. If any insights are found, offer solutions to state government on ways to minimize the probability of similar car crashes occuring, with explanations behind each suggestion."

context_data = json.dumps({
        "1": {
            "location": "McDonald Street",
            "blood_alcohol": 0.0,
            "time_of_day": 2400,
            "public_holiday": False,
            "traffic_conditions": "free-flowing",
            "road_type": "pavement",
            "area_type": "country",
            "collided_with": "tree",
            "speed_limit": 100,
            "driver_speed": 99,
            "driver": {
                "age": 30,
                "gender": "male",
            }
        },
        "2": {
            "location": "McDonald Street",
            "blood_alcohol": 0.01,
            "time_of_day": 200,
            "public_holiday": False,
            "traffic_conditions": "free-flowing",
            "road_type": "pavement",
            "area_type": "country",
            "collided_with": "embankment",
            "speed_limit": 100,
            "driver_speed": 103,
            "driver": {
                "age": 30,
                "gender": "male",
            }
        },
        "3": {
            "location": "McDonald Street",
            "blood_alcohol": 0.02,
            "time_of_day": 2200,
            "public_holiday": False,
            "traffic_conditions": "free-flowing",
            "road_type": "pavement",
            "area_type": "country",
            "collided_with": "n/a",
            "speed_limit": 100,
            "driver_speed": 90,
            "driver": {
                "age": 30,
                "gender": "male",
            }
        }
    })

prompt = prompt + " Context Data: " + context_data

response = model.generate_content(prompt)
print(response.text)