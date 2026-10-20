# dna-sequence-analyzer
# DNA Sequence Analyzer

A beginner-friendly Python project for basic DNA sequence analysis, developed as part of my learning journey in bioinformatics.

## Overview

The DNA Sequence Analyzer accepts a DNA sequence, checks whether it contains valid DNA bases, and calculates basic nucleotide statistics.

## Features

- Accepts a DNA sequence from the user.
- Converts lowercase input to uppercase.
- Validates that the sequence contains only A, T, G, and C.
- Calculates total sequence length.
- Counts individual nucleotide bases (A, T, G, and C).
- Calculates GC content as a percentage.
- Handles empty and invalid sequence input.
- Calculates GC content as a percentage.
- Generates the reverse complement of a valid DNA sequence.

## Technologies Used

- Python 3

## How to Run

1. Install Python 3 from https://www.python.org/downloads/ if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python day8_dna_analyzer.py
```

## Example

Input:

```text
AAGCTTGC
```

Expected output:

```text
Sequence length: 8
A bases: 2
T bases: 2
G bases: 2
C bases: 2
GC content: 50.0 %
Input: AAGC
Reverse complement: GCTT
```

## Learning Objectives

This project demonstrates introductory Python programming concepts, including variables, strings, loops, conditional statements, input validation, and basic sequence analysis.

## Future Improvements

- Calculate nucleotide frequencies.
- Implement reverse-complement generation.
- Add FASTA file input.
- Support analysis of multiple DNA sequences.
- Develop additional bioinformatics analysis features.

## Author

Francis-Bioresearch

GitHub: https://github.com/francis-Bioresearch
