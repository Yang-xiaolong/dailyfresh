# coding=utf-8
from hashlib import sha1


class PwdEncrypt(object):
    def __init__(self):
        pass

    @classmethod
    def encrypt(cls, pwd):
        s1 = sha1()
        s1.update(pwd)
        pwd_sha1 = s1.hexdigest()
        return pwd_sha1
