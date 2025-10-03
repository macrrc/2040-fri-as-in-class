# Assignment 1 – Text Stats Project (deliberately NO functions / NO try/except)
# Reads input.txt, prints results, and writes them to output.txt in the exact format.

import re
from collections import Counter

# --- Read the raw file text (assumes input.txt exists in the same folder) ---
with open("input.txt", "r", encoding="utf-8") as file_in:
    text_content = file_in.read()

# --- Character counts ---
characters_with_spaces = len(text_content)
characters_no_spaces = 0
char_index = 0
while char_index < len(text_content):
    current_char = text_content[char_index]
    if not current_char.isspace():
        characters_no_spaces += 1
    char_index += 1

# --- Word extraction: letters only (A–Z/a–z), case-insensitive for counting/uniqueness ---
lowered_text = text_content.lower()
word_list = re.findall(r"[a-zA-Z]+", lowered_text)

# --- Word statistics ---
word_count = len(word_list)
unique_word_count = len(set(word_list))

# total letters across all words
total_letter_count = 0
word_index = 0
while word_index < len(word_list):
    total_letter_count += len(word_list[word_index])
    word_index += 1

# average word length with one decimal; 0.0 if there are no words
average_word_length = (total_letter_count / word_count) if word_count != 0 else 0.0
average_word_length_str = f"{average_word_length:.1f}"

# --- Most common word(s) and frequency ---
if word_count == 0:
    most_common_line = "Most common word(s): (0)"
else:
    word_counts = Counter(word_list)
    highest_frequency = 0
    for word in word_counts:
        if word_counts[word] > highest_frequency:
            highest_frequency = word_counts[word]
    most_frequent_words = []
    for word in word_counts:
        if word_counts[word] == highest_frequency:
            most_frequent_words.append(word)
    most_frequent_words.sort()
    if len(most_frequent_words) == 1:
        most_common_line = f"Most common word(s): {most_frequent_words[0]} ({highest_frequency})"
    else:
        most_common_line = f"Most common word(s): {', '.join(most_frequent_words)} ({highest_frequency})"

# --- Build the six required lines in the exact order/format ---
output_lines = [
    f"Word count: {word_count}",
    f"Unique words: {unique_word_count}",
    f"Characters (with spaces): {characters_with_spaces}",
    f"Characters (no spaces): {characters_no_spaces}",
    f"Average word length: {average_word_length_str}",
    most_common_line,
]


# --- Print to console ---
line_index = 0
while line_index < len(output_lines):
    print(output_lines[line_index])
    line_index += 1

# --- Write to output.txt ---
with open("output.txt", "w", encoding="utf-8") as file_out:
    line_index = 0
    while line_index < len(output_lines):
        file_out.write(output_lines[line_index] + ("\n" if line_index < len(output_lines) - 1 else ""))
        line_index += 1
