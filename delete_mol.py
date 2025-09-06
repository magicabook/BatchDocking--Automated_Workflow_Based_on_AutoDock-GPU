# -*- coding: utf-8 -*-

from config import *



def delete_mol(name_list, function_number):

    print('正在删除旧文件')

    # 判断是否添加mol2目录
    # 添加条件：1）开启mol2输出 2）存在mol2目录 3）模式选择1，2，a，b
    if out_mol2 == 'true' and os.path.isdir(f'{work_path}/ligand_mol2') and function_number in ['1', '2', 'a', 'b']:
        name_list.append('ligand_mol2') # 添加ligand_mol2目录
    # 递归删除
    for name in name_list:
        dir_path = f'{work_path}/{name}' # 构建目录路径
        # 加载与排序相关目录下的文件（名称顺序）
        file_list = os.listdir(dir_path) # 获取目录下所有文件到一个列表
        file_list.sort() # 为列表进行顺序排序
        for file_name in file_list:
            if '#' in file_name:
                continue
            else:
                file_path = f'{dir_path}/{file_name}' # 拼接路径
                if os.path.isdir(file_path): # 判断是否为目录
                    shutil.rmtree(file_path) # 执行删除
                else:
                    os.remove(file_path) # 执行删除

    print('旧文件已删除完毕')
    return name_list, function_number

if __name__ == '__main__':
    delete_mol()