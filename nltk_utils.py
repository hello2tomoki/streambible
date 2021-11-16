import subprocess
# python -m textblob.download_corpora
cmd = ['python3','-m','textblob.download_corpora']
subprocess.run(cmd)
print("Working - textblob.download_corpora")