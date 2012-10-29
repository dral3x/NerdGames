import sys
import re

# metodo per il calcolo dei recycled numbers tra n e m
def number_of_rn_between(n, m): # n ed m sono ancora stringe
	
	i_n = int(n)
	i_m = int(m)
	count = 0

	for a in range(i_n, i_m):
		s = str(a)

		known = []
		for l in range(1, len(s)):

			b = int(s[l:] + s[:l])

			#print a, b

			if a < b and b <= i_m and not b in known:
				# trovato RN
				#print "match!", a, b
				count += 1
				known.append(b)

	return count


#
# lettura del file
#

filename = sys.argv[1]
file = open(filename, "r")

# leggo il numero di test T in testCases
line = file.readline();
if not line: file.close();
testCases = int(line);

#print "test cases:", testCases

regexpr = re.compile('^(\d*) (\d*)$')

# leggo il resto del file
t = 1
while t<=testCases:

	line = file.readline()
	if not line: break
	if regexpr.match(line):
		# riga ben formata
		
		n = regexpr.match(line).group(1)
		m = regexpr.match(line).group(2)

		#print "n:", n, "m:", m

		count = number_of_rn_between(n, m)

		print "Case #{0}: {1}".format(t, count)

	t += 1
		
file.close()