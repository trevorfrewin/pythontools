import base64
import datetime
import json
import os
import sys

def file_to_json(input_path, output_path):
    try:
        with open(input_path, 'rb') as input_file:
            file_content = input_file.read()

            base64_content = base64.b64encode(file_content).decode('utf-8')

            fileModifiedDate =  datetime.datetime.fromtimestamp(os.path.getmtime(input_path), datetime.UTC).isoformat()
            json_object = {'file': input_path, 'fileModifiedDate': fileModifiedDate, 'serialiseDate': datetime.datetime.now(datetime.UTC).isoformat(), 'content': base64_content}

            with open(output_path, 'w', encoding='utf-8') as output_file:
                json.dump(json_object, output_file, ensure_ascii=False, indent=4)

            return
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python serialise.py <input filename> <output filename>")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Convert file to JSON
    result = file_to_json(input_path, output_path)

    if result:
        # Print the JSON object
        print(json.dumps(result, indent=2))
        # You can save the JSON object to a file if needed
        # with open('output.json', 'w') as output_file:
        #     json.dump(result, output_file, indent=2)

if __name__ == "__main__":
    main()