# -*- coding: utf-8 -*-

import collections
import sxtwl
from . import datas

Gans = collections.namedtuple("Gans", "year month day time")
Zhis = collections.namedtuple("Zhis", "year month day time")


class BaZi():
    def __init__(self, year: int, month: int, day: int, hour: int):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hour = int(hour)
    
    def get_detail(self):
        detail = {}
        day = sxtwl.fromSolar(
            self.year, self.month, self.day)
        detail['solarDay'] = {
            'year': day.getSolarYear(),
            'month': day.getSolarMonth(),
            'day': day.getSolarDay()
        }
        detail['lunarDay'] = {
            'year': day.getLunarYear(),
            'leap': "闰" if day.isLunarLeap() else "",
            'month': day.getLunarMonth(),
            'day': day.getLunarDay()
        }
        yGZ = day.getYearGZ()
        mGZ = day.getMonthGZ()
        dGZ = day.getDayGZ()
        hGZ = day.getHourGZ(self.hour)
        gans = Gans(
            year=datas.Gan[yGZ.tg], month=datas.Gan[mGZ.tg], 
            day=datas.Gan[dGZ.tg], time=datas.Gan[hGZ.tg])
        zhis = Zhis(
            year=datas.Zhi[yGZ.dz], month=datas.Zhi[mGZ.dz], 
            day=datas.Zhi[dGZ.dz], time=datas.Zhi[hGZ.dz])
        detail['sizhu'] = {
            'gans': ' '.join(list(gans)),
            'zhis': ' '.join(list(zhis))
        }
        me = datas.Gan[dGZ.tg]
        gan_shens = []
        for seq, item in enumerate(gans):    
            if seq == 2:
                gan_shens.append('己')
            else:
                gan_shens.append(datas.ten_deities[me][item])
        zhi_shens = []
        for item in zhis:
            d = datas.zhi5[item]
            zhi_shens.append(datas.ten_deities[me][max(d, key=d.get)])
        detail['ten_deities'] = {
            'gan': gan_shens,
            'zhi': zhi_shens
        }
        return detail