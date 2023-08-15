import time

import asyncio

async def wash(basket):
    print(f'Washing Machine ({basket}) : Put the coin')
    print(f'Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    print(f'Washing Machine ({basket}) : Finished washing')
    return f'{basket} is completed'

async def main():
    coro = wash('Basket A')
    print(coro)
    print(type(coro))
    task = asyncio.create.task(coro)
    print(task)
    print(type(task))
    result = await task
    print(result)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')