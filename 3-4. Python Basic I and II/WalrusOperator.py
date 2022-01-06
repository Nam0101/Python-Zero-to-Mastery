a='helllllooooooo'

if (n:=len(a))>10:
    print(f"it too long about {n} characters")

while (n:=len(a))>1:
    print(a[:-1])
    a = a[:-1]
if (n:=len(a))>10:
    print(f"it too long about {n} characters")
else:
    print(n)