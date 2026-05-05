import asyncio
import random

class MarketScanner:
    def __init__(self, networks):
        self.networks = networks

    async def get_dex_price(self, pair: str, network: str):
        """Эмуляция получения цены из DEX (Raydium/Ston.fi)"""
        # В реальном коде здесь вызов Web3 или SDK блокчейна
        await asyncio.sleep(0.1)
        return random.uniform(140, 145)

    async def find_spreads(self):
        """Поиск разницы в ценах между сетями"""
        results = []
        for net in self.networks:
            price = await self.get_dex_price("SOL/USDC", net)
            results.append({"network": net, "price": price})
        return results
