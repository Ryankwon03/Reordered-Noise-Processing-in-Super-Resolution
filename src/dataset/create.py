import os
import numpy as np
from PIL import Image

def create_low_res_npz(input_folder, output_file, labels_mapping=None):
    """
    Creates an .npz file with low-resolution images from input_folder.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_file (str): Path to save the resulting .npz file.
        labels_mapping (list or None): List of labels corresponding to the images in order.
    """
    low_res_images = []
    labels = []

    # Get all image filenames in sorted order to maintain consistency
    image_filenames = sorted(
        [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    )

    # Ensure there are enough labels if a mapping is provided
    if labels_mapping and len(labels_mapping) != len(image_filenames):
        raise ValueError("The number of labels must match the number of images.")

    # Iterate through all image files in the input folder
    for idx, filename in enumerate(image_filenames):
        # Load the image
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            # Convert to RGB (if not already in RGB format)
            img = img.convert("RGB")
            # Convert to NumPy array
            img_array = np.array(img, dtype=np.uint8)
            low_res_images.append(img_array)

            # Add corresponding label if a mapping is provided
            if labels_mapping:
                labels.append(labels_mapping[idx])


    # Convert lists to NumPy arrays
    low_res_images = np.stack(low_res_images, axis=0)
    print(f"Processed {len(low_res_images)} images into low resolution.")

    if labels_mapping:
        labels = np.array(labels, dtype=int)  # Use string dtype for non-numeric labels
        # Save images and labels
        np.savez(output_file, arr_0=low_res_images, arr_1=labels)
        print(f"Saved low-resolution images and labels to {output_file}")
    else:
        # Save only images
        np.savez(output_file, arr_0=low_res_images)
        print(f"Saved low-resolution images to {output_file}")

# Parameters
input_folder = "../../data/original/image1.jpg"  # Path to your image folder
output_file = "../../data/low_res_1.npz"  # Output .npz file
#labels_mapping = ["goldfish", "goat", "cat"]  # Labels in the order of images
labels_mapping = [0, 1, 2]
#{"goldfish": 0, "goat": 1, "cat": 2}

# Run the script
create_low_res_npz(input_folder, output_file, labels_mapping)
