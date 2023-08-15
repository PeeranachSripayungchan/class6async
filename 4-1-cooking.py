import asyncio
import time

class Coffee:
    pass
class Egg:
    pass
class Toast:
    pass

async def PourCoffee():
    print(f"{time.ctime()} - Pouring Coffee")
    print(f"{time.ctime()} - Coffee is ready")
    await asyncio.sleep(1)
    return Coffee()


async def ApplyButter():
    print(f"{time.ctime()} - Spreading butter on toast")
    await asyncio.sleep(1)
  
async def FryEggsAsync(howMany):
    print(f"{time.ctime()} - Heat pan to fry Eggs")
    await asyncio.sleep(3)
    print(f"{time.ctime()} - Pan is ready")
    print(f"{time.ctime()} - Frying", howMany, "Eggs")
    await asyncio.sleep(3)
    print(f"{time.ctime()} - Eggs are ready")
    return Egg()

async def ToastAsync(slices):
    for slice in range(slices):
        s = time.perf_counter()

        print(f"{time.ctime()} - Toasting Bread", slice + 1)
        await asyncio.sleep(3)
        print(f"{time.ctime()} - Bread", slice + 1, "Toasted")
        await ApplyButter()
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
      
    return Toast()

async def main():
    await asyncio.gather(PourCoffee(), FryEggsAsync(2), ToastAsync(2))
    
if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{time.ctime()} - Breakfast cooked in",elapsed,"seconds.")

''' Result
Wed Aug 16 01:25:47 2023 - Pouring Coffee
Wed Aug 16 01:25:47 2023 - Coffee is ready
Wed Aug 16 01:25:47 2023 - Heat pan to fry Eggs
Wed Aug 16 01:25:47 2023 - Toasting Bread 1
Wed Aug 16 01:25:50 2023 - Pan is ready
Wed Aug 16 01:25:50 2023 - Frying 2 Eggs
Wed Aug 16 01:25:50 2023 - Bread 1 Toasted
Wed Aug 16 01:25:50 2023 - Spreading butter on toast
Wed Aug 16 01:25:51 2023 - Toast 1 ready
Wed Aug 16 01:25:51 2023 - Toasting Bread 2
Wed Aug 16 01:25:53 2023 - Eggs are ready
Wed Aug 16 01:25:54 2023 - Bread 2 Toasted
Wed Aug 16 01:25:54 2023 - Spreading butter on toast
Wed Aug 16 01:25:55 2023 - Toast 2 ready
Wed Aug 16 01:25:55 2023 - Breakfast cooked in 8.0406455 seconds.
'''