import os

os.system('pip install gpt_2_simple')
import gpt_2_simple as gpt2
model_name='124M'
gpt2.download_gpt2(model_name=model_name)

