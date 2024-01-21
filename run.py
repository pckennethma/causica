import os

os.makedirs("log", exist_ok=True)

node_size = 10

for i in range(10):
    command = f"python -u -m causica.run_experiment {node_size}_{i} --model_type bowfree_ddeci_gaussian --model_config configs/ddeci/bowfree_ddeci_gaussian.json -dc configs/dataset_config_latent_confounded_causal_dataset.json -lcc -te > log/out_{node_size}_{i}.log 2>&1"
    print(command)
    os.system(command)
