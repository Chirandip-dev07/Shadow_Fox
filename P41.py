weight = int(input("Enter the weight in kilograms : "))
height = float(input("Enter the height in metres : "))
BMI = weight / height**2

if BMI>=30:
    print("Obesity")
elif BMI<30 and BMI>=25:
    print("Overweight")
elif BMI<25 and BMI>=18.5:
    print("Normal")
else:
    print("Underweight")