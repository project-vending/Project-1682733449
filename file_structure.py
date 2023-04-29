
import os

# Define the directory structure
dir_structure = {
    "app": {
        "streamlit": {
            "Dockerfile": "",
            "requirements.txt": "",
            "app.py": "",
        },
        "fastapi": {
            "Dockerfile": "",
            "requirements.txt": "",
            "app.py": "",
        },
        "docker-compose.yml": "",
    },
    "aws": {
        "ec2": {
            "Dockerfile": "",
            "requirements.txt": "",
            "app.py": "",
        },
        "lambda": {
            "Dockerfile": "",
            "requirements.txt": "",
            "app.py": "",
        },
    },
    "data": {
        "raw": {},
        "processed": {},
    }
}

# Define a function to create directories and files
def create_dirs_and_files(root_dir, dir_structure):
    for name, contents in dir_structure.items():
        path = os.path.join(root_dir, name)
        os.makedirs(path, exist_ok=True)
        if isinstance(contents, dict):
            create_dirs_and_files(path, contents)
        else:
            with open(path, "w") as f:
                f.write(contents)

# Create the directories and files by calling the function
root_dir = "real-time-data-ingestion"
create_dirs_and_files(root_dir, dir_structure)
