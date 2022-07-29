# -*- coding: utf-8 -*-

import  sxtwl
import argparse
import collections
import pprint
import datetime

from bidict import bidict

from datas import *
from ganzhi import *
from sizi import summarys

def check_gan(gan, gans):
    result = ''
    if ten_deities[gan]['合'] in gans:
        result += "合" + ten_deities[gan]['合']
    if ten_deities[gan]['冲'] in gans:
        result += "冲" + ten_deities[gan]['冲']
    return result

def yinyang(item):
    if item in Gan:
        return '＋' if Gan.index(item)%2 == 0 else '－'
    else:
        return '＋' if Zhi.index(item)%2 == 0 else '－'
    
    
    
    
def get_empty(zhu, zhi):
    empty = empties[zhu]
    if zhi in empty:
        return "空"
    return ""

def get_zhi_detail(zhi, me, multi=1):
    out = ''
    for gan in zhi5[zhi]:
        out = out + "{}{}{}{} ".format(gan, gan5[gan], zhi5[zhi][gan]*multi,  
                                       ten_deities[me][gan])
    return out

def check_gong(zhis, n1, n2, me, hes, desc='三合拱'):
    result = ''
    if zhis[n1] + zhis[n2] in hes:
        gong = hes[zhis[n1] + zhis[n2]] 
        if gong not in zhis:
            result += "\t{}：{}{}-{}[{}]".format(
                desc, zhis[n1], zhis[n2], gong, get_zhi_detail(gong, me))
    return result