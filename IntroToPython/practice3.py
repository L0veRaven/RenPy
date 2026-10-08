course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('n'))
print(course.find('B'))
print(course.find('P'))
print(course.find('for'))
print(course.find('Beginners'))
pickASyde = course.find('p')
if (pickASyde == -1):
    print("This character does not exist.")

print(course.replace('for', '4'))
print(course.replace('for', 'x'))
print("Python" in course)