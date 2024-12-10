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
