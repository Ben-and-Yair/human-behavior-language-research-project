import pandas as pd


# user input
def input_params():
    csv_file = '../csvFiles/filtered_recordings_Olly.csv'
    output_path = '../csvFiles/check.csv'
    should_drop = True  # should drop ['TSKN', 'TRLN', 'BLKN', 'TASK'] columns

    return csv_file, output_path, should_drop  # do NOT change


def compress_csv_file(df, should_drop):
    df = drop_cols(df, should_drop)

    numeric_columns = [col for col in df.columns if col not in ['SUBJ', 'SESS', 'WORD', 'COND', 'cut_WORD']]
    print(numeric_columns)

    result = pd.DataFrame(
        columns=['SUBJ', 'SESS', 'WORD', 'COND', 'recordings_number'] +
                [f'{col}_mean' for col in numeric_columns] +
                [f'{col}_std' for col in numeric_columns])

    grouped = df.groupby(['SUBJ', 'SESS', 'WORD'], as_index=False)

    # Iterate over each group
    for name, group in grouped:
        # Save the original values of 'SUBJ', 'SESS', and 'WORD'
        subj, sess, word = name
        cond = group.iloc[0]['COND']

        # Calculate the number of recordings in the group
        recordings_number = len(group)

        # Drop 'SUBJ', 'SESS', and 'WORD' columns
        group = group.drop(columns=['SUBJ', 'SESS', 'WORD', 'COND', 'cut_WORD'])

        # Calculate mean and std for numeric columns
        means, stds = group.mean(), group.std()

        # Create a new row for the final DataFrame
        new_row = pd.DataFrame([[subj, sess, word, cond, recordings_number] + list(means) + list(stds)],
                               columns=['SUBJ', 'SESS', 'WORD', 'COND', 'recordings_number'] +
                                       [f'{col}_mean' for col in numeric_columns] +
                                       [f'{col}_std'  for col in numeric_columns])

        # Append the new row to the final DataFrame
        result = pd.concat([result, new_row], ignore_index=True)

    return result


def drop_cols(df, should_drop):
    might_drop = ['TSKN', 'TRLN', 'BLKN', 'TASK']
    drop = ['File_name']

    if should_drop:
        drop.extend(might_drop)

    return df.drop(columns=drop)


def main():
    csv_file, output_path, should_drop = input_params()
    df = pd.read_csv(csv_file).copy()
    df = compress_csv_file(df, should_drop)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
