def load_log_file(path):
    try:
        with open(path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Log file not found.")
        return []