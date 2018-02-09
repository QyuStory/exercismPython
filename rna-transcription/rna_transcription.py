def to_rna(dna_strand):
    table = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}

    rna = ""
    for x in dna_strand: 
        if table.has_key(x):
            rna = rna + table.get(x)
        else:
            raise ValueError(".+")
    return rna
