# HamHeat

### Hamming distance calculation from multiple sequence data for heatmap visualization

##### Authors: Alexey V. Rakov (<rakovalexey@gmail.com>) & Emilio Mastriani (<emiliomastriani@hrbmu.edu.cn>) 

#### How to cite this work in a publication: Rakov A.V., Schifferli D.M., Liu S.-L., Mastriani E. HamHeat: A fast and simple package for calculating Hamming distance from multiple sequence data for heatmap visualization. *bioRxiv, 2020* (in press).

The problem of fast calculation of Hamming distance inferred from many sequence datasets is still not a trivial task.

**HamHeat** is a new method to efficiently calculate Hamming distance from multiple aligned sequence data for later use for different purposes.

***Objective***: Create a fast and simple package for calculating Hamming distance from multiple sequence data for heatmap visualization.

## HamHeat Workflow

![My image](https://github.com/alexeyrakov/HamHeat/blob/master/HamHeatWorkflow.png)

## Usage

```
hamheat.sh input_file
```

## Input file format

TAB-delimited text file format with two columns: the first column for the sequence names and the second column for the aligned sequences.

*Example:*

seq1  ATGC

seq2  CGTA

seq3  ATGC

seq4  AGTC

## Output

TAB-delimited text file with three columns: the aligned sequences, the name of sequences, and the Hamming distance, where zero distance (0) is given for the most frequent variant which is selected as the reference sequence by HamHeat.

*Example:*

ATGC  seq1  0

CGTA  seq2  4

ATGC  seq3  0

AGTC  seq4  2

## Validation

The script was applied to the real *Salmonella* allelic data of our recently published paper [Rakov et al., 2019](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-5809-8). [Figure S1 (additional file 5)](https://static-content.springer.com/esm/art%3A10.1186%2Fs12864-019-5809-8/MediaObjects/12864_2019_5809_MOESM5_ESM.ppt) from this publication shows the heatmap for 70 virulence factors alleles for 500 *Salmonella* genomes. For this figure, the **HamHeat** results for each of the 70 alleles were combined in one file to be used as the input file for the Morpheus matrix visualization software.

## F.A.Q.

1. How to cite?

Rakov A.V., Schifferli D.M., Liu S.-L., Mastriani E. HamHeat: A fast and simple package for calculating Hamming distance from multiple sequence data for heatmap visualization. *bioRxiv, 2020* (in press)

2. How to use?

Follow the instructions on this page.

3. What if I need a help?

Feel free to contact authors if you need help.

## Reference

Rakov A.V., Schifferli D.M., Liu S.-L., Mastriani E. HamHeat: A fast and simple package for calculating Hamming distance from multiple sequence data for heatmap visualization. *bioRxiv, 2020* (in press)
