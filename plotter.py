import matplotlib.pyplot as plt

def plot_results(results):
    attempts = list(range(1, len(results) + 1))
    times = [r if r is not None else 0 for r in results]

    plt.figure(figsize=(10, 5))
    plt.plot(attempts, times, marker='o', linestyle='-', color='blue')
    plt.title('Время реакции по попыткам')
    plt.xlabel('Попытка')
    plt.ylabel('Время реакции (сек)')
    plt.xticks(attempts)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
