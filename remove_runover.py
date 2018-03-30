#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()

#parser.add_argument("input", help = \
#"Fastq file from which you would like to remove \
#primers and downstream sequences.")

parser.add_argument("-p", "--primer", help = \
    "which reverse primer are you looking for? \
    Note, all downstream sequence will also be \
    deleted. This should be in reverse-compliment \
    order.")

parser.add_argument("-f", "--fastq", help = \
    "The fastq file from which you will remove \
    primer and downstream sequence.")

parser.add_argument("-o", "--out", help = \
    "Output fastq file name.")

args = parser.parse_args()


## create a regex object with our primer:
if args.primer:
    p=re.compile(args.primer)

if args.fastq and args.out:
    with open(args.fastq,'r') as original:
        with open (args.out, 'w') as writeout:
            for i in original:
                if p.search(i): ## look for primer...
                    aa = p.search(i) ## save match object, has info we need...
                    writeout.write(i[:aa.start()]+"\n") ## use match start to cut sequence
                    i = next(original) ## skip to next line ("+")
                    writeout.write(i)
                    i = next(original) ## skip to next line, but...
                    writeout.write(i[:aa.start()]+"\n") ## cut to match
                else:
                    writeout.write(i) ## if no match, just write and move on...

else: 
    print ("Tell me your files and primer!")
    print(args)
