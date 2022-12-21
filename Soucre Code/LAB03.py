def CheckQaudrant(x,y):
    if(x == 0 and y == 0):
        return ("Point on origin point!")
    elif((x == 0 and y > 0) or (x == 0 and y < 0)):
        return("Point on Y axis")
    elif((x > 0 and y == 0) or (x < 0 and y == 0)):
        return("Point on X axis ")
    elif(x > 0 and y > 0):
        return ("Point on Qaudrant1")
    elif(x < 0 and y > 0):
        return("Point on Qaudrant2")
    elif(x < 0 and y < 0):
        return ("Point on Qaudrant3")
    elif(x > 0 and y < 0):
        return ("Point on Qaudrant4")
def main():
    x = int(input("X: "))
    y = int(input("Y: "))
    answer = CheckQaudrant(x,y)
    print(answer)

if __name__ == "__main__":
    main() 