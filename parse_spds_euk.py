from scripts.fasta import to_fasta, batch_to_fasta, batch_fasta_save
from scripts.fix_sequence import fix_sequences

def read_csv(file_path):
	IDs = None
	with open(file_path, 'r') as f:
		IDs = f.read().split('\n')
	IDs.pop(-1)

	IDs_ = []
	negative_IDs_ = []
	for i in IDs:
		if(i.split(',')[-1] == 'S'):
			IDs_.append(i.split(',')[0])
		else:
			negative_IDs_.append(i.split(',')[0])
	return IDs_, negative_IDs_

def read_fasta(file_path):
	Sequences = []
	with open(file_path, 'r') as f:
		Seqs = f.read().split('\n')
		f.close()
	Seqs.pop(-1)
	for i in range(0, len(Seqs), 2):
		Sequences.append((Seqs[i].split('>')[-1], Seqs[i + 1]))
	return Sequences

def pick_Sequences(IDs, Sequences):
	Sequences_ = []
	for i in IDs:
		for j in Sequences:
			if (j[0] == i):
				Sequences_.append(j)
	return Sequences_


if __name__ == '__main__':
	IDs, negative_IDs = read_csv('euk.spds17.csv')
	Sequences = read_fasta('euk.spds17.fasta')
	print('At the begin we have %s sequences' % str(len(Sequences)))
	sequences = pick_Sequences(IDs, Sequences)
	negative_sequences = pick_Sequences(negative_IDs, Sequences)
	sequences = fix_sequences(sequences, 20)
	negative_sequences = fix_sequences(negative_sequences, 20)
	print('At the end we have %s sequences that contain signal peptide' % str(len(sequences)))
	print('At the end we have %s sequences that dont contain signal peptide' % str(len(negative_sequences)))
	sequences = batch_to_fasta(sequences)
	negative_sequences = batch_to_fasta(negative_sequences)
	batch_fasta_save('parse_euk.spds17.fasta', sequences)
	batch_fasta_save('parse_euk.-.spds17.fasta', negative_sequences)
