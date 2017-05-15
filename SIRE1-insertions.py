#import
import pandas as pd
import numpy as np

#load csv into pandas as df
hit_file = "filtered_hit_table.csv"
df = pd.read_csv(hit_file, index_col=None)

#SIRE1-insertion-library
to_file = open('SIRE1-insertions.fasta', 'w')

#indel
def find_indel(start_pos, end_pos, chromosome, row):
	if (chromosome < 10):
		file_name = "Gm0" + str(chromosome) + ".fa"
		from_file = open(file_name, 'r')

	if (chromosome >= 10):
		file_name = "Gm" + str(chromosome) + ".fa"
		from_file = open(file_name, 'r')

	#initialize parameters (Swap if start position is larger)
	if (start_pos > end_pos):
		print "\nInsertion " + str(row + 1) + " is 3-5."
		temp = start_pos
		start_pos = end_pos
		end_pos = temp

	start_pos = start_pos - 500
	end_pos = end_pos + 500
	sequence = None
	target_region = False
	position = 0

	#write intended sequence
	for line in from_file:
		for char in line:
			if (position == start_pos):
				target_region = True
			if (position == end_pos):
				target_region=False
			if (target_region == True):
				sequence = str(sequence) + str(char)
			position = position + 1

	print "\nWriting Insertion Sequence " + str(row + 1) + "."
	to_file.write("\n> Insertion " +  str(row + 1) + "\n " + sequence)
#run find_indel function on every sequence
row = 0
while (row < 145):
	#find_flanking_region(start_pos, end_pos, chromosome, row)
	print "\n Searching for Insertion " + str(row + 1) + "."
	find_indel(df.iat[row,11], df.iat[row,12], df.iat[row,15], row)
	row = row + 1
