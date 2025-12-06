## MSSE-CHEM274B-Micropresentation
## A simple pattern-matching and brute-force substring search algorithm using a Ternary Search Trie (TST) for genome assembly 

# Group 6: 

Dongwan Kim, Trinity Ho, Robert Craig Wallace, and Priscilla Vaskez

https://docs.google.com/document/d/1xhsegW8prdSqqZbf1JeJ4FINKRPU9wh7IGOpU9e40_4/edit?tab=t.0



## Overview

This project compares three pattern-matching strategies applied to real biological DNA sequences:

1. Brute-Force Search
2. Ternary Search Trie (TST) — Recursive version
3. Ternary Search Trie (TST) — Iterative version

The goal is to examine how these algorithms behave on real biological datasets and to understand how performance changes when scaling from small genes to full chromosomes. Our tests include:

* *E. coli* K-12 genome (~4.6 Mbp)
* lac operon genes: **lacZ**, **lacY**, **lacI**
* **Human chromosome 21** with KCNE1 and KCNE2 genes (~48 Mbp)

The project demonstrates that brute-force becomes slow as genomes get larger, while the TST enables fast, scalable multi-pattern matching.

---

## **What This Project Demonstrates**

- Brute-force search requires rescanning the entire sequence for each pattern
- TST search depends only on the pattern length
- TST is ~15–20× faster for *E. coli* codon searches
- TST is ~1,000,000× faster than brute-force on human chromosome 21
- Results are repeatable using the included notebooks and scripts
- Both recursive and iterative TST implementations behave correctly
- Advantages and limitations of recursive and iterative TST

---

## **Repository Structure**

### **Genome & Gene Data**

```
ecoli_genome.fasta      # Full E. coli genome (~4.6 Mbp)
lacZ_gene.fna           # lacZ gene
lacY_gene.fna           # lacY gene
lacI_gene.fna           # lacI gene
human21.fna             # Human chromosome 21
kcne1.fna               # Human KCNE1 gene
kcne2.fna               # Human KCNE2 gene
```

---

### **Python Code & Notebooks**

```
brute_force.ipynb         # Brute-force implementation and E. coli tests
tst.py                     # Recursive TST implementation
tst_notebook.ipynb         # TST tests and demonstration
visualizer.py              # TST node/structure visualization
sequence_utils.py          # FASTA loading helpers
compare_with_graphs.py     # Timing comparison script
lacZ_graphs.ipynb          # Generates bar graphs for performance
test_ecoli_tst.py          # TST testing of lac operon genes
test_ecoli_bf.py           # Brute-force testing for same genes
test_human_tst.py          # Tests for iterative TST with human KCNE genes (optional)
```

---

## **How to Set Up the Environment**

### **1. Create the Conda environment**

```bash
make create_env
conda activate tst-micro-presentation
```

### **2. Run tests**

```bash
pytest -v
```

### **3. Remove environment**

```bash
make remove-env
```

---

# **How to Reproduce All Results**

## 1. E. coli (lacZ, lacY, lacI)

### Brute-force

Open:

```
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


Makefile — Automates environment creation and removal
environment.yaml — Conda environment specification

```

Run:

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


# **Results**

All results below come directly from your real runs.

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

### **Comparison: Call stack differences of recursive TST and iterative TST**

Recursive TST calls itself per character when inserting.

```
Auxiliary space: O(N)
N = genome length
```

Iterative TST uses while loop.

```
Auxiliary space: O(1)
```

The auxiliary space complexity is the main complexity difference between recursive TST and iterative TST.

---
# ** Advantages and Limitations of TSTs (Recursive and Iterative) **

### **Resursive TST**

Recursive TST is commonly adopted due to its readable and intuitive design, however, recursive TST cannot handle large genomes because Python has a recursion depth limited to 1000. `RecursionError` appears quickly when inserting or searching long sequences. Recursive TST is best for small and medium-sized genome datasets.

Iterative TST can handle large genome datasets because it does not use recursive thus avoiding Python's stack limitation. Iterative TST is not chosen over recursive TST because of the complicated traversal and node comparisons design.

---

# **Reproducibility Summary**

To reproduce any dataset:

1. Activate environment
2. Run notebooks or scripts listed above
3. Use test files for correctness
4. Generate timing graphs

Everything needed for full reproducibility is included in the repository.



## References

### **Biological Data Sources**

1. **E. coli K-12 MG1655 Genome**
   [https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2/](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2/)

2. **lac Operon Genes (lacZ, lacY, lacI)**
   [https://www.ncbi.nlm.nih.gov/nuccore/](https://www.ncbi.nlm.nih.gov/nuccore/)


3. **Human Chromosome 21 FASTA (for KCNE1/KCNE2 tests)**
   [https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.40/](https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.40/)

4. **KCNE1 and KCNE2 Genes**
   [https://www.ncbi.nlm.nih.gov/nuccore/](https://www.ncbi.nlm.nih.gov/nuccore/)

---

### **Algorithm / Computer Science Resources**

5. **Sedgewick, R., & Wayne, K. *Algorithms, 4th Edition*.**
   This was used in reference for TSTs.

6. **TST Visualization Tool (used by your group to verify structure)**
   [https://www.cs.usfca.edu/~galles/visualization/TST.html](https://www.cs.usfca.edu/~galles/visualization/TST.html)

7. **UC Berkeley bCourses Lecture Slides**

   * Discussion 6: Tries, kd-trees, TSTs
   * Discussion 9: Brute-force substring search

---

### **Biological Concept Images**


8. **NCBI lac operon figure**
   [https://www.ncbi.nlm.nih.gov/books/NBK526/figure/ch4.f1/](https://www.ncbi.nlm.nih.gov/books/NBK526/figure/ch4.f1/)


9. **BLAST (used conceptually at start of project idea)**
    [https://blast.ncbi.nlm.nih.gov/](https://blast.ncbi.nlm.nih.gov/)

10. **Biopython Quickstart Page**
    [https://biopython.org/docs/latest/Tutorial/chapter_quick_start.html](https://biopython.org/docs/latest/Tutorial/chapter_quick_start.html)



