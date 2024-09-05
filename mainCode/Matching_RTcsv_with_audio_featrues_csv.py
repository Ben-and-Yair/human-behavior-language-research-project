import pandas as pd


# user input
def input_params():
    file1_path = 'csv_files_old/Sliced_features.csv'
    file2_path = 'csv_files_old/processed_results2.csv'

    return file1_path, file2_path  # do NOT change


def main():
    file1_path, file2_path = input_params()

    # Read the CSV files into DataFrames
    df1 = pd.read_csv(file1_path)
    df1.drop(columns=df1.columns[0], axis=1, inplace=True)

    df2 = pd.read_csv(file2_path)
    print(f'{file1_path} info:')
    print(df1.info())
    print("\n\n")
    print(f'{file2_path} info:')
    print(df2.info())
    print("\n\n")
    # Merge the two DataFrames based on the "File_name" column
    merged_df = pd.merge(df1, df2, on='File_name', how='outer', suffixes=('_File1', '_File2'))

    # Print or use the merged DataFrame
    print(f'merged df info:')
    print(merged_df.info())
    merged_df.to_csv("csv_files/all_features.csv")


if __name__ == "__main__":
    main()
