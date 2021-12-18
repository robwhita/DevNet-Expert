

import aiohttp
import asyncio
import time

start_time = time.time()

async def main():


    async with aiohttp.ClientSession() as session:
        for number in range(1, 105):
            url = f'https://deckofcardsapi.com/api/deck/new/draw/'
            async with session.get(url) as resp:
                card = await resp.json()
                print(f'{card["cards"][0]["value"]} of {card["cards"][0]["suit"]}') 





print("--- %s seconds ---" % (time.time() - start_time))