import os #Operating System
import shutil #copying, moving, and removing files and directories.
from datetime import datetime

#Created this to associate the number of date into month
data_name = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

#THM
#LRV
search_format = 'JPG'
srcdir_path = "/Volumes/Untitled/MP4"

# Function that takes in source directory (Terminal)
def sort_files_by_date(source_dir):
    # If directory DOESN'T exist
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    # If directory DOES exist
    for filename in os.listdir(source_dir):
        # Skip hidden or system files OR if the filename contains XML then IGNORE
        if filename.startswith('.') or filename[len(filename)-3:] == 'XML':
            continue
        if filename[len(filename)-3:] == search_format:
           filepath = os.path.join(source_dir, filename)
        else:
            continue
        
        # Skip if it's a directory
        if os.path.isdir(filepath):
            continue
        
        print("File path: ", filepath)

        # Create the date-named folder if it doesn't exist
        destination_dir = "/Volumes/Untitled/" + search_format
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        # Move the file to the corresponding folder
        shutil.move(filepath, os.path.join(destination_dir, filename))
        print("filename " + filename)
        print("Destination" + destination_dir)

    print(f"Files in {source_dir} have been sorted by date.")

# Calls the method above
source_directory = srcdir_path
sort_files_by_date(source_directory)