import gpt_2_simple as gpt2
import time 

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gen = gpt2.generate(sess, nsamples=100, batch_size=20, length=20, return_as_list=True)

txt = "GENERATED SAMPLES BY SKYMOCHA\n\n"

for x in gen:
    txt += x + '\n\n'

output = open(f"out_{time.time()}.txt","w") 
output.write(txt) 
output.close()