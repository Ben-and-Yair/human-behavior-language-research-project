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
[Add explanations for CSV files here.]

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
[Add explanations for main code files here.]

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
