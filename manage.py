#!/usr/bin/env python


def run_tests():
    print("Running Tests")
    return False


def run_analysis():
    print("Analyzing Code")
    return False


if __name__ == "__main__":
    import sys

    keyword_function_pairs = (
        ('test', run_tests),
        ('analysis', run_analysis),
    )

    command = None
    error_message = ""
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        function_list = [func() if command == kw else None for kw, func in keyword_function_pairs]
        if all(func is None for func in function_list):
            error_message = "Invalid argument received"
    else:
        error_message = "No argument specified"

    if error_message:
        parameter_list = [kw for kw, func in keyword_function_pairs]
        print("{}, valid list is: {}".format(error_message, parameter_list))
