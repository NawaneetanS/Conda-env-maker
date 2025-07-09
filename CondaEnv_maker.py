import subprocess
import shutil

# Check if conda is available
if not shutil.which("conda"):
    print("Error: 'conda' is not found in your PATH. Please install Anaconda or Miniconda.")
    exit(1)

# Ask for the name of the conda environment
while True:
    env_name = input("Enter the name of your new Conda environment: ")
    env_conf = input("You chose %s as the conda environment name, shall we proceed? (Y/N)" % env_name )

    if env_conf.lower() == "y": # Take env name if confirmed by y
        print("Name of conda env: %s" % env_name)
        break
    elif env_conf.lower() == "n": # Request name of conda env again if n
        continue
    else:
        print("Name not given!!")
        continue

optional_tools = {
    "1": "picard",        # BAM file cleanup, marking duplicates, etc.
    "2": "gatk4",          # Variant calling and genome analysis toolkit
    "3": "htseq",         # Read counting for RNA-seq
    "4": "stringtie",     # Transcript assembly and quantification
    "5": "cutadapt",      # Adapter trimming (alternative to fastp)
    "6": "bedtools",      # Genomic intervals and BED file operations
    "7": "bcftools",      # VCF manipulation, filtering, stats
    "8": "deeptools",     # For ATAC-seq, ChIP-seq visualization
    "9": "qualimap",      # BAM quality checks, useful for RNA-seq
    "10": "subread",      # FeatureCounts + alignment
    "11": "star",         # RNA-seq alignment (fast, accurate)
}

# Print a list of optional tools available
for key, value in optional_tools.items():
        print(f"{key}: {value}")

# Ask for which tools they need
opTools = input("Choose tools from the list above (without space and commas or press any button to skip): ")
selected_opTools = [optional_tools[i] for i in opTools if i in optional_tools]
if not selected_opTools:
    print("No valid tools selected. Proceeding with core tools only.")

# Core tools
core_tools = [
    "fastqc",
    "fastp",
    "hisat2",
    "bwa",
    "samtools",
    "sra-tools",
    "multiqc"
]

# All req tools
all_tools = core_tools + selected_opTools

# Create yaml file out of it
yaml_content = f"""name: {env_name}
channels:
    - conda-forge
    - bioconda
    - defaults
dependencies:
"""

# Add the final list of tools
print(f"Tools chosen: \n{selected_opTools}")
for tool in all_tools:
    yaml_content += f"  - {tool}\n"

# Write the file with extension .yaml
with open(f"{env_name}.yaml", "w") as f:
    f.write(yaml_content)
    
# Make the conda environment
print(f"Creating conda environment '{env_name}' from {env_name}.yaml ...")
result = subprocess.run(f"conda env create -f {env_name}.yaml", shell=True)
if result.returncode == 0:
    print(f"Environment '{env_name}' created successfully.")
    print(f"To activate your environment, run:\n  conda activate {env_name}")
else:
    print("Error: Conda environment creation failed. Please check the YAML file and try again.")