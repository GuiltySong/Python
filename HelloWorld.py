print("Hello World")
print("*" * 10)
print("")
x = 1
unit_price = 3

student_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(student_count)
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:])
print(course_name[:])
print(course_name[:3])


first = "Jason"
last = "Liu"
full = f"{first} {last}"
print(full)

print(course_name.upper())

print("Hello World :)")


message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "🙁"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
