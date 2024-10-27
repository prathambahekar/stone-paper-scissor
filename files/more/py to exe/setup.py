import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','files', 'settings.json', "core.py", "README.md"]

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Stone Paper Scissor",
    version = "1.0.0",
    description = "A stone paper scissor made with beautiful python user interface",
    author = "Pratham H Bahekar",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
