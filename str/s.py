
import re



def extract_chinese(text):
    """提取文本中的中文字符"""
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    return ''.join(pattern.findall(text))



if __name__ == '__main__':
    a  = extract_chinese('hello, 你好，世界！')  # 你好世界
    print(a)