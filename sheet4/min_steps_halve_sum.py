import heapq

def min_steps_to_halve_sum(nums):
    current_sum = sum(nums)
    target = current_sum / 2
    # Max heap using negative values
    heap = [-float(x) for x in nums]
    heapq.heapify(heap)
    
    steps = 0
    while current_sum > target:
        steps += 1
        largest = -heapq.heappop(heap)
        halved = largest / 2
        current_sum -= halved
        heapq.heappush(heap, -halved)
        
    return steps

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    print(f"Minimum operations: {min_steps_to_halve_sum(arr)}")
