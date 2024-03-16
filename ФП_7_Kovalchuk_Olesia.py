import random

def simulate_dice_rolls(num_rolls):
    results = [0] * 13

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        results[total] += 1

    return results

def calculate_probabilities(results, num_rolls):
    probabilities = [round((count / num_rolls) * 100, 2) for count in results[2:]]

    return probabilities

def print_table(probabilities):
    print("Сума\tІмовірність")
    for i in range(2, 13):
        print(f"{i}\t{probabilities[i-2]}% ({probabilities[i-2] / 100})")

num_rolls = int(input("Введіть кількість кидків кубиків: "))

results = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(results, num_rolls)

print_table(probabilities)
