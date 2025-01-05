""" 
"""

from pathlib import Path
import json
import pandas as pd


def store_dtypes_as_csv(
    df: pd.DataFrame,
    full_path: str | None = None,
    directory_path: str | Path = "",
    file_name: str | Path | None = None,
    create_path: bool = False,
    print_success: bool = True,
) -> None:
    """
    Retrieves all data types from a DataFrame, and stores them in a CSV file. The CSV file will have two columns: 'column_name' and 'dtype'.

    Args:
        df (pd.DataFrame): The DataFrame to store the dtypes of.
        full_path (str | None, optional): A complete path to store the JSON to. Used instead of both 'directory_path' and 'file_name', and overrides them if provided. Defaults to None.
        directory_path (str | Path, optional): Path to the directory to store the JSON to. Must be provided alongside 'file_name'. Defaults to '', which results storing to current working directory.
        file_name (str | None, optional): File name. Must be provided alongside 'directory_path'. Defaults to None. Cannot be empty string if not using 'full_path'.
        create_path (bool, optional): Creates the specified directories if they currently do not exists. Defaults to False.
        print_success (bool, optional): Print a success message. Defaults to True.

    Raises:
        ValueError: Either 'full_path', or both 'directory_path' and 'file_name', must be provided.
        FileNotFoundError: Directory does not exist and function argument 'create_path' is set to False (i.e. no path will be created).
    """
    # Check that either full_path, or directory_path and file_name, are provided:
    if not full_path and (not directory_path or not file_name):
        raise ValueError(
            "Either 'full_path', or 'directory_path' and 'file_name', must be provided."
        )

    # Create a full path if full_path is provided, otherwise use directory_path and file_name:
    if full_path:
        path = Path(full_path)
    else:
        # Must provide a file name if not using full_path:
        if not file_name:
            raise ValueError("File name cannot be empty.")
        if isinstance(file_name, str):
            file_name = file_name if file_name.endswith(".csv") else file_name + ".csv"
        elif isinstance(file_name, Path):
            file_name = (
                file_name
                if file_name.suffix == ".csv"
                else file_name.with_suffix(".csv")
            )

        # Ensure directory_path is not None
        directory_path = directory_path or ""
        # Create a full path using directory_path and file_name:
        path = Path(directory_path) / file_name

    # Check that the parent directory exists, and create it if it doesn't:
    parent = path.parent
    if not parent.exists() and create_path:
        parent.mkdir(parents=True)
    elif not parent.exists():
        raise FileNotFoundError(f"Directory '{str(parent.resolve())}' does not exist.")

    # Create a df of all dtypes:
    dtype_df = df.dtypes.to_frame("dtype").reset_index()  # Make a df of all dtypes

    # Store dtype df as CSV:
    dtype_df.to_csv(path, index=False)

    # Print success message:
    if print_success:
        print(f"File '{file_name}' saved to path '{str(path.resolve())}'.")



def store_dtypes_as_json(
    df: pd.DataFrame,
    full_path: str | None = None,
    directory_path: str | Path = "",
    file_name: str | Path | None = None,
    create_path: bool = False,
    print_success: bool = True,
) -> None:
    """
    Retrieves all data types from a DataFrame, and stores them in a CSV file. The CSV file will have two columns: 'column_name' and 'dtype'.

    Args:
        df (pd.DataFrame): The DataFrame to store the dtypes of.
        full_path (str | None, optional): A complete path to store the JSON to. Used instead of both 'directory_path' and 'file_name', and overrides them if provided. Defaults to None.
        directory_path (str | Path, optional): Path to the directory to store the JSON to. Must be provided alongside 'file_name'. Defaults to '', which results storing to current working directory.
        file_name (str | None, optional): File name. Must be provided alongside 'directory_path'. Defaults to None. Cannot be empty string if not using 'full_path'.
        create_path (bool, optional): Creates the specified directories if they currently do not exists. Defaults to False.
        print_success (bool, optional): Print a success message. Defaults to True.

    Raises:
        ValueError: Either 'full_path', or both 'directory_path' and 'file_name', must be provided.
        FileNotFoundError: Directory does not exist and function argument 'create_path' is set to False (i.e. no path will be created).
    """
    # Check that either full_path, or directory_path and file_name, are provided:
    if not full_path and (not directory_path or not file_name):
        raise ValueError(
            "Either 'full_path', or 'directory_path' and 'file_name', must be provided."
        )

    # Create a full path if full_path is provided, otherwise use directory_path and file_name:
    if full_path:
        path = Path(full_path)
    else:
        # Must provide a file name if not using full_path:
        if not file_name:
            raise ValueError("File name cannot be empty.")
        if isinstance(file_name, str):
            file_name = file_name if file_name.endswith(".csv") else file_name + ".csv"
        elif isinstance(file_name, Path):
            file_name = (
                file_name
                if file_name.suffix == ".csv"
                else file_name.with_suffix(".csv")
            )

        # Ensure directory_path is not None
        directory_path = directory_path or ""
        # Create a full path using directory_path and file_name:
        path = Path(directory_path) / file_name

    # Check that the parent directory exists, and create it if it doesn't:
    parent = path.parent
    if not parent.exists() and create_path:
        parent.mkdir(parents=True)
    elif not parent.exists():
        raise FileNotFoundError(f"Directory '{str(parent.resolve())}' does not exist.")

    # Create a df of all dtypes:
    dtype_df = df.dtypes.to_frame("dtype").reset_index()  # Make a df of all dtypes
    # Create a dict of the df, with column names as keys and dtypes as values:
    dtype_dict = dtype_df.set_index("index")["dtype"].astype(str).to_dict()

    # Store dtype dict as JSON:
    with open(path, "w") as file:
        file.write(json.dumps(dtype_dict, indent=4))

    if print_success:
        print(f"File '{file_name}' saved to path '{str(path.resolve())}'.")



def set_column_order(df:pd.DataFrame, column_to_move:str, after_column:str) -> pd.DataFrame:
    """
    Reorder the columns in a data frame to have a specified column after another specified column.

    Args:
        df (pd.DataFrame): Data frame to reorder columns in.
        column_to_move (str): The name of the column to move.
        after_column (str): The name of the column to insert the moved column after.

    Raises:
        ValueError: If specified column to move is not in the data frame.
        ValueError: If specified column to insert column after is not in the data frame.

    Returns:
        pd.DataFrame: Original data frame with the columns in the new order.
    """
    
    if column_to_move not in df.columns:
        raise ValueError(f"Column '{column_to_move}' not in DataFrame.")
    if after_column not in df.columns:
        raise ValueError(f"Column '{after_column}' not in DataFrame.")

    columns = list(df.columns)
    columns.remove(column_to_move)
    after_column_index = columns.index(after_column)
    columns.insert(after_column_index + 1, column_to_move)
    
    return df[columns]
