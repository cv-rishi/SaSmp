import pandas as pd 

def clean_data(input_file, output_file):

    raw = pd.read_csv(input_file)

    # do shit here


    raw.to_csv(output_file, index=False)


if __name__ == "main":
    input_file = "..data/raw/rawdata.csv"
    output_file = "..data/processed/cleandata.csv"
    clean_data(input_file, output_file)

