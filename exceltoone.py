# -- coding: utf-8 --
import os
import openpyxl
import xlrd


# 设置表头
def sheetHead(ws, current_dir, filenames):
    excel_path = filenames[0]
    # 打开excel文件,获取工作簿对象
    excel = xlrd.open_workbook(current_dir + "\\" + excel_path.strip('\u202a'))
    table = excel.sheet_by_index(0)  # 通过索引获取，例如打开第一个sheet表格
    for i in range(table.nrows):
        if i < 3:
            hang = table.row_values(i)
            print(hang)
            ws.append(hang)  # 获取第i行


# 设置表内容
def sheetContent(ws, current_dir, filenames):
    for filename in filenames:
        print(filename)
        # 打开excel文件,获取工作簿对象
        excel = xlrd.open_workbook(current_dir + "\\" + filename)
        table = excel.sheet_by_index(0)
        for i in range(table.nrows):
            if i > 2:
                hang = table.row_values(i)
                print(hang)
                ws.append(hang)  # 获取第i行


if __name__ == '__main__':
    wb = openpyxl.Workbook()  # 创建一个工作表
    ws = wb.create_sheet('sheet1', 0)
    # 输出文件名
    current_dir = os.path.abspath(os.path.dirname(__file__))

    outPath = current_dir + "\\all.xlsx"
    # 输入文件夹
    inPath = current_dir
    filenames = os.listdir(inPath)
    files = []
    for file in filenames:
        if file.endswith("xls") or file.endswith("xlsx"):
            files.append(file)
    if len(files) < 1:
        print("当前目录下没有xls或者xlsx文件")
    else:
        sheetHead(ws, current_dir, files)
        sheetContent(ws, current_dir, files)
        wb.save(outPath)
        print("合并已经完成，关闭窗口即可")
