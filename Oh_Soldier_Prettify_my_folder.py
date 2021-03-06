"""
Exercise - Oh Soldier Prettify my folder
1. Write a function which take path and format as an input.
2. Capitalize name of all files available in given path except the selected format.
3. Rename all the files with 1,2,3...if it matches the given format.
"""
import os
def pretttify_soldier(path, format):
    os.chdir(path)
    file_list = os.listdir(os.getcwd())
    specific_ext_count = 1
    for f in file_list:
        if not f.endswith(format):
            os.renames(f, f.capitalize())
        if f.endswith(format):
            os.renames(f, f"{specific_ext_count}_{f}")
            specific_ext_count = specific_ext_count+1
            
            
print("Welcome to Prettifier Army, Soldier waiting for your command.")
path_input = input("Enter the path where you want to execute this program.\n:")
format_input = input("Enter the extension of files, for which you want to do numbering instead of capitalization.\n:")
pretttify_soldier(path_input, format_input)
