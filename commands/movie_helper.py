from sklearn.feature_extraction.text import TfidfVectorizer
import sys
# from model import SimpleNeuralNetwork
from pickle import load, dump
import torch
import numpy as np
import os
from commands.model import SimpleNeuralNetwork
global device 
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

vector_file = open("./assets/training_vector_file","rb")
model_file = open("./assets/trained_model_output","rb")
sys.path.append('./model.py')

classes_file = open("./assets/pickled_genres","rb")
classes:list = sorted(list(load(classes_file)))

vector = load(vector_file)
model = SimpleNeuralNetwork(28659, 3500, len(classes))
model.load_state_dict(torch.load(model_file,map_location=torch.device(device)))


def convert_to_tensor(sparse_csr_matrix):
    sparse_coo = sparse_csr_matrix.tocoo().astype(np.float32)
    indices = torch.from_numpy(np.vstack((sparse_coo.row, sparse_coo.col))).long().to(device=device)
    values = torch.from_numpy(sparse_coo.data).to(device=device)
    shape = torch.Size(sparse_coo.shape)
    return torch.sparse_coo_tensor(indices, values, shape, device=torch.device(device))

def string_to_vector(input_text:str):
    np_arr = vector.transform([input_text])
    return convert_to_tensor(np_arr)

def determine_genres(prediction:torch.Tensor ):
    result = []
    debug = []
    for i in range(len(classes)):
        if prediction[i].item() > .5:
            result.append(classes[i])
        debug.append(prediction[i].item())
    return result

def run_model(input_text:str):
    in_tensor = string_to_vector(input_text)
    out_tensor = model(in_tensor)
    print(input_text,": ",determine_genres(out_tensor[0]))
    return determine_genres(out_tensor[0])

if __name__ == "__main__":
    run_model("A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.")