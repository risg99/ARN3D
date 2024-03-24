def extract_sequence(input_fasta, start, end, output_fasta):
    sequences = {}
    current_sequence = None
    with open(input_fasta, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_sequence = line[1:]
                sequences[current_sequence] = ''
            else:
                sequences[current_sequence] += line

    extracted_sequences = {}
    for header, sequence in sequences.items():
        extracted_sequences[header] = sequence[start - 1:end]

    with open(output_fasta, 'w') as f:
        for header, sequence in extracted_sequences.items():
            f.write('>' + header + '\n')
            f.write(sequence + '\n')

def run():
    # Example usage:
    input_file = 'P0CX69.fasta'
    output_file = 'P0CX69_351-440.fasta'
    start_pos = 351
    end_pos = 440
    extract_sequence(input_file, start_pos, end_pos, output_file)

if __name__ == '__main__':
    run()
