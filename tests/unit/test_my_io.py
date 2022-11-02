#!/usr/bin/env python3
# test_my_io.py


"""Test suite for module my_io.py"""
import os
import pytest
from assignment5 import my_io


FILE_2_TEST = "test.txt"


def _create_test_file(file):
    '''Create File'''
    open(file, "w").close()


def test_is_valid_gene_file_name():
    '''Test if gene file name valid'''
    _create_test_file(FILE_2_TEST)
    assert my_io.is_valid_gene_file_name(FILE_2_TEST) is True, "Not valid"
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_reading():
    '''Read the file handle'''
    _create_test_file(FILE_2_TEST)
    test = my_io.get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_writing():
    '''Write the file hand'''
    test = my_io.get_fh(FILE_2_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_2_TEST)


def test_get_fh_4_valueerror():
    '''Test ValueError'''
    _create_test_file(FILE_2_TEST)
    with pytest.raises(ValueError):
        my_io.get_fh("test.txt", "rrr")
        os.remove(FILE_2_TEST)


def test_get_fh_4_typeerror():
    '''Test TypeError'''
    _create_test_file(FILE_2_TEST)
    with pytest.raises(TypeError):
        my_io.get_fh([], "r")
    os.remove(FILE_2_TEST)


def test_get_fh_4_oserror():
    '''Test OSErorr'''
    _create_test_file(FILE_2_TEST)
    with pytest.raises(OSError):
        my_io.get_fh("does_not_exist.txt", "r")
    os.remove(FILE_2_TEST)
