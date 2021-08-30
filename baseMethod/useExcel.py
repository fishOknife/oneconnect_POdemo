import sys
import pandas as pd


# 将数据保存至列表中
def get_excel_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name, keep_default_na=False, usecols=[4, 5, 6, 7])
    list_data = df.values.tolist()
    return list_data


# 将excel中的数据组合为字典形式，保存在列表中
# def get_excel_data(file_path, sheet_name):
#     df = pd.read_excel(file_path, sheet_name, keep_default_na=False)
#     test_data = []
#     # 获取表头
#     keys = df.columns.values
#     # 获取行号索引，并遍历
#     for i in df.index.values:
#         row_data = df.loc[i, keys].to_dict()
#         test_data.append(row_data)
#     return test_data


if __name__ == "__main__":
    rootDir = sys.path[1]
    filePath = rootDir + r"\testData\testData.xlsx"
    sheetName = "登录"
    testData = get_excel_data(filePath, sheetName)
    # print(testData)
    # 将字符串转为字典
    # str2dict = eval(testData[0]['requestData'])
    # print(str2dict["phone"])
