from itertools import combinations

def brute_force(number, capacity, weight_cost):
    """Brute force method for solving knapsack problem
    number: number of existing items
    capacity: the capacity of knapsack
    weight_cost: list of tuples like: [(weight, cost), (weight, cost), ...]
    returning tuple like: (best cost, best combination list(contains 1 and 0))
    """
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

print(brute_force(4,8,[(2,4),(1,3),(4,6),(4,8)]))
