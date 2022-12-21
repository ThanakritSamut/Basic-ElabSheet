import string
def Goodpassword(password):
    BIG_STRING = False
    SMALL_STRING = False
    NUMBER = False
    number = ['0','1','2','3','4','5','6','7','8','9']
    if(len(password) >= 10):
        if(password[0] in string.ascii_lowercase and password[1] not in number):
            for i in password:
                if i in string.ascii_letters:
                    if i in string.ascii_uppercase and BIG_STRING == False:
                        BIG_STRING = True
                    if i in string.ascii_lowercase and SMALL_STRING == False:
                        SMALL_STRING = True
                if i in number and NUMBER == False:
                    NUMBER = True
                if (BIG_STRING == True and SMALL_STRING == True and NUMBER == True):
                    return("GoodPassword")
            if NUMBER == False or BIG_STRING == False or SMALL_STRING == False:
                return("BadPassword")
        else:
            return("BadPassword")
    else:
        return("BadPassword")

def main():
    password = input("Input your password: ")
    print(Goodpassword(password))

if __name__ == "__main__":
    main()
