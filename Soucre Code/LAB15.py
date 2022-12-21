import string
def incremented(text,m):
    p = 0 #position
    for i in text:
        #ถ้า i เป็นตัวเล็ก เช็คว่า ord(i) + m เกิน 122 มั้ย
        #ถ้าเกิน ให้ลบออกด้วย 26 (กลับไปเป็น a)
        if(i in string.ascii_lowercase):#ตัวเล็ก
            p = ord(i) + m
            if(p > 122):
                p = ord(i) + m - 26
            print(chr(p),end="")
        elif(i in string.ascii_uppercase):#ตัวใหญ่
            p = ord(i) + m
            if(p > 90):
                p = ord(i) + m - 26
            print(chr(p),end="")
        else:#อักขระพิเศษ
            print(i,end="")

def main():
    text = input("Input your text: ")
    m = int(input("Increase: "))
    incremented(text,m)

if __name__ == "__main__":
    main()
