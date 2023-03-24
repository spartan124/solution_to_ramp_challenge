import re
from collections import Counter

nested_list = [
    ["Hello,",
    "We’re glad you’re here!"],
    ["Raw has been founded to expand entrepreneurial expertise with",
     "exciting entrepreneurial growth opportunities and the passion"],
    ["to use technology at the shelf",
     "of this situation, many startups opt to use of the shelf solutions.",
     "SaaS tools to help in the self-funded integration process."],
    ["In this situation, many startups, management startups or companies, will",
     "need to use these scalable solutions to optimize performance."],
    ["We thought this situation of scaling in the future and",
     "being able to offer your values. As we expect everyone to spend"],
    ["time on this gathering challenge, we were assured of various"],
    ["updates or our values. As we assure everyone would like to spend"],
    ["time and effort into providing the change [CTF[1] most or our values"],
    ["We’re aware that some people prefer keeping their money or opinions locked inside and"],
    ["would never join in making it"],
    ["a better place like this one."],
    ["All flags are as invented of each solution. As we’re aware solutions"],
    ["level together and work on one mission, our values are locked in mutual."],
    ["All flags are gathered for yourself."]
]


# 1. The number of unique characters in the list.
def count_unique_chars(nested_list):
    all_chars = ''.join([item for sublist in nested_list for item in sublist])
    unique_chars = set(all_chars)
    return len(unique_chars)

num_unique_chars = count_unique_chars(nested_list)
print("Number of unique characters:", num_unique_chars)


# 2. The most common character in the list.
def most_common_character(nested_list):
    all_chars = ''.join([item.replace(" ", "") for sublist in nested_list for item in sublist])
    char_count = Counter(all_chars)
    return char_count.most_common(1)[0][0]

# Get the most common character
most_common_char = most_common_character(nested_list)
print("Most common character:", most_common_char)

# 3. The character(s) that appear(s) the least in the list.
def least_common_character(nested_list):
    all_chars = ''.join([item.replace(" ", "") for sublist in nested_list for item in sublist])
    char_count = Counter(all_chars)
    return char_count.most_common()[-1][0]
# Get the least common character(s)
least_common_chars = least_common_character(nested_list)

print("Least common character(s):", least_common_chars)

# 4. How many times the word "challenge" appears in the list.
def count_word(nested_list, word):
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            count += count_word(item, word)
        elif isinstance(item, str):
            count += item.count(word)
    return count

num_challenges = count_word(nested_list, "challenge")
print("Number of times 'challenge' appears:", num_challenges)

# 5. The fourth character of each string in the list.
def get_fourth_chars(nested_list):
    fourth_chars = [item[3] for sublist in nested_list for item in sublist if len(item) > 3]
    return fourth_chars

fourth_chars = get_fourth_chars(nested_list)
print("Fourth character of each string in the list:", fourth_chars)

# 6. The number of strings in the list that start with the letter "L".
def count_words_starting_with(nested_list, char):
    flattened_list = [item for sublist in nested_list for item in sublist]
    count = sum([1 for word in flattened_list if word.startswith(char)])
    return count

print("Number of strings in the list that start with the letter 'L':", count_words_starting_with(nested_list, "L"))

# 7. How many unique words are in the list?
def count_unique_words(nested_list):
    unique_words = set()
    for sublist in nested_list:
        for word in sublist:
            unique_words.add(word)
    count = len(unique_words)
    return count

print("Number of unique words in the list:", count_unique_words(nested_list))

# 8. The longest string in the list.
def find_longest_string(nested_list):
    max_length = 0
    longest_string = ""
    for sublist in nested_list:
        for string in sublist:
            if len(string) > max_length:
                max_length = len(string)
                longest_string = string
    return longest_string

print("Longest string in the list:", find_longest_string(nested_list))

# 9. The shortest string in the list.
def find_shortest_string(nested_list):
    shortest_string = None
    for sublist in nested_list:
        for string in sublist:
            if shortest_string is None or len(string) < len(shortest_string):
                shortest_string = string
    return shortest_string

print("Shortest string in the list:", find_shortest_string(nested_list))

# 10. The flag hidden somewhere in the list.

flag = None

# iterate through each nested list in the main list
for list in nested_list:
    # iterate through each string in the nested list
    for string in list:
        # check if the string contains the flag substring
        if "[CTF[" in string and "]" in string:
            # extract the flag substring and assign it to the flag variable
            flag = string.split("[CTF[")[1].split("]")[0]
            break  # exit the loop if flag is found
    if flag is not None:
        break  # exit the outer loop if flag is found

# print the flag if it was found
if flag is not None:
    print("The hidden Flag: CTF[]", flag)
else:
    print("Flag not found.")

