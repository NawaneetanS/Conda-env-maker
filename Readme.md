# Conda environment maker for NGS analysis

**The python file makes conda environment with certain fixed tools and few optional tools.**

## Core Tools
- **fastqc** – Quality control checks on raw FASTQ files  
- **fastp** – Fast and efficient adapter trimming and quality filtering  
- **hisat2** – Spliced aligner for RNA-seq reads  
- **bwa** – Fast and accurate aligner for DNA sequences  
- **samtools** – Manipulation and conversion of SAM/BAM files  
- **sra-tools** – Download and convert sequencing data from NCBI SRA  
- **multiqc** – Aggregates results from QC tools like FastQC into a single report

## Optional Tools
- **picard** – BAM file cleanup, marking duplicates, etc.  
- **gatk4** – Variant calling and genome analysis toolkit  
- **htseq** – Read counting for RNA-seq  
- **stringtie** – Transcript assembly and quantification  
- **cutadapt** – Adapter trimming (alternative to fastp)  
- **bedtools** – Genomic intervals and BED file operations  
- **bcftools** – VCF manipulation, filtering, stats  
- **deeptools** – For ATAC-seq, ChIP-seq visualization  
- **qualimap** – BAM quality checks, useful for RNA-seq  
- **subread** – FeatureCounts + alignment  
- **star** – RNA-seq alignment (fast, accurate)
