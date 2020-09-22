# BioInformatics-PCR-Project
for class

## Notes

Since BLAST does not give primers that align perfectly, and we are only going to allow perfect allignments, we must pick our own primers.

Currently these primers are selected by first randomly selecting a sub-region of our gene that is between 150-250 nucleotides long, and then using the first 20 and last 20 nucleotides as forward and reverse primers (the reverse primer being the compliment of course).

The simulation is done in two "buckets" which account for the strands that are duplicated in the forward and reverse way. This simplification makes the solution much easier to follow.

Once the simulation is over it plots the lengths of all the strands on a histogram.
