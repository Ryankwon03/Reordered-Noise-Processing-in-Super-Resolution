import numpy as np

data = np.load("../../data/low_res_downsample.npz")
print("Images shape:", data["arr_0"].shape)
if "arr_1" in data:
    print("Labels shape:", data["arr_1"].shape)