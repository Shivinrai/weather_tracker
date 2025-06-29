from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_weather_data(location):
    """Get weather data from OpenWeatherMap API"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return {"error": "OpenWeatherMap API key not found"}
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return {
                "location": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }
        else:
            return {"error": f"Weather data not found for {location}"}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data: {str(e)}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def weather_function_calling(location):
    """Use OpenAI function calling to get weather information"""
    
    tools = [{
        "type": "function",
        "function": {
            "name": "get_weather_data",
            "description": "Get current weather information for a specific location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state/country, e.g. San Francisco, CA"
                    }
                },
                "required": ["location"]
            }
        }
    }]
    
    messages = [
        {"role": "system", "content": "You are a helpful weather assistant. When asked about weather, use the get_weather_data function to provide accurate information."},
        {"role": "user", "content": f"What's the weather like in {location}?"}
    ]
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message
        
        if response_message.tool_calls:
            tool_call = response_message.tool_calls[0]
            function_args = json.loads(tool_call.function.arguments)
            
            weather_data = get_weather_data(function_args["location"])
            return weather_data
        else:
            return {"error": "No weather function was called by the AI"}
            
    except Exception as e:
        return {"error": f"Error calling OpenAI API: {str(e)}"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather', methods=['POST'])
def api_weather():
    try:
        data = request.get_json()
        location = data.get('location', '').strip()
        
        if not location:
            return jsonify({"error": "Location is required"}), 400
        
        weather_data = weather_function_calling(location)
        
        if "error" in weather_data:
            return jsonify(weather_data), 400
        
        return jsonify(weather_data)
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)