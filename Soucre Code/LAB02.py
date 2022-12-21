from math import sqrt
def CalTriangle(b,h):
    area = (1/2) * b * h
    return area

def main():
    base = int(input("Base: "))
    height = int(input("Height: "))
    area = CalTriangle(base,height)
    print("Area of Triangle is: %d"%area)
if __name__ == "__main__":
    main()