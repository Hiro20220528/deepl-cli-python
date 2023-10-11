# coding: utf-8
import os
import deepl
from dotenv import load_dotenv

load_dotenv('.env')
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

source_lang = 'EN'
target_lang = 'JA'

# イニシャライズ
translator = deepl.Translator(DEEPL_API_KEY)

while True:
          print("英語を入力してください")
          # input
          text = input()
          print("実行しますか?: y/n")
          enter = input()
          if enter == 'y':
                    pass
          else:
                    print("終了します")
                    break
          # 翻訳を実行
          result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
          print("====結果============================")
          # print すると翻訳後の文章が出力される
          print(result)
          print("====================================")