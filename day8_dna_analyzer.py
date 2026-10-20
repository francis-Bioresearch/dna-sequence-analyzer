
print("Welcome to the DNA Analyzer!")

sequence = input("Enter a DNA sequence: ")
sequence = sequence.upper()

valid = True

for base in sequence:
    if base not in "ATGC":
        valid = False

if not sequence:
    print("Please enter a DNA sequence.")
elif not valid:
    print("Invalid DNA sequence. Use only A, T, G and C.")
else:
    length = len(sequence)
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / length) * 100

    print("Sequence length:", length)
    print("A bases:", a_count)
    print("T bases:", t_count)
    print("G bases:", g_count)
    print("C bases:", c_count)
    print("GC content:", round(gc_content, 2), "%")





