#!/usr/bin/env

def find_longest_string(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()

    longest_string = ""

    for line in lines:
        if len(line) > len(longest_string):
            longest_string = line

    longest_string = longest_string.capitalize()

    print("Longest string in " + filepath + ": " + longest_string)

def remove_duplicates_from_list(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()

    file = open(filepath, 'w')
    no_dup_lines = sorted(list(dict.fromkeys(lines)))

    for no_dup_line in no_dup_lines:
        file.write(no_dup_line) # adjust new line as needed

    file.close()

def separate_commaed_list(filepath):
    split_filepath = filepath.split("/")
    folder = split_filepath[0]
    filename = split_filepath[1].split(".")[0]
    new_base_filepath = folder + "/" + filename

    first_column = open(new_base_filepath + "_0.txt", 'w')
    second_column = open(new_base_filepath + "_1.txt", 'w')

    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        split_line = line.split(", ")
        first_column.write(split_line[0] + "\n") # adjust new line as needed
        second_column.write(split_line[1])

    first_column.close()
    second_column.close()

remove_duplicates_from_list("geography/canadian_us_cities.txt")
