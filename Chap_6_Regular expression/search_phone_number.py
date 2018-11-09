import re

phone = "(08) 38-351056 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone number: ", num)

# Remove anything other than digits \D: match a non-digit
num = re.sub(r'\D', "", phone)
print("Phone number: ", num)