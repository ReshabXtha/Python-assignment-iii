import csv

courses = ["HTML&CSS", "PHP", "Python", "R", "C#"]


def course_inq():
    print(courses)


def reg_student():
    print("Enter the name=")
    name = input()
    print("Enter address=")
    address = input()
    print("Enter contact no=")
    contact = input()
    print("Enter the email=")
    email = input()
    print("Select the course", courses)
    course = input()
    print("Enter the installment amount=")
    amount = int(input())
    due = 20000 - amount
    if amount == 10000 or amount == 20000:
        with open('Student.csv','a+')as file:
            wrt = csv.writer(file)
            wrt.writerow([name, address, contact, email, course, amount, due])


def dis_student():
    with open('Student.csv')as csv_file:
        rd = csv.reader(csv_file)
        for i in rd:
            print(i)


def del_student():
    print("Enter the name=")
    name = input()
    line = []
    with open('Student.csv', 'r')as readFile:
        rd = csv.reader(readFile)
        for i in rd:
            line.append(i)
            for j in i:
                if j == name:
                    line.remove(i)
    with open('Student.csv', 'w')as writeFile:
        wrt = csv.writer(writeFile)
        wrt.writerow(line)


def edit_student():
    print("Enter the value=")
    key = input()
    print("Enter the change=")
    rep = input()
    line = []
    with open('Student.csv', 'r')as readFile:
        rd = csv.reader(readFile)
        for i in rd:
            line.append(i)
            for j in i:
                if j == key:
                    k = i.index(j)
                    i[k] = rep
                    line.append(i)
    with open('Student.csv', 'w')as writeFile:
        wrt = csv.writer(writeFile)
        wrt.writerow(line)


print("""Enter the choice
            1)Display Course
            2)Register
            3)Display Student
            4)Edit Information
            5)Delete Student
            """)
q = int(input())
if q == 1:
    course_inq()
elif q == 2:
    reg_student()
elif q == 3:
    dis_student()
elif q == 4:
    edit_student()
elif q == 5:
    del_student()
else:
    print("invalid input")
