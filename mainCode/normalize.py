import pandas as pd


# user input
def input_params():
    csv_file = '../csvFiles/filtered_recordings_Olly.csv'
    output_path = '../csvFiles/check.csv'
    normalize_method = 'per_feature'  # one of ['per_feature', 'per_subject', 'per_subject_per_sess', 'drop']
    features = []  # which features to normalize

    return csv_file, output_path, normalize_method, features  # do NOT change


def normalize(df, normalization_method, features):
    if normalization_method == 'per_feature':
        return normalize_per_feature(df, features)
    elif normalization_method == "per_subject":
        return normalize_per_subject(df, features)
    elif normalization_method == "per_subject_per_sess":
        return normalize_per_subject(df, features)
    elif normalization_method == "drop":
        return normalize_per_subject(df, features)
    return df


def normalize_per_feature(df, features):
    means = df[features].mean()
    for feature in features:
        df[feature] = (df[feature] - means[feature]) / means[feature]
    return df


def normalize_per_subject(df, features):
    grouped_subject = df.groupby('SUBJ')
    for subject, subject_group in grouped_subject:
        for feature in features:
            mean = subject_group[feature].mean()
            subject_group[feature] = (subject_group[feature] - mean) / mean
        df.loc[subject_group.index, features] = subject_group[features]
    return df


def normalize_per_subject_per_session(df, features):
    grouped_subject = df.groupby('SUBJ')
    for subject, subject_group in grouped_subject:
        grouped_session = subject_group.groupby('SESS')
        for session, session_group in grouped_session:
            for feature in features:
                mean = session_group[feature].mean()
                session_group[feature] = (session_group[feature] - mean) / mean
            df.loc[session_group.index, features] = session_group[features]

    return df


def main():
    csv_file, output_path, normalize_method, features = input_params()
    df = pd.read_csv(csv_file).copy()
    df = normalize(df, normalize_method, features)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
