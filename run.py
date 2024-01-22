import os

os.makedirs("log", exist_ok=True)

node_size = 10

os.environ["SKELETON_POSTERIOR_PATH"] = f"/root/causica/skl_posterior/test-n-admg_o1.txt"
# command = f"python -u -m causica.run_experiment test-n-admg --model_type bowfree_ddeci_gaussian --model_config configs/ddeci/bowfree_ddeci_gaussian.json -dc configs/dataset_config_latent_confounded_causal_dataset.json -lcc -te > log/out_test_admg.log 2>&1"
# print(command)
# os.system(command)
os.environ["USE_SKELETON_POSTERIOR"] = "True"
command = f"python -u -m causica.run_experiment test-n-admg --model_type bowfree_ddeci_gaussian --model_config configs/ddeci/bowfree_ddeci_gaussian.json -dc configs/dataset_config_latent_confounded_causal_dataset.json -lcc -te > log/out_sp_o1_test_admg.log 2>&1"
print(command)
os.system(command)
# for i in range(10):
    
#     command = f"python -u -m causica.run_experiment {node_size}_{i} --model_type bowfree_ddeci_gaussian --model_config configs/ddeci/bowfree_ddeci_gaussian.json -dc configs/dataset_config_latent_confounded_causal_dataset.json -lcc -te > log/out_sp_{node_size}_{i}.log 2>&1"
#     print(command)
#     os.system(command)
