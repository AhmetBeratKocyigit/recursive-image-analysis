
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from skimage.color import rgb2gray
from common import load_images, RESULT_DIR, GRAPH_DIR

images = load_images()
original = images[0]

def ssim_score(img1, img2):
    img1 = np.array(img1.convert("L"), dtype=np.float32)
    img2 = np.array(img2.convert("L"), dtype=np.float32)

    return ssim(
        img1,
        img2,
        data_range=255  # 🔑 KRİTİK SATIR
    )

rows = []
for i in range(1, len(images)):
    rows.append({
        "iteration": i,
        "ssim_to_original": ssim_score(images[i], original),
        "ssim_to_previous": ssim_score(images[i], images[i-1])
    })

df = pd.DataFrame(rows)
df.to_csv(f"{RESULT_DIR}/ssim.csv", index=False)

plt.plot(df["iteration"], df["ssim_to_original"], label="To Original")
plt.plot(df["iteration"], df["ssim_to_previous"], label="To Previous")
plt.legend()
plt.savefig(f"{GRAPH_DIR}/ssim.png")
plt.close()
