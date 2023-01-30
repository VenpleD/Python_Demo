import os
import re
import math
from os.path import join, getsize
from shutil import copyfile
path = "./chatroom_pictures"
limit = 200 * 1000
def walkFile(filePath):
    totalcount = 0
    data_obj = {}

    for root, dirs, files in os.walk(filePath):
        # print(sum(getsize(join(root, name)) / 1024 for name in files), end="hellend")
        for f in files:
            if re.match(r'(.+\.(?:' + 'jpg|png' + '))', f):
                size = getsize(join(root, f))
                if size > limit:
                    totalcount+=1
                    data_obj[f] = str(math.ceil(size/1000))+" KB"
                    print(os.path.join(root, f) + "size:" + str(size))
                    print(f)
                    # copyfile(root+'/'+f, path+'/temp/'+f)

    return sorted(data_obj.items(), key=lambda item: item[1], reverse = True)
    # print("大于200kb的文件个数：" + str(totalcount)+str(ls))

# -*- coding: utf-8 -*-
import xlwt
import time
# 生成表格文件
def create_file(content):
    # 初始化样式
    style_head = xlwt.XFStyle()
    # 初始化字体相关
    font = xlwt.Font()
    font.name = "微软雅黑"
    font.bold = True
    # 必须是数字索引
    font.colour_index = 1
    # 初始背景图案
    bg = xlwt.Pattern()
    # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    bg.pattern = xlwt.Pattern.SOLID_PATTERN
    # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray
    bg.pattern_fore_colour = 4

    # 设置字体
    style_head.font = font
    # 设置背景
    style_head.pattern = bg

    # 创建一个excel
    excel = xlwt.Workbook(encoding='utf-8')
    # 添加工作区
    sheet = excel.add_sheet("演示表格")
    # xlwt中是行和列都是从0开始计算的
    # first_col_0 = sheet.col(0)
    # first_col_2 = 
    # 设置存储路径列宽度
    sheet.col(1).width = 256 * 15
    sheet.col(0).width = 256 * 50
    # 标题信息
    head = ["文件名", "文件大小"]
    for index, value in enumerate(head):
        sheet.write(0, index, value, style_head)

    # 循环写入
    for index, value_list in enumerate(content, 1):
        for i, value in enumerate(value_list):
            sheet.write(index, i, value)

    # 保存excel
    file_name = "超过200k图片.xls"
    '''
    保存excell
    '''
    excel.save(file_name)
    return file_name


def main(): 
    # walkFile(path)
    # index = 0
    # data_list = []
    # for key in data_obj.keys():
    #     index+=1
    #     sub_list = []
    #     sub_list.append(str(index))
    #     sub_list.append(key)
    #     sub_list.append(data_obj[key])
    #     data_list.append(sub_list)
    data = create_file(walkFile(path)) #不想写注释，怎么地了
    print(data)


if __name__ == '__main__':
    main()