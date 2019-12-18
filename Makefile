install:
	pip install conda
	conda create --prefix ./envs
	conda activate ./envs
	pip install -r requirements.txt
	set FLASK_APP=main.py

activate:
	conda activate ./envs

run: activate
	flask run
	