import aiohttp
from config import Config

class TelegramAlerter:
    def __init__(self, config: Config):
        self.config = config

    async def send_alert(self, message: str):
        url = f"https://api.telegram.org/bot{self.config.telegram_bot_token}/sendMessage"
        payload = {
            "chat_id": self.config.telegram_chat_id,
            "text": message
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    print(f"Failed to send Telegram alert: {await response.text()}")
