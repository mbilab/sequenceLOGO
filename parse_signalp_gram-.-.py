from scripts.fix_sequence import fix_sequences
from scripts.fasta import batch_fasta_save, batch_to_fasta

def read_csv(file_path):
	sequences_ = []
	with open(file_path, 'r') as f:
		raw = f.read().split('\n')
		f.close()
	raw.pop(-1)
	
	for i in raw:
		tmp = i.split(',')
		if (tmp[2] != 'S'):
			sequences_.append((tmp[0], tmp[1]))
	return sequences_


if __name__ == '__main__':
	sequences = read_csv('gram-.signalp.full.csv')
	sequences = fix_sequences(sequences, 20)
	sequences = batch_to_fasta(sequences)
	print('At the end we have %s sequences that contain signal peptide' % str(len(sequences)))
	batch_fasta_save('parse_gram-.-.signalp.fasta', sequences)
