import asyncio
import time 

async def cook(food, t):
    print(f'{time.ctime()} - Microwave ({food}): Cooking {t} seconds...')
    await asyncio.sleep(t)
    print(f'{time.ctime()} - Microwave ({food}): Finished Cooking')
    return f'{food} is completed'