# tutorial based on https://www.youtube.com/watch?v=8ext9G7xspg 
# create a string that says "blah blah ________" with a variable for the blank
# three ways to approach this
# print("string" + variable)
# print("string {}".format(variable)
# print(f"string {variable}") F-String is nice an clean
print("Welcome to the MadLib game!")

# gather up variables in use
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

# make a variable that contains a function, string, and another variable
# note the backslash acts as a line break in Python code, but doesn't show in the program as used by clients
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \ 
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
#end program
