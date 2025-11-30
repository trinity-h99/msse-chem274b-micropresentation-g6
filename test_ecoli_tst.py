from tst import TST

def load_sequence(path):
    """Load a FASTA file and return a continuous DNA string (no headers)."""
    with open(path, "r") as f:
        lines = f.readlines()
    return "".join([l.strip() for l in lines if not l.startswith(">")])

def build_codons(seq):
    """Break a long DNA sequence into 3-mer codons."""
    codons = []
    for i in range(0, len(seq) - 2, 3):
        codons.append(seq[i:i+3])
    return codons


class TestTSTEcoli:
    def test_ecoli_lac_operon_search(self):
        # Load full E. coli genome
        genome = load_sequence("ecoli_genome.fasta")
        assert len(genome) > 4_000_000

        # Load gene sequences (separate files)
        lacZ = load_sequence("lacZ_gene.fna")
        lacY = load_sequence("lacY_gene.fna")
        lacI = load_sequence("lacI_gene.fna")

        genes = {
            "lacZ": lacZ,
            "lacY": lacY,
            "lacI": lacI,
        }

        # Build codons from genome
        codons = build_codons(genome)

        # Insert all genome codons into the TST
        tst = TST()
        for i, codon in enumerate(codons):
            tst.put(codon, i)

        # Search for each gene’s FIRST *real* codon (first ATG)
        for gene_name, seq in genes.items():

            # Locate the real start codon within the FASTA sequence
            start_index = seq.find("ATG")
            assert start_index != -1, f"No ATG found in {gene_name}"

            start_codon = seq[start_index:start_index+3]

            found = tst.contains(start_codon)
            idx = tst.get(start_codon)

            print(f"\nGene: {gene_name}")
            print(f"  First codon: {start_codon}")
            print(f"  Found in genome? {found}")
            print(f"  Codon index: {idx}")

            assert found is True
            assert idx is not None
