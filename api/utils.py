def dp_knapsack(destinations, capacity):
    n = len(destinations)
    c = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if destinations[i - 1]['cost'] <= w:
                c[i][w] = max(
                    destinations[i - 1]['enjoyment_value'] + c[i - 1][w - destinations[i - 1]['cost']],
                    c[i - 1][w]
                )
            else:
                c[i][w] = c[i - 1][w]

    return c[n][capacity]
