import asyncio
from game_logic import run_reaction_game
from plotter import plot_results

async def main():
    print("Игра на реакцию. Нажимай Enter, когда увидишь 'НАЖМИ' (в течение 3 секунд).")
    results = await run_reaction_game(rounds=10)
    
    print("\nРезультаты:")
    valid_times = [t for t in results if t is not None]
    avg_time = sum(valid_times) / len(valid_times) if valid_times else None

    for i, t in enumerate(results, 1):
        print(f"{i}: {'%.3f сек' % t if t else 'Промах'}")

    if avg_time:
        print(f"\nСреднее время реакции: {avg_time:.3f} сек")
    else:
        print("\nНи одной успешной попытки :(")

    plot_results(results)

if __name__ == "__main__":
    asyncio.run(main())
