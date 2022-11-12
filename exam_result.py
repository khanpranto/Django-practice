mark = int(input())

if mark > 100 or mark < 0:
    print("invalid")
else:

    if mark < 33 :
        print("fail")
    elif mark >= 33:
        print("pass")
    else:
        print("A+")