gradeArray = []
'''gradeArray.append(5.5)
gradeArray.append(3.2)
gradeArray.append(-2.7)
gradeArray[1] = 25.5
print(gradeArray)
print(gradeArray[1])'''
numGrades = int(input("How many grades do you have? "))

for i in range(0, numGrades, 1):
	grade = float(input("Input the grade: "))
	gradeArray.append(grade)

for j in range(0, numGrades, 1):
	print("Your ", "#", j+1, " grade is ", gradeArray[j])

print("Thank you for playing")
