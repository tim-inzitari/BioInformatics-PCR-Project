## PCR Project
# Group 5  (nsp1)
# Tim Inzitari, Andrew Robinson, Weston Jessie



def find_compliment(RNA):
	#compliment the sequence

	#dictionary for complimenting
	compliment = {'A' : 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

	#set original sequence to a list
	bases = list(RNA)

	##replace each iteration against the dictionary
	bases = [compliment[base] for base in bases]

	#join back into a string
	#and return as tuple (RNA, cDNA)
	return (RNA,''.join(bases))


def pcr_run(DNA, fPrimer, rPrimer, cycles):
	#Run PCR
	return
## Original Code for our section, nsp1 from https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
with open('genome.txt', 'r') as file:
	RNA = file.read()

	#convert to uppercase
	RNA = RNA.upper()

	#Tuple (RNA, cDNA)
	DNA = find_compliment(RNA)

	#print(DNA) testing

	#get R primer and F primer (from Blast)
	# R being the reverse of F
	# Format ("Sequence", Starting Point, Ending Point, GC Content")

	#Primer pair #2
	fPrimer = ("TCGTACGTGGCTTTGGAGAC", 80, 99, 0.55)
	rPrimer = ("AGATCGGCGCCGTAACTATG", 419, 400, 0.55)

	#Print the sequences to replicate
	# should be 340 long
	print("\nReplicating: \n\nForward:")
	print(DNA[0][fPrimer[1]:rPrimer[1]])
	print("\nReverse:")
	print(DNA[1][fPrimer[1]:rPrimer[1]])

	#run the replication function for X Cycles
	#set right now to 20
	replicated_DNA = pcr_run(DNA, fPrimer, rPrimer, cycles=30)
