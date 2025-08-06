
def get_unique_words(paragraph):
    # Remove punctuation and convert to lowercase
    for ch in ",.!?;:\"'":
        paragraph = paragraph.replace(ch, "")
    paragraph = paragraph.lower()
    
    # Split into words and convert to set for uniqueness
    words = paragraph.split()
    unique_words = set(words)
    return unique_words

# Input two paragraphs from user
para1 = input("Enter Paragraph 1:\n")
para2 = input("\nEnter Paragraph 2:\n")

# Get unique words from each paragraph
unique1 = get_unique_words(para1)
unique2 = get_unique_words(para2)

# Find common words
common_words = unique1.intersection(unique2)

# Total unique words from both paragraphs
total_unique = unique1.union(unique2)

# Output the results
print("\n--- Analysis Result ---")
print("1. Unique words in Paragraph 1:")
print(unique1)

print("\n2. Unique words in Paragraph 2:")
print(unique2)

print("\n3. Common words in both paragraphs:")
print(common_words if common_words else "No common words found.")

print("\n4. Total count of unique words from both paragraphs:", len(total_unique))
