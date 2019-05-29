from scripts.fix_sequence import fix_sequences
from scripts.fasta import batch_fasta_save, batch_to_fasta

def read_csv(file_path):
	sequences_ = []
	negative_sequences_ = []
	with open(file_path, 'r') as f:
		raw = f.read().split('\n')
		f.close()
	raw.pop(-1)
	
	for i in raw:
		tmp = i.split(',')
		if (tmp[2] == 'S'):
			sequences_.append((tmp[0], tmp[1]))
		else:
			negative_sequences_.append((tmp[0], tmp[1]))
	return sequences_, negative_sequences_


if __name__ == '__main__':
	sequences, negative_sequences = read_csv('euk.signalp.full.csv')
	sequences = fix_sequences(sequences, 96)
	negative_sequences = fix_sequences(negative_sequences, 96)
	sequences = batch_to_fasta(sequences)
	negative_sequences = batch_to_fasta(negative_sequences)
	print('At the end we have %s sequences that contain signal peptide' % str(len(sequences)))
	print('At the end we have %s sequences that dont contain signal peptide' % str(len(negative_sequences)))
	batch_fasta_save('parse_euk.signalp.fasta', sequences)
	batch_fasta_save('parse_euk.-.signalp.fasta', negative_sequences)
