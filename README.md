# statistical-simulation-monty-hall-problem

This project simulates and visualizes the results of the Monty Hall paradox, a famous statistics and probability puzzle, under two strategies:
1. **Switch**: The contestant always switches doors.
2. **No Switch**: The contestant always sticks with their initial choice.

## Features
- Simulate the Monty Hall problem for a configurable number of trials.
- Compare the outcomes of the "Switch" and "No Switch" strategies.
- Save simulation results as CSV files.
- Generate bar chart visualizations of the results.

## Folder Structure
```
monty_hall_simulation/
├── main.py                # Main script to run the simulation
├── visualize.py           # Visualization script to create charts
├── outputs/               # Folder to store results (CSV and charts)
└── README.md              # Documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd monty_hall_simulation
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate       # On macOS/Linux
   venv\Scripts\activate          # On Windows
   ```

3. Install required dependencies:
   ```bash
   pip install pandas matplotlib
   ```
   OR
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Step 1: Run the Simulation
Use `main.py` to run the simulation and save the results to the `outputs/` folder.

```bash
python main.py
```

### Step 2: Visualize the Results
Use `visualize.py` to generate bar charts from the simulation results.

```bash
python visualize.py
```

### Outputs
- **CSV Files**:
  - `outputs/switch_results.csv`: Results for the "Switch" strategy.
  - `outputs/no_switch_results.csv`: Results for the "No Switch" strategy.

- **Charts**:
  - `outputs/switch_results_chart.png`: Bar chart for the "Switch" strategy.
  - `outputs/no_switch_results_chart.png`: Bar chart for the "No Switch" strategy.

## Example Results
For 10,000 trials:
- **Switch Strategy**: ~66% win rate.
- **No Switch Strategy**: ~33% win rate.

This demonstrates the counterintuitive nature of the Monty Hall problem.

## Customization
You can adjust the number of trials in `main.py` by modifying:
```python
trials = 10000
```

## Dependencies (use pip install -r requirements.txt)
- Python 3.7+
- pandas
- matplotlib

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments
Inspired by the classic Monty Hall problem and its surprising probability outcomes.
