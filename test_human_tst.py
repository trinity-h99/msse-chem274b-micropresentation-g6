from tst import IterativeTST
from sequence_utils import load_sequence, build_codons

class TestTSTHumanChr21:
    def test_kcne_genes_on_chr21(self):
        # Load chromosome 21
        chr21_seq = load_sequence("human21.fna")
        assert len(chr21_seq) > 46_000_000  # sanity check

        # Load gene sequences
        genes = {
            "kcne1": load_sequence("kcne1.fna"),
            "kcne2": load_sequence("kcne2.fna"),
        }

        # Build codons for chromosome
        chr_codons = build_codons(chr21_seq)

        # Build IterativeTST for chromosome codons
        tst = IterativeTST()
        for idx, codon in enumerate(chr_codons):
            tst.put(codon, idx)

        # Search for all codons of each gene
        for gene_name, gene_seq in genes.items():
            codons = build_codons(gene_seq)

            # Optionally sample first 50 codons to match prior performance tests
            select_codons = codons[:50] if len(codons) > 50 else codons

            for codon in select_codons:
                found = tst.contains(codon)
                idx = tst.get(codon)
                print(f"\nGene: {gene_name}")
                print(f"  Codon: {codon}")
                print(f"  Found in chromosome? {found}")
                print(f"  Chromosome index: {idx}")

                assert found is True
                assert idx is not None
