import os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = "D:/python3.5/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "D:/python3.5/tcl/tk8.6"
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [],
                    include_files=["D:/python3.5/DLLs/tk86t.dll","D:/python3.5/DLLs/tcl86t.dll"],
                    )

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('gui.py', base=base)
]

setup(name='wzb',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
