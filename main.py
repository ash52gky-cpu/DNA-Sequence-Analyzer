from utils import (
    validate_dna,
    calculate_gc,
    get_complement,
    get_reverse_complement
)


def analyze_dna(dna):

    if not validate_dna(dna):
        return f"DNA: {dna}\nStatus: Invalid DNA\n----------------"

    result = (
        f"DNA: {dna}\n"
        f"Status: Valid DNA\n"
        f"Sequence Length: {len(dna)}\n"
        f"GC Content: {round(calculate_gc(dna), 2)} %\n"
        f"Complement: {get_complement(dna)}\n"
        f"Reverse Complement: {get_reverse_complement(dna)}\n"
        f"----------------"
    )

    return result


with open("sample_sequences.txt", "r") as file:
    sequences = file.readlines()


with open("results.txt", "w") as output_file:

    for dna in sequences:
        dna = dna.strip()

        result = analyze_dna(dna)

        print(result)
        output_file.write(result + "\n")