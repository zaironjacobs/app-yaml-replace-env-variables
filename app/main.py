import os

if __name__ == "__main__":
    yaml_file_path = os.environ.get("app_yaml_path")
    print(yaml_file_path)
    yaml_file = open(os.environ.get("app_yaml_path"), "r")
    print(yaml_file.read())