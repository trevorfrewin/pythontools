import base64
import json
import sys
import uuid

def json_to_file(json_path):
    try:
        with open(json_path, 'r') as json_file:
            json_data = json.load(json_file)

            file_path = json_data.get('file')
            base64_content = json_data.get('content')

            if not file_path or not base64_content:
                print("Error: 'file' or 'content' not found in JSON.")
                return

            content = base64.b64decode(base64_content)

            decorated_file_path = uuid.uuid4().hex + '_' + file_path

            with open(decorated_file_path, 'wb') as output_file:
                output_file.write(content)

            print(f"File '{decorated_file_path}' successfully created.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_filename>")
        return

    json_path = sys.argv[1]

    # Convert JSON to file
    json_to_file(json_path)

if __name__ == "__main__":
    main()
