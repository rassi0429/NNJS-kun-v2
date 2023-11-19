
import random
import string
import os
import requests

def random_string(length):
    """指定された長さのランダムな文字列を生成する"""
    letters = string.ascii_letters # a-zとA-Zを含む文字列
    return ''.join(random.choice(letters) for i in range(length))


async def downloadImage(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    save_path = os.path.join(os.getcwd(),"images", filename + ".jpg")
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    return save_path