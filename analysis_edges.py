
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import sobel
from common import load_images, RESULT_DIR, GRAPH_DIR

images = load_images()
rows = []

for i, img in enumerate(images[1:], start=1):
    gray = rgb2gray(np.array(img))
    edges = sobel(gray)
    density = (edges > 0.05).mean()
    rows.append({
        "iteration": i,
        "edge_density": density
    })

df = pd.DataFrame(rows)
df.to_csv(f"{RESULT_DIR}/edges.csv", index=False)

plt.plot(df["iteration"], df["edge_density"])
plt.savefig(f"{GRAPH_DIR}/edges.png")
plt.close()
