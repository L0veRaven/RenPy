course = "Python Programming"
print(len(course))
print(course[0])  # first character in string
print(course[-1])  # last character in string
print(course[-2])  # second-to-last character in string
print(course[0:3])  # first three characters of the first array of text
print(course[0:])  # full text
print(course[:3])  # first three characters of the first array of text
course = "Python\nProgramming"
print(course)

first = "Josh"
last = "Lancer"
# formatted string evaluated at runtime; the curly braces contain a variable
full = f"{first} {last}"
print(full)
# formatted string evaluated at runtime; the curly braces contain a variable
full = F"{first} {last}"
print(full)
# formatted string evaluated at runtime; the curly braces contain a variable
full = f"{len(first)} {last}"
print(full)
full = f"{len(first)} {2 + 2}"
print(full)

print(course.upper())
print(course.lower())

course = "        python programming      "
print(course.capitalize())
print(course.title())
print(course.strip())
print(course.rstrip())

course = "Python Programming"
print(course.find("pro"))
print(course.find("Pro"))
print(course.replace("m", "x"))
print("pro" in course)
print("Pro" in course)
print("swift" not in course)
