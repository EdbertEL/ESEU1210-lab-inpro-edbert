
age = int(input("How old are you? "))
if 0 <= age <= 150:
    age_future = str(age + 50)
    if len(age_future) >= 3:
        print("In 50 years, you will be", age_future, "years old.")
    elif len(age_future) == 2:
        new_age = "0" + age_future
        print("In 50 years, you will be", new_age, "years old.")
else:
    print("Your age must be between 0 to 150!")