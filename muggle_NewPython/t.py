import os
import time
import uuid
import httpx
import hashlib
import typing as t
from pprint import pprint
from httpx import Response
from dataclasses import dataclass
from functools import cached_property



class Signer:

    @cached_property
    def time(self):
        return str(int(time.time()))

    @cached_property
    def salt(self):
        return str(uuid.uuid1())

    def __init__(self, key, secret) -> None:
        self.key = key
        self.secret = secret

    def _truncate(self, q):
        if q is None:
            return None
        size = len(q)
        return q if size <= 20 else q[0:10] + str(size) + q[size - 10 : size]

    def sign(self, q):
        time = self.time
        salt = self.salt
        signStr = f"{self.key}{self._truncate(q)}{salt}{time}{self.secret}"
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(signStr.encode("utf-8"))
        return {
            "sign": hash_algorithm.hexdigest(),
            'curtime': time,
            "salt": salt,
            "signType": "v3",
            "appKey": self.key,
        }


class Config:
    API:t.Text
    Q:t.Text
    CONFIG:t.Dict

class OCRConfig(Config):
    Q      = "img"
    API    = "https://openapi.youdao.com/ocrapi",
    CONFIG = {
        "detectType": "10012",
        "langType": "auto",
        "imageType": "1",
        "docType": "json",
    }



class TransConfig(Config):
    Q      ="q"
    API    = "https://openapi.youdao.com/api/"
    CONFIG =  {
        "from": "auto",
        "to": "auto",
        "vocabId": ""
    }


@dataclass
class Result:

    _res:Response

    @property
    def raw(self):
        return self._res.content

    @property
    def result(self):
        return self._res.json()

    @property
    def err(self)-> int:
        return int(self._res.json()["errorCode"])

    def __getitem__(self, key):
        return self.result.get(key)

    def eject(self)->Response:
        return self._res



def _get_p(s:Signer,c:Config,q:t.Text,**kwd):
    query = {c.Q:q}
    return {
        "url":c.API,
        "data":{
            **c.CONFIG,
            **s.sign(q),
            **query,
            **kwd
        },
        "headers":{"Content-Type": "application/x-www-form-urlencoded"}
    }



def api(config:t.Text):

    config_map = {
        "trans":TransConfig(),
        'ocr':OCRConfig(),
    }
    _Config = config_map.get(config)
    if not _Config:
        raise Exception(f"This service({config}) is not implement yet")

    def inner(func:t.Callable):

        def ins(self,*args,**kwd):
            assert isinstance(_Config,Config)
            signer = Signer(key=self.key,secret=self.secret)
            param = _get_p(signer,_Config,q=args[0],**kwd)
            res = httpx.post(**param)
            return Result(res)

        return ins

    return inner



class YouDao:
    def __init__(self,key:t.Text=None,secret:t.Text=None) -> None:
        # if not key or not secret:
        #     try:
        #         key = os.environ["APP_KEY"]
        #         secret = os.environ["APP_SECRET"]
        #     except KeyError:
        #         raise Exception("To use YouDao Api we need APP_KEY n APP_SECRET ")

        self.key = key
        self.secret = secret


    @api('trans')
    def translate(self,q,config:Config=None,**kwd)->Result:
        ...

    @api('ocr')
    def ocr_upload(self,img,config=None,**kwd)->Result:
        ...

y = YouDao(key="xxx",secret="xxx")
res = y.translate("hello")

pprint(res["basic"]["explains"])
pprint(res.err)
