# HamHeat

### Hamming distance calculation from multiple allelic sequence data for heatmap visualization

##### Authors: Alexey V. Rakov (<rakovalexey@gmail.com>) & Emilio Mastriani (<emiliomastriani@hrbmu.edu.cn>) 

#### How to cite this work in a publication:  Rakov A.V., Mastriani E. HamHeat: A fast and simple package for calculating Hamming distance from multiple allelic sequence data for heatmap visualization. *bioRxiv, 2020* (in press).

The problem of fast calculation of Hamming distance inferred from many sequence datasets is still not a trivial task.

**HamHeat** is a new method to efficiently calculate Hamming distance from multiple aligned allelic sequence data for later use for different purposes.

***Objective***: Create a fast and simple package for calculating Hamming distance from multiple allelic sequence data for heatmap visualization.

## HamHeat Workflow

![My image](https://github.com/alexeyrakov/HamHeat/blob/master/HamHeatWorkflow.png)

## Usage

```
hamheat.sh input_file
```

## Input file format

TAB-delimited text file format with two columns: first column containing the name of the sequence and the second column filled with the aligned sequence.

*Example:*

seq1  ATGC

seq2  CGTA

seq3  ATGC

## Output

TAB-delimited text file with three columns: the aligned sequences, the name of sequences, and the Hamming distance, where zero distance (0) is for most frequent allele used here as the reference sequence.

*Example:*

ATGC  seq1  0

CGTA  seq2  4

ATGC  seq3  0

## Validation

The script was applied to the real *Salmonella* allelic data in our recently published paper [Rakov et al., 2019](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-5809-8). [Figure S1 (additional file 5)](https://static-content.springer.com/esm/art%3A10.1186%2Fs12864-019-5809-8/MediaObjects/12864_2019_5809_MOESM5_ESM.ppt) from the paper shows the heatmap for 70 virulence factors alleles for 500 *Salmonella* genomes. The input file for the matrix were combined results from **HamHeat** software for each of the 70 alleles.

## F.A.Q.

1. How to cite?

Rakov A.V., Mastriani E. HamHeat: A fast and simple package for calculating Hamming distance from multiple allelic sequence data for heatmap visualization. *bioRxiv, 2020* (in press).

2. How to use?

Follow the instructions on this page.

3. What if I need a help?

Feel free to contact authors if you need help.

## Reference

Rakov A.V., Mastriani E. HamHeat: A fast and simple package for calculating Hamming distance from multiple allelic sequence data for heatmap visualization. *bioRxiv, 2020* (in press).
