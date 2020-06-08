# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.


__author__ = 'Anubhav Jain, Kiran Mathew'
__email__ = 'ajain@lbl.gov, kmathew@lbl.gov'
__copyright__ = "Copyright 2020, The Materials Project"
__version__ = "0.1"
__date__ = "April 2020"


def load_class(modulepath, classname):
    """
    Load and return the class from the given module.

    Args:
        modulepath (str): dotted path to the module. eg: "pymatgen.io.vasp.sets"
        classname (str): name of the class to be loaded.

    Returns:
        class
    """
    mod = __import__(modulepath, globals(), locals(), [classname], 0)
    return getattr(mod, classname)
