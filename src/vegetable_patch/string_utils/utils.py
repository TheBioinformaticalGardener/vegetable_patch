import re
from typing import Optional, Iterable


def replace_case_insensitive(input_string:str, search_pattern:str, replacement:str) -> str:
    """
    Replace substring in a case insensitive matter.  
    """
    pattern = re.compile(search_pattern, re.IGNORECASE)
    output_string = pattern.sub(replacement, input_string) 
    return output_string



def dayfirst_to_international_format_date(text:str) -> str:
    """
    Uses RegEx to convert a string representation of a date on the format dd.mm.yyyy to yyyy-mm-dd
    """
    # Match dates in the format 'dd.mm.yyyy'
    date_pattern = r'\b(\d{2})\.(\d{2})\.(\d{4})\b'
    
    # Replace with the desired format 'yyyy-mm-dd'
    def format_date(match) -> str:
        day, month, year = match.groups()
        return f"{year}-{month}-{day}"
    
    return re.sub(date_pattern, format_date, text)




def format_string(string:str, strip:bool=True, sep:str=' ', return_sep:str=' ', case_to:Optional[str]=None, capitalize_substrings:bool=False, ignore_words:Optional[Iterable[str]]=None) -> str:
    """
    Function to format a string according to chosen settings

    Args:
        string (str): The string to be formatted
        strip (bool, optional): Remove all trailing separators and replaces multiple separators in succession with a single one. Defaults to True.
        sep (str, optional): Separator that is in the original string. Defaults to ' '.
        return_sep (str, optional): Separator that is left when string is formatted. Defaults to ' '.
        case_to (Optional[str], optional): Choose; 'lower', 'upper', or 'capitalize'. Defaults to None.
        capitalize_substrings (bool, optional): If case_to='capitalize', capitalize_substring as True will set all substrings to be capitalized as well. Defaults to False.
        ignore_words (Optional[Iterable[str]], optional): List of strings (words) that should be ignored when formatting. Defaults to None.

    Raises:
        ValueError: case_to is not string type (str) or None.
        ValueError: case_to is set to something else than ('upper', 'lower', 'capitalize', None).
        ValueError: capitalize_substrings==True and case_to==False.

    Returns:
        str: Formatted string.
    """
    

    ignore_words_set: set = set() if ignore_words is None else set(ignore_words)

    if not (isinstance(case_to, str) or case_to is None):
        raise ValueError("`case_to` must be of type `str` or `None`.")

    if isinstance(case_to, str):
        case_to = case_to.strip().lower()

    if case_to:
        VALID_CASE = ('upper', 'lower', 'capitalize', None)
        if case_to not in VALID_CASE:
            raise ValueError(f'Case must be set to one of {VALID_CASE}, currently {case_to=}.')
        
        if case_to != 'capitalize' and capitalize_substrings:
            raise ValueError(f"Can only capitalize if case_to='capitalize'. Currently {case_to=}.")

        
    # Do nothing is the string is effectively empty:
    if not string:
        return string

    if sep != return_sep:
        string = string.replace(sep, return_sep)

    # Remove trailing and occurrences of multiple separator characters (e.g. multiple whitespaces):
    if strip:
        string = re.sub(f'{return_sep}+', return_sep, string.strip(return_sep))

    # Split string into substring on the separator:
    # str_list = string.split(sep)
    str_list = string.split(return_sep)

    # TODO Handle upper-case letters that we want to keep (e.g. pH or 3D)
    
    # Handle casing:
    match case_to:
        case None:
            pass
        case 'lower':
            if ignore_words_set:
                str_list = [word.lower() if word not in ignore_words_set else word for word in str_list]
            else:
                str_list = [word.lower() for word in str_list]
        case 'upper':
            if ignore_words_set:
                str_list = [word.upper() if word not in ignore_words_set else word for word in str_list]
            else:
                str_list = [word.upper() for word in str_list]
        case 'capitalize':
            if capitalize_substrings:   # Capitalize all substrings
                if ignore_words_set:
                    str_list = [word.capitalize() if word not in ignore_words_set else word for word in str_list]
                else:
                    str_list = [word.capitalize() for word in str_list]
            else:   # Capitalize only first substring
                if str_list and str_list[0] not in ignore_words_set:  # Also checks the edge case where the str_list is empty
                    str_list[0] = str_list[0].capitalize()

    # Return the formatted string:        
    return return_sep.join(str_list)

