first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
birth_year =  input("What is your birth year? ")

age = 2025 - int(birth_year)
print(age)

new_patient = True
print(new_patient)

print("Hello " + first_name + " " + last_name + ", " + str(age) + ". New Patient: " + str(new_patient))