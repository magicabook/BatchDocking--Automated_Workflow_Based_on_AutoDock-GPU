import os
import properties
from properties import *



def make_file():
    # 定义目录检查函数
    def check_directory(work_path: str, dir_name: str) -> bool:
        target_path = os.path.join(work_path, dir_name)
        if os.path.isdir(target_path) : # 如果目录存在，则输出存在信息
            print(f"\033[92m    {lang_inter_make_file_dir_yes.format(dir_name)}\033[0m")
        else: # 如果目录不存在，则创建目录
            print(f"\033[92m    {lang_inter_make_file_dir_make.format(dir_name)}\033[0m")
            os.system(f'\mkdir {work_path}/{dir_name}')
            print(f"\033[92m    {lang_inter_make_file_dir_suc.format(dir_name)}\033[0m")

    print(f"\033[92m{lang_inter_make_began}\033[0m")
    # 检测工作目录是否存在
    if os.path.isdir(work_path) == True: # 如果目录存在，则输出存在信息
        print(f"\033[92m    {lang_inter_make_work_path_yes.format(work_path)}\033[0m")
    else: # 如果目录不存在，则创建目录
        print(f"\033[92m    {lang_inter_make_work_path_make.format(work_path)}\033[0m")
        os.system(f'mkdir {work_path}')
        print(f"\033[92m    {lang_inter_make_work_path_suc.format(work_path)}\033[0m")
    # 检测工作目录下文件完整性
    work_catalog = ['ligand_smi', 'ligand_smi_single', 'ligand_pdb', 'ligand_pdbqt', 'protein', 'result_csv',
                    'result_complex', 'result_dlg']
    for dir_name in work_catalog:
        check_directory(work_path, dir_name)

    if __name__ == "__main__":
        make_file()
