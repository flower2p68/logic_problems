score = int(input("What's your score? "))

if score >=90 :
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score< 80:
    print("Grade C")
elif score>= 60 and score<70:
    print("Grade: D")
else:
    print("Grade: F ")
    # We are doing two questions in the line. We could do just one:

# Grade assignment based on score
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
