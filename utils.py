import os
import pickle


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def get_tuned_model(model_name):
    with open(f"./tuned_models/{model_name}.pkl", "rb") as file:
        model = pickle.load(file)

    return model
