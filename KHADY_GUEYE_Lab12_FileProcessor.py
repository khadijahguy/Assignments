# Creator: Khady Gueye

import os
import csv

# Function to merge the two text files and save the result
def merge(file1_path, file2_path, result_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

        with open(result_path, 'w') as result:
            result.write(content1 + '\n' + content2)

        print(f"Files merged successfully into '{result_path}'")
    except Exception as e:
        print(f"Error merging files: {e}")

# Function to create multiple copies of a file
def copy(file1_path, num_copies):
    try:
        with open(file1_path, 'r') as source:
            content = source.read()

        for i in range(1, num_copies + 1):
            new_file = f"copy_{i}_{os.path.basename(file1_path)}"
            with open(new_file, 'w') as new:
                new.write(content)
        print(f"{num_copies} copies created successfully.")
    except Exception as e:
        print(f"Error copying file: {e}")

# Function to convert a text file to CSV format
def convert_to_csv(text_file_path, csv_file_path):
    try:
        with open(text_file_path, 'r') as txt, open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for line in txt:
                writer.writerow([line.strip()])
        print(f"File converted to CSV successfully at '{csv_file_path}'")
    except Exception as e:
        print(f"Error converting to CSV: {e}")

# Function to print number of lines and words in a text file
def file_statistics(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
        print(f"Lines: {num_lines}, Words: {num_words}")
    except Exception as e:
        print(f"Error calculating file statistics: {e}")
