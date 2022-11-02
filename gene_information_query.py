#!/usr/bin/env python3
# gene_information_query.py


"""
Query for a given gene and species
"""

import argparse
import sys
import re
from assignment5 import my_io
from assignment5 import config


def main():
    """Business Logics"""
    argvs = get_cli_args()
    temp_host_name = argvs.HOST
    temp_gene_name = argvs.GENE
    host_name = modify_host_name(temp_host_name) \
        if temp_host_name is not None else "Homo_sapiens"
    message, tissue_list = get_gene_data(temp_gene_name)
    print(message)
    print_output(host_name, temp_gene_name, tissue_list)


def get_cli_args():
    """Using command line when two argument are added"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-host', dest='HOST',
                        help='Please specify species name', required=False)
    parser.add_argument('-gene', dest='GENE',
                        help='Please specify gene name', required=False)
    return parser.parse_args()


def __print_scientific_name():
    """Printing scientific names from file"""
    keyword_dict = config.get_host_keywords()
    scientific_name = keyword_dict.values()
    print(f"\nHere is a (non-case sensitive) list of available Hosts by "
          f"scientific name\n")
    list_scietific = tuple(enumerate(set(scientific_name), 1))
    for index, name in list_scietific:
        print("{:>2}. {}".format(index, name.capitalize()))


def __print_common_name():
    """Print common names from the file"""
    keyword_dict = config.get_host_keywords()
    common_name = keyword_dict.keys()
    print(f"\nHere is a (non-case sensitive) list of available Hosts "
          f"by common name\n")
    list_common = tuple(enumerate(sorted(set(common_name)), 1))
    for index, name in list_common:
        print("{:>2}. {}".format(index, name.capitalize()))


def __print_host_directories():
    """Print the host directories"""
    print(f"\nEither the Host Name you are searching for is not in the "
          f"database or If you are trying to use the scientific name"
          f"please put the name in double quotes: ''Scientific name''\n")
    __print_scientific_name()
    __print_common_name()


def modify_host_name(temp_host_name):
    """Change common name to scientific name"""
    keyword_dict = config.get_host_keywords()
    if temp_host_name is None:
        temp_host_name = "Homo_sapiens"
    else:
        temp_host_name = temp_host_name.lower()
    if temp_host_name in keyword_dict.keys():
        return keyword_dict.get(temp_host_name)
    __print_host_directories()
    sys.exit()


def get_gene_data(gene_name):
    """
    extract expressed tissues list given by the gene name
    """
    argvs = get_cli_args()
    temp_host_name = argvs.HOST
    temp_gene_name = argvs.GENE
    if temp_host_name is None:
        host_name = "Homo_sapiens"
        gene_name = "TGM1"
    else:
        host_name = modify_host_name(temp_host_name)
        gene_name = temp_gene_name
    file = "/".join((config.get_unigene_directory(),
                     host_name,
                     gene_name + "." + config.get_uigene_extension()))
    if my_io.is_valid_gene_file_name(file):
        # using f-strings
        message = f"\nFound Gene {gene_name} for {host_name}"
    else:
        print(f"Not found\n\
              Gene {gene_name} does not exist for "
              f"{host_name}. exiting now...")
        sys.exit()
    fh_in = my_io.get_fh(file, "r")
    for line in fh_in:
        match = re.search(r'^EXPRESS\s+(\D+)', line)
        if match:
            tissue_string = match.group(1)
            temp_tissue_list = list(tissue_string.split(sep='|'))
            tissue_list = sorted([tissue.strip()
                                  for tissue in temp_tissue_list])
            return message, tissue_list
    return None


def print_output(host_name="Homo_sapiens", gene_name="TGM1",
                 tissue_list=get_gene_data("TGM1")):
    """
    Print expressed tissues with index by default values
    """
    tissues_number = len(tissue_list)
    print(f"In {host_name}, There are {tissues_number} tissues "
          f"that {gene_name} is expressed in:\n")
    for index, tissue in sorted(enumerate(tissue_list, 1)):
        print(f"{index:>2}. {tissue.capitalize()} ")


if __name__ == '__main__':
    main()
