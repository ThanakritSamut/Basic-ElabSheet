import string
def CheckLetter(text):
    BIG = string.ascii_uppercase
    SMALL = string.ascii_lowercase
    big_letter = 0
    small_letter = 0
    for i in text:
        if i in BIG:
            big_letter += 1
        elif i in SMALL:
            small_letter += 1
    BL = big_letter
    SL = small_letter
    print("Big letter in this text is: %d"%BL)
    print("Small letter in this text is: %d"%SL)
def main():
    text = input(str("Input text: "))
    CheckLetter(text)
if __name__ == "__main__":
    main()