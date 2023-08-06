# Task 1 :
def task1():
    name = "Shahidul islam"
    age = int(34)
    print("My name is %s and I am %d years old." % (name ,age) )

# Task 2 :
def task2():
    num1 = 1
    num2 = 1.652
    num1_float = float(num1)
    num2_int = int(num2)
    print("num1 :", num1)
    print("num1_float :", num1_float)
    print("num2 :", num2)
    print("num2_int :", num2_int)

# Task 3 :
def task3():
    a = "\"Python programming is fun!\""
    print("Length of" + a + " is " , len(a))
    print("8th character (index 7) in the string is " + a[8] )
    b = a[1:7]
    print(b + " I enjoy it!")

# Task 4 :
def task4():
    fruits = [ "apple", "banana", "cherry", "date"]
    fruits.append("grape")
    fruits.remove("banana")
    print("Length of the list is " , len(fruits))
    sliced_fruits = fruits[2:4]
    extra_fruits = ["kiwi" , "lemon"]
    combined = sliced_fruits + extra_fruits
    print("combined list are : " , combined)

# Task 5 :
def task5():
    num = 5
    mod = num % 2
    if mod > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")

# Task 6 :
def task6():
    i = 0
    while (i <= 10) :
        print( i )
        i = i + 1
    j = 0
    sum = 0
    while (j <= 100) :
        sum = sum + j
        j = j + 1
    print("sum is " , sum)

# Task 7 :
def calculate_square (num):
    num = int(num)
    print("Square is " , (num*num) )
def is_prime (num):
    num = int(num)
    i = 2
    t = 0
    while (i <= (num/2)) :
        if (num % i == 0) :
            t = 1
        i = i + 1

    if (t == 1) :
        print("This number is not prime")
    else :
        print("This number is prime")

# Task 8 :
def task8():
    student = {
        "name" : "Shahidul islam" ,
        "age" : 34 ,
        "grade" : "A+"
    }
    student["course"] = "DPT"
    print(student)
    print("All key-value pairs: ")
    for i,j in student.items():
        print(i,j)
task1()
task2()
task3()
task4()
task5()
task6()
calculate_square(7)
is_prime(29)
task8()