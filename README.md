# DNA Sequence Analyzer 🧬

A Python-based DNA Sequence Analyzer that validates DNA sequences and performs basic sequence analysis.

## Project Overview

This project analyzes DNA sequences using Python. It checks whether a DNA sequence is valid and calculates important sequence information.

## Features

- DNA sequence validation
- DNA sequence length calculation
- GC Content calculation
- DNA Complement generation
- DNA Reverse Complement generation
- Read multiple DNA sequences from a text file
- Save analysis results to a text file
- Handle invalid and empty DNA sequences

## Technologies Used

- Python 3
- File Handling
- Python Functions
- Lists and Loops
- Conditional Statements

## Project Structure

```text
Project_01_DNA_Analyzer/
│
├── main.py
├── utils.py
├── dna_analyzer.py
├── practice.python
├── sample_sequences.txt
├── results.txt
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Project_01_DNA_Analyzer
```

### 3. Run the Program

```bash
python main.py
```

The program reads DNA sequences from `sample_sequences.txt`, analyzes them, displays the results in the terminal, and saves the results in `results.txt`.

## Sample DNA Sequences

```text
ATGC
AATTGGCC
GCGT
ATGX
```

## Sample Output

```text
DNA: ATGC
Status: Valid DNA
Sequence Length: 4
GC Content: 50.0 %
Complement: TACG
Reverse Complement: GCAT
```

## Learning Objectives

This project demonstrates practical Python programming skills, including functions, validation, loops, conditional statements, imports, and file handling.

## Author

Ayesha Arshad

## Project Status

Completed — Version 1.0