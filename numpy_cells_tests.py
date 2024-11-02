# %% 
import numpy as np
from PIL import Image


# %% crear matriz aleatoria
image_ruido = np.random.randn(20, 20, 3)
image_ruido

# %% Normalizar
# f(x) = (x - Xmin) / (Xmax - Xmin)
def normalization(X:np.ndarray) -> np.ndarray:
    '''
    
    
    
    
    
    
    '''
    upper = X - X.min()
    down = X.max() - X.min()

    return upper / down


def norm255(X):
    normalized = normalization(X)
    return (normalized * 255).astype(np.uint8)


check = lambda x: print(f"minimo: {x.min()}, maximo: {x.max()}")

# %%
check(image_ruido)
#
norm_img = normalization(image_ruido)
check(norm_img)

#255
image_int = norm255(image_ruido)
check(image_int)
# %%
Image.fromarray(image_int[...,0])



if __name__ == "__main__":
    pass