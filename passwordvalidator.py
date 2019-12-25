passcode=input('Enter your password:')
special_characters=['&','+','@','$','#','%','(',')','!','^','-','=']
numbers = list(range(0,10))
passcode=list(passcode)
numbers=str(numbers)
if (len(passcode)<6):
  print("passcode should contain 6 characters")
elif (len(passcode)>15):
  print("passcode should contain atmost 15 characters")
elif not any(i in numbers for i in passcode):
    print("passcode should contain atleast one number")
elif not any(i in special_characters for i in passcode):
    print("passcode should contain atleast one character")
elif not any(i.isupper() for i in passcode):
  print("passcode should contain atleast one uppercase letter")
else:
  print("your passcode is valid")
