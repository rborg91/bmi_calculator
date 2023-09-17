name = input("Enter your name: ")

weight = int(input("Enter your weight in kg: "))

height = int(input("Enter your height in cm: "))

BMI = (weight/height/height * 10000)

print(name + ", you're BMI is " + str(BMI))

if BMI>0:
    if(BMI<18.5):
        print("You are underweight")
    elif(BMI<=24.9):
        print("You are at a normal weight")
    elif(BMI<=29.9):
        print("You are overweight")
    elif(BMI<=34.9):
        print("You are obese")
    elif(BMI<=39.9):
        print("You are serverely obese")
    else:
        print("You are morbidly obese")
