"""TDD-Kata Exercise"""
# pylint: disable=anomalous-backslash-in-string
import re


def add(numbers: str) -> int:
    """Function that adds numbers given in a single string seperated by commas or delimiters"""
    if numbers == "":  # If string is empty return 0
        return 0

    # Find the delimiter
    if re.match("\/\/\[(.+)\]", numbers):
        delimiter = re.match("\/\/\[(.+)\]", numbers)[1]
        delimiter = re.escape(delimiter)
        numbers = numbers.strip("//[{}]\n".format(delimiter))
    elif numbers[0:2] == "//":
        delimiter = numbers[2]
        numbers = numbers.strip("//{}\n".format(delimiter))
    else:
        delimiter = ","

    numbers = re.split("{}|\n".format(delimiter), numbers)
    # Check for negative numbers
    negative_numbers = [x for x in numbers if x.startswith("-") and x[1:].isdigit()]

    # Check if a result was given
    if negative_numbers:
        # Return no negatives allowed
        raise Exception("Negatives are not allowed {}".format(negative_numbers))

    # Sum up the result given from list comp
    if len(numbers) == 1:
        return sum([int(x) for x in numbers[0] if x.isdigit() and int(x) < 1000])
    return sum([int(x) for x in numbers if x.isdigit() and int(x) < 1000])
