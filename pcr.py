## PCR Project
# Group 5  (nsp1)
# Tim Inzitari, Andrew Robinson, Weston Jessie



def find_compliment(RNA):
	#compliment the sequence
	DNA = ""
	return DNA


## Original Code for our section, nsp1 from https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
with open('genome.txt', 'r') as file:
	RNA = file.read()

	#convert to uppercase
	RNA = RNA.upper()

	DNA = find_compliment(RNA)

	#get R primer and F primer (from Blast)
	# R being the reverse of F

	#Print the sequences to replicate

	#run the replication function