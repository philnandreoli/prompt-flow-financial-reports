# Startup script for the flow container

CONDA_ENV_PATH="$(conda info --base)/envs/promptflow-serve"
export PATH="$CONDA_ENV_PATH/bin:$PATH"

ls
ls connections
pf connection create --file /connections/andropenaicgsrch001.yaml
pf connection create --file /connections/andropenaidemo001.yaml
pf flow serve --source flow --host 0.0.0.0
