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
* **Yeast ACT1** gene
* **Human chromosome 21** with KCNE1 and KCNE2 genes

The project demonstrates that brute-force becomes slow as genomes get larger, while the TST enables fast, scalable multi-pattern matching.

---

## **What This Project Demonstrates**

- Brute-force search requires rescanning the entire sequence for each pattern
- TST search depends only on the pattern length
- TST is ~15–20× faster for *E. coli* codon searches
- TST is ~1,000,000× faster than brute-force on human chromosome 21
- Results are repeatable using the included notebooks and scripts
- Both recursive and iterative TST implementations behave correctly

---

## **Repository Structure**

### **Genome & Gene Data**

```
ecoli_genome.fasta      # Full E. coli genome (~4.6 Mbp)
lacZ_gene.fna           # lacZ gene
lacY_gene.fna           # lacY gene
lacI_gene.fna           # lacI gene
yeast.fna               # Yeast genome
act1_gene.fna           # Yeast ACT1 gene
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
test_human_tst.py          # Tests for human KCNE genes (optional)
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

---

# **Reproducibility Summary**

To reproduce any dataset:

1. Activate environment
2. Run notebooks or scripts listed above
3. Use test files for correctness
4. Generate timing graphs

Everything needed for full reproducibility is included in the repository.

