import numpy as np
from matplotlib.path import Path
from matplotlib.textpath import TextToPath
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname=r"fa-solid-900.ttf")

icons = {'cat': '\uf6be', 'crow': '\uf520', 'dog': '\uf6d3',
         'fish': '\uf578', 'horse': '\uf6f0', 'house': '\uf015',
         'leaf': '\uf18c', 'person': '\uf554', 'spider': '\uf717',
         'tent': '\uf6bb', 'tree': '\uf1bb'}

def get_icon(icon):
    v, codes = TextToPath().get_text_path(fp, icons[icon])
    v = np.array(v)
    mean = np.mean([np.max(v, axis=0), np.min(v, axis=0)], axis=0)

    return Path(v-mean, codes, closed=False)