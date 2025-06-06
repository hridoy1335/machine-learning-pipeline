import os
import logging
from pathlib import Path

project_name = "mlproject"
list_of_file = [
    f"github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"config/config.yml",
    f"params.yml",
    f"schema.yml",
    f"dvc.yml",
    f"Dockerfile",
    f"requirements.txt",
    f"main.py",
    f"app.py",
    f"setup.py",
    ".dockerignore"
]
for file in list_of_file:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
        logging.info(f"{file_name} is empty file.")
        
    else:
        logging.info(f"{file_name} file is already exists.")
        
print("OK")