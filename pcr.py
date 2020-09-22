## PCR Project
# Group 5  (nsp1)
# Tim Inzitari, Andrew Robinson, Weston Jessie
from random import randint
import matplotlib.pyplot as plt

# Parameters
cycles = 20
hangOffAllowance = 0
copyLength = 200
e = 50

def find_compliment(RNA):
	f = RNA.replace('A','x')
	f = f.replace('T','A')
	f = f.replace('x','T')
	f = f.replace('C','x')
	f = f.replace('G','C')
	f = f.replace('x','G')
	return f


def pcr_run(DNA, fPrimer, rPrimer, cycles):
	#Run PCR
	return

def andrew_pcr_run(forwardStrands,reverseStrands,fPrimer,rPrimer):

	forwardSize = len(forwardStrands)
	reverseSize = len(reverseStrands)

	for x in range(0,forwardSize):
		index = forwardStrands[x].find(fPrimer)
		if index != -1:
			newStrand = forwardStrands[x][index:index+20+min(copyLength+randint(-e,e),len(forwardStrands[x])-(index+20))]
			newStrand = find_compliment(newStrand)
			newStrand = newStrand[::-1]
			reverseStrands.append(newStrand)

	for x in range(0,reverseSize):
		index = reverseStrands[x].find(rPrimer)
		if index != -1:
			newStrand = reverseStrands[x][index:index+20+min(copyLength+randint(-e,e),len(reverseStrands[x])-(index+20))]
			newStrand = find_compliment(newStrand)
			newStrand = newStrand[::-1]
			forwardStrands.append(newStrand)

	return;

## Original Code for our section, nsp1 from https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
with open('genome.txt', 'r') as file:

	RNA = file.read()

	#convert to uppercase
	RNA = RNA.upper()
	cDNA = find_compliment(RNA)
	cDNA = cDNA[::-1]

	# get a random sub string of size 150-250
	rsRNA = RNA[randint(25,75):randint(225,275)]

	#Primer pair #2
	fPrimer = (rsRNA[0:20])
	rPrimer = (find_compliment(rsRNA[len(rsRNA)-20:len(rsRNA)]))

	# Doing this so that I can read all strands left to right
	forwardStrands = []
	forwardStrands.append(RNA)
	reverseStrands = []
	reverseStrands.append(cDNA)

	# Same reason as above
	fPrimerA = fPrimer[0]
	rPrimerA = rPrimer[0][::-1]

	for _ in range(cycles):
		andrew_pcr_run(forwardStrands,reverseStrands,fPrimerA,rPrimerA)

	print("Total forward: "+str(len(forwardStrands))+"\n")
	print("Total reverse: "+str(len(reverseStrands)) + "\n")

	lengths = []

	for strand in forwardStrands:
		lengths.append(len(strand))

	for strand in reverseStrands:
		lengths.append(len(strand))

	plt.hist(lengths, bins= 30)
	plt.show()
