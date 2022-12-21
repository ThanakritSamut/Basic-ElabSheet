def convert(F):
    K = (5/9)*(F-32) + 273
    return K

def main():   
    F = int(input("Input temperature in Fahrenheit: "))
    Kelvin = convert(F)

    print("Temperature in Kelvin: %.2f"%Kelvin)

if __name__ == "__main__":
    main()