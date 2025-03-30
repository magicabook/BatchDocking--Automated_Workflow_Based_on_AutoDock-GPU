from properties import *

def change_smi_single():
    # 初始化计数器
    pdb_number = 0
    pdb_war_number = 0
    pdb_err_number = 0
    # Make ligand_single.SMI change to ligand.PDB
    # 将小分子从.SMI格式转换到.PDB格式
    print(f'\n\033[92m{lang_smi_sing_began}\033[0m')
    for smi_sing in os.listdir(ligand_smi_single): # 获取ligand_smi_single目录下所有文件到一个列表
        no_work_smi_sing = '#' in smi_sing  # the protein to_work or no_work ? 判断该小分子是否被注释
        if no_work_smi_sing != True:
            if smi_sing.endswith('.smi'): # checking file type 检查文件后缀是否正确
                smi_single_path = os.path.join(ligand_smi_single, smi_sing) # fund file path 该目录下所有.smi文件的路径
                # set pdb file name
                # 获取PDB名称
                ligand_smi_single_name = smi_single_path.rsplit('/', 1)[-1]  # abstracting smi file name 去除路径中的其他信息
                start = ligand_smi_single_name.rfind('/') # 从/后开始提取
                end = ligand_smi_single_name.rfind('.') # 到.前停止
                ligand_pdb_name = ligand_smi_single_name[start + 1:end] # 组合成pdb的名称
                # 运行OpenBaBel
                obabel_smi_cmd = ['obabel',
                                '-ismi', smi_single_path,
                                '-opdb',
                                '-O', f"{ligand_pdb}/{ligand_pdb_name}.pdb",
                                '-h',
                                '--gen3D',
                                '--partialcharge', 'gasteiger',
                                '--minimize',
                                '--ff', 'gaff']
                #print(obabel_smi_cmd)
                obabel_out = subprocess.check_output(obabel_smi_cmd,shell=False,stderr=subprocess.STDOUT,text=True) # 捕获OpenBaBel输出
                os.system('killall -9 obabel') # 杀死那个OpenBaBel进程
                if (obabel_out.find('1 molecule converted') >= 0): # 检查是否转换成功
                    pdb_number += 1 # pdb计数器+1，用于该模块运行完毕后的总结
                    print(f'    \033[92m{lang_smi_sing_suc} \033[95m{ligand_smi_single_name}\033[0m') # print green information # 打印成功信息
                elif '#' in smi_sing: # 若该文件被“#”注释，则停止执行对该文件的操作
                    break
                else: # 文件后缀错误，停止执行操作并输出警告
                    pdb_err_number += 1 # 错误计数器+1，用于该模块运行完毕后的总结输出
                    error_smi_single_path = os.path.join(ligand_smi_single, smi_sing)  # fund error file path 获取错误分子路径
                    error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name 获取错误分子名称
                    print(f'\033[91m{lang_smi_sing_err.format(error_smi_single_name,obabel_out)}\033[0m')
            else:
                pdb_war_number += 1 # 警告计数器+1，用于该模块运行完毕后的总结输出
                error_smi_single_path = os.path.join(ligand_smi_single, smi_sing)  # fund error file path 获取错误分子路径
                error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name 获取错误分子名称
                print(f'    \033[93m{lang_smi_sing_war} \033[95m{error_smi_single_name}\033[0m') # print red error
        else: # 如果文件被“#”注释
            no_work_smi_name = smi_sing.replace("#", "") # 获取被注释的文件名称
            print(f'\033[92m    {lang_smi_sing_commend} \033[95m{no_work_smi_name}\033[0m') # 打印注释信息
    return pdb_number, pdb_war_number, pdb_err_number # 将运行次数，错误数，警告数打包为元组

if __name__ == '__main__':
    result = change_smi_single # 将元组作为函数的输出
    change_smi_single()

# # 输出总结信息
# print(f'\033[92m{lang_smi_sing_end}\033[0m') # 打印smi转换到pdb模块执行结束信息
# if pdb_err_number + pdb_war_number == 0: # 判断异常计数是否为0
#     print(f'\033[92m\n    {lang_smi_sing_summary_suc.format(pdb_number)}\033[0m') # 输出无异常结束语句
# else: # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
#     print(f'\033[91m\n{lang_smi_sing_summary_failure.format(pdb_number, pdb_err_number, pdb_war_number)}\033[0m')