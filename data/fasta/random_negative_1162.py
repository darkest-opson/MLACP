import random
from Bio import SeqIO

def extract_random_sequences(input_fasta, output_fasta, num_sequences):
    # Read all sequences from the input FASTA file
    sequences = list(SeqIO.parse(input_fasta, "fasta"))
    
    # Check if there are enough sequences in the input file
    if len(sequences) < num_sequences:
        raise ValueError(f"The input file contains only {len(sequences)} sequences, which is less than the requested {num_sequences} sequences.")

    # Randomly select the specified number of sequences
    selected_sequences = random.sample(sequences, num_sequences)
    
    # Write the selected sequences to the output FASTA file
    SeqIO.write(selected_sequences, output_fasta, "fasta")
    print(f"Successfully wrote {num_sequences} sequences to {output_fasta}")

# Example usage
input_fasta = "negative_5064.fasta"
output_fasta = "negative.fasta"
num_sequences = 1162

extract_random_sequences(input_fasta, output_fasta, num_sequences)