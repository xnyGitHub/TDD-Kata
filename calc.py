"""TDD-Kata Exercise"""
# pylint: disable=anomalous-backslash-in-string
import re


def add(numbers: str) -> int:
    """Function that adds numbers given in a single string seperated by commas or delimiters"""
    if numbers == "":  # If string is empty return 0
        return 0

    # Split delimiters
    split_delim = re.split(";|,|\*|\n|%", numbers)

    # Check for negative numbers
    negative_numbers = [x for x in split_delim if x.startswith("-") and x[1:].isdigit()]

    # Check if a result was given
    if negative_numbers:
        # Return no negatives allowed
        return "Negatives are not allowed {}".format(negative_numbers)

    # Sum up the result given from list comp
    result = sum([int(x) for x in split_delim if x.isdigit() and int(x) < 1000])
    return result
