#! python2
# Written by nixawk: https://github.com/chanwit/wannacry_blocker. Packed and adapted by @joseccnet
# Caution: Use at your own risk

# Please consider a donation for maintain this work
# any amount is welcome at this bitcoin address: 
# Bitcoin is not for criminals it is for work of professionals. Thanks.

from distutils.core import setup
import py2exe, sys

sys.argv.append('py2exe')

py2exe_options = dict(
   ascii=False,  # Include encodings
   excludes=['_ssl',  # Exclude _ssl
             'pyreadline', 'difflib', 'doctest', 'locale', 
             'optparse', 'pickle', 'calendar','pdb','unittest','inspect'],  # Exclude standard library
              dll_excludes=['msvcr71.dll','w9xpopen.exe'],  # Exclude msvcr71
              compressed=True,  # Compress library.zip
              bundle_files= 1,
   )

setup(
    name = 'smb_ms17_010_local',
    version = '1.0',
    description="smb_ms17_010 WannaCry WannaCrypt Scanner, Written by nixawk. Packed and adapted by @joseccnet",
    author="Written by nixawk: https://github.com/chanwit/wannacry_blocker. Packed and adapted by @joseccnet",
    options = {'py2exe': py2exe_options},
    windows = [{'script': "smb_ms17_010_local.py"}],
    zipfile = None,
)

