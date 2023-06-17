try:
  num1=int (input ('Enter the First Number: num2-int (input ('Enter the second Number: '))
  operator=input ('Enter the Operator: ')
  if operator=='+'
                   ans=num1+num2
                   print('The answer is ' ‚ans)
  elif operator=='-'
                   ans=num1-num2
                   print ('The answer is '‚ans)
  elif operator=='*'
                   ans=num1*num2 
                   print('The answer is ',ans)
  elif operator=='/'
    try:
                   ans=num1/num2
                   print('The answer is '‚ans)
    except ZeroDivisionError:
                   print("Sorry! Division By Zero is not possible")
  else:
                   raise KeyError
except ValueError:
                   print("Sorry. You have entered an invalid number")
except KeyError:
                   print ("Sorry. You have entered an invalid operator')
