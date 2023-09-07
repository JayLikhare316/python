classesheld = int(input("Enter the number of classes held: "))
classesattended = int(input("Enter the number of classes attended: "))

studentattendance = (classesattended / classesheld) * 100

if studentattendance >= 75:
    print(f"Percentage of classes attended: {studentattendance}%")
    print("You are allowed to sit in the exam.")
else:
    print(f"Percentage of classes attended: {studentattendance}%")
    print("You are not allowed to sit in the exam.")
