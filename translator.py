

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter the Phrase : ")))

# Example of Try and Except Blocks
try:
    number = int(input("Enter the value"))
    print(number)
except ValueError as err:
    print(err)






