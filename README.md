# README

## Authors
- **Ben Rofe-Oren**
- **Yair Slobodin**

## Supervised By
- **Hagit Hel-Or**
- **Tali Bitan**

## About the Project
This project is a machine learning and human behavior research initiative focused on language learning processes, conducted at the University of Haifa.

In this study, approximately 42 participants engaged in an experiment designed to explore the mechanics of learning a new language, which consisted of three language families (COND): Linear, Non-linear, and Complex. The experiment was structured into four sessions, each comprising three parts: training, testing, and training. During each session, participants listened to a robot pronouncing a word and repeated it five times. The collected data includes participants' audio recordings and an Excel file per participant with basic recording details.

## What We Did
1. **Audio Processing**: We trimmed all recordings to isolate the participant's voice.
2. **Vocal Parameters Calculation**: We calculated vocal parameters using existing code from Git.
3. **Segmentation**: We segmented the recordings using the WebMAUS website, which provided word-level divisions.
4. **Prediction Modeling**: We attempted to predict the session (SESS) of each participant based on various vocal parameters using Random Forest and k-fold algorithms.

## Additional Explorations
- Filtered features that showed high correlation with other features to avoid compromising feature ranking.
- Modified the dataset by session, calculating average values and standard deviations for each feature within a session.
- Analyzed the recording length parameter for further insights.
- Added a "difficulty" column to each word, based on the percentage of participants who translated it correctly.
- Applied various normalization techniques: by session, by participant, by participant and session, and general normalization across all features.

## Running the Project and File Explanations

### Folder Structure

#### csv_files
   - `sliced_features.csv`: Contains the file name of each recording, reaction time (number of seconds from when the computer finished uttering the word until the participant started speaking), and the total duration (number of seconds it took for the participant to say the word). The CSV was created using `slice_recordings.py`.
   - `processed_results2.csv`: Contains a list of auditory features (mean and standard deviation of intensity, pitch, medians of formants, another duration calculation, and jitter and shimmer calculations). The CSV was created using `measure_and_extract_auditory_features.py`.
   - `participants_logs_csv.csv`: Contains a list of features extracted from the Excel files of each participant. This includes additional information on each recording (participant's subject number, session, accuracy, the word said, and more). The CSV was created using `extract_features_from_participants_logs.py`.
   - `segments_features.csv`: Contains a list of auditory features extracted from the recordings and WebMaus segmentation (the mean and standard deviation of intensity and pitch of the first and last segments, as well as whether the word ends in a consonant or vowel). The CSV was created using `translation_csv_segments_to_features.py`.
   - `segments_features_and_all_features_with_participants_logs.csv`: Contains all the features in the aforementioned CSV files. **This CSV is the main one used for predictions**, created using `merging_recordings_and_participants_data.py`.

#### graphs
1. **basic_statistics**: Generates plots of basic CSV statistics and saves them in the "basic_statistics_result" directory:
   - `number_of_recordings_in_each_SESS.png`: Number of recordings in each session (SESS).
   - `number_of_recordings_in_each_SESS_for_each_COND.png`: Number of recordings in each session for each language family (COND).
   - `overall_number_of_recordings_in_each_COND.png`: Total number of recordings in each language family (COND).
   - `number_of_recordings_in_each_ACCR.png`: Number of recordings for each accuracy level (ACCR).
   - `number_of_accr_0_and_1_by_sess.png`: Number of recordings with accuracy levels 0 and 1, grouped by session.

2. **box_plots.py**: Generates box plots for input features, with an option to normalize the CSV data.

3. **duration_graphs**: Generates the following duration-related graphs:
   - Average duration difference per word (one consolidated graph).
   - A graph for each subject, showing the average difference for each word.
   - A graph for each word, displaying the average difference for each subject.
   - A graph showing one column per participant, illustrating overall durations.
   - A graph that represents the average sign of duration differences for each word.

#### main_code
   - `compress_sessions_csv_file.py`: generates a new csv file with average and std values for each participant for each session for each word.
   - `extract_features_from_participants_logs.py`: Receives a path to all the excel files containing extra data on each recording (`participants_logs`) and creates a CSV file (`participants_logs_csv_files`) with chosen features.
   - `measure_and_extract_auditory_features.py`: Accumulation of code from different sources that receive a source directory filled with audio files and
computes a plethora of auditory features using parselmouth (which uses PRAAT) such as intensity, pitch,
formants and more. Saves them to `csv_files/processed_results2.csv`.
   - `merging_recordings_and_participants_data.py`: Takes the given CSV files (`Sliced_features.csv`, `processed_results2.csv`, `segments_features.csv`, `participants_logs_csv.csv`) and merges them to a single CSV file used for predictions (`segments_features_and_all_features_with_participants_logs.csv`).
   - `normalize.py`: Recevies a CSV file, a list of featuers to normalize, a normalization method and an output directory and creates a new CSV file with the given features normalized according to the given method.
   - `prepare_files_for_webMaus.py`: Takes the recordings files from the source directory and pairs them with
a txt contating the word uttered in this recording (both files will have the
same name). Stores all the files in a single destination directory (given by the user) for convenience.
   - `random_forest_prediction_no_separation.py`: Reads the given configurations (and iterates over a set of options for parameters), creates a random forest
classifier, get the most important features and removes a portion of the least important ones. We repeat this
process until the number of features hits a certain threshold. All the results (and the chosen parameters) are
stored in a directory named `reports/pred...`.
   - `random_forest_prediction_with_separation.py`: Reads the given configurations (and iterates over a set of options for parameters), separates the data according to the given feature, creates a random forest
classifier, get the most important features and removes a portion of the least important ones. We repeat this
process until the number of features hits a certain threshold. All the results (and the chosen parameters) are
stored in a directory named `reports/pred...`.
   - `slice_recordings.py`: Receives as input several hyperparameters, a destination directory and a source directory filled with audio files and
slices them in order to get only the moment the participant spoke and in order to extract reaction time and duration
of speaking features for each participant. The code puts all the sliced files in the destination directory (retaining
 the folder structure of the source directory) and saves a csv named `Sliced_features_cvs` in the `csv_files`.
 directory
   - `translation_csv_segmants_to_features.py`: Reads the csv files from segmentation_separation_csv directory, extracts the information
and calculates the features from the segments, saving it to `csv_files/segments_features.csv`.

#### recordings
The recordings of the participants. **Note:** For privacy reasons, audio files will not be uploaded here.

#### sliced_recordings
The sliced recordings of the participants. **Note:** For privacy reasons, audio files will not be uploaded here.

## List of Features
[Include a detailed list of all features and columns in the dataset.]

## Special Thanks and Credits
1. **Oliver Niebuhr** - For meeting with us twice online, offering additional ideas for exploration.
2. **David Feinberg** - For writing the script used to measure vocal values in recordings. [PraatScripts](https://github.com/drfeinberg/PraatScripts/blob/master/Measure%20Pitch%2C%20HNR%2C%20Jitter%2C%20Shimmer%2C%20and%20Formants.ipynb).
3. **WebMAUS Site** - For providing segmentation of recordings into word-level segments.
