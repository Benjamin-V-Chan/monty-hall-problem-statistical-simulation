import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the outputs folder exists
os.makedirs("outputs", exist_ok=True)

def load_results(filename):
    filepath = f"outputs/{filename}"
    return pd.read_csv(filepath)

def plot_results(results, title, filename):
    plt.figure(figsize=(8, 6))
    plt.bar(results["Outcome"], results["Count"], width=0.4, edgecolor="black")
    plt.title(title)
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"outputs/{filename}")
    plt.close()

def main():
    # Load data for each strategy
    switch_results = load_results("switch_results.csv")
    no_switch_results = load_results("no_switch_results.csv")

    # Plot results for each strategy
    plot_results(switch_results, "Monty Hall Results (Switch)", "switch_results_chart.png")
    plot_results(no_switch_results, "Monty Hall Results (No Switch)", "no_switch_results_chart.png")

    print(f"Visualization completed. Charts saved to 'outputs' folder.")

if __name__ == "__main__":
    main()