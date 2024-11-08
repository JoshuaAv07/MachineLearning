#%% Importamos las librerías necesarias
import numpy as np
from PIL import Image
import os


# %% functions
def load_category(cat:str, base_path:str):
    x_ = []
    labels = []
    path = os.path.join(base_path, cat)
        
    # Cargamos todas las imagenes
    for img_name in os.listdir(path):
        img_path = os.path.join(path, img_name)
        
        try:
            # Cargamos y reducimos tamaño
            img = Image.open(img_path).convert("RGB")
            img = img.resize((64, 64))
            # Pasamos a numpy y añadimos a lista y su categoria
            x_.append(np.array(img))
            
            if cat == "cat":
                labels.append(1)
            else:
                labels.append(0)
            
        except Exception as e:
            print(f"[Error] Falló la carga. {e} ")
        
    return np.array(x_) / 255, np.array(labels)


def load_set(base_path:str):
    # Cargamos las imagenes.
    X_ = []; Y_ = []
    for cat in ["cat", "rabbit"]:
        x, y_ = load_category(cat, base_path)
        X_.append(x); Y_.append(y_)
        
    X_ = np.vstack([X_[0], X_[1]])
    Y_ = np.hstack([Y_[0], Y_[1]])
    
    return X_, Y_


# %% Tests
if __name__ == "__main__":
    X, y = load_set("./datasets/cat-bunny/train-cat-rabbit/")
    print("Train")
    print(X.shape)
    print(y.shape)

    X, y = load_set("./datasets/cat-bunny/val-cat-rabbit/")
    print("Validación")
    print(X.shape)
    print(y.shape)

    X, y = load_set("./datasets/cat-bunny/test-images/")
    print("Test")
    print(X.shape)
    print(y.shape)




