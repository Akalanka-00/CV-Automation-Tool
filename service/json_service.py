import json
import os


def create_json_files():
    json_files = [
        "configure.json",
        "companies.json",
        "cover_letters.json",
        "default_cover_letter.json",
    ]


    with open("./data/" + json_files[0], "w") as file:
        json.dump({}, file, indent=4)

    with open("./data/"+json_files[1], "w") as file:
        json.dump([], file, indent=4)

    with open("./data/"+json_files[2], "w") as file:
        json.dump([], file, indent=4)

    with open("./data/" + json_files[3], "w") as file:
        json.dump({}, file, indent=4)


def store_data_in_json(file_name, data, append=False):
    file_path = f"./data/{file_name}"
    if append and os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                existing_data = json.load(file)
                if isinstance(existing_data, list):
                    existing_data.append(data)
                elif isinstance(existing_data, dict) and isinstance(data, dict):
                    existing_data.update(data)
                else:
                    print("❌ Incompatible types for appending.")
                    return
            except json.JSONDecodeError:
                existing_data = [data]
    else:
        existing_data = data

    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)


def read_json_file(file_name):
    file_path = f"./data/{file_name}"
    if not os.path.exists(file_path):
        print(f"❌ File '{file_path}' not found.")
        return None

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print(f"❌ File '{file_path}' contains invalid JSON.")
        return None