import base64

print('Enter your string: ')
x = input()

string = x
string_bytes = string.encode("ascii")

base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode("ascii")


print(f"Encoded string: {base64_string}")
