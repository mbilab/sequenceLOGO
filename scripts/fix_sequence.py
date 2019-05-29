def fix_sequence(sequence, length):
        print(len(sequence))
        if (len(sequence) >= length):
            return sequence[:length]
        else:
            return None

def fix_sequences(sequences, length):
	sequences_ = []
	for i in sequences:
		tmp = fix_sequence(i[1], length)
		if (tmp is not None):
			sequences_.append((i[0], tmp))
	return sequences_
