import os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = "E:/Anaconda3/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "E:/Anaconda3/tcl/tk8.6"
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [],
                    include_files=["E:/Anaconda3/DLLs/tk86t.dll","E:/Anaconda3/DLLs/tcl86t.dll"],
                    )

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('num/test.py', base=base)
]

setup(name='wzb',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
