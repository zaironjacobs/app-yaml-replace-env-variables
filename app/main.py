import os

if __name__ == "__main__":

    files = os.listdir('/github/workspace/')
    for f in files:
        print(f)

    print('##########')

    yaml_file_path = os.environ.get("app_yaml_path")
    print(yaml_file_path)

    """
    yaml_file = open(os.environ.get("app_yaml_path"), "r")
    print(yaml_file.read())
    """
