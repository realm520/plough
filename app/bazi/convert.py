# -*- coding: utf-8 -*-

import argparse
   
description = '''
'''
parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('gans', action="store", help=u'天干')
parser.add_argument('zhis', action="store", help=u'地支')
parser.add_argument('--version', action='version',
                    version='%(prog)s 0.1 Rongzhong xu 2019 4 12 钉钉或微信pythontesting')
options = parser.parse_args()

for item in zip(options.gans, options.zhis):
    print("".join(item), end=' ')

