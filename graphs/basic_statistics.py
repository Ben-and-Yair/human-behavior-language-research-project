import pandas as pd
import matplotlib.pyplot as plt
import os


def input_params():
    csv_path = '../csvFiles/filtered_recordings_Olly.csv'
    output_folder = 'basic_statistics_results'
    return csv_path, output_folder


def plot_session_distribution(df, output_folder, file_name):
    """
    This function takes a DataFrame with a column named 'SESS' containing integer values 1-4
    and generates a bar plot showing the number of recordings in each session.
    The exact number of recordings is displayed on top of each bar.
    The plot is saved in the specified output directory with the given filename.
    """
    # Count the number of recordings for each session
    session_counts = df['SESS'].value_counts().sort_index()

    # Create a bar plot
    plt.figure(figsize=(8, 6))
    bars = session_counts.plot(kind='bar', color='skyblue')

    # Annotate bars with the exact number of recordings
    for bar in bars.containers[0]:
        bars.annotate(f'{int(bar.get_height())}',
                      xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                      xytext=(0, 3),  # 3 points vertical offset
                      textcoords="offset points",
                      ha='center', fontsize=12)

    plt.title('Number of Recordings in Each Session', fontsize=16)
    plt.xlabel('Session', fontsize=14)
    plt.ylabel('Number of Recordings', fontsize=14)

    # Save the plot in the specified directory
    plt.savefig(os.path.join(output_folder, file_name))
    plt.close()


def plot_conditional_session_distribution(df, output_folder):
    """
    This function takes a DataFrame with a 'SESS' and 'COND' column.
    It creates a subdirectory in the specified output directory for each unique value in 'COND'.
    Within each subdirectory, it generates and saves a bar plot showing the number of recordings in each session.
    """
    # Get unique values in 'COND'
    cond_values = df['COND'].unique()

    # Create a directory for each 'COND' and plot the session distribution
    cond_dir = os.path.join(output_folder, "number_of_recordings_in_each_SESS_per_COND")
    os.makedirs(cond_dir, exist_ok=True)
    for cond in cond_values:
        cond_df = df[df['COND'] == cond]
        file_name = "number_of_recordings_in_each_SESS_COND_" + cond.strip()
        plot_session_distribution(cond_df, cond_dir, file_name)


def plot_cond_overall_distribution(df, output_folder, file_name):
    """
    This function takes a DataFrame with a 'COND' column and generates a bar plot
    showing the overall number of recordings for each 'COND'.
    The exact number of recordings is displayed on top of each bar.
    The plot is saved in the specified output directory with the given filename.
    """
    # Count the number of recordings for each 'COND'
    cond_counts = df['COND'].value_counts().sort_index()

    # Create a bar plot
    plt.figure(figsize=(8, 6))
    bars = cond_counts.plot(kind='bar', color='skyblue')

    # Annotate bars with the exact number of recordings
    for bar in bars.containers[0]:
        bars.annotate(f'{int(bar.get_height())}',
                      xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                      xytext=(0, 3),  # 3 points vertical offset
                      textcoords="offset points",
                      ha='center', fontsize=12)

    # Set plot title and labels
    plt.title('Overall Number of Recordings in Each Condition (COND)', fontsize=16)
    plt.xlabel('Condition (COND)', fontsize=14)
    plt.ylabel('Number of Recordings', fontsize=14)

    # Save the plot in the specified directory
    plt.savefig(os.path.join(output_folder, file_name))
    plt.close()


def plot_accr_distribution(df, output_folder, file_name):
    """
    This function takes a DataFrame with a column named 'ACCR'
    and generates a bar plot showing the number of recordings for each unique value in 'ACCR'.
    The exact number of recordings is displayed on top of each bar.
    The plot is saved in the specified output directory with the given filename.
    """
    # Count the number of recordings for each value in 'ACCR'
    accr_counts = df['ACCR'].value_counts().sort_index()

    # Create a bar plot
    plt.figure(figsize=(8, 6))
    bars = accr_counts.plot(kind='bar', color='skyblue')

    # Annotate bars with the exact number of recordings
    for bar in bars.containers[0]:
        bars.annotate(f'{int(bar.get_height())}',
                      xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                      xytext=(0, 3),  # 3 points vertical offset
                      textcoords="offset points",
                      ha='center', fontsize=12)

    # Set plot title and labels
    plt.title('Number of Recordings in Each ACCR', fontsize=16)
    plt.xlabel('ACCR', fontsize=14)
    plt.ylabel('Number of Recordings', fontsize=14)

    # Save the plot in the specified directory
    plt.savefig(os.path.join(output_folder, file_name))
    plt.close()


def plot_accr_by_sess(df, output_folder, file_name):
    """
    This function takes a DataFrame with 'SESS' and 'ACCR' columns
    and generates a grouped bar plot showing the number of rows where ACCR=0 and ACCR=1 for each session.
    The plot is saved in the specified output directory with the given filename.
    """
    # Group by 'SESS' and 'ACCR', then count the occurrences
    accr_sess_counts = df.groupby(['SESS', 'ACCR']).size().unstack(fill_value=0)

    # Create a grouped bar plot
    accr_sess_counts.plot(kind='bar', stacked=False, color=['skyblue', 'lightcoral'], figsize=(10, 7))

    # Annotate bars with the exact number of recordings
    for i, (sess, counts) in enumerate(accr_sess_counts.iterrows()):
        plt.text(i - 0.15, counts[0] + 1, str(counts[0]), ha='center', va='bottom', fontsize=12)
        plt.text(i + 0.15, counts[1] + 1, str(counts[1]), ha='center', va='bottom', fontsize=12)

    # Set plot title and labels
    plt.title('Number of Rows for Each ACCR Value by Session', fontsize=16)
    plt.xlabel('Session', fontsize=14)
    plt.ylabel('Number of Rows', fontsize=14)

    # Set legend
    plt.legend(title='ACCR', labels=['0', '1'])

    # Save the plot in the specified directory
    plt.savefig(os.path.join(output_folder, file_name))
    plt.close()


csv_path, output_folder = input_params()
os.makedirs(output_folder, exist_ok=True)
df = pd.read_csv(csv_path)

plot_session_distribution(df, output_folder, 'number_of_recordings_in_each_SESS.png')
plot_conditional_session_distribution(df, output_folder)
plot_cond_overall_distribution(df, output_folder, "overall_number_of_recordings_in_each_COND.png")
plot_accr_distribution(df, output_folder, "number_of_recordings_in_each_ACCR.png")
plot_accr_by_sess(df, output_folder, "number_of_accr_0_and_1_by_sess.png")