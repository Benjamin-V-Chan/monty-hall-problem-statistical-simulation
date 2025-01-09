import random
import csv
import os

# Ensure the outputs folder exists
os.makedirs("outputs", exist_ok=True)

def monty_hall_simulation(num_trials=1000, switch=True):
    results = {"win": 0, "lose": 0}

    for _ in range(num_trials):
        # Place a car behind one random door
        doors = ["goat", "goat", "car"]
        random.shuffle(doors)

        # Contestant randomly chooses a door
        chosen_door = random.randint(0, 2)

        # Host opens a door with a goat (not the chosen one)
        available_doors = [i for i in range(3) if doors[i] == "goat" and i != chosen_door]
        host_door = random.choice(available_doors)

        # Contestant decides whether to switch or not
        if switch:
            # Switch to the remaining unopened door
            chosen_door = [i for i in range(3) if i != chosen_door and i != host_door][0]

        # Determine if the contestant wins or loses
        if doors[chosen_door] == "car":
            results["win"] += 1
        else:
            results["lose"] += 1

    return results

# Streamlined save results to csv func
def save_results_to_csv(results, filename):
    with open(f"outputs/{filename}", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Outcome", "Count"])
        for key, value in results.items():
            writer.writerow([key, value])

def main():
    trials = 10000

    # Run simulations for both each strategy
    switch_results = monty_hall_simulation(trials, switch=True)
    no_switch_results = monty_hall_simulation(trials, switch=False)

    # Save each strategy results to csv
    save_results_to_csv(switch_results, "switch_results.csv")
    save_results_to_csv(no_switch_results, "no_switch_results.csv")

    print(f"Simulation completed. Results saved to 'outputs' folder.")

if __name__ == "__main__":
    main()