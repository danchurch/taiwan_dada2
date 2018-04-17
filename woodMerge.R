
rm(list=ls())

library('dada2')

load('woodDadaFs.rda')
load('derepFs.rda')
load('woodDadaRs.rda')
load('derepRs.rda')

woodMergers <- mergePairs(woodDadaFs, derepFs, woodDadaRs, derepRs, verbose=TRUE)

save(woodMergers, file='woodMergers.rda')
