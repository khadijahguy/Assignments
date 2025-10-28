"""
Program Description: This program takes a given DNA sequence translates it to a protein sequence.

Author: Khady Gueye
"""

import helper

def transcription(dna_sequence):
    complement = ''

    # Create the Base Pair Complement
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'

    # Replace Thymine with Uracil
    mrna = complement.replace('T', 'U')

    return mrna

def translate(mrna):
    protein = ''

    # Split mrna into nucleotide triplets
    triplets = helper.chunk(mrna, 3)

    # Replace Triplets with Amino Acids
    for triplet in triplets:
        if triplet in helper.amino_acids:
            amino_acid = helper.amino_acids[triplet]
            if amino_acid != 'STOP':  # Ignore STOP codons
                protein.append(amino_acid)
            else:
                break  # Stop translation at a STOP codon

    return ' '.join(protein)


dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

# Print the DNA
print("DNA Sequence")
print(dna)
print(' ')
# Transcribing the given DNA sequence to mRNA
mrna_sequence = transcription(dna)
print("mRNA Sequence ")
print(mrna_sequence)
print(" ")
# Translating the mRNA sequence to a protein sequence
protein_sequence = translate(mrna_sequence)
print("Protein Sequence ")
print(protein_sequence)