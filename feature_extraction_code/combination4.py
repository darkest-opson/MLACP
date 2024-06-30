import subprocess
import pandas as pd
import os

# Define the path to your iFeature installation
ifeature_path = ".\\iFeature\\"

path = [p for p in os.listdir(path='.\\data') if p.endswith(".fasta")]
for p in path:
    # Define the input FASTA file
    input_fasta = f'.\\data\\{p}'

    # Define output files for each feature
    output_files = {
        'DPC': 'DPC.tsv',
        'CTDT': 'CTDT.tsv',
        'TPC': 'TPC.tsv',
        'AAC': 'AAC.tsv'
    }

    # Define the commands for each feature
    commands = {

        'DPC': f'python {ifeature_path}iFeature.py --type DPC --file {input_fasta} --out {input_fasta[:-6]+"_4_"+output_files["DPC"]}',
        'CTDT': f'python {ifeature_path}iFeature.py --type CTDT --file {input_fasta} --out {input_fasta[:-6]+"_4_"+output_files["CTDT"]}',
        'TPC': f'python {ifeature_path}iFeature.py --type TPC --file {input_fasta} --out {input_fasta[:-6]+"_4_"+output_files["TPC"]}',
        'AAC': f'python {ifeature_path}iFeature.py --type AAC --file {input_fasta} --out {input_fasta[:-6]+"_4_"+output_files["AAC"]}',
    }

    # Run the commands
    for feature, command in commands.items():
        print(f'Running command for {p}--{feature}...')
        subprocess.run(command, shell=True)


    # Load the TSV files into pandas DataFrames
    dfs = {feature: pd.read_csv(input_fasta[:-6]+"_4_"+output_files[feature], sep='\t') for feature in output_files}

    # Ensure that all dataframes have the same index
    indexes = [df.index for df in dfs.values()]
    assert all(index.equals(indexes[0]) for index in indexes)

    # Combine all features
    combined_df = pd.concat(dfs.values(), axis=1)
    combined_df.to_csv(f'.\\data\\Combined_Features_{p[:-6]}4.csv', index=False)

    print("Feature extraction and combination completed and saved to CSV file.")

df_neg = pd.read_csv(".\\data\\Combined_Features_negative4.csv")
df_pos = pd.read_csv(".\\data\\Combined_Features_positive4.csv")

# Concatenate the DataFrames vertically
merged_df = pd.concat([df_neg, df_pos], axis=0, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('.\\data\\datasets\\combination4.csv', index=False)
print("code done------>")
