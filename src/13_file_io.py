"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os
# YOUR CODE HERE
p = os.path.dirname(os.path.abspath(__file__))
print(p)
f = open(f'{p}/foo.txt')
print(f.read())


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
n = open('bar.txt', "w")
n.write('this is a test\nto see if this working\nthe way i think it should')
n.close()
w = f'{os.path.dirname(os.path.abspath(__file__))}/../bar.txt'
z = open(w)
print(z.read())
bar = open(f'{os.getcwd()}/bar.txt').read()
print(bar)
