import asyncio
from config import Config
from monitor import PolygonMonitor
from alerts import TelegramAlerter

async def main():
    config = Config('config.yaml')
    monitor = PolygonMonitor(config)
    alerter = TelegramAlerter(config)

    async for alert in monitor.monitor():
        await alerter.send_alert(alert)

if __name__ == "__main__":
    asyncio.run(main())
