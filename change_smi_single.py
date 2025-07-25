# -*- coding: utf-8 -*-

from config import *

def change_smi_single():

    # 初始化计数器
    pdb_number = 0
    pdb_war_number = 0
    pdb_err_number = 0

    # 加载与排序相关目录下的文件（名称顺序）
    ligand_smi_single_list = os.listdir(ligand_smi_single_path) # 获取输入目录ligand_smi_path下所有文件到一个列表
    ligand_smi_single_list.sort() # 为蛋白质列表进行顺序排序



    # Make ligand_single.SMI change to ligand.PDB
    # 将小分子从.SMI格式转换到.PDB格式
    print(f'\n\033[92m    {lang_smi_sing_began}\033[0m')
    for smi_sing in ligand_smi_single_list:  # 获取ligand_smi_single目录下所有文件到一个列表
        no_work_smi_sing = '#' in smi_sing  # the protein to_work or no_work ? 判断该小分子是否被注释
        if no_work_smi_sing != True:
            if smi_sing.endswith('.smi'):  # checking file type 检查文件后缀是否正确
                smi_single_path = os.path.join(ligand_smi_single_path, smi_sing)  # fund file path 该目录下所有.smi文件的路径
                # set pdb file name
                # 获取PDB名称
                ligand_smi_single_name = smi_single_path.rsplit('/', 1)[-1]  # abstracting smi file name 去除路径中的其他信息
                start = ligand_smi_single_name.rfind('/')  # 从/后开始提取
                end = ligand_smi_single_name.rfind('.')  # 到.前停止
                ligand_pdb_name = ligand_smi_single_name[start + 1:end]  # 组合成pdb的名称
                # 运行OpenBaBel
                obabel_smi_cmd = ['obabel',
                                  '-ismi', smi_single_path,
                                  '-opdb',
                                  '-O', f"{ligand_pdb_path}/{ligand_pdb_name}.pdb",
                                  '-h',
                                  '--partialcharge', 'gasteiger',
                                  '--minimize',
                                  '--gen3D',
                                  '--ff', 'MMFF94']
                # print(obabel_smi_cmd)
                # 防止程序报错后退出
                try:
                    obabel_out = subprocess.check_output(obabel_smi_cmd, shell=False, stderr=subprocess.STDOUT, text=True)  # 捕获OpenBaBel输出
                    os.system('killall -9 obabel')  # 杀死那个OpenBaBel进程
                except:  # 获取异常
                    obabel_out = traceback.format_exc()
                if (obabel_out.find('1 molecule converted') >= 0):  # 检查是否转换成功
                    pdb_number += 1  # pdb计数器+1，用于该模块运行完毕后的总结
                    print(f'\033[92m    {lang_smi_sing_suc} \033[95m{ligand_smi_single_name}\033[0m')  # print green information # 打印成功信息
                else:  # 文件后缀错误，停止执行操作并输出警告
                    pdb_err_number += 1  # 错误计数器+1，用于该模块运行完毕后的总结输出
                    error_smi_single_path = os.path.join(ligand_smi_single_path, smi_sing)  # fund error file path 获取错误分子路径
                    error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name 获取错误分子名称
                    print(f'\033[91m    {lang_smi_sing_err.format(error_smi_single_name, obabel_out)}\033[0m')
        else:
            pdb_war_number += 1  # 警告计数器+1，用于该模块运行完毕后的总结输出
            error_smi_single_path = os.path.join(ligand_smi_single_path, smi_sing)  # fund error file path 获取错误分子路径
            error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name 获取错误分子名称
            print(f'\033[93m    {lang_smi_sing_war} \033[95m{error_smi_single_name}\033[0m')  # print red error
    else:  # 如果文件被“#”注释
        no_work_smi_name = smi_sing.replace("#", "")  # 获取被注释的文件名称
        print(f'\033[92m    {lang_smi_sing_commend} \033[95m{no_work_smi_name}\033[0m')  # 打印注释信息

    return pdb_number, pdb_war_number, pdb_err_number  # 将运行次数，错误数，警告数打包为元组

if __name__ == '__main__':
    result = change_smi_single  # 将元组作为函数的输出
    change_smi_single()