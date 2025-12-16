
import pandas as pd
import matplotlib.pyplot as plt
from common import RESULT_DIR, GRAPH_DIR

df = pd.read_csv(f"{RESULT_DIR}/ssim.csv")
df["ssci"] = df["ssim_to_previous"] / df["ssim_to_original"]
df.to_csv(f"{RESULT_DIR}/ssci.csv", index=False)

plt.plot(df["iteration"], df["ssci"])
plt.savefig(f"{GRAPH_DIR}/ssci.png")
plt.close()
