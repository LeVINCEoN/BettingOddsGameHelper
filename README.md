
# BettingOddsGameHelper

## Overview
BettingOddsGameHelper is a Python-based tool designed to enhance prediction accuracy in sports gaming by utilizing real-time betting odds. It calculates the expected value (EV) of various outcomes based on provided odds and a point system, offering guidance on the most statistically advantageous picks.

## Features
- Calculate expected values based on game-specific odds and point rewards.
- Easy to use with JSON formatted input for match details.
- Outputs calculated EVs and recommends the best pick based on these calculations.

## Requirements
Python 3.x is required to run this tool. No external libraries are needed.

## Installation
Clone the repository to your local machine:
```
git clone https://github.com/yourusername/BettingOddsGameHelper.git
cd BettingOddsGameHelper
```

## Usage
1. Ensure the input data is correctly formatted in the `match_data.json` file. Here is a sample format for the JSON data:
   ```json
   {
       "country1": "CountryA",
       "country2": "CountryB",
       "points_country1_win": 3,
       "points_draw": 2.5,
       "points_country2_win": 2,
       "odds_country1_win": "14/5",
       "odds_draw": "23/10",
       "odds_country2_win": "16/13"
   }
   ```

2. Run the script:
   ```
   python predictor.py
   ```

3. Review the output for expected values and suggested best pick.
