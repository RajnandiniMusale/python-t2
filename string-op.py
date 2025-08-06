# Simple Text Analysis Tool

# Input text from the user
text = input("Enter your text:\n")

# Task 1: Count total number of words
words = text.split()
word_count = len(words)

# Task 2: Count total number of spaces
space_count = text.count(' ')

# Task 3: Count frequency of each word
from collections import Counter
word_freq = Counter(words)

# Task 4: Display top 3 most frequent words
top_3 = word_freq.most_common(3)

# Task 5: Count number of vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)

# Task 6: Sort string in reverse ascending order
sorted_text = ''.join(sorted(text))            # Ascending sorted characters
reverse_sorted_text = sorted_text[::-1]        # Reversed (descending) string

# -------------------------
# Display results
print("\n--- Text Analysis Report ---")
print("1. Total number of words:", word_count)
print("2. Total number of spaces:", space_count)

print("3. Frequency of each word:")
for word, freq in word_freq.items():
    print(f"   {word}: {freq}")

print("4. Top 3 most frequent words:")
for word, freq in top_3:
    print(f"   {word} ({freq} times)")

print("5. Total number of vowels:", vowel_count)

print("6. Sorted string in reverse ascending order:")
print(reverse_sorted_text)
