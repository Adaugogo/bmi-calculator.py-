weight = float(input('Please type in your weight'))
height =float(input('Please type in your height'))

bmi = weight / (height ** 2)
if bmi < 18.5:
    print ('underweight')
elif bmi <=25:
    print ('normal weight')
else:
    print ('overweight')
