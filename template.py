import os
from pathlib import Path


project_name = 'us_visa'

files_list = [
	f"{project_name}/components/__init__.py",
	f"{project_name}/components/data_injestion.py",
	f"{project_name}/components/data_transformation.py",
	f"{project_name}/components/model_evaluation.py",
	f"{project_name}/components/model_trainer.py",
	f"{project_name}/components/model_pusher.py",
	f"{project_name}/configuration/__init__.py",
	f"{project_name}/configuration/s3_operations.py",
	f"{project_name}/constant/__init__.py",
	f"{project_name}/entity/__init__.py",
	f"{project_name}/entity/artifact_entity.py",
	f"{project_name}/entity/config_entity.py",
	f"{project_name}/exception/__init__.py",
	f"{project_name}/logger/__init__.py",
	f"{project_name}/pipeline/__init__.py",
	f"{project_name}/pipeline/training.py",
	f"{project_name}/pipeline/prediction.py",
	f"{project_name}/utils/__init__.py",
	f"{project_name}/utils/main_utils.py",
	"config/model.yaml",
	"config/schema.yaml",
	"app.py",
	"requirements.txt",
	"Dockerfile",
	".dockerignore",
	"demo.py",
	"setup.py"
]

for file_path in files_list:
	file_path = Path(file_path)
	file_dir , file_name = os.path.split(file_path)
	if(file_dir != ''):
		os.makedirs(file_dir,exist_ok=True)
	if((not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0)):
		with open(file_path,'w') as f:
			pass
	else:
		print(f'File already exists at path {file_path}')
