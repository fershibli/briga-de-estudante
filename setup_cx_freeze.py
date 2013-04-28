from cx_Freeze import setup, Executable
import sys

sys.argv.append("build")  # replaces commandline arg 'build'

# change the filename to your program file
filename = "briga_de_estudante_v3.py"

setup(
    name = "Briga de Estudante",
    version = "3.0",
    description = "console cx_Freeze script",
    executables = [Executable(filename)])
