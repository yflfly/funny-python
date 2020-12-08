# coding:utf-8
import os
from pycorrector import Corrector

pwd_path = os.path.abspath(os.path.dirname(__file__))

lm_path = os.path.join(pwd_path, './lm_4gram_wxjs.arpa')
model = Corrector(language_model_path=lm_path)

corrected_sent, detail = model.correct('民警遂依法对被告人王昇辉血液进行采集')
print(corrected_sent, detail)
