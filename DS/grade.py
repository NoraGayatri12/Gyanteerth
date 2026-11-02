marks=int(input("Enter marks"))
if marks>=80 and marks<=100:
    print("A Grade")
elif marks<80 and marks>=50:
    print("B Grade")
elif marks<50 and marks>=20:
    print("C Grade")
else:
    print("Fail")