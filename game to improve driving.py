import time


def display_instructions():
    print("Welcome to the Driving School Simulator!")
    print("Instructions:")
    print("1. Use 'W' to accelerate, 'S' to decelerate.")
    print("2. Use 'A' to turn left, 'D' to turn right.")
    print("3. Follow traffic signals and avoid obstacles.")
    print("4. Score points by making correct decisions.")


def get_input():
    return input("Enter your move (W/A/S/D): ").upper()


def simulate_traffic_signal():
    signals = ["Red", "Green", "Yellow"]
    signal = random.choice(signals)
    print(f"Traffic signal: {signal}")
    return signal


def play_game():
    display_instructions()
    score = 0
    for _ in range(5):  # Simulate 5 scenarios
        signal = simulate_traffic_signal()
        move = get_input()

        if signal == "Red" and move != 'S':
            print("You ran a red light! -10 points.")
            score -= 10
        elif signal == "Green" and move != 'W':
            print("You didn't accelerate on green! -5 points.")
            score -= 5
        elif signal == "Yellow" and move != 'S':
            print("You didn't slow down on yellow! -5 points.")
            score -= 5
        else:
            print("Good decision! +10 points.")
            score += 10

        # Simulate a short delay
        time.sleep(1)

