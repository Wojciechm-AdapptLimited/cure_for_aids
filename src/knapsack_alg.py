from itertools import combinations


def brute_force(number, capacity, weight_cost):
    best_cost = None
    best_combination = []

    for way in range(number):
        for comb in combinations(weight_cost, way + 1):
            weight = sum([wc[0] for wc in comb])
            cost = sum([wc[1] for wc in comb])
            if (best_cost is None or best_cost < cost) and weight <= capacity:
                best_cost = cost
                best_combination = [0] * number
                for wc in comb:
                    best_combination[weight_cost.index(wc)] = 1
    return best_cost, best_combination


def dynamic(number, capacity, weight_cost):
    knapsack = [[0 for _ in range(capacity + 1)] for _ in range(number + 1)]
    best_combination = [0] * number
    for i in range(number + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                knapsack[i][w] = 0
            elif weight_cost[i - 1][0] <= w:
                knapsack[i][w] = max(knapsack[i - 1][w], weight_cost[i - 1][1]
                                     + knapsack[i - 1][w - weight_cost[i - 1][0]])
            else:
                knapsack[i][w] = knapsack[i - 1][w]
    i = number
    w = capacity
    while i != 0 and w != 0:
        if knapsack[i][w] == knapsack[i - 1][w]:
            best_combination[i - 1] = 0
            i -= 1
        else:
            best_combination[i - 1] = 1
            w -= weight_cost[i - 1][0]
            i -= 1
    return knapsack[number][capacity], best_combination
