import heapq

def min_cost_to_connect_cables(cables):
    if not cables or len(cables) == 1:
        return 0
    
    heapq.heapify(cables)
    
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        current_connection_cost = first + second

        total_cost += current_connection_cost

        heapq.heappush(cables, current_connection_cost)

    return total_cost

cables_list = [8, 4, 6, 12]
min_costs = min_cost_to_connect_cables(cables_list)
print(f"Minimum costs: {min_costs}")
