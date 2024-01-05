import os
import sys
from email import message_from_file
from email.utils import parsedate_to_datetime
from datetime import datetime

def rename_eml_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".eml"):
            file_path = os.path.join(directory_path, filename)
            try:
                # Parse the date from the email file
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    msg = message_from_file(file)
                    date_str = msg.get("Date")
                    if date_str:
                        date = parsedate_to_datetime(date_str)
                    else:
                        # If Date header is not present, use the file's last modification time
                        date = datetime.fromtimestamp(os.path.getmtime(file_path))
                    
                    # Format the date and time in YYYYMMDD HHmmSS order
                    formatted_date = date.strftime("%Y%m%d %H%M%S")

                    # Construct the new filename
                    new_filename = f"{formatted_date} {filename}"

                    # Rename the file
                    new_file_path = os.path.join(directory_path, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f'Renamed: {filename} to {new_filename}')
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python decorateFilename.py <pathToEMLFiles>")
        return

    directory_path = sys.argv[1]

    # Rename EML files at this path
    rename_eml_files(directory_path)

if __name__ == "__main__":
    main()