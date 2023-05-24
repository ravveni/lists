#!/usr/bin/env

def find_longest_string(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()

    longest_string = ""

    for line in lines:
        if len(line) > len(longest_string):
            longest_string = line

    longest_string = longest_string.capitalize()

    print("Longest string in " + filepath + ": " + longest_string)

find_longest_string('people/first_names.txt')
find_longest_string('people/last_names.txt')

find_longest_string('people/femme_names.txt')
find_longest_string('people/masc_names.txt')
