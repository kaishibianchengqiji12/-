# -*- coding: utf-8 -*-
import json
import requests
from qiniu import Auth
from qiniu import BucketManager
from xpinyin import Pinyin
from xpinyin import Pinyin
p = Pinyin()
gk = p.get_pinyin("影子", ' ', tone_marks='marks')

headers = \
    {
        'X-Access-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODk4MjQ0OTE'
                          'sInVzZXJuYW1lIjoiYWRtaW4ifQ.gHgKY6aswKlmmvFs9dAFdUqdGHxWQFSsjV-FoAew-A0',

        "Content-Type": "application/json"
    }


# data = {
#   "batch": 0,
#   "clickRate": 0,
#   "cnTranslationList": [
#     {
#       "sentencesList": [
#         {
#           "sentence": "string",
#           "sentenceKey": "string",
#           "sentenceUrl": "string",
#           "transleteSentence": "string"
#         }
#       ],
#       "speech": "uuuu",
#       "translation": "kkkkk",
#       "transleteKey": "string",
#       "transleteUrl": "string"
#     }, {
#       "sentencesList": [
#         {
#           "sentence": "jjhjhjh",
#           "sentenceKey": "string",
#           "sentenceUrl": "string",
#           "transleteSentence": "string"
#         }
#       ],
#       "speech": "iuuu",
#       "translation": "ooooooo",
#       "transleteKey": "string",
#       "transleteUrl": "string"
#     }, {
#       "sentencesList": [
#         {
#           "sentence": "jjhjhjh",
#           "sentenceKey": "string",
#           "sentenceUrl": "string",
#           "transleteSentence": "string"
#         }
#       ],
#       "speech": "iuuu",
#       "translation": "ghjdghfdgjdfghf",
#       "transleteKey": "string",
#       "transleteUrl": "string"
#     }
#
#
#
#   ],
#   "pronKey": "string",
#   "pronUrl": "string",
#   "spell": "string",
#   "type": 2,
#   "word": "学科2"
# }

data = [
  {
    "batch": 0,
    "clickRate": 0,
    "cnTranslationList": [
      {
        "sentencesList": [
          {
            "sentence": "string",
            "sentenceKey": "string",
            "transleteSentence": "string"
          }
        ],
        "speech": "string",
        "translation": "string",
        "transleteKey": "string"
      }
    ],
    "photoKey": "string",
    "pronKey": "string",
    "spell": "string",
    "type": 2,
    "word": "gujhghghj"
  },

  {
    "batch": 0,
    "clickRate": 0,
    "cnTranslationList": [
      {
        "sentencesList": [
          {
            "sentence": "string",
            "sentenceKey": "string",
            "transleteSentence": "string"
          }
        ],
        "speech": "string",
        "translation": "string",
        "transleteKey": "string"
      }
    ],
    "photoKey": "string",
    "pronKey": "string",
    "spell": "string",
    "type": 2,
    "word": "jhk"
  }

]

url = "http://192.168.8.10:8080/dict/cn/word/batch/insert"

response = requests.post(url, json=data, headers=headers)

print(response.text)










# try:
#     def data_voice(url1):
#         access_key = 'fB7yr7kZhvRCVv2MN-BkCybnPFZSHhDXej2dTMuN'
#         secret_key = 'hRAWT-cuKY5q-hlxmOyRDJ457hH24OFPiH27coJD'
#         bucket_name = 'dev-pub-lsbc'
#         q = Auth(access_key, secret_key)
#         bucket = BucketManager(q)
#         key = None
#         ret1 = bucket.fetch(url1, bucket_name, key)
#         if ret1[0] is not None:
#             ret4 = ret1[0]["key"]
#         else:
#             ret4 = ""
#         return ret4
#
#
#     def chi_voice(url2):
#         access_key = 'fB7yr7kZhvRCVv2MN-BkCybnPFZSHhDXej2dTMuN'
#         secret_key = 'hRAWT-cuKY5q-hlxmOyRDJ457hH24OFPiH27coJD'
#         bucket_name = 'dev-pub-lsbc'
#         q = Auth(access_key, secret_key)
#         bucket = BucketManager(q)
#         key = None
#         ret2 = bucket.fetch(url2, bucket_name, key)
#         print(ret2)
#         print(type(ret2))
#         if ret2[0] is not None:
#             ret3 = ret2[0]["key"]
#         else:
#             ret3 = ""
#         return ret3
#
#
#     headers = {
#         'X-Access-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODk4MjQ0OTE'
#                           'sInVzZXJuYW1lIjoiYWRtaW4ifQ.gHgKY6aswKlmmvFs9dAFdUqdGHxWQFSsjV-FoAew-A0',
#
#         "Content-Type": "application/json"
#     }
#
#     with open("cizu100.json", "r", encoding="utf-8") as f:
#         temp = json.loads(f.read())
#
#     for i in temp:
#         if i['all_example']:
#             print(i["word_group"])
#             phoneticize = Pinyin()
#             spell = phoneticize.get_pinyin(i["word_group"], ' ')
#             if i["chinese_voice"]:
#                 chinese_voice = data_voice(i["chinese_voice"])
#             else:
#                 chinese_voice = ""
#
#             mylist = list()
#             for ind, j in enumerate(i["all_example"]):
#                 locals()['list' + str(ind)] = list()
#                 if j["english_voice"]:
#                     print(j["english_voice"])
#                     english_voice = chi_voice(j["english_voice"])
#                 else:
#                     english_voice = ""
#                 jsonzidina = {
#                     "sentencesList": [
#                         {
#                             "sentence": j["english_example"],
#                             "sentenceKey": "",
#                             "sentenceUrl": "",
#                             "transleteSentence": j["chinese_example"]
#                         }
#                     ],
#                     "speech": j["word_property"],
#                     "translation": j["english_word"],
#                     "transleteKey": english_voice,
#                     "transleteUrl": ""
#                 }
#
#                 locals()['list' + str(ind)].append(jsonzidina)
#                 mylist.append(locals()['list' + str(ind)][0])
#
#             data = {
#                 "batch": 0,
#                 "clickRate": 0,
#                 "cnTranslationList": mylist,
#                 "pronKey": chinese_voice,
#                 "pronUrl": "",
#                 "spell": spell,
#                 "type": 2,
#                 "word": i["word_group"]
#             }
#
#             url = "http://192.168.8.10:8080/dict/cn/word/insert"
#
#             response = requests.post(url, json=data, headers=headers)
#             rep = json.loads(response.text)
#
#             with open("cizu100.txt", "a", encoding="utf-8") as f:
#                 f.write(i["word_group"] + "\n")
#             print(response.text)
#
#         else:
#             phoneticizet = Pinyin()
#             spell = phoneticizet.get_pinyin(i["word_group"], ' ')
#             if i["chinese_voice"]:
#                 chinese_voice = data_voice(i["chinese_voice"])
#             else:
#                 chinese_voice = ""
#             data = {
#                 "batch": 0,
#                 "clickRate": 0,
#                 "cnTranslationList": [
#                     {
#                         "sentencesList": [
#                             {
#                                 "sentence": "",
#                                 "sentenceKey": "",
#                                 "sentenceUrl": "",
#                                 "transleteSentence": ""
#                             }
#                         ],
#                         "speech": "",
#                         "translation": "",
#                         "transleteKey": "",
#                         "transleteUrl": ""
#                     }
#                 ],
#                 "pronKey": chinese_voice,
#                 "pronUrl": "",
#                 "spell": spell,
#                 "type": 2,
#                 "word": i["word_group"]
#             }
#             url = "http://192.168.8.10:8080/dict/cn/word/insert"
#
#             response = requests.post(url, json=data, headers=headers)
#             with open("cizu100.txt", "a", encoding="utf-8") as f:
#                 f.write(i["word_group"] + "\n")
#             print(response.text)
# except:
#     pass


