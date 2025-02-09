def frequency_analysis(text):
    # Count the frequency of each letter in the text
    counts = {}
    total_letters = 0
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
            total_letters += 1  # Count total letters
    
    # Sort letters by frequency
    sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    
    # Calculate percentage and format output
    frequency_list = [(char, count, (count / total_letters) * 100) for char, count in sorted_counts]
    
    return frequency_list

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
for letter, count, percentage in result:
    print(f"{letter}: {count} ({percentage:.2f}%)")

