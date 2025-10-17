"""Create a dictionary to represent details of a student (name, roll number, register number, department, 
semester). Add new element total mark. Based on total mark find grade of student and add to 
dictionary. (total mark: 90>= A,82>=B,75>= C,60>= D ,50>=P). Delete roll number.*/"""
student = {
    "name": "john",
    "roll_number": "32",
    "register_number": "CS456",
    "department": "Computer Science",
    "semester": 5
}
print(f"befor\n {student}\n")
total_mark = 78  
student["total_mark"] = total_mark

if total_mark >= 90:
    grade = "A"
elif total_mark >= 82:
    grade = "B"
elif total_mark >= 75:
    grade = "C"
elif total_mark >= 60:
    grade = "D"
elif total_mark >= 50:
    grade = "P"
else:
    grade = "F" 

student["grade"] = grade
student.pop("roll_number", None)
print(f"after\n {student}\n")
