import os

output_dir = "adj_mat"
os.makedirs(output_dir, exist_ok=True)

for sub_dir in os.listdir("runs"):
    # if is dir
    sub_dir_path = os.path.join("runs", sub_dir)
    if os.path.isdir(sub_dir_path):
        models_path = os.path.join(sub_dir_path, "models")
        for model_id in os.listdir(models_path):
            model_path = os.path.join(models_path, model_id)
            if os.path.isdir(model_path):
                directed_adj_mat_path = os.path.join(model_path, "pred_directed_adj.npy")
                bidirected_adj_mat_path = os.path.join(model_path, "pred_bidirected_adj.npy")
                dataset_name_path = os.path.join(model_path, "dataset_name.txt")
                if os.path.exists(directed_adj_mat_path) and os.path.exists(bidirected_adj_mat_path) and os.path.exists(dataset_name_path):
                    with open(dataset_name_path, "r") as f:
                        dataset_name = f.read().strip()
                    directed_output_path = os.path.join(output_dir, f"{dataset_name}_D.npy")
                    bidirected_output_path = os.path.join(output_dir, f"{dataset_name}_B.npy")
                    os.system("cp {} {}".format(directed_adj_mat_path, directed_output_path))
                    os.system("cp {} {}".format(bidirected_adj_mat_path, bidirected_output_path))