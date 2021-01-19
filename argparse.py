import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Insert this command summary ')
    # add action to set this arugment default would be False, if use this argument it wout set to True
    parser.add_argument('-o', '--option_argument', help='explain the purpose of this argument', action='store_true')
    # add positional argument, have to insert the value after this argument
    # <type>: means the value type of this argument is string
    parser.add_argument('-p', '--positional_argument', metavar='search target', type=str, nargs='+',help='explain the purpose of this argument')
    args = parser.parse_args()