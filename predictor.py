import json


def calculate_decimal_odds(fractional_odds):
    numerator, denominator = map(int, fractional_odds.split('/'))
    return 1 + (numerator / denominator)


def calculate_probability(decimal_odds):
    return 1 / decimal_odds


def calculate_expected_value(probability, game_points):
    return probability * game_points


def process_match_data(data):
    # Extract match details
    country1 = data["country1"]
    country2 = data["country2"]
    points_country1_win = data["points_country1_win"]
    points_draw = data["points_draw"]
    points_country2_win = data["points_country2_win"]
    odds_country1_win = data["odds_country1_win"]
    odds_draw = data["odds_draw"]
    odds_country2_win = data["odds_country2_win"]

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

    outcomes = {
        f"{country1} win": ev_country1_win,
        "Draw": ev_draw,
        f"{country2} win": ev_country2_win
    }
    return outcomes


def print_match_data(data):
    print("Input Parameters:")
    print(f"Match: {data['country1']} vs {data['country2']}")
    print(f"Points - {data['country1']} Win: {data['points_country1_win']}, Draw: {data['points_draw']}, {data['country2']} Win: {data['points_country2_win']}")
    print(f"Odds - {data['country1']} Win: {data['odds_country1_win']}, Draw: {data['odds_draw']}, {data['country2']} Win: {data['odds_country2_win']}\n")


def print_results(outcomes):
    print("Expected Values:")
    for outcome, value in outcomes.items():
        print(f"{outcome} - Expected Value: {value:.3f}")
    best_pick = max(outcomes, key=outcomes.get)
    print(f"\nRecommended pick: {best_pick} with EV: {outcomes[best_pick]:.3f}")


def main():
    # Load data from a JSON file
    with open("match_data.json", "r") as file:
        all_data = json.load(file)

        # Loop through each match data
    for data in all_data:
        print_match_data(data)
        outcomes = process_match_data(data)
        print_results(outcomes)
        print("\n")


if __name__ == "__main__":
    main()
