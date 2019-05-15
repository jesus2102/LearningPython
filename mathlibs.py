#MadLibs - Practice Inout and Output
#
#Template:
#   I enjoy practice! I find it helps me to __(verb)__ better.
#   Without practice, my __(noun)__ would probably not even work.
#    My code is getting more __(adjetive)__ every single day!


#TODO: Prompt the user for parts of speech and store them in variables

v = input("Please enter a verb: ")
n = input("Now I need a noun: ")
a = input("Finally enter an adjetive: ")

#TODO: Output the template to the screen with the blanks filled out with what the user stated

s = """
I enjoy practice! I find it helps me to %s better.
Without practice, my %s would probably not even work.
My code is getting more %s every single day!
""" % (v, n, a)

print(s)
