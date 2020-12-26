from typing import List
import json


def get_content():
    """获取colors, 将前半部分获取出来, 并将驼峰命名用空格拆开, 便于翻译"""
    with open(file='themes/monokai without underline-italic-color-theme.json', mode='r', encoding='utf-8') as f:
        content_str = f.read()
    content = json.loads(content_str)
    colors: dict = content['colors']
    for key in colors:
        key: str
        keys = key.split('.')
        if len(keys) == 2:
            aaa = keys[0]
            bbb = keys[1]
            a_str = ''
            for a in aaa:
                if ord(a) >= 65 and ord(a) <= 90:
                    a = ' ' + a
                a_str = a_str + a
            
            b_str = ''
            for b in bbb:
                if ord(b) >= 65 and ord(b) <= 90:
                    b = ' ' + b
                b_str = b_str + b
            print(a_str, b_str)
        else:
            print(key)


def get_tokenColors():
    with open(file='themes/monokai without underline-italic-color-theme.json', mode='r', encoding='utf-8') as f:
        content_str = f.read()
    content = json.loads(content_str)
    tokenColors:List[dict] = content['tokenColors']
    for item in tokenColors:
        if 'name' in item:
            name = item['name']
            print(name)


if __name__ == "__main__":
    # get_content()
    get_tokenColors()
    # 65 90
    # print(ord('Z'))