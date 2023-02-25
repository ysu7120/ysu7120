# from insta.metadata import EXT_PATH
import os
import numpy as np
from datetime import datetime

def datetime_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def backup_numpy(article_ids, save_path):
    os.mkdir(save_path)
    # 혹시나 발생할 오류 등을 위하여 article_ids 변수를 numpy의 save 기능으로 백업
    article_ids_numpy = np.array(article_ids)
    np.save(f'{save_path}{len(article_ids)} insta_article_ids.npy', article_ids_numpy)
