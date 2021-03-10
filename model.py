# https://www.geeksforgeeks.org/reading-excel-file-using-python/
import gpt_2_simple as gpt2
import os
import requests
import time 

import resource 

def limit_memory(): 
    soft, hard = resource.getrlimit(resource.RLIMIT_AS) 
    resource.setrlimit(resource.RLIMIT_AS, (8 * 1024 / 2, hard)) 

limit_memory()

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/


# file_name = "shakespeare.txt"
# if not os.path.isfile(file_name):
# 	url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
# 	data = requests.get(url)
	
# 	with open(file_name, 'w') as f:
# 		f.write(data.text)
    
file_name = "./animemes_2019_500+.csv"

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=500)   # steps is max number of training steps

gen = gpt2.generate(sess, nsamples=100, batch_size=20, length=20, return_as_list=True)

txt = "GENERATED SAMPLES BY SKYMOCHA\n\n"

for x in gen:
    txt += x + '\n\n'

output = open(f"out_{time.time()}.txt","w") 
output.write(txt) 
output.close()