#!/usr/bin/python3

"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns the list of available attributes"""
    return dir(obj)
