"""NBI SAS Code Conversion.

This module is to generate sas code that is used in a SAS macro. The codes are generate in a if then style..

Example:
    for ICD10code that contains "H33", "H431", "H450", the following will be generated
    if icd3 in ("H33") or icd4 in ("H431", "H450") then flag = 1 else flag = 0
        $ python nbi_sas_code_conversion.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * Enhance code excluding part

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import pandas as pd
import re
import string
import math


def file_importer(df, f, s):
    """function to import primary and foreign excel files
    Arg:
        df: The name of the pandas data frame
        f: The file name of the file that being imported
        s: The sheet name of the excel
    Return
        The corresponding pandas data frame
    """
    df = pd.read_excel(f, index_col=None, sheet_name=s)

def file_cleaning(col):
    return None


file_importer(pri_sas, '7001479 Japan Local Protocol covariates code list formatted for SAS v1.0.xlsx', 'Covariates for PS-match')
file_importer(fore_sas1, 'NBI covariates name .xlsx', 'Diabetes complications')
file_importer(fore_sas2, 'NBI covariates name .xlsx', 'Sheet2')
file_importer(fore_sas3, 'NBI covariates name .xlsx', 'Sheet1')