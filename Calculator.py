def Calculator():
  print("Welcome to Calculator...\nAdd: 1\nSubtraction: 2\nMultiplication: 3\nDivision: 4")
  selection = input()
  number1 = int(input("Enter first number: "))
  number2 = int(input("Enter second number: "))
  
  if(selection == "1"):
    print(number1,"+",number2,"=",(number1+number2))
  elif(selection == "2"):
    print(number1,"-",number2,"=",(number1-number2))
  elif(selection == "3"):
    print(number1,"X",number2,"=",(number1*number2))
  elif(selection == "4"):
    print(number1,"/",number2,"=",(number1/number2))
Calculator()
