#!/usr/bin/env python3
# my_io.py


"""
A submodule of getting gene information
"""

import os
from assignment5 import config


def is_valid_gene_file_name(file):
    """Getting the valild gene and file"""
    if os.path.exists(file):
        return True
    return None


def get_fh(file, arg):
    """ Get the filehandle"""
    try:
        fobj = open(file, arg)
        return fobj
    except ValueError as err:
        config.get_error_string_4_valueerror()
        raise err
    except TypeError as err:
        config.get_error_string_4_typeerror()
        raise err
    except OSError as err:
        config.get_error_string_4_unable_to_open(file, arg)
        raise err
