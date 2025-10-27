import aiohttp
import asyncio
import json
import logging
from config.config import Config,load_config
from lexicon.lexicon import LEXICON_RU
logger=logging.getLogger(__name__)

config:Config=load_config()
url_template=config.url.url

async def fetch(gorod) -> dict:
    url: str = url_template.format(gorod)
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                logger.error("Ошибка сервера")
                err_txt: dict = await response.json()
                return {"error": True, "code": err_txt.get("error", {}).get("code", "unknown")}

            

async def get_weather(gorod: str) -> str:
    data = await fetch(gorod)
    if data is None or "error" in data:
        logger.error(data)
        return f"Ошибка: {LEXICON_RU.get(str(data.get('code')))}"
    try:
        return (
                f"{LEXICON_RU.get("city")} : {data['location']['name']},\n"
                f"{LEXICON_RU.get("time")} : {data['current']['last_updated']},\n"
                f"{LEXICON_RU.get("temp")} : {int(data["current"]["temp_c"])},\n"
                f"{LEXICON_RU.get("temp_c")} : {int(data["current"]["feelslike_c"])},\n"
                f"{LEXICON_RU.get("weather")} : {data['current']['condition']['text']}"
                )
    except KeyError as e:
        logger.error(e)
        return f"Ошибка:{LEXICON_RU.get("unknown")}"   
if __name__=="__main__":
 print(asyncio.run(get_weather(input("gorod: "))))