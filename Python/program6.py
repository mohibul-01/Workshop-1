#strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.

my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)

#replace(old, new): Returns a new string with all occurrences of old replaced by new.

my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)

#split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.

my_str = 'hello world'

split_words = my_str.split()
print(split_words)

#join(iterable): Joins elements of an iterable into a string with a separator.

my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)

#startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)

#endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)

#find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)

#count(substring): Returns the number of times a substring appears in a string.
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)

#capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

#isupper(): Returns True if all letters in the string are uppercase and False if not.
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False


#islower(): Returns True if all letters in the string are lowercase and False if not.
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True


#title(): Returns a new string with the first letter of each word capitalized.
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
