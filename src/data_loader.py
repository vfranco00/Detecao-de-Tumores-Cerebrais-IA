import os
import numpy as np
from PIL import Image
from src import config
import time

def load_images_from_folder(directory, img_size=config.IMG_SIZE):
    class_names = sorted(
        d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))
    )
    X, y = [], []

    for label_idx, class_name in enumerate(class_names):
        class_dir = os.path.join(directory, class_name)
        arquivos = sorted(os.listdir(class_dir))
        print(f"Carregando '{class_name}' ({len(arquivos)} imagens)...")
        inicio_classe = time.time()

        for i, fname in enumerate(arquivos):
            fpath = os.path.join(class_dir, fname)
            try:
                with Image.open(fpath) as img:
                    img = img.convert("L")
                    img = img.resize((img_size, img_size))
                    vetor = np.asarray(img, dtype=np.float32).flatten() / 255.0
                X.append(vetor)
                y.append(label_idx)
            except Exception as e:
                print(f"  Aviso: nao consegui ler {fpath} ({e})")

            if (i + 1) % 200 == 0:
                print(f"  ... {i+1}/{len(arquivos)} ({time.time()-inicio_classe:.1f}s decorridos)")

        print(f"  '{class_name}' concluida em {time.time()-inicio_classe:.1f}s")

    return np.array(X), np.array(y), class_names