import os, sys
from glob import glob
files = ['parse_gram-.-.signalp.fasta', 'parse_gram+.-.signalp.fasta',\
	'parse_gram-.spds17.fasta', 'parse_euk.-.signalp.fasta',\
	'parse_gram+.-.spds17.fasta', 'parse_euk.spds17.fasta',\
	'parse_gram+.signalp.fasta', 'parse_gram+.spds17.fasta',\
	'parse_gram-.signalp.fasta', 'parse_euk.-.spds17.fasta',\
	'parse_euk.signalp.fasta', 'parse_gram-.-.spds17.fasta']
titles = ['Gram-negative,Signalp,negative_samples', 'Gram-positive,Signalp,negative_samples',\
	'Gram-negative,SPDS17,positive_samples', 'EUK,Siganlp,negative_samples',\
	'Gram-positive,SPDS17,negative_samples', 'EUK,SPDS17,positive_samples',\
	'Gram-positive,Signalp,positive_samples', 'Gram-positive,SPDS17,positive_samples',\
	'Gram-negative,Signalp,positive_samples', 'EUK,SPDS17,negative_samples',\
	'EUK,Signalp,positive_samples', 'Gram-negatvie,SPDS17,negative_samples']

for f, t in zip(files, titles):
	command = 'weblogo'
	output =  '--format PNG < %s > %s.png' % (f, t)
	color = '--color red KRHDE \'Charged\'' + ' --color blue STCPNQ \'Polar\'' + ' --color green GAVLMIFWY \'Rest\''
	size = '--size large'
	units = '--units probability'
	title = '--title %s' %t
	command = ' '.join([command, color, size, units, output])
	print(command)
	os.system(command)
