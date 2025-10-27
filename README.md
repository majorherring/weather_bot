Here is a README.md example for your weather bot project:

```markdown
# Weather Bot

Weather Bot is a Telegram bot that provides real-time weather information for any city using the WeatherAPI service. It delivers accurate data including temperature, humidity, wind speed, and weather conditions in a clear, easy-to-read format.

## Features
- Get current weather by city name
- Temperature in Celsius and Fahrenheit
- Weather condition description
- Wind speed, humidity, and more
- Error handling for invalid city names or API errors

## Setup

1. Clone the repository:
   ```
   git clone git@github.com:majorherring/weather_bot.git
   ```

2. Create and activate a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env_example` and set your credentials:
   ```
   BOT_TOKEN=your_telegram_bot_token
   API=http://api.weatherapi.com/v1/current.json?key=your_weatherapi_key&aqi=no&lang=ru&q={}
   LOG_LEVEL=DEBUG
   LOG_FORMAT="[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s"
   ```

5. Run the bot:
   ```
   python main.py
   ```

## Usage

Send your city name to the bot in Telegram and receive a detailed weather report instantly.

## License

This project is licensed under the MIT License.
```

This README covers installation, usage, features, and configuration details relevant to your bot project.
