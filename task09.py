a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a == b == c:
    print("Teng tomonli")
if a == b or b == c or a == c:
    print("teng yonli")
else:
    print("turli tomonli")