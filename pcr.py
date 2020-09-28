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

def get_GC(strand):
	#print((strand.count('C')+strand.count('G'))/(float(len(strand))))
	return ((strand.count('C')+strand.count('G'))/(float(len(strand))))
	return 0;

def find_compliment(RNA):
	f = RNA.replace('A','x')
	f = f.replace('T','A')
	f = f.replace('x','T')
	f = f.replace('C','x')
	f = f.replace('G','C')
	f = f.replace('x','G')
	return f

def andrew_pcr_run(forwardStrands,reverseStrands,fPrimer,rPrimer, GcList):

	forwardSize = len(forwardStrands)
	reverseSize = len(reverseStrands)

	for x in range(0,forwardSize):
		index = forwardStrands[x].find(fPrimer)
		if index != -1:
			newStrand = forwardStrands[x][index:index+20+min(copyLength+randint(-e,e),len(forwardStrands[x])-(index+20))]
			newStrand = find_compliment(newStrand)
			newStrand = newStrand[::-1]
			reverseStrands.append(newStrand)
			GcList.append(get_GC(newStrand))

	for x in range(0,reverseSize):
		index = reverseStrands[x].find(rPrimer)
		if index != -1:
			newStrand = reverseStrands[x][index:index+20+min(copyLength+randint(-e,e),len(reverseStrands[x])-(index+20))]
			newStrand = find_compliment(newStrand)
			newStrand = newStrand[::-1]
			forwardStrands.append(newStrand)
			GcList.append(get_GC(newStrand))

	return;

## Original Code for our section, nsp1 from https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
with open('genome.txt', 'r') as file:

	RNA = file.read()

	#convert to uppercase
	RNA = RNA.upper()
	cDNA = find_compliment(RNA)
	cDNA = cDNA[::-1]
	totalStrands = [0]*8
	GC_List = []
	for i in range(8):
		totalStrands[i] = [0]*cycles

	for x in range (0,8):
		# get a random sub string of size 150-250
		rsRNA = RNA[25+x*10:325-x*10]
		print("rsRNA length: " + str(len(rsRNA))+"\n")

		primer_GC = 0.0
		rPrimer_GC = 0.0


		# Throw out any primers with GC content not within 40% <= GC <= 60%
	while(((primer_GC > 0.6) or (primer_GC < 0.4)) and ((rPrimer_GC > 0.6) or (rPrimer_GC < 0.4))):
			#Primer pair #2
		fPrimer = (rsRNA[0:20])
		rPrimer = (find_compliment(rsRNA[len(rsRNA)-20:len(rsRNA)]))

			# See if Acceptable GC for Primer
		primer_GC = get_GC(fPrimer)
		rPrimer_GC = get_GC(rPrimer)


		# Doing this so that I can rea#d all strands left to right
		forwardStrands = []
		forwardStrands.append(RNA)
		GC_List.append(get_GC(RNA))
		reverseStrands = []
		reverseStrands.append(cDNA)
		GC_List.append(get_GC(cDNA))

		# Same reason as above
		fPrimerA = fPrimer
		rPrimerA = rPrimer[::-1]


		cycle = 0
		for y in range(cycles):
			print("Start Cycle {0}".format(cycle))
			andrew_pcr_run(forwardStrands,reverseStrands,fPrimerA,rPrimerA, GC_List)
			totalStrands[x][y] = int(len(forwardStrands) + len(reverseStrands))
			cycle+=1

		print("Total forward: "+str(len(forwardStrands))+"\n")
		print("Total reverse: "+str(len(reverseStrands)) + "\n")

		lengths = []

		for strand in forwardStrands:
			lengths.append(len(strand))

		for strand in reverseStrands:
			lengths.append(len(strand))

		plt.hist(GC_List, bins= 50)
		plt.title("Strand Count: {0}".format(len(forwardStrands)))
		plt.xlabel("GC Count")
		plt.ylabel("Occurances")
		plt.show()

	print(totalStrands)
	print("Average GC Content is: {0}".format(sum(GC_List)/len(GC_List)))
