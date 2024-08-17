# human-behavior-language-research-project
## About the project
Using ML tools to study the language learning process - Part of a research project in Haifa University

We received the recordings of multiple participants (about 50) saying different made up words (from 3 artificially constructed vocabularies) over the course of several days. Then, We cleaned up the data (removed silent sections and removed unintelligible recordings), separated each recording to it's syllables, extracted auditory features and then used the random forest classifier to find the distinguishing features of learning (thanks to sklearn's feature selection option we were able to receive a ranking of each feature's importance in the construction of the random forest)

The data we worked with is currently unavailable to the public (which is why it isn't in this repository)


## Run the project
### Installations
1. install python 3.11 and python IDE (e.g. Pycharm)
2. install the following packages: seaborn, matplotlib, pandas, parselmouth, numpy, librosa, noisereduce, soundfile, re, shutil, os, unidecode

### Project
1. *Slicing*: The slicing is done by applying noise suppression several times, then finding the loudest point
     in the recording, then expanding left and right as long as the recording isn't below a certain threshold
     for too long (determined by the hyperparameters given).
2. *Measure*: Using both parselmouth (a python API for PRAAT) and librosa to extract a plethora of auditory features (intensity, pitch, formants and more...).
3. *Segmentation*: Using WebMaus Basic (a site which does forced alignment online) to segment each of the recordings in order to measure the first and last segment of each recording.
4. *Extracting logs information*: Extracting relevant features (e.g. the session of the recording, the number of subject, whether the participant guessed the meaning of the word correctly, etc.) from the given logs of the experiment.
5. *Merging the data*: Merging all the csv files created so far into a single csv containing all the relevant information for making predictions.
6. *Predictions*: ----
8. *Compress*: note that ['TSKN', 'TRLN', 'BLKN', 'TASK'] columns might be dropped. moreover, any non-numeric column will araise an error. 'cut_WORD' is dropped.

### Graphs and statistics
