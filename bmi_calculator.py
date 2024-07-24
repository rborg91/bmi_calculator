name = input("Enter your first name: ")

weight = float(input("Enter your weight in kilograms (kg): "))

height = float(input("Enter your height in centimetres (cm): "))

BMI = round((weight/height/height * 10000), 2)

print("Hello " + name + ",")
print("Your BMI is " + str(BMI))

if BMI>0:
    if(BMI<18.5):
        print("Underweight")
    elif(BMI<=24.9):
        print("Normal weight")
    elif(BMI<=29.9):
        print("Overweight")
    elif(BMI<=34.9):
        print("Obese")
    elif(BMI<=39.9):
        print("Serverely obese")
    else:
        print("Morbidly obese")
