
def to_fasta(ID, sequence):
	return '>%s\n%s' % (ID, sequence)

def batch_to_fasta(sequences):
	sequences_ = []
	for i in sequences:
		sequences_.append(to_fasta(i[0], i[1]))
	return sequences_

def batch_fasta_save(file_path, sequences):
	with open(file_path, 'w') as f:
		f.write('\n'.join(sequences))
		f.close()

def read_fasta(file_path):
	with open(file_path) as f:
		tmp = f.read().split('\n')
		f.close()
	sequences = []
	for i in range(0, len(tmp), 2):
		sequences.append((tmp[i][1:], tmp[i + 1]))
	print(sequences)
	return sequences

def remove_first(sequences):
	seq_ = []
	for s in sequences:
		seq_.append((s[0], s[1][1:]))
	return seq_
