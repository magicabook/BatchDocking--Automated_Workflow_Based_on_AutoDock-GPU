from properties import *

# 定义合法的选择集合
select_set = {'0','1','2','3','4','a','b','z'}

# 打印程序信息
print(f'\033[92m{lang_inter_describe}\033[0m')

# 程序交互的主要代码
while True:
    # 模式选择，让用户自行决定执行的功能
    function_number = None # 清空选择缓存
    while function_number not in select_set: # 检查输入的选择是否合法
        try:
            print(f'\033[92m{lang_inter_select}\033[0m') # 打印功能列表
            function_number = input(lang_inter_function_number).strip().lower() # 用户的输入写入选择缓存
            if function_number in select_set: # 检查输入的选择是否合法
                break  # 输入正确则退出循环
            else: # 输出警告信息
                print(f'\033[93m{lang_inter_function_err}\033[0m')
        except ValueError: # 输出警告信息
            print(f'\033[93m{lang_inter_function_err}\033[0m')

    # 打印选择结果
    select_out = f'lang_inter_select_{function_number}' # 基于用户的选择决定调用的输出变量名称
    print(f'\n\033[92m    {lang_inter_suc.format(globals().get(select_out))}\033[0m') # 打印选择结果
    # 基于用户的选择，执行相关模块
    # 设置界面（语言和对接迭代次数）
    if function_number == '0':
        print('run 0')
    # 仅将输入的txt拆分为单个smiles小分子
    elif function_number == '1':
        import change_smi
        if __name__ == '__main__':
            smi_number, smi_war_number, smi_err_number = change_smi.change_smi() # 执行模块并将元组拆包
        # 输出总结信息
        print(f'\033[92m{lang_smi_end}\033[0m') # 打印提取单个smi模块执行结束信息
        if smi_err_number + smi_war_number == 0:  # 判断异常计数是否为0
            print(f'\033[92m\n    {lang_smi_summary_suc.format(smi_number)}\033[0m')  # 输出无异常结束语句
        else:  # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
            print(f'\033[91m\n{lang_smi_summary_failure.format(smi_number, smi_err_number, smi_war_number)}\033[0m')
    # 仅将单个smiles小分子转换为PDB格式
    elif function_number == '2':
        import change_smi_single
        if __name__ == '__main__':
            pdb_number, pdb_war_number, pdb_err_number = change_smi_single.change_smi_single() # 执行模块并将元组拆包
        # 输出总结信息
        print(f'\033[92m{lang_smi_sing_end}\033[0m')  # 打印smi转换到pdb模块执行结束信息
        if pdb_err_number + pdb_war_number == 0:  # 判断异常计数是否为0
            print(f'\033[92m\n    {lang_smi_sing_summary_suc.format(pdb_number)}\033[0m')  # 输出无异常结束语句
        else:  # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
            print(f'\033[91m\n{lang_smi_sing_summary_failure.format(pdb_number, pdb_err_number, pdb_war_number)}\033[0m')
    # 仅将PDB格式的小分子转换为PDBQT配体格式
    elif function_number == '3':
        import change_pdb
        if __name__ == '__main__':
            pdbqt_number, pdbqt_war_number, pdbqt_err_number = change_pdb.change_pdb() # 执行模块并将元组拆包
        # 输出总结信息
        print(f'\033[92m{lang_pdb_end}\033[0m')  # 打印将小分子转换为.PDBQT格式并设置为配体模块执行结束信息
        if pdbqt_war_number + pdbqt_err_number == 0:  # 判断异常计数是否为0
            print(f'\033[92m\n    {lang_pdb_summary_suc.format(pdbqt_number)}\033[0m')  # 输出无异常结束语句
        else:  # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
            print(f'\033[91m\n{lang_pdb_summary_failure.format(pdbqt_number, pdbqt_err_number, pdbqt_war_number)}\033[0m')
    # 仅运行批量自动对接
    elif function_number == '4':
        import dock
        # 自定义结果文件名称
        inter_result_name = input(lang_dock_inter_name).strip().lower()  # 获取用户自定义的名称
        if len(inter_result_name) > 0:  # 通过查询变量长度判断用户是否自定义名称
            globel_result_name_hat = inter_result_name # 定义传递的变量内容为用户输入
            dock.globel_result_name_hat = globel_result_name_hat # 将用户输入的内容通过变量globel_result_name_hat传递给dock.py
        # def result_name_hat():
        #     return result_name_hat # 将自定义的结果文件名称打包为元组并封装进函数
        if __name__ == '__main__':
            dock_number, dock_war_number, dock_err_number, csv_name = dock.dock()  # 执行模块并将元组拆包
        # 输出总结信息
        print(f'\n\033[92m    {lang_dock_csv_suc} "{csv_name}"\033[0m')
        if dock_war_number + dock_err_number == 0:  # 判断异常计数是否为0
            print(f'\n\033[92m    {lang_dock_summary_suc.format(dock_number)}\033[0m')  # 输出无异常结束语句
        else:  # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
            print(f'\n\033[91m{lang_dock_summary_failure.format(dock_number, dock_err_number, dock_war_number)}\033[0m')
    # 运行小分子前处理的全部流程（ 1 ~ 3 ）
    elif function_number == 'a':
        import change_smi
        import change_smi_single
        import change_pdb
        if __name__ == '__main__':
            smi_number, smi_war_number, smi_err_number = change_smi.change_smi()  # 执行模块并将元组拆包
            pdb_number, pdb_war_number, pdb_err_number = change_smi_single.change_smi_single()
            pdbqt_number, pdbqt_war_number, pdbqt_err_number = change_pdb.change_pdb()
        change_error_number = smi_err_number + pdb_err_number + pdbqt_err_number
        change_warning_number = smi_war_number + pdb_war_number + pdbqt_war_number
        # 输出总结信息
        print(f'\033[92m{lang_pdb_end}\033[0m')  # 打印将小分子转换为.PDBQT格式并设置为配体模块执行结束信息
        if pdbqt_war_number + pdbqt_err_number == 0:  # 判断异常计数是否为0
            print(f'\033[92m\n    {lang_pdb_summary_suc.format(pdbqt_number)}\033[0m')  # 输出无异常结束语句
        else:  # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
            print(f'\033[91m\n{lang_pdb_summary_failure.format(pdbqt_number, change_error_number, change_warning_number)}\033[0m')
    # 运行分子对接的全部流程（ 1 ~ 4 ）
    elif function_number == 'b':
        import change_smi
        import change_smi_single
        import change_pdb
        import dock
        # 自定义结果文件名称
        inter_result_name = input(lang_dock_inter_name).strip().lower()  # 获取用户自定义的名称
        if len(inter_result_name) > 0:  # 通过查询变量长度判断用户是否自定义名称
            globel_result_name_hat = inter_result_name  # 定义传递的变量内容为用户输入
            dock.globel_result_name_hat = globel_result_name_hat  # 将用户输入的内容通过变量globel_result_name_hat传递给dock.py
        if __name__ == '__main__':
            smi_number, smi_war_number, smi_err_number = change_smi.change_smi()  # 执行模块并将元组拆包
            pdb_number, pdb_war_number, pdb_err_number = change_smi_single.change_smi_single()
            pdbqt_number, pdbqt_war_number, pdbqt_err_number = change_pdb.change_pdb()
            dock_number, dock_war_number, dock_err_number, csv_name = dock.dock()
        error_number = smi_err_number + pdb_err_number + pdbqt_err_number + dock_err_number
        warning_number = smi_war_number + pdb_war_number + pdbqt_war_number + dock_war_number
        # 输出总结信息
        print(f'\n\033[92m    {lang_dock_csv_suc} "{csv_name}"\033[0m')
        if dock_war_number + dock_err_number == 0:  # 判断异常计数是否为0
            print(f'\n\033[92m    {lang_dock_summary_suc.format(dock_number)}\033[0m')  # 输出无异常结束语句
        else:  # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
            print(f'\n\033[91m{lang_dock_summary_failure.format(dock_number, error_number, warning_number)}\033[0m')
    # 退出程序
    elif function_number == 'z':
        print(f'\033[92m    {lang_inter_quit}\033[0m')
        break