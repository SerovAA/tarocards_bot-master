import aiohttp
import os

from dotenv import load_dotenv

load_dotenv()

YANDEX_API = os.getenv('YANDEX_API_KEY')
YANDEX_MODEL = os.getenv('YANDEX_MODEL')


async def get_gpt_interpretation(cards: list[str]) -> str:
    """
       Fetches a GPT-based interpretation of a Tarot card spread from Yandex API.

       Args:
           cards (list[str]): List of card names to interpret.

       Returns:
           str: The interpretation text.

       Raises:
           Exception: If the API request fails.
       """
    prompt = {
        "modelUri": f"{YANDEX_MODEL}",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты таролог, интерпретируй расклад из трех карт таро. "
                        "не нужно описывать карты отдельно, интересует общий взгляд на сочетание трех карт. "
                        "Важно, не описывай карты! Ответ должен быть в шуточном стиле"
            },
            {
                "role": "user",
                "text": f"Выпали карты {', '.join(cards)}"
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {YANDEX_API}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=prompt) as response:
            if response.status == 200:
                result = await response.json()
                return result['result']['alternatives'][0]['message']['text']
            else:
                raise Exception(f"Ошибка API: {response.status}")
