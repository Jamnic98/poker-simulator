# Poker Simulator

The **Poker Simulator** is a Python-based tool designed to simulate poker hands and analyse the pre-flop win rates of different starting hands. It leverages multiprocessing for efficient batch simulations and provides graphical insights into hand statistics.

## Features

- **Simulation of Poker Hands**: Generates random poker scenarios with players, flop, turn, and river.
- **Pre-Flop Analysis**: Calculates win percentages of starting hands based on large-scale simulations.
- **Concurrency**: Utilises Python's `ProcessPoolExecutor` for concurrent execution to maximise performance.
- **Graphical Visualisation**: Provides a visual representation of the win percentages for each starting hand.
- **Modular Design**: Extensible structure for additional poker modes and custom analyses.

---

## Table of Contents

- [Installation](#installation)
- [Configuration](#command-line-configuration)
- [Usage](#usage)
- [Simulation Results](#simulation-results)
- [Simulation Details](#simulation-details)
- [Licence](#licence)

---

## Installation

### Requirements
- Python 3.10 or higher
- Virtual Environment (optional but recommended)

### Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/poker-simulator.git
   cd poker-simulator
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```
   
3. Install the dependencies:
    ```
    pip install -r requirements.txt
   ```
   
## Command-Line Configuration
The simulator now uses argparse for dynamic configuration via command-line arguments. Here are the available options:

* Player Count:
Use -p or --players to specify the number of players (default: 2, range: 2-10).
Example: --players 6

* Simulation Runs:
Use -r or --runs to specify the number of simulation runs (required).
Example: --runs 1_000_000

* Top Starting Hands:
Use -tsh or --top-starting-hands to analyze the top starting hands (default: None, max value: 1326).
Example: --top-starting-hands 20

### Example Command
    python main.py --players 6 --runs 100000 --top-starting-hands 20


## Usage
1. Run the simulator:
   ```
   python main.py
   ```

2. The simulator outputs:
   - Progress logs during simulation.
   - Chunked results as JSON files in the created results/ folder.
   - A graphical visualisation of pre-flop win percentages.


## Simulation Results

The simulation was run with **2 players** over **10,000,000 games**. Below are the observed percentages for each hand type compared to theoretical probabilities:

| **Hand Type**       | **Observed Percentage** | **Theoretical Percentage** | **% Difference**         |
|---------------------|-------------------------|----------------------------|--------------------------|
| **Royal Flush**     | 0.0033%                 | 0.0032%                    | 0.31%                    |
| **Straight Flush**  | 0.0279%                 | 0.0279%                    | 0.00%                    |
| **Four of a Kind**  | 0.1694%                 | 0.1681%                    | 0.77%                    |
| **Full House**      | 2.5962%                 | 2.5961%                    | 0.00%                    |
| **Flush**           | 3.0279%                 | 3.0255%                    | 0.08%                    |
| **Straight**        | 4.6153%                 | 4.6194%                    | -0.09%                   |
| **Three of a Kind** | 4.8237%                 | 4.8290%                    | -0.11%                   |
| **Two Pair**        | 23.4836%                | 23.4955%                   | -0.05%                   |
| **One Pair**        | 43.8232%                | 43.8226%                   | 0.00%                    |
| **High Card**       | 17.4294%                | 17.4127%                   | 0.10%                    |


These results align closely with theoretical probabilities for poker hands in a 52-card deck and validate the accuracy of the hand evaluation logic.


## Simulation Details

### How It Works

1. **Game Setup**:  
   Initialises players and a dealer, who shuffles and deals cards.

2. **Simulation**:  
   Runs `n` games of poker:  
   - Pre-flop cards are dealt to players.  
   - The flop, turn, and river are dealt on the board.  
   - Hands are evaluated to determine winners.

3. **Chunked Results**:  
   Saves intermediate results to prevent memory overload.

4. **Analysis**:  
   Aggregates the results and calculates the win rates of each starting hand.

---

### Key Components

- **`_run_single_pre_flop_sim()`**:  
  Simulates one game and returns the data as a pandas DataFrame.

- **`__run_pre_flop_sim()`**:  
  Orchestrates the entire simulation in parallel using multiple processes.

- **Graphing**:  
  Uses grouped data to calculate and visualise win rates of starting hands.


## Licence
This project is licensed under the MIT Licence.
