# CRG Research Portfolio
# Project 01: DNA Sequence Analyzer

dna = "ATGC"

print("===== DNA SEQUENCE ANALYSIS =====")
print("DNA Sequence:", dna)
print("Sequence Length:", len(dna))

# Validate DNA sequence
valid_bases = "ATGC"
is_valid = True

for base in dna:
    if base not in valid_bases:
        is_valid = False
        break

if not is_valid:
    print("DNA Sequence is Invalid")

else:
    print("DNA Sequence is Valid")

    # Count DNA nucleotides
    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    # Calculate GC Content
    gc_content = ((g + c) / len(dna)) * 100

    print("A Count:", a)
    print("T Count:", t)
    print("G Count:", g)
    print("C Count:", c)
    print("GC Content:", round(gc_content, 2), "%")
        # Generate DNA Complement
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

    print("DNA Complement:", complement)
    reverse_complement = complement[::-1]
    print("Reverse Complement:", reverse_complement)