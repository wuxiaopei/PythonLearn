from sys import argv

script, filename = argv

print "We're going to erase %r." % filename

print "If you don't want that, hit CTRL-C(^C)."

print "IF you do want that, hit RETURN."

raw_input("?")

print "Opendin the file..."

target = open(filename, 'w')

print "Truncating the file .GoodBye!"

target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to the file."

target.write(line1)8u9
target.write("/n")
target.write(line2)
target.write("/n")
target.write(line3)
target.write("/n")

print "And finally, we close it."

target.close()
