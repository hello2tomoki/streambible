import subprocess
# python -m textblob.download_corpora
cmd = ['python3','-m','textblob.download_corpora']
subprocess.run(cmd)
print("Working - textblob.download_corpora")


### python -c "import nltk; nltk.download('punkt')" 
cmd2 = ['python','-c',"import nltk; nltk.download('punkt')"]
subprocess.run(cmd2)
print("Working - nltk")


### python -m textblob.download_corpora;2D
cmd3 = ['python','-m','textblob.download_corpora']
subprocess.run(cmd3)
print("Working - textblob")

