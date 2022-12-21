money = int(input("Input money: "));
remaining = money

coin10 = money / 10
remaining = money % 10

coin5 = remaining / 5
remaining = remaining % 5

coin1 = remaining

print("Change coin 10 baht = %d"%coin10)
print("Change coin 5 baht = %d"%coin5)
print("Change coin 1 baht = %d"%coin1)

