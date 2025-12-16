
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from common import load_images, RESULT_DIR, GRAPH_DIR

images = load_images()
rows = []

for i, img in enumerate(images[1:], start=1):
    gray = rgb2gray(np.array(img))
    hist, _ = np.histogram(gray, bins=256, density=True)
    hist += 1e-9
    entropy = -np.sum(hist * np.log2(hist))
    rows.append({
        "iteration": i,
        "entropy": entropy
    })

df = pd.DataFrame(rows)
df.to_csv(f"{RESULT_DIR}/entropy.csv", index=False)

plt.plot(df["iteration"], df["entropy"])
plt.savefig(f"{GRAPH_DIR}/entropy.png")
plt.close()
