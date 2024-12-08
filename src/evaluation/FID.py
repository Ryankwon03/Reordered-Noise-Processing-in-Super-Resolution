import torch
from pytorch_fid import fid_score



def main(): 
    original_path = "../../data/for_fid/"
    compare_path = "../../results/for_fid/"


    fid_value = fid_score.calculate_fid_given_paths([original_path, compare_path],
                                                    batch_size=3,
                                                    device='cuda' if torch.cuda.is_available() else 'cpu',
                                                    dims=2048)
    print(f'FID score for images: {fid_value}')\
    #lower the value of FID, the better is the quality of the image. (out of 100)


if __name__ == "__main__": 
    main()