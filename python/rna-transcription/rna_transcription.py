#import string


# Useful docs:
# https://docs.python.org/3/library/stdtypes.html#str.translate
# https://docs.python.org/3/library/stdtypes.html#str.maketrans


dna_values = 'GCTA'
rna_values = 'CGAU'
dna_to_rna_translation = str.maketrans(dna_values,rna_values)

def to_rna(dna_strand):
    return dna_strand.translate(dna_to_rna_translation)



