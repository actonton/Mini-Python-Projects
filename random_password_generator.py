import random
import string

# Shuffle function to create reorder password
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter1= random.choice(string.ascii_letters.upper())  
uppercaseLetter2= random.choice(string.ascii_letters.upper()) 

#Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter1= random.choice(string.ascii_letters.lower())
lowercaseLetter2= random.choice(string.ascii_letters.lower())

#Generate a random digit
digit1 = random.choice(string.digits)
digit2 = random.choice(string.digits)

#Generate a random punctuation
punctuationSign1 = random.choice(string.punctuation)
punctuationSign2 = random.choice(string.punctuation)

#Generate a password
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
print(password)
change = input("Do you want to shuffle your password? ").lower()
if change != "yes":
    quit()
else:
    new_password = shuffle(password)
    print(new_password)