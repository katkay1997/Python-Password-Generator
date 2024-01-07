import string
import random

def main():
    pass_length = int(input("Enter password length: "))

    print("** choose character set for password from these options:"
          " 1.Numbers"
          " 2.Letters "
          "3.Special characters"
          " 4.Done")

    characterList = ""

    while(True):
      choice = int(input("Pick an option:"))
      if(choice == 1):
        characterList += string.ascii_letters
      elif(choice == 2):
        characterList += string.digits
      elif(choice == 3):
        characterList += string.punctuation
      elif(choice == 4):
        break
      else:
        print("Pick another option an then type 4")

    password = []

    for i in range(pass_length):
      randomnum = random.choice(characterList)
      password.append(randomnum)

    print("The new password is " + "".join(password))

if __name__ == '__main__':
  main()


