#!/usr/bin/env python3
# test_config.py


"""Test suite for module config.py"""


from assignment5 import config


def test_get_error_string_4_unable_to_open(capfd):
    """Testing error to oepn"""
    config.get_error_string_4_unable_to_open("test.txt", "r")
    out, err = capfd.readouterr()
    assert out, err == "Could not open the file: test.txt for type 'r'\n"


def test_get_error_string_4_valueerror(capfd):
    """Testing Value Error"""
    config.get_error_string_4_valueerror()
    out, err = capfd.readouterr()
    assert out, err == "Invalid argument Value for opening a file\n"


def test_get_error_string_4_typeerror(capfd):
    """Testing TypeError"""
    config.get_error_string_4_typeerror()
    out, err = capfd.readouterr()
    assert out, err == "Invalid argument Type\n"


def test_get_file_keywords():
    """Geting key file words"""
    test = config.get_host_keywords()
    assert test.get("bos taurus") == "Bos_taurus"
    assert test.get("rats") == "Rattus_norvegicus"
    assert len(test.keys()) == 18
