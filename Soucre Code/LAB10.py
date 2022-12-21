def check_pythagoras_triple(a,b,c):
    if(a >= b):
        max_ = a
        min_ = b
        mid_ = c
    elif(b >= a):
        max_ = b
        min_ = a
        mid_ = c
    if(c >= max_):
        max_ = c
        min_ = a
        mid_ = b
    if (max_ == ((min_**2) + (mid_**2))**0.5):
        return True                           
    else:                                     
        return False


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(check_pythagoras_triple(a,b,c))
if __name__ == "__main__":
    main()