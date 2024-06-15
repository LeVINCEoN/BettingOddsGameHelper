import json


def calculate_decimal_odds(fractional_odds):
    numerator, denominator = map(int, fractional_odds.split('/'))
    return 1 + (numerator / denominator)


def calculate_probability(decimal_odds):
    return 1 / decimal_odds


def calculate_expected_value(probability, game_points):
    return probability * game_points


def main():
    # Load data from a JSON file
    with open("match_data.json", "r") as file:
        data = json.load(file)

    # Extracting match details
    country1 = data["country1"]
    country2 = data["country2"]
    points_country1_win = data["points_country1_win"]
    points_draw = data["points_draw"]
    points_country2_win = data["points_country2_win"]
    odds_country1_win = data["odds_country1_win"]
    odds_draw = data["odds_draw"]
    odds_country2_win = data["odds_country2_win"]

    # Print input parameters for verification
    print("Input Parameters:")
    print(f"Match: {country1} vs {country2}")
    print(f"Points - {country1} Win: {points_country1_win}, Draw: {points_draw}, {country2} Win: {points_country2_win}")
    print(f"Odds - {country1} Win: {odds_country1_win}, Draw: {odds_draw}, {country2} Win: {odds_country2_win}\n")

    # Calculations
    decimal_odds_country1_win = calculate_decimal_odds(odds_country1_win)
    decimal_odds_draw = calculate_decimal_odds(odds_draw)
    decimal_odds_country2_win = calculate_decimal_odds(odds_country2_win)

    probability_country1_win = calculate_probability(decimal_odds_country1_win)
    probability_draw = calculate_probability(decimal_odds_draw)
    probability_country2_win = calculate_probability(decimal_odds_country2_win)

    ev_country1_win = calculate_expected_value(probability_country1_win, points_country1_win)
    ev_draw = calculate_expected_value(probability_draw, points_draw)
    ev_country2_win = calculate_expected_value(probability_country2_win, points_country2_win)

    # Output results
    print("Expected Values:")
    print(f"{country1} win - Expected Value: {ev_country1_win:.3f}")
    print(f"Draw - Expected Value: {ev_draw:.3f}")
    print(f"{country2} win - Expected Value: {ev_country2_win:.3f}\n")

    # Determine the best pick
    outcomes = {
        f"{country1} win": ev_country1_win,
        "Draw": ev_draw,
        f"{country2} win": ev_country2_win
    }
    best_pick = max(outcomes, key=outcomes.get)
    print(f"Recommended pick: {best_pick} with EV: {outcomes[best_pick]:.3f}")


if __name__ == "__main__":
    main()
