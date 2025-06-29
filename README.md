# Weather Website

A modern web application to get real-time weather information for any city, powered by Flask, OpenAI, and OpenWeatherMap APIs. The app features a clean, responsive UI and leverages OpenAI's function calling to fetch and display weather data.

## Features
- 🌦️ Get current weather for any city worldwide
- 🤖 Uses OpenAI's function calling for weather queries
- 📦 Simple, modern, and responsive UI
- ⚡ Fast, AJAX-based search (no page reloads)
- 🔒 API keys and secrets are protected via `.env`

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (custom, responsive), JavaScript (vanilla)
- **APIs:** OpenWeatherMap, OpenAI

## Getting Started

### 1. Clone the repository
```bash
git clone <repo-url>
cd weather-website
```

### 2. Install dependencies
It is recommended to use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the project root with the following content:
```env
OPENAI_API_KEY=your_openai_api_key
OPENWEATHER_API_KEY=your_openweathermap_api_key
```
- Get your [OpenAI API key](https://platform.openai.com/account/api-keys)
- Get your [OpenWeatherMap API key](https://home.openweathermap.org/api_keys)

### 4. Run the app
```bash
python app.py
```
The app will be available at [http://localhost:8000](http://localhost:8000)

## Usage
- Enter a city name (e.g., `London`, `New York`, `Tokyo`) and click the search button or press Enter.
- The app will display current temperature, weather description, humidity, wind speed, and more.

## Project Structure
```
weather-website/
├── app.py                # Flask backend
├── requirements.txt      # Python dependencies
├── .env                 # API keys (not committed)
├── static/
│   ├── css/style.css    # Styles
│   └── js/script.js     # Frontend logic
├── templates/
│   └── index.html       # Main HTML template
└── README.md            # This file
```

## Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENWEATHER_API_KEY`: Your OpenWeatherMap API key

## Security
- `.env` is included in `.gitignore` and will not be committed to git.

## Credits
- [Flask](https://flask.palletsprojects.com/)
- [OpenAI](https://openai.com/)
- [OpenWeatherMap](https://openweathermap.org/)
- UI inspired by modern weather apps

## License
MIT License
