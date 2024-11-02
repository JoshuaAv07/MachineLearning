# %%
import numpy as np
from PIL import Image


#
#
def normalization(X:np.ndarray) -> np.ndarray:


    '''
        Args:

        Returns:   
    
    '''
    upper = X - X.min()
    down = X.max() - X.min()

    return upper / down


def norm255(X):
    normalized = normalization(X)
    return (normalized * 255).astype(np.uint8)


def spot_differences(X1, X2, thereshold=0.1): 
    diff = np.abs(X1 - X2)
    mask = diff > thereshold

    diff[mask] = 0
    return norm255(diff)

check = lambda x: print(f"minimo: {x.min()}, maximo: {x.max()}, dtype: {x.dty}")

# %%
image_basepath = "./images/movement/"
images_names = ["original.jpg", "mov1.jpg", "mov2.jpg", "mov3.jpg"]

images = []

for path in images_names:
    name = image_basepath + path

    img = np.array(Image.open(name))
    images.append(img)

original = images.pop(0)

original
# %%
print("")
for index, img in enumerate(images):
    img_ = normalization(img)
    images[index] = img_

original = normalization(original)
check(original)