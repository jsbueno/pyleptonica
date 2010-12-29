# -*- coding: utf-8 -*-

from distutils.core import setup
import os

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["leptonica/*"]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = "pyleptonica",
    version = "0.2",
    description = "Wrapper and wrapper generators for the 2D Image Leptonica Library",
    author = "João Sebastião de Oliveira Bueno",
    author_email = "jsbueno@python.org.br",
    url = "",
    packages = ["leptonica"],
    package_data = {'leptonica' : files },
    scripts = [],
    long_description = read("README")


    classifiers=[
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Environment :: Other Environment",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    "Topic :: Multimedia :: Graphics",
    "Topic :: Software Development :: Libraries :: Python Modules"
    
    ]
)