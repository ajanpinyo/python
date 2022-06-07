import base64
import os
import sys

os.system('clear')

input_string = input("Enter your password: ")
input_bytes = input_string.encode("ascii")
b64bytes = base64.b64encode(input_bytes)
b64string = b64bytes.decode("ascii")

print(f"Password: {input_string}")
print(f"Base64: {b64string}")