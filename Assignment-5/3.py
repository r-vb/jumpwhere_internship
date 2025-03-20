# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
# Sample String : 'ab'
# Expected Result : 'abab'
# Sample String : 'f'
# Expected Result : Empty String 

def string(str):
    if len(str) < 2:
        return ''
    return str[:2] + str[-2:]

print(string('thisisniceone'))
print(string('ab'))
print(string('f'))
