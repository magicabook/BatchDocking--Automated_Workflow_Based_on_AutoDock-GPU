# -*- coding: utf-8 -*-

from config import *

def change_pdb():

    # 初始化计数器
    pdbqt_number = 0
    pdbqt_war_number = 0
    pdbqt_err_number = 0

    # 加载与排序相关目录下的文件（名称顺序）
    ligand_pdb_list = os.listdir(ligand_pdb_path) # 获取输入目录ligand_smi_path下所有文件到一个列表
    ligand_pdb_list.sort() # 为蛋白质列表进行顺序排序



    # Make ligand.PDB change to ligand.PDBQT and setting ligand
    # 将小分子转换为.PDBQT格式并设置为配体
    print(f"\n\033[92m    {lang_pdb_began}\033[0m")
    for pdb in ligand_pdb_list: # 顺序执行ligand_pdb目录下所有文件
        no_work_pdb = '#' in pdb  # the protein to_work or no_work ? 判断该小分子是否被注释
        if no_work_pdb != True:
            if pdb.endswith('.pdb'):  # checking file type 检查文件后缀是否正确
                pdb_path = os.path.join(ligand_pdb_path, pdb)  # fund file path list 该目录下所有.smi文件的路径
                ligand_pdbqt_name = pdb_path.rsplit('/', 1)[-1]  # set pdbqt file name 获取PDB名称
                change_pdbqt_cmd = [py2, Grid,
                                    '-l', pdb_path,
                                    '-o', f'{ligand_pdbqt_path}/{ligand_pdbqt_name}qt']
                # 防止程序报错后退出
                try:
                    change_pdbqt_out = subprocess.check_output(change_pdbqt_cmd,shell=False,stderr=subprocess.STDOUT,text=True)
                except: # 获取异常
                    change_pdbqt_out = traceback.format_exc()
                # 检查报错捕获是否有内容
                if (len(change_pdbqt_out) < 1): # 如果无错误捕获
                    pdbqt_number += 1 # pdbqt计数器+1，用于该模块运行完毕后的总结
                    print(f"\033[92m    {lang_pdb_suc}\033[95m{ligand_pdbqt_name}\033[0m")  # print green information
                else: # 如果报错捕获存在内容
                    pdbqt_err_number += 1 # 错误计数器+1，用于该模块运行完毕后的总结输出
                    error_pdb_path = os.path.join(ligand_pdb_path, pdb)  # fund error file path 获取错误分子路径
                    error_pdb_name = error_pdb_path.rsplit('/', 1)[-1]  # set error file name 获取错误分子名称
                    print(f'\033[31m    {lang_pdb_err.format(error_pdb_name, change_pdbqt_out)}\033[0m')
            else: # 文件后缀错误，停止执行操作并输出警告
                pdbqt_war_number += 1 # 错误计数器+1，用于该模块运行完毕后的总结输出
                error_pdb_path = os.path.join(ligand_pdbqt_path, pdb)  # fund error file path 获取错误分子路径
                error_pdb_name = error_pdb_path.rsplit('/', 1)[-1]  # set error file name 获取错误分子名称
                print(f"\033[33m    {lang_pdb_war}\033[95m{error_pdb_name}\033[0m")  # print yellow warning
        else: # 如果文件被“#”注释
            no_work_pdb_name = pdb.replace("#", "") # 获取被注释的文件名称
            print(f"\033[92m    {lang_pdb_commend} \033[95m{no_work_pdb_name}\033[0m") # 打印注释信息

    return pdbqt_number, pdbqt_war_number, pdbqt_err_number # 将运行次数，错误数，警告数打包为元组

if __name__ == '__main__':
    result = change_pdb # 将元组作为函数的输出
    change_pdb()