import glob
import random
import csv
### Generates a datasetlist based on all available .tif files  ###
### Place this file in the top directory of your sentinel data ###

# Configure the split for the dataset
TRAIN_PERC = 0.6
VALIDATION_PERC = 0.2
TEST_PERC = 0.2

assert TRAIN_PERC + VALIDATION_PERC + TEST_PERC == 1.0

all_filenames = [fn.replace('s1/', '') for fn in glob.glob('s1/*.tif')]
len_all_files = len(all_filenames)
print(len(all_filenames), 'files found in s1.')

random.shuffle(all_filenames)

train_val_split_idx = int(TRAIN_PERC * len_all_files)
val_test_split_idx = int((VALIDATION_PERC + TRAIN_PERC) * len_all_files)

with open('datasetfilelist_full.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')

    # Write training set
    for fn in all_filenames[:train_val_split_idx]:
        csvwriter.writerow(['1', 's1', 's2_cloudFree', 's2_cloudy', fn])
    
    # Write validation set
    for fn in all_filenames[train_val_split_idx:val_test_split_idx]:
        csvwriter.writerow(['2', 's1', 's2_cloudFree', 's2_cloudy', fn])

    # Write test set
    for fn in all_filenames[val_test_split_idx:]:
        csvwriter.writerow(['3', 's1', 's2_cloudFree', 's2_cloudy', fn])


