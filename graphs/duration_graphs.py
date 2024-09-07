import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np


duration_type = 'duration'  # can be also 'Total_duration(s)'

def input_params():
    csv_path = '../csvFiles/filtered_recordings_Olly.csv'
    output_folder = 'duration_graphs_results'
    return csv_path, output_folder


# One graph, average difference per word
def plot_duration_difference(df, output_dir):
    words = sorted(df['WORD'].unique())  # Get unique words
    duration_difference = [] # Prepare a list to store the difference in mean durations

    for word in words:
        word_df = df[df['WORD'] == word]

        # Calculate mean durations for SESS 4 and SESS 1
        mean_duration_4 = word_df[word_df['SESS'] == 4][duration_type].mean()
        mean_duration_1 = word_df[word_df['SESS'] == 1][duration_type].mean()

        # Calculate the difference and append to the list
        duration_difference.append(mean_duration_4 - mean_duration_1)

    x = range(len(words))
    plt.figure(figsize=(10, 6))
    plt.bar(x, duration_difference, width=0.4, align='center')
    plt.xlabel('Words')
    plt.ylabel('Mean Duration Difference (s)')
    plt.title('Difference in Mean Duration (SESS 4 - SESS 1) for Each Word')
    plt.xticks(x, words, rotation=90)
    plt.tight_layout()

    plt.savefig(os.path.join(output_folder, 'duration_difference_bar_chart.png'))
    plt.close()


# Graph for each subj, with average difference for each word
def subj_plot_duration_difference(df, output_folder):
    subjects = df['SUBJ'].unique()  # Get unique subjects

    subj_dir = os.path.join(output_folder, 'subjs')
    os.makedirs(subj_dir, exist_ok=True)

    for subj in subjects:
        subj_df = df[df['SUBJ'] == subj]
        words = sorted(subj_df['WORD'].unique())  # Get unique words
        duration_difference = []

        for word in words:
            word_df = subj_df[subj_df['WORD'] == word]

            # Calculate mean durations for SESS 4 and SESS 1
            mean_duration_4 = word_df[word_df['SESS'] == 4][duration_type].mean()
            mean_duration_1 = word_df[word_df['SESS'] == 1][duration_type].mean()

            # Calculate the difference and append to the list
            duration_difference.append(mean_duration_4 - mean_duration_1)

        x = range(len(words))
        plt.figure(figsize=(10, 6))
        plt.bar(x, duration_difference, width=0.4, align='center')
        plt.xlabel('Words')
        plt.ylabel('Mean Duration Difference (s)')
        plt.title(f'Difference in Mean Duration (SESS 4 - SESS 1) for Each Word - SUBJ {subj}')
        plt.xticks(x, words, rotation=90)
        plt.tight_layout()

        # Save the plot with prefix of SUBJ number
        filename = f'{int(subj):03f}_duration_difference_bar_chart.png'
        plt.savefig(os.path.join(subj_dir, filename))
        plt.close()


# A graph for each word, with an average difference for each subj
def word_plot_duration_difference(df, output_folder):
    # Get unique words and subjects
    words = sorted(df['WORD'].unique())
    subjects = df['SUBJ'].unique()

    # Create a directory to save the word plots
    words_dir = os.path.join(output_folder, 'words')
    os.makedirs(words_dir, exist_ok=True)

    # Iterate over each word
    for word in words:
        # Prepare a list to store the difference in mean durations for each subject
        duration_difference = []

        # Iterate over each subject
        for subj in subjects:
            # Filter the DataFrame for the current word and subject
            word_df = df[(df['WORD'] == word) & (df['SUBJ'] == subj)]

            # Calculate mean durations for SESS 4 and SESS 1
            mean_duration_4 = word_df[word_df['SESS'] == 4][duration_type].mean()
            mean_duration_1 = word_df[word_df['SESS'] == 1][duration_type].mean()

            # Calculate the difference and append to the list
            duration_difference.append(mean_duration_4 - mean_duration_1)

        # Create a bar chart
        x = range(len(subjects))
        plt.figure(figsize=(10, 6))
        plt.bar(x, duration_difference, width=0.4, align='center')
        plt.xlabel('Subjects')
        plt.ylabel('Mean Duration Difference (s)')
        plt.title(f'Difference in Mean Duration (SESS 4 - SESS 1) for Each Subject - WORD {word}')
        plt.xticks(x, subjects, rotation=90)
        plt.tight_layout()

        # Save the plot with prefix of WORD
        filename = f'{word}_duration_difference_bar_chart.png'
        plt.savefig(os.path.join(words_dir, filename))
        plt.close()


# One graph, one column per participant
def overall_subject_plot_duration_difference(df, output_folder):
    # Get unique subjects and sort them
    subjects = sorted(df['SUBJ'].unique())

    # Prepare a list to store the overall difference in mean durations for each subject
    overall_duration_difference = []

    # Iterate over each subject
    for subj in subjects:
        # Filter the DataFrame for the current subject
        subj_df = df[df['SUBJ'] == subj]

        # Calculate mean durations for SESS 4 and SESS 1 over all words
        mean_duration_4 = subj_df[subj_df['SESS'] == 4][duration_type].mean()
        mean_duration_1 = subj_df[subj_df['SESS'] == 1][duration_type].mean()

        # Calculate the difference and append to the list
        overall_duration_difference.append(mean_duration_4 - mean_duration_1)

    # Create a bar chart
    x = range(len(subjects))
    plt.figure(figsize=(10, 6))
    plt.bar(x, overall_duration_difference, width=0.4, align='center')
    plt.xlabel('Subjects')
    plt.ylabel('Mean Duration Difference (s)')
    plt.title('Overall Difference in Mean Duration (SESS 4 - SESS 1) for Each Subject')
    plt.xticks(x, subjects, rotation=90)
    plt.tight_layout()

    plt.savefig(os.path.join(output_folder, 'overall_subject_duration_difference_bar_chart.png'))
    plt.close()


# One graph, for each word average sign
def word_sign_mean_plot(df, output_folder):
    # Get unique words and sort them
    words = sorted(df['WORD'].unique())
    subjects = df['SUBJ'].unique()
    word_sign_means = []

    for word in words:
        sign_differences = []

        for subj in subjects:
            word_subj_df = df[(df['WORD'] == word) & (df['SUBJ'] == subj)]

            # Calculate mean durations for SESS 4 and SESS 1
            mean_duration_4 = word_subj_df[word_subj_df['SESS'] == 4][duration_type].mean()
            mean_duration_1 = word_subj_df[word_subj_df['SESS'] == 1][duration_type].mean()

            # Calculate the difference and take the sign
            if pd.notnull(mean_duration_4) and pd.notnull(mean_duration_1):  # Check if values are not NaN
                duration_difference = mean_duration_4 - mean_duration_1
                sign_difference = np.sign(duration_difference)
                sign_differences.append(sign_difference)

        # Calculate the mean of the signs for the current word
        if sign_differences:  # Check if list is not empty
            mean_sign_difference = np.mean(sign_differences)
            word_sign_means.append(mean_sign_difference)
        else:
            word_sign_means.append(np.nan)  # In case there are no valid differences

    # Create a bar chart
    x = range(len(words))
    plt.figure(figsize=(10, 6))
    plt.bar(x, word_sign_means, width=0.4, align='center')
    plt.xlabel('Words')
    plt.ylabel('Mean of Sign Differences')
    plt.title('Mean of Sign Differences (SESS 4 - SESS 1) for Each Word')
    plt.xticks(x, words, rotation=90)
    plt.tight_layout()

    # Save the plot
    plt.savefig(os.path.join(output_folder, 'word_sign_mean_bar_chart.png'))
    plt.close()


csv_path, output_folder = input_params()
os.makedirs(output_folder, exist_ok=True)
df = pd.read_csv(csv_path)


plot_duration_difference(df, output_folder)
subj_plot_duration_difference(df, output_folder)
word_plot_duration_difference(df, output_folder)
overall_subject_plot_duration_difference(df, output_folder)
word_sign_mean_plot(df, output_folder)
