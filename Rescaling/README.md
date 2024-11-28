# Rescaling

1] In project directory(main directory) another directory "datafiles" created to store input data. There are 2 files of sample analysis i.e. shuf.a.bed.gz and shuf.b.bed.gz downloaded from website - https://figshare.com/s/2d3d4d60a82de9cc3cc6 using 'curl -JLO' and stored it into data directory. These files unziped by using 'gunzip' command[Not able to upload here because of file size]. Also there is reference file in data directory, we have rescale our data to that reference file.

2] Again two files created sample_data.tsv and metadata.tsv in datafiles directory.
3] sample_data.tsv contain information of sample and their runs and metadata.tsv contain runs and their respective path.

4] Scripts directory created in main directory, contain scripts for to obtain frequency, to extract lines and plot graph.

5] Snakemake(rescale.smk) file created in main directory, required scripts and rules are incorporated.
