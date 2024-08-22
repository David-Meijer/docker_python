import sys
import pandas as pd

passed_arguments = sys.argv #all command line arguments passed into the script

print(f"program name {sys.argv[0]} ran with argument(s): {'none passed' if not passed_arguments[1:] else passed_arguments[1:]}")