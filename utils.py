def validate_dna(dna):

    valid_bases = "ATGC"

    if dna == "":
        return False

    for base in dna:
        if base not in valid_bases:
            return False

    return True


def calculate_gc(dna):

    gc = dna.count("G") + dna.count("C")
    gc_content = (gc / len(dna)) * 100

    return gc_content


def get_complement(dna):

    complement = ""

    for base in dna:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    return complement


def get_reverse_complement(dna):

    complement = get_complement(dna)

    return complement[::-1]