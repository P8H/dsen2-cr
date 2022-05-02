import glob
import random
import csv
import re
regex = r"ROIs\d*_\w*_"
prog = re.compile(regex)

### Takes the datasplit used in the paper and applies it on a datasetfilelist with the new file names ###
### Place this file in the directory of the datasetfilelist.csv and the new datasetfilelist_full.csv ###

with open('Data/datasetfilelist_full.csv', 'r') as csvfile_new_names, open('Data/datasetfilelist_full_correct_split.csv', 'w') as csvfile_new_names_with_old_split, open('Data/datasetfilelist.csv', 'r') as csvfile_old_with_correct_split:
        csvreader_old = csv.reader(csvfile_old_with_correct_split, delimiter='\t')
        old_split_dict = {prog.match(line[4])[0] : int(line[0]) for line in csvreader_old} # prefix : split_id


        csvreader = csv.reader(csvfile_new_names, delimiter='\t')
        csvwriter = csv.writer(csvfile_new_names_with_old_split, delimiter='\t')

        failed_n = 0
        success_n = 0
        for line in csvreader:
            prefix = prog.match(line[4])[0]
            split_id = old_split_dict.get(prefix)
            if split_id == None:
                print("File with prefix", prefix, "doesn't exists in the old datasetfilelist.")
                failed_n += 1
            else:
                line[0] = split_id
                csvwriter.writerow(line)
                success_n += 1
        print("Failed on", failed_n, "files to reconstruct old filename.")
        print("Succeeded on", success_n, "files to reconstruct old filename.")

        

        

        



