import numpy as np

data = np.load("../../data/all_low_res.npz")
print("Images shape:", data["arr_0"].shape)
if "arr_1" in data:
    print("Labels shape:", data["arr_1"].shape)