def are_anagrams(str1, str2):
    # Removing spaces and converting to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are equal
    if len(str1) != len(str2):
        return False

    # Initialize hash tables to store character frequencies
    freq_table1 = {}
    freq_table2 = {}

    # Populate the hash tables with character frequencies
    for char in str1:
        freq_table1[char] = freq_table1.get(char, 0) + 1

    for char in str2:
        freq_table2[char] = freq_table2.get(char, 0) + 1

    # Compare the two hash tables
    return freq_table1 == freq_table2

# Example usage:
string1 = "Listen"
string2 = "Silent"
result = are_anagrams(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {result}")