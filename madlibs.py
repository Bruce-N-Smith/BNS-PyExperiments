# tutorial based on https://www.youtube.com/watch?v=8ext9G7xspg 
# there are 3 ways to approach creating a string that says "blah blah ________" with a variable for the blank
# print("string" + variable)
# print("string {}".format(variable)
# print(f"string {variable}") F-String is nice and clean
print("Welcome to the MadLib game!")

# gather up variables in use, and run them first 
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

# make a variable that contains a function, string, and another variable
# note the backslash acts as a line break in Python code, but doesn't show in the program as used by clients, it's just to help Devs
# note when I run this in Python 3.10.4 it complains about the next line and an unterminated string literal and points to the f character
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \ 
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
# end program
# if you copy all this text and drop it in a .py file in your VSCode you can run it in a terminal there for testing and tweaking
# packaging this code up so that it can run on a web page or a desktop is a whole other bit of work
