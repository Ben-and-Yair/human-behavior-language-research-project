import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# user input
def inputParams():
    csvPath = '../csvFiles/filtered_recordings_Olly.csv'
    features = ['SESS', 'Reaction_time(s)', 'Total_duration(s)'] # do NOT remove SESS from the list
    sess = [1, 4]  # SESSions to plot
    should_normalize = True

    return csvPath, features, sess, should_normalize


def normalize_df(df, should_normalize):
    if should_normalize:
        for column in list(df.columns):
            if column != "SESS":
                df[column] = (df[column] - df[column].mean()) / df[column].mean()
    return df

def plot_feature_boxplot(df, title):
    sns.set(style="ticks")
    fig, ax = plt.subplots(1, figsize=(10, 10))

    df_melted = pd.melt(df, id_vars=['SESS'], value_vars=list(df.columns))
    p = sns.boxplot(x="variable", y="value", hue='SESS', data=df_melted, palette="Pastel1", showfliers=False)
    labels = [label.get_text() for label in ax.get_xticklabels()]
    ax.set_xticklabels([label[::-1] if not label.isascii() else label for label in labels])
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.2)
    p.set_title(title)
    plt.show()


csvFile, features, sess, should_normalize = inputParams()
df = pd.read_csv(csvFile)
df = df[features]
df = df[df['SESS'].isin(sess)]

df = normalize_df(df, should_normalize)
plot_feature_boxplot(df, "features box plots")

