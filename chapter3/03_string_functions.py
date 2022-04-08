story = "once upon a time there was a youtuber named harry who uploaded python course with notes"
# print(story[0:6])

# String functions
# Size of string
print(len(story))

# Ends with returns True or False if the story ends with the given string
print(story.endswith("h notes"), story.endswith("hello"))

#Count occurance of a given string in story
print(story.count("on"))
print(story.count("a"))

# Capitalize first letter of a string
print(story.capitalize())

# Find index of a given string's first index of first word return -1 if not found
print(story.find("youtuber"), story.find('unavailable'), story[29])

# String replace replace old string with new string for all occurences
print(story.replace("youtuber", "tiktoker"))

