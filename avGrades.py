gradeArray = []
numGrades = int(input('How many grades do you have? '))

for i in range(0, numGrades, 1):
	newGrade = float(input('Enter your next grade: '))
	gradeArray.append(newGrade)
print(' ')
print('Your grades are: ')

for j in range(0, numGrades, 1):
	print(gradeArray[j])

bucket = 0

for k in range(0, numGrades, 1):
	bucket = bucket + gradeArray[k]

average = bucket / numGrades
print(' ')
print('Your average is: ', "{:.2f}".format(average))
print(' ')

highGrade = 0
lowGrade = 100

for l in range(0, numGrades, 1):
	if gradeArray[l] < lowGrade:
		lowGrade = gradeArray[l]
	if gradeArray[l] > highGrade:
		highGrade = gradeArray[l]
print('Your high grade is: ', highGrade)
print('Your low grade is: ', lowGrade)

