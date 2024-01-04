from huggingface_hub import hf_hub_download


REPO_ID = "runwayml/stable-diffusion-v1-5"
FILE_NAME = "v1-5-pruned-emaonly.safetensors"
DEST_DIR = "test_hf"

hf_hub_download(repo_id=REPO_ID, filename=FILE_NAME, local_dir=DEST_DIR)


output_text = f"""
Done!
----------- INFO -----------
REPO_ID: {REPO_ID}
FILE_NAME: {FILE_NAME}
DEST_DIR: {DEST_DIR}
-------------------------
"""
print(output_text)
