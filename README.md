## MSSE-CHEM274B-Micropresentation
## A simple pattern-matching and brute-force substring search algorithm using a Ternary Search Trie (TST) for genome assembly 

# Group 6: Dongwan Kim, Trinity Ho, Robert Craig Wallace, and Priscilla Vaskez

https://docs.google.com/document/d/1xhsegW8prdSqqZbf1JeJ4FINKRPU9wh7IGOpU9e40_4/edit?tab=t.0

# Overview

This repository explores how DNA sequence pattern-matching can be performed using three different algorithmic approaches:

# Brute-Force Search

Ternary Search Tree (TST) – Recursive version
Ternary Search Tree (TST) – Iterative version

The goal of this micro-presentation is to compare time and space efficiency when searching real biological genomes, including:
The E. coli K-12 genome (~4.6 Mbp)
The lac operon genes (lacZ, lacY, lacI)
A eukaryotic example using yeast ACT1 (~12 Mbp genome)

This project shows how algorithmic choices dramatically impact performance when scaling from simple examples (like the sickle-cell mutation) to realistic genome sizes and multi-pattern searches.

# We demonstrate:

Why brute-force searching becomes inefficient with large genomes
Why TST enables rapid multi-pattern matching
How iterative TST improves auxiliary space compared to recursive TST
Real-world performance differences validated using group-generated timing graphs
Files Contained in This Repository
DNA and Genome Data
ecoli_genome.fasta — Full E. coli K-12 genome (~4.6 million bp)
lacZ_gene.fna — lacZ gene sequence
lacY_gene.fna — lacY gene sequence
lacI_gene.fna — lacI gene sequence
yeast.fna — Yeast genome
act1_gene.fna — Yeast ACT1 gene

# Python Notebooks & Scripts

brute_force.ipynb
Implements brute-force string matching
Includes HBB example, cDNA generation, and E. coli brute-force tests
tst_notebook.ipynb
Implements recursive TST insertion + search
Includes performance testing and comparison graphs
test_ecoli_tst.py
TST tests for lacZ, lacY, lacI
test_ecoli_bf.py
Brute-force tests using the E. coli genome and lac operon genes
tst.py
Contains TST class, recursive version
visualizer.py
TST tree visualizer for understanding node structure
compare_with_graphs.py
Timing and performance comparison for brute-force vs. TST

# Configuration

<<<<<<< Updated upstream
Makefile — Automates environment creation and removal
environment.yaml — Conda environment specification
=======
```
“Testing E. coli genome and lac operon genes”
```

### **TST (recursive + iterative)**

```bash
pytest test_ecoli_tst.py -v
```

### **Graphs**

Open:

```
lacZ_graphs.ipynb
```

Run all cells to generate timing bar charts comparing:

* Iterative TST
* Brute-force

---

# **E. coli Results**

### **Gene Statistics**

| Gene | Length (nt) | Codons | Unique Codons | Patterns Tested |
| ---- | ----------- | ------ | ------------- | --------------- |
| lacZ | 3075        | 1025   | 59            | 50              |
| lacY | 1254        | 418    | 57            | 50              |
| lacI | 1083        | 361    | 59            | 50              |

### **Timing (Recursive TST vs Brute-force)**

| Gene     | TST Time              | Brute-force Time      |
| -------- | --------------------- | --------------------- |
| **lacZ** | 0.000055 s            | 0.000768 s            |
| **lacY** | 0.000124 s            | 0.001430 s            |
| **lacI** | (truncated in output) | (truncated in output) |

### **Timing (Iterative TST vs Brute-force)**

| Gene     | Iterative TST | Brute-force |
| -------- | ------------- | ----------- |
| **lacZ** | 0.000046 s    | 0.000750 s  |
| **lacY** | 0.000040 s    | 0.000871 s  |
| **lacI** | 0.000036 s    | 0.000670 s  |

---

# **Human Genome Results (Chr21)**

### **KCNE1**

* Total Codons: **45,079**
* Unique Codons: **64**
* Patterns Tested: **50**

| Method          | Time        |
| --------------- | ----------- |
| **TST**         | 0.000040 s  |
| **Brute-force** | 51.561617 s |

### **KCNE2**

* Total Codons: **4,917**
* Unique Codons: **64**
* Patterns Tested: **50**

| Method          | Time        |
| --------------- | ----------- |
| **TST**         | 0.000054 s  |
| **Brute-force** | 49.210667 s |

- TST is approximately 1,000,000× faster than brute-force on human chromosome 21.

---

# **Overall Summary Table**

| Dataset       | TST Time            | Brute-force Time    | Speedup         |
| ------------- | ------------------- | ------------------- | --------------- |
| lacZ          | 0.000046–0.000055 s | 0.000750–0.000768 s | ~15×            |
| lacY          | 0.000040–0.000124 s | 0.000871–0.001430 s | ~10×            |
| lacI          | 0.000036 s          | 0.000670 s          | ~18×            |
| KCNE1 (Human) | 0.000040 s          | 51.56 s             | **>1,000,000×** |
| KCNE2 (Human) | 0.000054 s          | 49.21 s             | **>900,000×**   |

---

# **Algorithm Complexity**

### **Brute-force**

```
O(P × N × M)
P = number of patterns
N = genome length
M = pattern length
```

### **TST (recursive or iterative)**

```
O(P × M)
Search depends only on pattern length (M = 3 for codons)
```

This explains why brute-force collapses on human-scale data, while TST finishes instantly.

---

# **Reproducibility Summary**

To reproduce any dataset:

1. Activate environment
2. Run notebooks or scripts listed above
3. Use test files for correctness
4. Generate timing graphs

Everything needed for full reproducibility is included in the repository.
>>>>>>> Stashed changes

## References

### **Biological Data Sources**

1. **E. coli K-12 MG1655 Genome**
   [https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2/](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2/)

2. **lac Operon Genes (lacZ, lacY, lacI)**
   [https://www.ncbi.nlm.nih.gov/nuccore/](https://www.ncbi.nlm.nih.gov/nuccore/)

3. **Yeast ACT1 Gene (Saccharomyces cerevisiae)**
   [https://www.ncbi.nlm.nih.gov/nuccore/](https://www.ncbi.nlm.nih.gov/nuccore/)

4. **Human Chromosome 21 FASTA (for KCNE1/KCNE2 tests)**
   [https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.40/](https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.40/)

5. **KCNE1 and KCNE2 Genes**
   [https://www.ncbi.nlm.nih.gov/nuccore/](https://www.ncbi.nlm.nih.gov/nuccore/)

---

### **Algorithm / Computer Science Resources**

6. **Sedgewick, R., & Wayne, K. *Algorithms, 4th Edition*.**
   This was used in reference for TSTs.

7. **TST Visualization Tool (used by your group to verify structure)**
   [https://www.cs.usfca.edu/~galles/visualization/TST.html](https://www.cs.usfca.edu/~galles/visualization/TST.html)

8. **UC Berkeley bCourses Lecture Slides**

   * Discussion 6: Tries, kd-trees, TSTs
   * Discussion 9: Brute-force substring search

---

### **Biological Concept Images**


9. **NCBI lac operon figure**
   [https://www.ncbi.nlm.nih.gov/books/NBK526/figure/ch4.f1/](https://www.ncbi.nlm.nih.gov/books/NBK526/figure/ch4.f1/)


10. **BLAST (used conceptually at start of project idea)**
    [https://blast.ncbi.nlm.nih.gov/](https://blast.ncbi.nlm.nih.gov/)

11. **Biopython Quickstart Page**
    [https://biopython.org/docs/latest/Tutorial/chapter_quick_start.html](https://biopython.org/docs/latest/Tutorial/chapter_quick_start.html)




