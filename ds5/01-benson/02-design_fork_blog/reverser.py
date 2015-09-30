# author = "Jason K and Callum"
import sys    #gives us access to stdin

for line in sys.stdin:
	sys.stdout.write(line.replace("\n","")[::-1] + "\n")