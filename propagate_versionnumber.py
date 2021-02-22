"""
   propagate_versionumber.py

   Inject musamusa.aboutproject.__version__ in various files

   ____________________________________________________________________________

   pyproject_toml() : Update the version number in the `pyproject.toml file.
"""
import os
import os.path
import re

from musamusa.aboutproject import __version__


def pyproject_toml():
    """
        pyproject_toml()

        Update the version number in the `pyproject.toml file.

        Inject musamusa.aboutproject::__version__ into the
        `pyproject.toml` file at line :
            version = "..."
    """
    target_filename = "pyproject.toml"

    print(f"* about to update '{target_filename}'...")

    # regex describing the line to be modified:
    regex = '(?P<versionline>^version = "(?P<versionname>.*)")'

    def repl(matchobject):
        """
            repl() sub-function

            Modify the version number in a line defined by regex
        """
        line = matchobject.group("versionline")
        return line[:matchobject.start("versionname")] + \
            __version__ + \
            line[matchobject.end("versionname"):]

    if not os.path.exists(target_filename):
        print("Error : missing pyproject.toml file.")
        return

    # ---- read current file --------------------------------------------------
    new_lines = []  # new lines of the future pyproject.toml file
    with open(target_filename, "r") as current_pyproject_toml:
        for _line in current_pyproject_toml:
            line = _line.strip()

            res = re.search(regex, line)
            if res:
                new_line = re.sub(regex, repl, line)
                new_lines.append(new_line)
                print(f"  > in '{target_filename}', version number is now defined by '{new_line}'.")
            else:
                new_lines.append(line)

    # ---- remove current file ------------------------------------------------
    os.remove(target_filename)

    # ---- write new file -----------------------------------------------------
    with open(target_filename, "w") as new_pyproject_toml:
        for line in new_lines:
            new_pyproject_toml.write(line+"\n")


if __name__ == "__main__":
    pyproject_toml()
