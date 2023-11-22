def count_frequencies(numbers):
    # Initialize an empty dictionary to store frequencies
    freq_dict = {}

    # Iterate through the list of numbers
    for num in numbers:
        # Update the frequency in the dictionary
        freq_dict[num] = freq_dict.get(num, 0) + 1

    return freq_dict

# Example usage:
numbers_list = [1, 2, 3, 1, 2, 4, 5, 1, 2, 3]
result_dict = count_frequencies(numbers_list)
print(result_dict)