import datetime
import pandas as pd
import numpy as np

area_info = pd.read_excel('./data/idcard2021.xls', header=0, dtype={"编码": str})
area_info = area_info.set_index('编码')


class GetInformation(object):
    def __init__(self, id):
        self.id = id
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])
        self.address_code = str(self.id[0:6])

    def get_birthday(self):
        # 通过身份证号获取出生日期
        birthday = "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)
        return birthday

    def get_sex(self):
        if self.id[16:17].isdigit():
            # 男生：1 女生：2
            num = int(self.id[16:17])
            if num % 2 == 0:
                return 2
            else:
                return 1

    def get_age(self):
        # 获取年龄
        now = (datetime.datetime.now() + datetime.timedelta(days=1))
        year = now.year
        month = now.month
        day = now.day

        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year

    def get_province_only(self):
        """通过身份证号获取省份"""
        province_code = int(self.id[0:2])
        province_dict = {
            11: "北京",
            12: "天津",
            13: "河北",
            14: "山西",
            15: "内蒙古",
            21: "辽宁",
            22: "吉林",
            23: "黑龙江",
            31: "上海",
            32: "江苏",
            33: "浙江",
            34: "安徽",
            35: "福建",
            36: "江西",
            37: "山东",
            41: "河南",
            42: "湖北",
            43: "湖南",
            44: "广东",
            45: "广西",
            46: "海南",
            50: "重庆",
            51: "四川",
            52: "贵州",
            53: "云南",
            54: "西藏",
            61: "陕西",
            62: "甘肃",
            63: "青海",
            64: "宁夏",
            65: "新疆",
            71: "台湾",
            81: "香港",
            82: "澳门",
            91: "国外"
        }
        if province_dict[province_code] is not None:
            return province_dict.get(province_code, '')

    def get_province(self):
        """通过身份证号获取省份"""
        province = area_info.to_dict()['省']

        if self.address_code in list(province.keys()):
            province = province.get(self.address_code, '')
            if str(province) == 'nan':
                province = None
            return province
        else:
            return

    def get_city(self):
        """通过身份证号获取城市"""
        city = area_info.to_dict()['市']

        if self.address_code in list(city.keys()):
            city = city.get(self.address_code, '')
            if str(city) == 'nan':
                city = None
            return city
        else:
            return

    def get_district(self):
        """通过身份证号获取区/县"""
        district = area_info.to_dict()['区县']

        if self.address_code in list(district.keys()):
            district = district.get(self.address_code, '')
            if str(district) == 'nan':
                district = None
            return district
        else:
            return


def get_card_info(user_list):
    if user_list[2] == 1:
        id = user_list[1]
        info = GetInformation(id)
        birth = info.get_birthday()  # 1990-11-11
        # age = info.get_age()  # 28
        sex = info.get_sex()  # 1
        province = info.get_province()
        city = info.get_city()
        district = info.get_district()
        print('id:', id)
        print('birth:', birth)
        print('sex:', sex)
        print('province:', province)
        print('city:', city)
        print('district:', district)
        return (id, birth, sex, province, city, district)
