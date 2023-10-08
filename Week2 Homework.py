#task1
name = input("What is your name?")

print(f"Hello, {name}. good to meet you!")

#task2
c = float(input("Temperature in Celsius:"))
f = (c * 1.8) + 32

print(f"{c}C is equal to {f}F!")

#task3 with grammer fix
students = int(input("Total amount of students:"))
group = int(input("Required group size:"))
remainder = students % group

groups = students / group

if remainder == 1:
    print("There will be {:.0f} groups, with {:.0f} student left over.".format(groups, remainder))
else:
    print("There will be {:.0f} groups, with {:.0f} students left over.".format(groups, remainder))

#task4
sweets = int(input("Amount of sweets:"))
students = int(input("Amount of students:"))
total = sweets / students
remainder = sweets % students

print("Each pupil will have {:.0f} sweets each, with {:.0f} sweets remaining!".format(total, remainder))