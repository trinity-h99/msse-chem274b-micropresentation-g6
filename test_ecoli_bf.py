from brute_force import brute_force_search  #your function name may differ
from tst import TST

def load_sequence(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return "".join([l.strip() for l in lines if not l.startswith(">")])

class TestBruteForceEcoli:
    def test_bruteforce_lac_operon(self):
        genome = load_sequence("ecoli_genome.fasta")

        lacZ = load_sequence("lacZ_gene.fna")
        lacY = load_sequence("lacY_gene.fna")
        lacA = load_sequence("lacA_gene.fna")

        genes = {
            "lacZ": lacZ,
            "lacY": lacY,
            "lacA": lacA,
        }

        for gene_name, seq in genes.items():
            pattern = seq[:30]   # use 30 bp to avoid random matches
            index = brute_force_search(genome, pattern)

            print(f"\nGene: {gene_name}")
            print(f"  Pattern matched? {index != -1}")
            print(f"  Position: {index}")

            assert index != -1