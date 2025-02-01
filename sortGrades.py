gArray = []
nGrades = int(input('How many grades do you have? '))

for i in range(0, nGrades, 1):
	grade = float(input('Enter your grade: '))
	gArray.append(grade)

print(' ')
print('Your grades are: ')

for j in range(0, nGrades, 1):
	print(gArray[j])

print(' ')
bucket = 0

for k in range(0, nGrades, 1):
	bucket = bucket + gArray[k]

av = bucket / nGrades
print('Your average is: ', "{:.2f}".format(av))
print(' ')

lowGrade = 100
highGrade = 0

for l in range(0, nGrades, 1):
	if gArray[l] < lowGrade:
		lowGrade = gArray[l]
	if gArray[l] > highGrade:
		highGrade = gArray[l]

print('Your high grade is: ', highGrade)
print('Your low grade is: ', lowGrade)

breadCrumb = 1

while (breadCrumb == 1):
    breadCrumb = 0
    for m in range(0, nGrades - 1, 1):
        if gArray[m] > gArray[m + 1]:
            swap = gArray[m]
            gArray[m] = gArray[m + 1]
            gArray[m + 1] = swap
            breadCrumb = 1

print(' ')
print('Your sorted grades are: ')

for n in range (0, nGrades, 1):
    print(gArray[n])

