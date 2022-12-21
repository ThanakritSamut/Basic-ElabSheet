def HalfPyramid(n):
    for i in range (0, n):
        for j in range (0, i+1):
            print("o", end=" ")
        print("") # new line
def main():
    n = int(input("N: "))
    HalfPyramid(n)

if __name__ == "__main__":
    main()
