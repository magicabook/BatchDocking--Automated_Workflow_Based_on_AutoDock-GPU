# -*- coding: utf-8 -*-

import config
from config import *
import importlib
from importlib import reload



# 定义检查函数，检查输入是否为整数，输出布尔值
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False



def set():
    # 定义合法的选择集合
    set_select_list = {'1', '2', '3','4','z'}
    # 程序交互的主要代码
    while True:
        # 模式选择，让用户自行决定执行的功能
        set_function_number = None  # 清空选择缓存
        while set_function_number not in set_select_list:  # 检查输入的选择是否合法
            try:
                print(f"\033[92m{lang_inter_set}\n\033[0m")  # 打印功能列表
                set_function_number = input(lang_inter_set_select).strip().lower()  # 用户的输入写入选择缓存
                if set_function_number in set_select_list:  # 检查输入的选择是否合法
                    break  # 输入正确则退出循环
                else:  # 输出警告信息
                    print(f"\033[33m\n{lang_inter_function_err}\n\033[0m")
            except ValueError:  # 输出警告信息
                print(f"\033[33m\n{lang_inter_function_err}\n\033[0m")
        # 打印选择结果
        set_select_out = f'lang_inter_set_select_{set_function_number}'  # 基于用户的选择决定调用的输出变量名称
        print(f"\n\033[92m{lang_inter_suc.format(globals().get(set_select_out))}\033[0m")  # 打印选择结果



        # 基于用户的选择，执行相关模块
        # 语言
        if set_function_number == '1':
            lang_list_raw = os.listdir(f'{program_path}BatchDock-{ver}/language')
            lang_list = [s[:-3] for s in lang_list_raw if s.endswith(".py") and s not in ["__init__.py", "__pycharm__.py"]] # 提取language目录下的所有语言包文件
            set_lang = None
            while set_lang not in lang_list:  # 检查输入的选择是否合法
                try:
                    set_lang = input(lang_inter_set_lang.format(lang_list)).strip().lower() # 获取用户选择的语言
                    if set_lang in lang_list:  # 检查输入的选择是否合法
                        break  # 输入正确则退出循环
                    elif set_lang == 'z': # 若选择返回则结束循环
                        break
                    else:  # 输出警告信息
                        print(f"\033[33m\n{lang_inter_function_err}\033[0m")
                except ValueError:  # 输出警告信息
                    print(f"\033[33m\n{lang_inter_function_err}\033[0m")
            if set_lang == 'z': # 判断是否返回上级目录
                print(f"{lang_return_list}\n")
            else:
                # 打开配置文件
                with open(f'{program_path}/BatchDock-{ver}/properties.py', 'r') as properties_data:
                    content_lang = properties_data.read()
                old_lang = re.search(r"language\s*=\s*'([^']*)'", content_lang).group(1)  # 使用正则表达式提取language = ‘？’
                # 替换文件内容
                new_lang = set_lang
                # 查询并修改
                content_lang = content_lang.replace(f"language = '{old_lang}'", f"language = '{new_lang}'")
                # 保存修改
                with open(f'{program_path}/BatchDock-{ver}/properties.py', 'w') as properties_data:
                    properties_data.write(content_lang)
                reload(config)
                print(f"\n\033[92m{lang_inter_set_lang_suc}{set_lang}\n\033[0m")

        # 设置单次对接迭代次数
        elif set_function_number == '2':
            # 打开配置文件
            with open(f'{program_path}/BatchDock-{ver}/properties.py', 'r') as properties_data:
                content_nrun = properties_data.read()
            while True:
                old_nrun = re.search(r"nrun\s*=\s*[’']?(\d+)[’']?", content_nrun).group(1)  # 使用正则表达式提取nrun = ‘？’并提取其中的数字
                set_nrun = input(lang_inter_set_nrun.format(old_nrun)).strip().lower()  # 获取用户输入的种子
                # 检测seed是否为整数
                if (is_integer(set_nrun)) == True:
                    break
                elif set_nrun == 'z': # 若选择返回则结束循环
                    break
                elif (is_integer(set_nrun)) == False:
                    print(f"\033\n[33m{lang_inter_set_nrun_war}\033[0m")
                elif len(set_nrun) == 0:
                    print(f"\033[33m{lang_inter_set_nrun_none}\033[0m")
            if set_nrun == 'z': # 判断是否返回上级目录
                print(f"{lang_return_list}\n")
            else:
                # 替换文件内容
                new_run = set_nrun
                # 查询并修改
                content_nrun = content_nrun.replace(f"nrun = '{old_nrun}'", f"nrun = '{new_run}'")
                # 保存修改
                with open(f'{program_path}/BatchDock-{ver}/properties.py', 'w') as properties_data:
                    properties_data.write(content_nrun)
                print(f"\n\033[92m{lang_inter_set_nrun_suc}{set_nrun}\n\033[0m")

        # 设置默认结果文件名
        elif set_function_number == '3':
            # 打开配置文件
            with open(f'{program_path}/BatchDock-{ver}/properties.py', 'r') as properties_data:
                content_name = properties_data.read()
            old_name = re.search(r"result_name_hat\s*=\s*'([^']*)'", content_name).group(1)  # 使用正则表达式提取name = ‘？’
            set_name = input(lang_inter_set_name.format(old_name)).strip().lower()  # 获取用户输入的名称
            if set_name == 'z': # 判断是否返回上级目录
                print(f"{lang_return_list}\n")
            else:
                # 替换文件内容
                new_name = set_name
                # 查询并修改
                content_name = content_name.replace(f"result_name_hat = '{old_name}'", f"result_name_hat = '{new_name}'")
                # 保存修改
                with open(f'{program_path}/BatchDock-{ver}/properties.py', 'w') as properties_data:
                    properties_data.write(content_name)
                print(f"\n\033[92m{lang_inter_set_name_suc}{set_name}\n\033[0m")

        #设置对接程序运行种子
        elif set_function_number == '4':
            # 打开配置文件
            with open(f'{program_path}/BatchDock-{ver}/properties.py', 'r') as properties_data:
                content_seed = properties_data.read()
            while True:
                try:
                    old_seed = re.search(r"seed\s*=\s*'([^']*)'", content_seed).group(1)  # 使用正则表达式提取seed = ‘？’
                except ValueError: # 若用户输入为空，则不报错且将种子字符串长度清空为0
                    old_seed = ''
                set_seed = input(lang_inter_set_seed.format(old_seed)).strip().lower()  # 获取用户输入的种子
                # 检测seed是否为整数或空
                if set_seed == '':
                    break
                elif set_seed == 'z': # 若选择返回则结束循环
                    break
                elif (is_integer(set_seed)) == True:
                    break
                elif (is_integer(set_seed)) == False:
                    print(f"\033[33m\n{lang_inter_set_seed_war}\033[0m")
            if set_seed == 'z': # 判断是否返回上级目录
                print(f"{lang_return_list}\n")
            else:
                # 替换文件内容
                new_seed = set_seed
                # 查询并修改
                content_seed = content_seed.replace(f"seed = '{old_seed}'", f"seed = '{new_seed}'")
                # 保存修改
                with open(f'{program_path}/BatchDock-{ver}/properties.py', 'w') as properties_data:
                    properties_data.write(content_seed)
                if len(set_seed) == 0:
                    print(f"\n\033[92m{lang_inter_set_seed_suc1}{set_seed}\n\033[0m")
                else:
                    print(f"\n\033[92m{lang_inter_set_seed_suc}{set_seed}\n\033[0m")

        #返回上级目录
        elif set_function_number == 'z':
            break



if __name__ == '__main__':
    set()