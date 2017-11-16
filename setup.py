#!/usr/bin/env python
"""
setup.py file for SWIG example
"""
import sys

from setuptools import setup, Extension

if sys.platform.startswith("darwin"):
    libs = ['-liconv']
else:
    # need iconv too but without proper -L adding -liconv here won't always work
    libs = []

simstring_module = Extension(
    '_simstring',
    sources = [
        'export.cpp',
        'export_wrap.cpp',
    ],
    extra_link_args=libs,
    language='c++',
    )

setup(
    name = 'blink-simstring',
    version = '1.1.2',
    author = 'Naoaki Okazaki',
    description = """SimString Python module""",
    ext_modules = [simstring_module],
    py_modules = ["simstring"],
)
