from huggingface_hub import hf_hub_download


REPO_ID = "h94/IP-Adapter"
FILE_NAME = "svd_xt-fp16.safetensors"
FILE_NAME = None
DEST_DIR = "/mnt/hdd0/prj/stable_diffusion/data/models/Stable-diffusion/"
DEST_DIR = "./test_hf"

hf_hub_download(repo_id=REPO_ID, filename=FILE_NAME, local_dir=DEST_DIR, local_dir_use_symlinks="False")


output_text = f"""
Done!
----------- INFO -----------
REPO_ID: {REPO_ID}
FILE_NAME: {FILE_NAME}
DEST_DIR: {DEST_DIR}
-------------------------
"""
print(output_text)
