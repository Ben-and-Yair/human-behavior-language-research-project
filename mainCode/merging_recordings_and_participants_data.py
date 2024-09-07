import pandas as pd


# user input
def input_params():
    sliced_features_csv = '../csv_files/Sliced_features.csv'
    audio_features_csv = '../csv_files/processed_results2.csv'
    segments_features_csv = '../csv_files/segments_features.csv'
    participants_logs_csv = '../csv_files/participants_logs_csv.csv'

    destination_path = '../csv_files/segments_features_and_all_features_with_participants_logs.csv'

    return sliced_features_csv, audio_features_csv, segments_features_csv, participants_logs_csv, destination_path  # do NOT change


def fixing_path_mistake(string):
    string = string.lower()
    indexes = [index for index in range(len(string))
               if string.startswith('sub', index)]

    string1 = string.replace(string[indexes[1] + 3: indexes[1] + 7], string[indexes[0] + 3: indexes[0] + 7])
    if string1 != string:
        print(string)
        print(string1)
        print('\n')

    return string1


def main():
    sliced_features_csv, audio_features_csv, segments_features_csv, participants_logs_csv, destination_path = input_params()

    # matching sliced features with audio features csv
    # Read the CSV files into DataFrames
    df1 = pd.read_csv(sliced_features_csv)
    df1.drop(columns=df1.columns[0], axis=1, inplace=True)

    df2 = pd.read_csv(audio_features_csv)
    print(f'{sliced_features_csv} info:')
    print(df1.info())
    print("\n\n")
    print(f'{audio_features_csv} info:')
    print(df2.info())
    print("\n\n")
    # Merge the two DataFrames based on the "File_name" column
    whole_word_features = pd.merge(df1, df2, on='File_name', how='outer', suffixes=('_File1', '_File2'))

    # Print or use the merged DataFrame
    print(f'whole_word_features df info:')
    print(whole_word_features.info())
    # -------------------------------------------------------------------------------

    # matching segments features with all features
    # Read the CSV files into DataFrames
    df2 = pd.read_csv(segments_features_csv)

    df2['File_name'] = df2['File_name'].str.replace("exampleNewData", "sliced_exampleFiles")

    whole_word_features = whole_word_features.dropna()
    df2 = df2.dropna()

    print(f'whole_word_features info:')
    print(whole_word_features.info())
    print("\n\n")
    print(f'{segments_features_csv} info:')
    print(df2.info())
    print("\n\n")

    # Merge the two DataFrames based on the "File_name" column
    segments_features_with_whole_word_features = pd.merge(whole_word_features, df2, on='File_name', how="outer", suffixes=('_File1', '_File2'))

    segments_features_with_whole_word_features = segments_features_with_whole_word_features.dropna()

    # Print or use the merged DataFrame
    print(f'segments_features_with_whole_word_features df info:')
    print(segments_features_with_whole_word_features.info())
    print("\n\n")

    # -------------------------------------------------------------------------------

    # fixing specific filenames due to human error in data collection
    pd.set_option('max_colwidth', None)

    segments_features_with_whole_word_features['File_name'] = segments_features_with_whole_word_features['File_name'].apply(fixing_path_mistake)

    # -------------------------------------------------------------------------------

    # matching segments and all features_with participants logs
    # Read the CSV files into DataFrames
    df1 = pd.read_csv(participants_logs_csv)
    df1.drop(columns=df1.columns[0], axis=1,  inplace=True)

    df1 = df1.dropna()
    segments_features_with_whole_word_features = segments_features_with_whole_word_features.dropna()

    df1['File_name'] = df1['File_name'].str.replace("exampleNewData", "sliced_examplefiles")
    df1['File_name'] = df1['File_name'].str.lower()

    segments_features_with_whole_word_features['File_name'] = segments_features_with_whole_word_features['File_name'].str[:-18] + "'"

    print(f'{participants_logs_csv} info:')
    print(df1.info())
    print("\n\n")
    print(f'segments_features_with_whole_word_features info:')
    print(segments_features_with_whole_word_features.info())
    print("\n\n")

    # Merge the two DataFrames based on the "File_name" column
    merged_df = pd.merge(df1, segments_features_with_whole_word_features, on='File_name', how="outer", suffixes=('_File1', '_File2'))

    merged_df = merged_df.dropna()

    # Print or use the merged DataFrame
    print(f'merged df info:')
    print(merged_df.info())
    merged_df.to_csv(destination_path)


if __name__ == "__main__":
    main()
