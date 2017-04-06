from glob import glob
import os.path, time
import json
from ftplib import *

tmp = glob('*.mp3')
arquivos = sorted(tmp, reverse=True)

print(arquivos[0:30])
