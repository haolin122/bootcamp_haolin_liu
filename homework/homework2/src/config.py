import os
from dotenv import load_dotenv

def load_env():
    """
    加载 .env 文件中的环境变量。
    """
    # load_dotenv 会自动寻找 .env 文件并加载
    load_dotenv()
    print("Environment variables from .env file loaded.")

def get_key(key_name="API_KEY"):
    """
    从环境变量中获取指定的 key。
    返回 key 的值，如果不存在则返回 None。
    """
    return os.getenv(key_name)