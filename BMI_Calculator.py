# calculate BMI


#h,w = input('h,w').split

h = input('enter your height(cm):')
w = input('enter your weight(kg):')
h = float(h) / 100
w = float(w)  

BMI = w / pow(h, 2)

print('your BMI is:' , round(BMI, 2))

if BMI < 18.5:
    print('you are UNDERWEIGHT')
elif 18.5 <= BMI <= 24.9:
    print('you are NORMAL')
elif 25 <= BMI <= 29.9:
    print('you are OVERWEIGHT')
elif 30 <= BMI <= 34.9:
    print('you are OBESE')
else:
    print('you are EXTEREMLY OBESE')

print("The End")