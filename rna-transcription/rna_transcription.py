def to_rna(dna):
    dct = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    if set(dna) - set(dct):
        return ''
    return ''.join([val for ch in dna for key, val in dct.items() if ch == key])


# Fuctional way

# def to_rna(dna):
#     dct = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
#     r = ''.join(map(lambda x: dct.get(x, ''), dna))
#     return r if len(r) == len(dna) else ''