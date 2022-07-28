import re

string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
print(string)

# substitute with Regex. Keep in mind that strings are immutable. So a new string needs to be created.
new = re.sub('[A-Z]', '', string)
print(string)
print(new)

new = re.sub('[a-z]', '', string)
print(new)

new = re.sub('[.,\']', '', string)
print(new)

# Remove chars and spaces
new = re.sub('[.,\' + " "]', '', string)
print(new)

string = string + "6 298 - 345"
print(string)

# Remove anything, but numbers
new = re.sub('[^0-9]', '', string)
print(new)
