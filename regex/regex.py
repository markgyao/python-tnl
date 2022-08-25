import re
import sys
email=sys.argv[1]
print(f'email entered : {email}')

rgs=r"^.+@.+\.edu$"
rgs=r"^[^@]+@[^@]+\.edu$"
rgs=r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$" # equivlant ==> rgs=r"^\w+@\w+\.edu$", note \w is [a-zA-Z0-9_]
rgs=r"^\w+@\w+\.\w{3}$" # or ==> rgs=r"^\w+@\w+\.(com|edu|gov|org|net)$"
flag=re.IGNORECASE
flag=re.MULTILINE
flag=re.DOTALL

if re.search(rgs,email,flags=0):
    print("valid")
else:
    print("invalid")