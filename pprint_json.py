import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(json_file_content):
    return json.dumps(json_file_content, indent=3, ensure_ascii=False)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        print(pretty_print_json(load_data(file_path)))
    except FileNotFoundError:
        print('No file')
    except json.decoder.JSONDecodeError:
        print('Troubles with content of json file')
    except IndexError:
        print('You did not write the name of file')
