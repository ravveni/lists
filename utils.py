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

def remove_duplicates_and_sort_list(filepath, capitalize = True, new_line = True):
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()

    file = open(filepath, 'w')
    no_dup_lines = sorted(list(dict.fromkeys(lines)))

    for no_dup_line in no_dup_lines:
        no_dup_line = no_dup_line.strip()

        if capitalize:
            no_dup_line = no_dup_line.capitalize()

        if new_line:
            no_dup_line = no_dup_line + "\n"

        file.write(no_dup_line)

    file.close()

def separate_commaed_list(filepath, new_line = True):
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
        if new_line:
            first_column.write(split_line[0] + "\n")
        else:
            first_column.write(split_line[0])

        second_column.write(split_line[1])

    first_column.close()
    second_column.close()

remove_duplicates_and_sort_list("names/popes.txt", False)
