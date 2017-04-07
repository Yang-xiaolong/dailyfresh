# coding=utf-8
from hashlib import sha1


class PwdEncrypt(object):
    # 该类是一个工具类，用于密码的sha1加密
    def __init__(self):
        pass

    @classmethod
    def encrypt(cls, pwd):
        """密码sha1加密

        Args:
            pwd: 需要经过sha1加密的字符串

        Returns:
            一个经过sha1加密后的字符串
        """
        s1 = sha1()
        s1.update(pwd)
        pwd_sha1 = s1.hexdigest()
        return pwd_sha1
