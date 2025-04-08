import asyncio
import random
import time

async def run_reaction_game(rounds=10):
    results = []
    for i in range(rounds):
        delay = random.uniform(1, 5)
        await asyncio.sleep(delay)
        print(f"\nПопытка {i + 1}: Готовься...")
        await asyncio.sleep(0.5)

        print("НАЖМИ!")
        start = time.perf_counter()

        try:
            response = await asyncio.wait_for(async_input(), timeout=3.0)
            end = time.perf_counter()
            reaction_time = end - start
            results.append(reaction_time)
        except asyncio.TimeoutError:
            print("Слишком медленно :(")
            results.append(None)
    
    return results

async def async_input():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, input)
