#!/usr/bin/env python

def run_tests():
    print("Running Tests")
    return false
    
def run_analysis():
    print("Analyzing Code")
    return false

if __name__ == "__main__":
    import sys

    command = None
    if len(sys.argv) >= 2:
        command = sys.argv[1]
    if 'test' in command:
        run_tests()
    elif 'analysis' in command:
        run_analysis()
    else:
        return
