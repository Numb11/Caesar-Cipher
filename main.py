import string
alphabetl = string.ascii_lowercase
alphabeth = string.ascii_uppercase
encrypted = []
while True:
 encrypted = []
 plaintext = input("Enter message to be encrytped:")
 shift = int(input("Enter the shift value:"))
 for i in plaintext:
     if i.isupper():
      encrypted.append(alphabeth[alphabeth.index(i)+shift])
     else:
      encrypted.append(alphabetl[alphabetl.index(i)+shift])
 encrypted = "".join(encrypted)
 print(f"{plaintext}, encrytped is {encrypted}")
