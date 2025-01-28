def frequency_analysis(text):
    # Count the frequency of each letter in the text
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    # Sort letters by frequency
    sorted_counts = []
    for key in counts:
        sorted_counts.append((key, counts[key]))
    sorted_counts.sort(key=lambda pair: pair[1], reverse=True)
    return sorted_counts

# Read file content
filename = input("Enter the file name: ")
try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
    exit()

# Perform frequency analysis
result = frequency_analysis(text)

# Output the result
print("\nMost frequent letters:")
for letter, count in result:
    print(f"{letter}: {count}")

