# The MIT License (MIT)

# Copyright (c) 2014 INSPIRE Lab, BITS Pilani

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
Provides a script to plot results
"""


import sys

import matplotlib.pyplot as plt


def main():

	try:
		inFile = open(sys.argv[1], 'r')
	except Exception, e:
		print 'A valid input file was not passed'
		sys.exit(-1)

	y = []
	x = []
	
	lines = inFile.readlines()
	count = 1
	noGain = 0

	for line in lines:
		currentLine = line.strip().split()
		
		try:
			if int(currentLine[0]) == 0:
				noGain += 1
			y.append(int(currentLine[0])) 
			x.append(count)
		except:
			pass

		count += 1


	# Compute redundancy
	redundancy = 0
	for i in range(len(y)):
		redundancy += y[i]

	print 'redundancy:', redundancy


	# Compute information gain
	infoGain = []
	infoGainX = []
	infoGainCount = 1
	bins = []
	for i in range(10):
		bins.append(i)

	nineCount = [0 for i in range(10)]
	for i in range(len(y)):
		if i < 1:
			continue
		temp = y[i] - y[i-1]
		if temp == 0:
			noGain += 1
		infoGain.append(temp)
		infoGainX.append(infoGainCount)
		
		nineCount[temp] += 1
		infoGainCount += 1

	#print 'nineCount:', nineCount
	# plt.bar(x, y)
	# plt.plot(x, y)
	print len(y)
	# plt.plot(x,y)
	# plt.bar(bins, nineCount)
	
	plt.title('FreeWorld Redundancy')
	# plt.title('Office Information Gain Histogram')
	# plt.xlabel('Number of new cells visited in one timestep')
	# plt.ylabel('Frequency of occurance')
	plt.xlabel('Number of timesteps')
	# plt.ylabel('Percentage of Map covered')
	plt.ylabel('Number of redundant moves')
	plt.show()
	print 'noGain:', noGain


if __name__ == '__main__':
	
	main()