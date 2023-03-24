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
unique_chars = set(''.join([''.join(sublist) for sublist in nested_list]))
print("Solution #1: Number of unique characters in the list:", len(unique_chars))

# 2. The most common character in the list.
most_common_char = Counter(''.join([''.join(sublist) for sublist in nested_list])).most_common(1)[0][0]
print("Solution #2: Most common character in the list:", most_common_char)

# 3. The character(s) that appear(s) the least in the list.
least_common_chars = Counter(''.join([''.join(sublist) for sublist in nested_list])).most_common()[:-2:-1]
print("Solution #3: Least common character(s) in the list:", least_common_chars[0][0])

# 4. How many times the word "challenge" appears in the list.
num_challenge = sum([sublist.count("challenge") for sublist in nested_list])
print("Solution #4: Number of times the word 'challenge' appears in the list:", num_challenge)

# 5. The fourth character of each string in the list.
fourth_chars = [sublist[i][3] for sublist in nested_list for i in range(len(sublist))]
print("Solution #5: Fourth character of each string in the list:", fourth_chars)

# 6. The number of strings in the list that start with the letter "L".
num_start_L = sum([sublist[0][0] == 'L' for sublist in nested_list])
print("Solution #6: Number of strings in the list that start with the letter 'L':", num_start_L)

# 7. How many unique words are in the list?
unique_words = set([word for sublist in nested_list for word in sublist])
print("Solution #7: Number of unique words in the list:", len(unique_words))

# 8. The longest string in the list.
longest_string = max([' '.join(sublist) for sublist in nested_list], key=len)
print("Solution #8: Longest string in the list:", longest_string)

# 9. The shortest string in the list.
shortest_string = min([' '.join(sublist) for sublist in nested_list], key=len)
print("Solution #9: Shortest string in the list:", shortest_string)

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
    print("Solution #10: The hidden Flag:", flag)
else:
    print("Flag not found.")

