import re

pattern = re.compile(r"[A-Za-z0-9!@#$%^&]{8,}\d")
while True:
    password =input('Enter your password:')
    if(password.isalnum()):
        break
    a=pattern.fullmatch(password)
    if(a):
        print('Validate password')
    else:
        print('Unvalidate password')

# Python-RegEx
# https://www.w3schools.com/python/python_regex.asp

# Solution-Repl
# https://repl.it/@aneagoie/password-regex
