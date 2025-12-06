import heapq

def merge_k_lists(lists):
    """Merges k sorted lists and return them as a one sorted list."""

    min_heap = []
    merged_list = []

    # First, fill the heap with the first elements of each list
    # Store the tuple: (value, list_index, element_index)
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)
        next_element_index = element_index + 1

        # If there are still elements in this list, add the next one to the heap
        if next_element_index < len(lists[list_index]):
            next_value = lists[list_index][next_element_index]
            heapq.heappush(min_heap, (next_value, list_index, next_element_index))

    return merged_list

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
