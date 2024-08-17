import pandas as pd


# user input
def input_params():
    csv_path = '../csvFiles/filtered_recordings_Olly.csv'
    output_path = '../csvFiles/filtered_recordings_Olly.csv'

    return csv_path, output_path # do NOT change


def compress_csv_file(df):

    return df

# Load the CSV file
csv_file_path = 'csv_files/segments_features_and_all_features_with_participants_logs_with_difficulty.csv'
df_copy = pd.read_csv(csv_file_path)

# Drop columns starting with 'Unnamed', 'TSKN', 'TRLN', 'BLKN', 'TASK', 'File_name'
columns_to_drop = [col for col in df_copy.columns if
                   col.startswith(('Unnamed', 'TSKN', 'TRLN', 'BLKN', 'TASK', 'File_name'))]
df_copy = df_copy.drop(columns=columns_to_drop)

# Group by 'SUBJ', 'SESS', 'WORD'
grouped = df_copy.groupby(['SUBJ', 'SESS', 'WORD'], as_index=False)

# Get all numeric columns (excluding 'SUBJ', 'SESS', 'WORD')
columns = [col for col in df_copy.columns if col not in ['SUBJ', 'SESS', 'WORD', 'COND']]

# Initialize an empty DataFrame to store the final results
final_data = pd.DataFrame(
    columns=['SUBJ', 'SESS', 'WORD', 'COND', 'recordings_number'] +
            [f'{col}_mean' for col in columns] + [f'{col}_std' for col in columns])

# Iterate over each group
for name, group in grouped:
    # Save the original values of 'SUBJ', 'SESS', and 'WORD'
    subj, sess, word = name
    cond = group.iloc[0]['COND']

    # Calculate the number of recordings in the group
    recordings_number = len(group)

    # Drop 'SUBJ', 'SESS', and 'WORD' columns
    group = group.drop(columns=['SUBJ', 'SESS', 'WORD', 'COND'])

    # Calculate mean and std for numeric columns
    means = group.mean()
    stds = group.std()

    # Create a new row for the final DataFrame
    new_row = pd.DataFrame([[subj, sess, word, cond, recordings_number] + list(means) + list(stds)],
                           columns=['SUBJ', 'SESS', 'WORD', 'COND', 'recordings_number'] + [f'{col}_mean' for col in
                                                                                    columns] + [f'{col}_std' for
                                                                                                        col in
                                                                                                        columns])

    # Append the new row to the final DataFrame
    final_data = pd.concat([final_data, new_row], ignore_index=True)

# Save the processed data to a new CSV file
output_csv_file_path = 'csv_files/compressed_csv_file.csv'
final_data.to_csv(output_csv_file_path, index=False)

print("Processing completed. Output saved to", output_csv_file_path)
