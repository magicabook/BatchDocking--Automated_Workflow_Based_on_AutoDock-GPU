# -*- coding: utf-8 -*-

from config import *

def change_smi():

    # 初始化计数器
    smi_number = 0
    smi_war_number = 0
    smi_err_number = 0

    # 加载与排序相关目录下的文件（名称顺序）
    ligand_smi_txt_list = os.listdir(ligand_smi_path) # 获取输入目录ligand_smi_path下所有文件到一个列表
    ligand_smi_txt_list.sort() # 为输入蛋白质列表进行顺序排序

    

    # 定义对txt文件的处理模式
    def txt_change(ligand_smi_path, smi_file, smi_number, smi_war_number, smi_err_number):
        # read smi.txt
        # 开始阅读小分子集的.txt文件
        smi_path = os.path.join(ligand_smi_path, smi_file) # 该目录下所有.txt文件的路径
        with open(smi_path, "r", encoding="utf-8") as smi_txt_data: #  txt 数据写入 smi_txt_data
            # line read
            # 每次读取一行
            line_number = 0
            for line in smi_txt_data: # 读取每一行
                line_number += 1
                smi_txt_all = (line.strip()) # delete \n 删除所有换行符
                if not smi_txt_all:
                    continue
                # abstracting structure and name
                # 分别提取结构字符串和名称字符串
                parts = smi_txt_all.split() # 按行进行切片
                #print(parts)
                try:
                    smi_str_raw, smi_name_raw = parts[0], parts[1] # abstracting and set 第一个空格前切片为结构字符串，第二个空格前切片为名称字符串
                    # 删除引号
                    smi_str = smi_str_raw.replace("'", '')
                    smi_name = smi_name_raw.replace("'", '')
                    # make file and rename
                    # 新建只包含一个结构的smi文件
                    out_smi =  os.path.join(ligand_smi_single_path, smi_name + ".smi") # define out_file path 定义新建smi文件的路径
                    with open(out_smi,'w') as smi_sing_file: # define out_fine content 读取新建的smi文件，进入写模式
                        smi_sing_file.write(smi_str) # 将结构字符串写入smi文件
                    print(f"\033[92m    {lang_smi_suc} \033[95m{smi_name}\033[0m") # 打印成功信息
                    smi_number += 1 # smi计数器+1，用于该模块运行完毕后的总结
                except: # 若无法提取与转换则跳过
                    print(f"\033[33m    {lang_smi_jump.format(smi_file, line_number, parts)}\033[0m")
        return smi_number, smi_war_number, smi_err_number, smi_war_number, smi_err_number # 将运行信息打包为元组
    


    # # 定义对excel类文件的处理
    # def excel_change(ligand_smi_path, smi_file, smi_number, smi_war_number, smi_err_number):
    #     # read smi.csv
    #     # 开始阅读小分子集的excel文件
    #     smi_path = os.path.join(ligand_smi_path, smi_file) # 该目录下所有.csv文件的路径
    #     # 尝试读取的引擎顺序
    #     engines = [
    #     ('openpyxl', ['.xlsx']),
    #     ('xlrd', ['.xls']),
    #     ('odf', ['.ods']),
    #     ('pyxlsb', ['.xlsb'])
    #     ]
    #     # 按优先级尝试引擎
    #     for engine, exts in engines:
    #         try:
    #             smi_excel_data = pd.read_excel(smi_path, engine=engine) # excel 数据写入 smi_excel_data
    #             print(smi_excel_data)
    #         except Exception as e:
    #             print("读取失败")
    #     # smi_excel_data = pd.read_excel(smi_path) # excel 数据写入 smi_excel_data
    #     # print(smi_excel_data)
    #     # line read
    #     # 每次读取一行
    #     # line_number = 0
    #     # for line in smi_excel_data: # 读取每一行
    #     #     line_number += 1


    #     return ligand_smi_path, smi_file, smi_number, smi_war_number, smi_err_number # 将运行信息打包为元组



    # Change to single_file
    # 将ligand_smi目录下的.txt文件拆分为单个.smi文件存储到ligand_smi_single目录下，并以小分子名称命名
    print(f"\033[92m{lang_smi_began}\033[0m")
    for smi_file in ligand_smi_txt_list:  # make ligand list 阅读该目录下的所有文件并存储到一个list中
        no_work_smi = '#' in smi_file  # the ligand to_work or no_work ? 通过“#”判断该小分子集是否参与工作
        if no_work_smi != True:
            if smi_file.endswith('.txt'):  # checking file type 检查文件后缀是否正确
                smi_number, smi_war_number, smi_err_number, smi_war_number, smi_err_number = txt_change(ligand_smi_path, smi_file, smi_number, smi_war_number, smi_err_number) # 执行对txt模块的处理
            # elif smi_file.endswith('.csv'):
            #     smi_number, smi_war_number, smi_err_number, smi_war_number, smi_err_number = excel_change(ligand_smi_path, smi_file, smi_number, smi_war_number, smi_err_number) # 执行对excel模块的处理
            elif '#' in smi_file: # 若该文件被“#”注释，则停止执行对该文件的操作
                break
            else: # 文件后缀错误，停止执行操作并输出警告
                smi_war_number += 1 # 警告计数器+1，用于该模块运行完毕后的总结输出
                error_smi_path = os.path.join(ligand_smi_path, smi_file)  # fund error file list # 获取错误文件的路径
                error_smi_name = error_smi_path.rsplit('/', 1)[-1]  # set error file name # 提取错误文件的名称
                print(f"\033[33m    {lang_smi_war} {error_smi_name}\033[0m")  # print yellow warning # 打印文件类型警告
        else: # 如果文件被“#”注释file
            no_work_txt_name = smi_file.replace("#", "") # 获取被注释的文件名称
            print(f"\033[92m    {lang_smi_commend} \033[95m{no_work_txt_name}\033[0m") # 打印注释信息

    return smi_number, smi_war_number, smi_err_number # 将运行次数，错误数，警告数打包为元组

if __name__ == '__main__':
    result = change_smi # 将元组作为函数的输出
    change_smi()