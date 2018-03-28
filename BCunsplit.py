#!/usr/bin/env python3

## lets try to take a two unpaired read files, cut out the bp from the reverse,
## and tack it onto the forward.
## have to preserve the fastq format so that pandaseq can do unsplit3.py forward_reads reverse_reads

#The first six bps and quality ratings of the reverse reads should be chopped off and placed after
#the first six bps of the forward reads and quality ratings. For use with fastq files. It will spit
#out two files, with the names: "rearranged_[your orignial forward and reverse read file names].fastq".

import itertools ##to let us jump around 
from sys import argv

script, forward_file, reverse_file = argv

forwardlabels=[]
reverselabels=[]
forwardreads=[]
forwardreadsq=[]
reversereads=[]
reversereadsq=[]
forwardBC=[]
forwardBCq=[]
reverseBC=[]
reverseBCq=[]

with open(forward_file) as foop:

	#labels:

	for h in itertools.islice(foop, 0, None, 4):
		forwardlabels.append(h)

##forward sequencies, barcodes: 

	foop.seek(0)
    
	for i in itertools.islice(foop, 1, None, 4):
		forwardreads.append(i[6:])        
		forwardBC.append(i[0:6])

##forward quality info:

	foop.seek(0)

	for j in itertools.islice(foop, 3, None, 4):
		forwardreadsq.append(j[6:])
		forwardBCq.append(j[0:6])

## reverse reads and sequences:

with open(reverse_file) as coop:

#labels:

	for h in itertools.islice(coop, 0, None, 4):
		reverselabels.append(h)

##Reverse reads and sequences: 

	coop.seek(0)
    
   
	for i in itertools.islice(coop, 1, None, 4):
		reversereads.append(i[6:])        
		reverseBC.append(i[0:6])

## reverse quality info

	coop.seek(0)

	for j in itertools.islice(coop, 3, None, 4): 
		reversereadsq.append(j[6:])
		reverseBCq.append(j[0:6])

##do I need the reverse compliment on these? Don't think so, guess I'll find out. 
##Now, to combine into a new fastq file

ee=['rearranged_', forward_file]
ff=''.join(ee)

with open(ff,'w') as foop2:

	for j in range(len(forwardreads)):
		    
		print(forwardlabels[j], file = foop2, end = '')
		print(forwardBC[j]+reverseBC[j]+forwardreads[j], sep = '', file = foop2, end='') 
		print('+', file = foop2)
		print(forwardBCq[j]+reverseBCq[j]+forwardreadsq[j], file = foop2, end = '')

gg=['rearranged_', reverse_file]
hh=''.join(gg)

with open(hh,'w') as goop2:

	for j in range(len(reversereads)):
	    
		print(reverselabels[j], file = goop2, end = '')
        ## this line is edited to keep barcodes in reverse reads:
		print(forwardBC[j]+reverseBC[j]+reversereads[j], file = goop2, end='')
		print('+', file = goop2)
		#print(reversereadsq[j], file = goop2, end = '')
        ## this line above replaced with line below, also 
        ## to keep barcodes in reverse reads:
		print(forwardBCq[j]+reverseBCq[j]+reversereadsq[j], file = goop2, end = '')









##a function for reverse complimenting (may need this?):

#def revcompl(x): 

#    aa=''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
#    return(aa)
 
