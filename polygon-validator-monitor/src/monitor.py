import asyncio
import aiohttp
from web3 import Web3
from config import Config

class PolygonMonitor:
    def __init__(self, config: Config):
        self.config = config
        self.w3 = Web3(Web3.HTTPProvider(config.rpc_endpoint))

    async def get_latest_checkpoint(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.config.checkpoint_api}/latest") as response:
                if response.status == 200:
                    data = await response.json()
                    return data['result']
                else:
                    return None

    async def get_validator_set(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.config.checkpoint_api}/validator-set") as response:
                if response.status == 200:
                    data = await response.json()
                    return data['result']
                else:
                    return None

    async def check_checkpoint_signing(self):
        latest_checkpoint = await self.get_latest_checkpoint()
        validator_set = await self.get_validator_set()

        if latest_checkpoint and validator_set:
            if self.config.validator_address in validator_set:
                return latest_checkpoint['proposer'] == self.config.validator_address
        return False

    async def check_bor_heimdall_sync(self):
        bor_height = self.w3.eth.block_number
        heimdall_height = await self.get_heimdall_height()

        if bor_height and heimdall_height:
            return abs(bor_height - heimdall_height) <= self.config.max_height_difference
        return False

    async def get_heimdall_height(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.config.heimdall_api}/status") as response:
                if response.status == 200:
                    data = await response.json()
                    return int(data['result']['sync_info']['latest_block_height'])
                else:
                    return None

    async def monitor(self):
        while True:
            checkpoint_signed = await self.check_checkpoint_signing()
            heights_in_sync = await self.check_bor_heimdall_sync()

            if not checkpoint_signed:
                yield "Checkpoint signing issue detected"

            if not heights_in_sync:
                yield "Bor and Heimdall heights out of sync"

            await asyncio.sleep(self.config.check_interval)
