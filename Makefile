create_env:
	conda env create -f environment.yaml

remove-env:
	conda remove --name TST-micro-presentation --all --yes
