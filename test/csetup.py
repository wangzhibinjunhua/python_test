import os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = "E:/Anaconda3/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "E:/Anaconda3/tcl/tk8.6"
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('num/test.py', base=base, targetName = 'aa')
]

setup(name='w',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
