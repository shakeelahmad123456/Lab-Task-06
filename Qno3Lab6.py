def longest_subarray_sum(arr, K):
    # Initialize a hash table to store cumulative sums and their corresponding indices
    sum_table = {}
    max_length = 0
    current_sum = 0

    # Iterate through the array
    for i, num in enumerate(arr):
        # Update the cumulative sum
        current_sum += num

        # Check if the current sum equals K
        if current_sum == K:
            max_length = i + 1

        # Check if the current sum - K exists in the hash table
        if current_sum - K in sum_table:
            max_length = max(max_length, i - sum_table[current_sum - K])

        # If the current sum is not in the hash table, add it
        if current_sum not in sum_table:
            sum_table[current_sum] = i

    return max_length

# Example usage:
array = [10, 5, 2, 7, 1, 9]
target_sum = 15
result = longest_subarray_sum(array, target_sum)
print(result)