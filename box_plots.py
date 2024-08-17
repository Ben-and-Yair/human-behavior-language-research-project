import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def normalize_by_category(df, category_column, value_columns):
    for value_column in value_columns:
        # Group by the category column
        grouped = df.groupby(category_column)

        # Calculate mean and standard deviation for each category
        mean_per_category = grouped[value_column].mean()
        std_per_category = grouped[value_column].std()

        # Normalize values based on mean and standard deviation
        df[value_column] = df.apply(
            lambda row: (row[value_column] - mean_per_category[row[category_column]]) / std_per_category[
                row[category_column]], axis=1)

    return df


def normalize_column(df, columns):
    for column in columns:
        df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df


def plot_feature_boxplot(df_all_classes, important_features, title, target_label):
    sns.set(style="ticks")
    fig, ax = plt.subplots(1, figsize=(10, 10))

    # normalizing all features, so they fit in
    # the same range for visibility considerations
    for f in important_features:
        df_all_classes[f] = (df_all_classes[f] - df_all_classes[f].mean()) / df_all_classes[f].mean()

    df_melted = pd.melt(df_all_classes, id_vars=[target_label], value_vars=important_features)
    # Plot the boxplot using seaborn
    p = sns.boxplot(x="variable", y="value", hue=target_label, data=df_melted, palette="Pastel1", showfliers=False)
    labels = [label.get_text() for label in ax.get_xticklabels()]
    ax.set_xticklabels([label[::-1] if not label.isascii() else label for label in labels])
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.2)
    p.set_title(title)
    plt.show()
    return fig


df = pd.read_csv('csv_files/filtered_recordings_Olly.csv')
label_column = 'SESS'
remove_sessions = [2, 3]
important_features = list(df.columns)


for sess in remove_sessions:
    df = df.drop(df[df['SESS'] == sess].index)


important_features = ['Reaction_time(s)', 'Total_duration(s)', 'duration', 'meanIntesnity', 's_last_duration', 's_last_pitch_mean', 's_last_intensity_mean']
# columns = ['Reaction_time(s)', 'Total_duration(s)', 'duration']
# df = df[columns]

# categorical_features = ['WORD', 'COND']
#
# for feature in categorical_features:
#     df[feature] = df[feature].astype('category')
#     df[feature] = df[feature].cat.codes

plot_feature_boxplot(df, important_features, "features box plots", label_column)

