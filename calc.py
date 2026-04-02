def main();
def main() : 
    print ("Let's calculation. Select calculation type which you want")
    print ("1:add // 2:divide")
    calcType = int(input())

def add();
    if calcType == 1 :
        print("Start add, input number x, y that are integer")

def divide();        x = int(input("x = "))
        y = int(input("y = "))

        print("%d + %d = %d" % (x, y, add(x, y)))

    elif calcType == 2 :
        print("Start divide, input number a, b thar are integer")

        a = int(input("a = "))
        b = int(input("b = "))

        if b != 0 :
            print("%d / %d = %g" % (x, y, divide(x, y)))
        else : 
            print("b can't be 0")

    else : 
        print("it should be 1 or 2")



def add(x, y) :
    return x + y

def divide(a, b) : 
    if b != 0 :
        return round(a/b, 3)
    else :
        print("b can't be 0")


if __name__ == "__main__" :
    main()