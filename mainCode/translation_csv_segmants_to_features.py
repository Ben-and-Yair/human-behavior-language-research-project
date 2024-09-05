"""Reads the csv files from segmentation_separation_csv directory, extracts the information
and calculates the features from the segments, saving it to "csv_files/segments_features.csv"""
import pandas as pd
import pickle
import os
import librosa
import re

import parselmouth
from parselmouth.praat import call

import numpy as np

import statistics


# user input
def input_params():
    csv_directory = "segmentation_separation_csv_exampleNewData"

    return csv_directory  # do NOT change


# This function calculates auditory features based on the division to segments of the data
# This function returns whatever it needs to turn it into a row of a pandas dataframe
# (probably a dictionary of features)
def calculate_features(segments_df, file_path_original):
    # Do fancy calculations:
    # For the last 2 segments we extract their duration and the mean and std of their intensity, pitch and formants

    # Loading the matching file
    # Convert backslashes to forward slashes for cross-platform compatibility
    file_path = file_path_original.replace('\\\\', '/')

    file_path = file_path[1:-1]

    if not os.path.exists(file_path):
        print("not found: ", file_path)
        return {}

    audio_data, sample_rate = librosa.load(file_path)

    # Remove rows containing the "<p:>" in "MAU"
    segments_df = segments_df[~segments_df["MAU"].str.contains("<p:>")]

    attributes = {}

    # X-SAMPA representation of vowels
    x_sampa_vowels = {'i', 'I', 'I\\', 'e', 'E', 'a', 'A', 'O', 'o', 'u', 'U', 'M', 'Q', 'U\\', 'V', 'Y'
                      '@\\', '{', '}', '1', '2', '3', '3\\', '6', '7', '8', '9', '&', '/', 'u:', 'i:',
                      '@U'}

    pattern = r'\((.*?)\)'  # This regular expression captures content inside parentheses
    match = re.search(pattern, file_path)

    word = match.group(1)

    if segments_df.iloc[-1]["MAU"] in x_sampa_vowels:
        type_of_word = 1
    else:
        type_of_word = 0

    attributes["type"] = type_of_word

    time_step = 0.
    min_time = 0.
    max_time = 0.
    pitch_floor = 101.
    # pitch_floor = 100.

    pitch_ceiling = 600.
    unit = 'Hertz'

    # f0min, f0max = 75, 300
    f0min, f0max = pitch_floor, 300

    last_index = segments_df.shape[0]

    segments_to_calculate = [0, last_index-1]
    for i in segments_to_calculate:
        si = segments_df.iloc[i]
        si_audio = audio_data[si["BEGIN"]: si["BEGIN"] + si["DURATION"]]

        # Extract intensity (loudness) features
        rms_window = int(len(si_audio) / 10)  # Set window size to 1/10th of the signal length
        intensity = librosa.feature.rms(y=si_audio, frame_length=rms_window)

        # Extract pitch features
        hop_length = 128  # 512  # Adjust as needed
        pitches, magnitudes = librosa.piptrack(y=si_audio, sr=sample_rate,
                                               hop_length=hop_length, n_fft=min(2048, len(si_audio)))

        index = "first"
        if i == segments_df.shape[0]-1:
            index = "last"

        attributes['s_'+str(index)+"_intensity_mean"] = np.mean(intensity)
        attributes['s_'+str(index)+"_intensity_std"] = np.std(intensity)
        attributes['s_'+str(index)+"_pitch_mean"] = np.mean(pitches)
        attributes['s_'+str(index)+"_pitch_std"] = np.std(pitches)
        attributes['s_'+str(index)+"_duration"] = si["DURATION"]

    return attributes


def main():
    csv_directory = input_params()

    # Load the dictionary that translate csv file to actual name
    with open('name_to_num.pkl', 'rb') as handle:
        name_to_num = pickle.load(handle)

    # Load the dictionary that translate csv file to actual name
    with open('num_to_name.pkl', 'rb') as handle:
        num_to_name = pickle.load(handle)

    segments_features_csv = pd.read_csv("csv_files/segments_features.csv")

    all_extracted_features = []

    count = 0
    amount = len(os.listdir(csv_directory))
    for filename in os.listdir(csv_directory):
        f = os.path.join(csv_directory, filename)

        count += 1

        if count == 1:
            continue

        if count % 200 == 0:
            print("processed ", count, " files out of ", amount)

        df = pd.read_csv(f, sep=";")
        df = df[["BEGIN", "DURATION",  "MAU", "ORT"]]
        file_name = num_to_name[int(filename[:-4])]

        extracted_features1 = calculate_features(df, file_name)

        if extracted_features1:  # is the dictionary not empty
            extracted_features = {"File_name": file_name, **extracted_features1}
            all_extracted_features.append(extracted_features)

    all_extracted_features_csv = pd.DataFrame(all_extracted_features)
    all_extracted_features_csv.to_csv("csv_files/segments_features.csv", index=False)


if __name__ == "__main__":
    main()
