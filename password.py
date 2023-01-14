import secrets
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

alphabet = lowercase + uppercase + digits + special_chars

password_length = 12

while True:
  password = ''
  for i in range(password_length):
    password += ''.join(secrets.choice(alphabet))

  if (any(char in lowercase for char in password) and
        any(char in uppercase for char in password) and
        any(char in digits for char in password) and
        any(char in special_chars for char in password)):
            break

print(password)
