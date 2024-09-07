"""Takes the recordings files from the source directory and pairs them with
a txt contating the word uttered in this recording (both files will have the
same name). Stores all the files in a single directory for convenience"""
import librosa
import librosa.display
import soundfile as sf
import os
import pickle

import pandas as pd

import re  # for regular expressions
from unidecode import unidecode  # for removing special characters like é


# user input
def input_params():
    # Path of the directory with the example audio files
    source_directory_name = 'exampleNewData'
    source_directory = f"../{source_directory_name}"

    # Specify the path for the new audio file
    destination_directory = '../prepared_manually_' + source_directory_name

    # Stimuli duration table path
    stimuli_duration_path = '../Excels/Stimuli Duration.xlsx'

    return source_directory, destination_directory, stimuli_duration_path  # do NOT change


# The dictionaries for indexing file names
num_to_name = {}
name_to_num = {}


def load_audio_files(samples_folder):
    folder_content = os.listdir(samples_folder)
    loaded_audio = []
    loaded_sr = []
    for file in folder_content:
        print("Loading " + file)
        loaded_audio.append(librosa.load(samples_folder + "/" + file)[0])
        loaded_sr.append(librosa.load(samples_folder + "/" + file)[1])
    return loaded_audio, loaded_sr


def process_wav_file(input_file, output_directory, relative_path, robot_times):
    # The function slices the file and saves the result in a similar path to the original
    # The function returns features that cannot be extracted after the slicing is done, like reaction time

    if not input_file.endswith(".wav"):
        return

    print(input_file)
    audio_data, sample_rate = librosa.load(input_file)
    copied_audio_data = audio_data.copy()
    file_name = input_file

    pattern = r'\((.*?)\)'  # This regular expression captures content inside parentheses
    match = re.search(pattern, file_name)

    word = match.group(1)

    # Create the output file with the same relative path in the specified directory
    output_file = os.path.join(output_directory, relative_path)
    sf.write(output_file, copied_audio_data, int(sample_rate))

    return word


def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


def copy_directory_with_wav_processing(source_directory, destination_directory, robot_times):
    # Copy the directory tree
    os.mkdir(destination_directory)

    count = 0

    # Walk through the copied directory and process each WAV file
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith('.wav'):
                if count % 100 == 0:
                    print("copied ", count, " files")
                file_path = os.path.join(root, file)
                # Get the relative path within the directory structure
                relative_path = os.path.relpath(file_path, source_directory)

                audio_data, sample_rate = librosa.load(file_path)
                copied_audio_data = audio_data.copy()
                file_name = file_path

                pattern = r'\((.*?)\)'  # This regular expression captures content inside parentheses
                match = re.search(pattern, file_name)

                word = match.group(1)

                # Create the output file with the same relative path in the specified directory
                output_file = os.path.join(destination_directory, str(count)+".wav")
                sf.write(output_file, copied_audio_data, int(sample_rate))

                # Create a text file with the transcription of the file
                output_text_file = os.path.join(destination_directory, str(count) + ".txt")
                with open(output_text_file, 'w') as text_file:
                    text_file.write(word)

                # added the name and numbers to the dictionary
                name_to_num[repr(file_path)] = count
                num_to_name[count] = repr(file_path)

                count += 1


def main():
    source_directory, destination_directory, stimuli_duration_path = input_params()

    # get the duration of each recording of the computer
    df = pd.read_excel(stimuli_duration_path)
    robot_times = df.set_index('Word')['Modified Duration'].to_dict()
    robot_times = {unidecode(key).lower(): value for key, value in robot_times.items()}

    copy_directory_with_wav_processing(source_directory, destination_directory, robot_times)
    print(num_to_name)
    print()
    print(name_to_num)

    # create a binary pickle file
    f = open("num_to_name.pkl", "wb")
    # write the python object (dict) to pickle file
    pickle.dump(num_to_name, f)
    # close file
    f.close()

    # create a binary pickle file
    f = open("name_to_num.pkl", "wb")
    # write the python object (dict) to pickle file
    pickle.dump(name_to_num, f)
    # close file
    f.close()

if __name__ == "__main__":
    main()
