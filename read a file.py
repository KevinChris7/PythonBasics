
# open the file in read mode
personal_details = open("details", "r")

# .readable returns true or false to open the file
print(personal_details.readable())



# .read()
# .readline() for single row
for person in personal_details.readlines():
    print(person)

# close the file
personal_details.close()
