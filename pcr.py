## PCR Project
# Group 5  (nsp1)
# Tim Inzitari, Andrew Robinson, Weston Jessie



def find_compliment(seq):
	#compliment the sequence

	#dictionary for complimenting
	compliment = {'A' : 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

	#set original sequence to a list
	bases = list(seq)

	##replace each iteration against the dictionary
	bases = [compliment[base] for base in bases]

	#join back into a string
	return ''.join(bases)


## Original Code for our section, nsp1 from https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
with open('genome.txt', 'r') as file:
	RNA = file.read()

	#convert to uppercase
	RNA = RNA.upper()

	DNA = find_compliment(RNA)

	# print(DNA) for testing the Find_Compliment

	#get R primer and F primer (from Blast)
	# R being the reverse of F

	#Print the sequences to replicate

	#run the replication function