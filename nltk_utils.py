import subprocess
cmd = ['python3','-m','pip install textblob']
cmd2 = ['python3','-m','textblob.download_corpora']
subprocess.run(cmd)
subprocess.run(cmd2)
print("Working")


import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('all-corpora')

