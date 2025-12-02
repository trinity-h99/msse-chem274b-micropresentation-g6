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

Makefile — Automates environment creation and removal
environment.yaml — Conda environment specification

