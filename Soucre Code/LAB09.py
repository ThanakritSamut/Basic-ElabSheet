def max_mid_min(A,B,C):
    if(A > B):
        MAX = A
        MIN = B
    else:
        MAX = B
        MIN = A

    if (C > MAX):
        MAX = C
    if(C < MIN):
        MIN = C
    MID = (A + B + C) - (MAX + MIN)
    print(MIN, MID, MAX)

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    max_mid_min(A,B,C)
if __name__ == "__main__":
    main()
