from pathlib import Path


def get_stem_path(stem_dir_name: str) -> str:
    """
    Meant to facilitate sys.path.append() in scripts that are run from within a project
    """
    cwd = Path()
    if stem_dir_name not in cwd.resolve().parts:
        raise ModuleNotFoundError(f"""\
Program is executed from path that do not include the specified stem directory 
(i.e. '{stem_dir_name}' is not included in the working directory path). Run the
program from within a sub-directory of the stem directory.
""")
    path_parts = cwd.resolve().parts
    stem_path = Path(*path_parts[: path_parts.index(stem_dir_name) + 1])

    return str(stem_path)



def check_read_file(file_path) -> None:
    """
    Check if the file exists and can be read.
    """
    try:
        # Try opening the file in append mode (non-destructive test)
        with open(file_path, "a"):
            pass  # Just open and immediately close to check access
    except PermissionError:
        raise PermissionError(
            f"Permission denied: The file '{file_path}' is open in another program."
        )
    except FileNotFoundError:
        raise FileNotFoundError(f"No file with path '{file_path}'.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while checking file access: {e}")



def check_write_file(file_path) -> None:
    """
    Check if the file can be made or be written to if already present.
    """
    try:
        # Try opening the file in append mode (non-destructive test)
        with open(file_path, "a"):
            pass  # Just open and immediately close to check access
    except PermissionError:
        raise PermissionError(
            f"Permission denied: The file '{file_path}' is open in another program."
        )
    except FileNotFoundError:
        pass  # Do nothing if the file is not currently made.
    except Exception as e:
        raise Exception(f"An unexpected error occurred while checking file access: {e}")