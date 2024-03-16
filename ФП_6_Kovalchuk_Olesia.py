def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    selected_items = {}
    total_calories = 0
    total_cost = 0
    drink_selected = False  

    for item, properties in sorted_items:
        if "drink" in properties and drink_selected:
            continue  
        if total_cost + properties["cost"] <= budget:
            selected_items[item] = properties
            total_calories += properties["calories"]
            total_cost += properties["cost"]
            if "drink" in properties:
                drink_selected = True  
    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    drink_selected = False  

    for i, (item, properties) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            cost = properties["cost"]
            calories = properties["calories"]
            if "drink" in properties and drink_selected:
                dp_table[i][j] = dp_table[i - 1][j]  
            elif cost > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - cost] + calories)
                if "drink" in properties:
                    drink_selected = True  

    selected_items = {}
    j = budget
    total_cost = 0  
    for i in range(len(items), 0, -1):
        if dp_table[i][j] != dp_table[i - 1][j]:
            item, properties = list(items.items())[i - 1]
            selected_items[item] = properties
            total_cost += properties["cost"]  
            j -= properties["cost"]

    total_calories = dp_table[-1][-1]

    return selected_items, total_calories, total_cost

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100, "drink": True},
    "cola": {"cost": 15, "calories": 220, "drink": True},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100  

greedy_selected_items, greedy_total_calories, greedy_total_cost = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_selected_items)
print("Total calories:", greedy_total_calories)
print("Total cost:", greedy_total_cost)

dp_selected_items, dp_total_calories, dp_total_cost = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected items:", dp_selected_items)
print("Total calories:", dp_total_calories)
print("Total cost:", dp_total_cost)
