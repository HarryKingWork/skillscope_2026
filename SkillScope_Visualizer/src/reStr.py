import re

# Function to concatenate strings
def concatenate_strings(str1, str2):
    return str1 + str2

# Function to slice a string (get substring)
def slice_string(s, start, end):
    return s[start:end]

# Function to find the length of a string
def string_length(s):
    return len(s)

# Function to check if a string contains another string
def contains_string(main_str, sub_str):
    return sub_str in main_str

# Function to convert string to uppercase
def to_uppercase(s):
    return s.upper()

# Function to convert string to lowercase
def to_lowercase(s):
    return s.lower()

# Function to replace a substring in a string
def replace_substring(s, old, new):
    return s.replace(old, new)

# Function to split a string by a delimiter
def split_string(s, delimiter):
    return s.split(delimiter)

# Function to join a list of strings into one string
def join_strings(string_list, delimiter):
    return delimiter.join(string_list)

# Function to strip whitespace from the beginning and end of a string
def strip_string(s):
    return s.strip()

# Function to check if a string starts with a specified prefix
def starts_with(s, prefix):
    return s.startswith(prefix)

# Function to check if a string ends with a specified suffix
def ends_with(s, suffix):
    return s.endswith(suffix)

# Function to find the index of the first occurrence of a substring
def find_substring(s, sub_str):
    return s.find(sub_str)

# Function to check if a string is a valid integer
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Function to check if a string is a valid float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to format a string (f-strings)
def format_string(name, age):
    return f"My name is {name} and I am {age} years old."

# Function to encode a string to bytes (utf-8)
def encode_string(s):
    return s.encode('utf-8')

# Function to decode bytes back to string (utf-8)
def decode_bytes(b):
    return b.decode('utf-8')

# Function to check if a string is alphanumeric
def is_alphanumeric(s):
    return s.isalnum()

# Function to check if a string is a digit
def is_digit(s):
    return s.isdigit()

# Function to replace all occurrences of a pattern using regex
def regex_replace(s, pattern, replacement):
    return re.sub(pattern, replacement, s)

# Function to find all occurrences of a pattern using regex
def regex_findall(s, pattern):
    return re.findall(pattern, s)

# Function to validate email using regex
def is_valid_email(s):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(email_regex, s))

# Function to split a string into lines
def split_lines(s):
    return s.splitlines()

# Function to capitalize the first letter of each word in a string
def capitalize_words(s):
    return s.title()

# Function to check if a string is a valid JSON string
import json
def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except ValueError:
        return False

# Function to repeat a string multiple times
def repeat_string(s, times):
    return s * times