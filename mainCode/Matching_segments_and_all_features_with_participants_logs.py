import pandas as pd


# user input
def input_params():
    file1_path = 'csv_files/participants_logs_csv.csv'
    file2_path = 'csv_files/fixed_segments_features_with_all_features.csv'

    return file1_path, file2_path  # do NOT change


def main():
    file1_path, file2_path = input_params()

    # Read the CSV files into DataFrames
    df1 = pd.read_csv(file1_path)
    df1.drop(columns=df1.columns[0], axis=1,  inplace=True)

    df2 = pd.read_csv(file2_path)
    df2.drop(columns=df2.columns[0], axis=1,  inplace=True)

    df1 = df1.dropna()
    df2 = df2.dropna()

    df1['File_name'] = df1['File_name'].str.replace("exampleNewData", "sliced_examplefiles")
    df1['File_name'] = df1['File_name'].str.lower()

    df2['File_name'] = df2['File_name'].str[:-18] + "'"

    print(f'{file1_path} info:')
    print(df1.info())
    print("\n\n")
    print(f'{file2_path} info:')
    print(df2.info())
    print("\n\n")

    # Merge the two DataFrames based on the "File_name" column
    merged_df = pd.merge(df1, df2, on='File_name', how="outer", suffixes=('_File1', '_File2'))

    merged_df = merged_df.dropna()

    # Print or use the merged DataFrame
    print(f'merged df info:')
    print(merged_df.info())
    merged_df.to_csv("csv_files/segments_features_and_all_features_with_participants_logs.csv")


if __name__ == "__main__":
    main()
