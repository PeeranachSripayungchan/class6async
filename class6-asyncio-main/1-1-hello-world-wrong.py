# When do coroutines start running?
import asyncio
import time

async def print_after(message, delay):
    # Print a message after the specified delay (in seconds)
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = print_after("World!", 2)
    second_awaitable = print_after("Hello", 1)
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable
    
asyncio.run(main())