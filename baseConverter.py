alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
baseMax = 36

############################################
#
### convert an input from base r to 10    max=36 => you can increase it by changin alphabet
#
##############################################

def ConvertToBaseTen(number , base):
  base = int(base)
  alphabetBase = ''
  tenBase = 0
  if base >= 2 and base <= baseMax:
    alphabetBase = alphabet[0:base]
  else:
    return 'base must be between 2 and 36'
  number = number[::-1].upper()
  counter = -1
  for i in number:
    counter += 1
    length = alphabetBase.find(i)
    tenBase += length * (base ** counter)
  return tenBase
  
############################################
#
### conver an input from base 10 to r
#
##############################################
def ConvertFromTenToR(number , base):
  base = int(base)
  listOfReminder = []
  alphabetBase = ''
  if base >= 2 and base <= baseMax:
    alphabetBase = alphabet[0:base]
  else:
    return 'base must be between 2 and 36'
  
  while number >= base:
    i = number % base
    number //= base
    listOfReminder.append(alphabetBase[i])
  listOfReminder.append(alphabetBase[number])
  return ''.join(listOfReminder[::-1])

def main():
  while True:
    try:
      number1 , base1 = input("please enter your first number and it\'s base? ").split()
      number2 , base2 = input("please enter your second number and it\'s base? ").split()
    except:
      print("please enter values correctly like \'56 16")
      continue

    else:
      sum = ConvertToBaseTen(number1 , base1) + ConvertToBaseTen(number2,base2)
      subtraction = ConvertToBaseTen(number1 , base1) - ConvertToBaseTen(number2,base2)

      print(f"({number1}) in base {base1} + ({number2}) in base {base2} are=> ")
      print(f"sum = ({sum}) in base 10 and ({ ConvertFromTenToR(int(sum),base1) }) in base {base1}")

      print(f"({number1}) in base {base1} - ({number2}) in base {base2} are=> ")
      print(f"subtraction = ({subtraction}) in base 10 and ({ ConvertFromTenToR(int(sum),base1) }) in base {base1}")

      if not input("if you want to continue enter y? ") == 'y':
        break
        
if __name__ == '__main__':
  main()
    
