def if_test(score):
    if score >= 90:
        print("Excellent")
    #if score<=90 and score>=80:
    elif score >= 80:
        print("Very Good")
    elif score >= 70:
        print("Good")
    elif score >= 60:
        print("Pass")
    else:
        print("Fail")
if_test(100)
