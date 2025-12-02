"""
Common utilities for loading and processing DNA sequences.
"""


def load_sequence(path: str) -> str:
    """
    Load a FASTA file and return a continuous DNA string (no header lines).
    
    Args:
        path: Path to the FASTA file
        
    Returns:
        A continuous DNA sequence string with all header lines removed
    """
    with open(path, "r") as f:
        lines = f.readlines()
    return "".join([l.strip() for l in lines if not l.startswith(">")])


def build_codons(seq: str) -> list[str]:
    """
    Split a DNA sequence into 3-bp codons.
    
    Args:
        seq: DNA sequence string
        
    Returns:
        List of 3-bp codons
    """
    codons = []
    for i in range(0, len(seq) - 2, 3):
        codons.append(seq[i:i+3])
    return codons


def load_gene_and_codons(gene_name: str):
    """
    Load one gene (lacZ, lacY, or lacI) and return:
      - full nucleotide sequence
      - list of 3-bp codons

    Expects files like:
      lacZ_gene.fna, lacY_gene.fna, lacI_gene.fna
    
    Args:
        gene_name: Name of the gene (e.g., "lacZ", "lacY", "lacI")
        
    Returns:
        Tuple of (sequence, codons)
    """
    fasta_path = f"{gene_name}_gene.fna"
    seq = load_sequence(fasta_path)
    codons = build_codons(seq)
    return seq, codons

