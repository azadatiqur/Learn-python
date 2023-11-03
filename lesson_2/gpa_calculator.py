bengaliMarks = int(input("Please enter your marks in Bengali: "))
englishMarks = int(input("Please enter your marks in English: "))
mathMarks = int(input("Please enter your marks in Math: "))
scienceMarks = int(input("Please enter your marks in Science: "))

numberOfSubs = 4

avg = (bengaliMarks+englishMarks+mathMarks+scienceMarks)//4


if 100 >= avg >= 91:
    print("Your grade is : A+")
elif 90 >= avg >= 81:
    print("Your grade is : A")
elif 80 >= avg >= 71:
    print("Your grade is : B")
elif 70 >= avg >= 61:
    print("Your grade is : C")
elif 60 >= avg >= 41:
    print("Your grade is : D")
else:
    print("Your grade is : F")
