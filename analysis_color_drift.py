
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from common import load_images, RESULT_DIR, GRAPH_DIR

images = load_images()
rows = []

for i, img in enumerate(images[1:], start=1):
    arr = np.array(img)
    rows.append({
        "iteration": i,
        "R": arr[:,:,0].mean(),
        "G": arr[:,:,1].mean(),
        "B": arr[:,:,2].mean()
    })

df = pd.DataFrame(rows)
df.to_csv(f"{RESULT_DIR}/color_drift.csv", index=False)

plt.plot(df["iteration"], df["R"], color=(1,0,0), label="Red")
plt.plot(df["iteration"], df["G"], color=(0,1,0), label="Green")
plt.plot(df["iteration"], df["B"], color=(0,0,1), label="Blue")
plt.legend()
plt.savefig(f"{GRAPH_DIR}/color_drift.png")
plt.close()
