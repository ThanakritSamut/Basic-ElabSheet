def Healthy(BMI):
    if(BMI < 18.5):
        print("Underweight")#น้ำหนักน้อย
    elif(BMI < 23):
        print("Healthy weight")#น้ำหนักปกติ
    elif(BMI < 25):
        print("Overweight")#น้ำหนักเกิน
    elif(BMI < 30):
        print("Obese")#อ้วน
    else:
        print("Clinically Obese")#อ้วนมากเกินไป

def main():
    Weight = float(input("Your weight(kg): "))
    Height = float(input("Your height(cm): "))
    BMI = Weight/((Height/100)*(Height/100))
    Healthy(BMI)
if __name__ == "__main__":
    main()
