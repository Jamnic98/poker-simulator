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
- [Configuration](#configuration)
- [Usage](#usage)
- [Simulation Details](#simulation-details)
- [Licence](#licence)

---

## Configuration
To customise the simulation, you can update the constants in the `app/utils/constants.py` file:

- **`PLAYER_COUNT`**: Change the number of players in the game.  
- **`RUN_COUNT`**: Set the number of simulation runs.

For example:
    ```python
    # app/utils/constants.py
    PLAYER_COUNT = 6  # Number of players in the game
    RUN_COUNT = 100000  # Total number of simulation runs
    ```


## Installation

### Requirements
- Python 3.10 or higher
- Virtual Environment (optional but recommended)

### Setup Instructions

1. Clone the repository:
   ```git clone https://github.com/yourusername/poker-simulator.git```
   ```cd poker-simulator```

2. Create a virtual environment and activate it:
   ```python3 -m venv .venv```
   ```source .venv/bin/activate  # On Windows, use .venv\Scripts\activate```
   
3. Install the dependencies:
    ```pip install -r requirements.txt```

4. Create a directory for simulation results:
   ```mkdir results```

## Usage
1. Run the simulator:
   ```python main.py```

2. The simulator outputs:
   - Progress logs during simulation.
   - Chunked results as JSON files in the results/ folder.
   - A graphical visualisation of pre-flop win percentages.


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
