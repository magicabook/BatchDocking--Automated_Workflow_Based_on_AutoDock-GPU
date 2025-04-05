from properties import *

def dock():
    # get system time to make file sign
    time_raw = datetime.datetime.now()
    # change to str
    time_str = time_raw.strftime('%Y-%m-%d %H-%M-%S')
    time_str_file = time_raw.strftime('%Y-%m-%d\ %H-%M-%S')
    # 初始化计数器
    dock_number = 0
    dock_war_number = 0
    dock_err_number = 0

    result_name_hat = globals().get('globel_result_name_hat') # 获取从main.py传递来的变量globel_result_name_hat并作为结果文件名

    # Checking protein.maps.fld
    # 检查蛋白质网格文件是否缺失
    print(f"\n\033[92m{lang_dock_workfile_began}\033[0m")
    for protein_name in os.listdir(protein_list_path): # make protein list 获取蛋白质列表
        if os.system(f'find {protein_list_path}/{protein_name}/ -type f -name "*.maps.fld" | grep -q .;') != 0: # 检查网格文件是否存在
            if '#' in protein_name: # 若蛋白质被注释，则终止执行该模块
                break
            else: # 若该蛋白未被注释且无网格文件
                dock_err_number += 1 # 错误计数器+1，用于该模块运行完毕后的总结输出
                print(f"\033[91m{lang_dock_fld_err}\033[96m{protein_name}\033[0m")
    # Make result_complex/name_time
    # 创建复合物存放目录并以系统时间为结尾
    os.system(f'mkdir {result_complex}/{result_name_hat}\ {time_str_file}')
    print(f"\033[92m    {lang_dock_complex} '{result_name_hat} {time_str}'\033[0m")
    # Make result_dlg/name_time
    # 创建构象结果存放目录并以系统时间为结尾
    os.system(f'mkdir {result_dlg}/{result_name_hat}\ {time_str_file}')
    print(f"\033[92m    {lang_dock_dlg} '{result_name_hat} {time_str}'\033[0m")
    # Make result_dlg/protein
    # 为小分子构象创建以蛋白质为名称的二级目录
    for protein_name in os.listdir(protein_list_path): # make protein list 浏览蛋白质目录并生成列表
        no_work = '#' in protein_name # the protein to_work or no_work ? 判断蛋白质是否被注释
        if no_work != True: # 如果蛋白质没有被注释
            # checking do .result_dlg have protein ?
            # 检查二级目录是否存在
            checking_protein_cmd = f'ls {result_dlg}/{result_name_hat}\ {time_str_file}'
            checking_protein_out = subprocess.check_output(checking_protein_cmd, shell=True, stderr=subprocess.STDOUT, text=True)
            if protein_name in checking_protein_out: # 如果二级目录存在
                print(f"\033[92m  {lang_dock_have_dlg}\033[96m{protein_name}\033[0m")  # print result catalog
            else: # 如果二级目录不存在
                print(f"\033[92m    {lang_dock_mk_dlg}\033[0m")
                os.system(f'mkdir {result_dlg}/{result_name_hat}\ {time_str_file}/{protein_name}') #make result file
                print(f"\033[92m    {lang_dock_mk_dlg_suc}\033[96m{protein_name}\033[0m")  # print result catalog
        else: # 如果蛋白质被注释
            no_work_protein = protein_name.replace("#", "")
            print(f"\033[92m    {lang_dock_pro_commend}\033[96m{no_work_protein}\033[0m")
    # # Make result_complex/protein
    # for protein_name in os.listdir(protein_list_path): # make protein list
    #     # checking do .result_dlg have protein ?
    #     checking_complex_cmd = f'ls {result_complex}'
    #     checking_protein_out = subprocess.check_output(checking_complex_cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    #     if protein_name in checking_protein_out:
    #         print(f'\033[92m  have result_complex catalog > \033[96m{protein_name}\033[0m')  # print result catalog
    #     else:
    #         print(f'\033[92m<<<===============[ 正在进行目录补全 > 对接复合体目录 ]===============>>>\033[0m')
    #         print(f'\033[92m<<<======[ Performing catalog completion > result_complex ]======>>>\033[0m')
    #         os.system(f'mkdir {result_complex}/{protein_name}') #make result file
    #         print(f'\033[92m  make result_complex catalog > \033[96m{protein_name}\033[0m')  # print result catalog
    print(f"\033[92m{lang_dock_workfile_end}\033[0m") # 打印工作目录校验通过信息

    # Set result csv file
    # 初始化csv文件和结果列表
    print(f"\n\033[92m{lang_dock_csv_began}\033[0m")
    csv_name = f'{result_name_hat} {time_str}.csv' # 定义结果excel的名称
    csv_path = os.path.join(f'{result_csv}/', csv_name) # important! use save as docking cent(Best_Low_Energy)!
    # make protein list (line)
    # 将蛋白质名称存储到一个列表
    first_line_list = ['Ligand_name'] # 初始化标题名称
    for protein_name in os.listdir(protein_list_path):
        no_work_pro_csv = '#' in protein_name  # the protein to_work or no_work ?
        if no_work_pro_csv != True:
            first_line_list.append(protein_name)
    # make ligand list (column)
    # 将小分子名称存储到一个列表
    first_column_list = ['Ligand_name']
    for pdbqt_name in os.listdir(ligand_pdbqt_path):
        no_work_lig_csv = '#' in pdbqt_name  # the ligand to_work or no_work ?
        if no_work_lig_csv != True:
            # abstracting ligand name
            start = pdbqt_name.rfind('/')
            end = pdbqt_name.rfind('.')
            ligand_name = pdbqt_name[start + 1:end]
            first_column_list.append(ligand_name)
    # make csv_data_2d
    # 创建一个二维列表
    num_rows = len(first_column_list) # 将小分子列创建为一个列表
    num_cols = len(first_line_list) # 将蛋白质行创建为一个列表
    csv_data_2d = [[None] * num_cols for _ in range(num_rows)] # 获取蛋白质和小分子的数量数据，并以此为基础创建二维列表
    if num_cols > 1:
        csv_data_2d[0][1:] = first_line_list[1:] # 从第一行第二列开始横向填充蛋白质名称列表到二维列表
    for i in range(1, num_rows):
        csv_data_2d[i][0] = first_column_list[i] # 从第一列开始纵向填充小分子名称列表到二维列表，小分子列表的第一个不填
    csv_data_2d[0][0] = first_line_list[0] # 填充标题名称
    print(f"\033[92m{lang_dock_csv_end}\033[0m") # 打印csv模块初始化完毕与二维数组就绪信息

    # Make AutoDock-GPU docking
    # 运行AD-GPU主程序
    print(f"\n\033[92m{lang_dock_main_began}\033[0m")
    # matrix dot product
    for protein_name in os.listdir(protein_list_path): # make protein list 获取蛋白质名称到列表
        no_work_pro = '#' in protein_name  # the protein to_work or no_work ?  判断蛋白质是否参与对接
        if no_work_pro != True:
            for pdbqt_name in os.listdir(ligand_pdbqt_path): # make ligand list 获取小分子名称到列表
                no_work_pdbqt = '#' in pdbqt_name  # the pdbqt to_work or no_work ? 判断小分子是否参与对接
                if no_work_pdbqt != True:
                    # docking
                    if pdbqt_name.endswith('.pdbqt'): # checking file type 判断小分子文件类型
                        # define protein.maps.fld and ligand.pdbqt path
                        # 定义蛋白质网格文件与小分子文件路径
                        # find and define protein.maps.fld path
                        # 寻找蛋白质网格文件路径
                        for protein_maps_fld_find in os.listdir(f'{protein_list_path}/{protein_name}'): # 获取网格文件列表
                            if protein_maps_fld_find.endswith('.maps.fld'):
                                protein_maps_fld = protein_maps_fld_find # 寻找蛋白质网格文件所在目录
                                protein_path = os.path.join(protein_list_path, protein_name, protein_maps_fld) # define protein.maps.fld path 设置蛋白质网格文件路径
                                pdbqt_path = os.path.join(ligand_pdbqt_path, pdbqt_name) # define ligand.pdbqt path  设置小分子路径
                                # abstracting ligand name
                                # 提取小分子名称
                                start = pdbqt_path.rfind('/')
                                end = pdbqt_path.rfind('.')
                                ligand_name = pdbqt_path[start + 1:end]
                                dock_number += 1  # give ligand number 对接计数器+1，用于该模块运行完毕后的总结输出
                                print(f"{lang_dock_mess.format(dock_number, protein_name ,ligand_name)}\033[0m")
                                result_path = f'{result_dlg}/{result_name_hat} {time_str}/{protein_name}/'
                                if len(seed) == 0:
                                    dock_cmd = [AD_GPU,
                                                '--ffile', protein_path,
                                                '--lfile', pdbqt_path,
                                                '-nrun', nrun,
                                                '-resnam', result_path]
                                else:
                                    dock_cmd = [AD_GPU,
                                                '--ffile', protein_path,
                                                '--lfile', pdbqt_path,
                                                '-nrun', nrun,
                                                '-resnam', result_path,
                                                '-seed',seed]
                                dock_out = subprocess.check_output(dock_cmd, shell=False, stderr=subprocess.STDOUT, text=True)
                                result_energy = r'([-+]?[0-9]*\.?[0-9]+)\s*kcal/mol'  # fund *kcal/mol 提取自由能
                                # fund all *kcal/mol
                                result_class = re.findall(result_energy, dock_out)  # all docking energy result 整理所有输出
                                if result_class:
                                    # abstracting(extracted) last
                                    energy = result_class[-1] # 寻找最优构象自由能
                                    energy_unit = f'{energy} kcal/mol' # 添加量纲
                                    print(f"    \033[92m{lang_dock_suc.format(protein_name, ligand_name, energy)}\033[0m")  # print docking result
                                    # abstracting dlg and out put complex pdbqt
                                    # 提取最优构象分子并输出复合物3D结构
                                    dlg_path = f'{result_dlg}/{result_name_hat} {time_str}/{protein_name}/{ligand_name}.dlg' # find dlg file 寻找dlg文件所在路径
                                    ER_bast = fr'Estimated Free Energy of Binding\s*=\s*{energy}\s*kcal/mol(.*?)(?=DOCKED: ENDMDL)' # Expression for find bast low energy data 提取dlg文件中最优构象的相关内容
                                    with open(dlg_path, "r", encoding="utf-8") as f_dlg:
                                        dlg_data = f_dlg.read()
                                    match = re.search(ER_bast, dlg_data, re.DOTALL)
                                    extracted = match.group(1)
                                    ligand_pdbqt_data = extracted.replace("DOCKED: ", "") # this complex.pdbqt in ligand part 删除每行开头的DOCK:
                                    # find and read protein.pdbqt
                                    # 寻找蛋白质文件
                                    for pro_f in os.listdir(f'{protein_list_path}/{protein_name}/'):
                                        if pro_f.endswith('.pdbqt'):
                                            protein_pdbqt_name = pro_f
                                    with open(f'{protein_list_path}/{protein_name}/{protein_pdbqt_name}', "r", encoding="utf-8") as protein_pdbqt:
                                        protein_pdbqt_data = protein_pdbqt.read() # 读取蛋白质文件的全部内容
                                    complex_data = protein_pdbqt_data + "\n" + ligand_pdbqt_data # 将蛋白质文件与小分子最优构象组合
                                    with open(f'{result_complex}/{result_name_hat} {time_str}/{protein_name}-{ligand_name}-complex.pdbqt', "w", encoding="utf-8") as fout: # 定义复合物文件路径和名称
                                        fout.write(complex_data) # 输出复合物的pdbqt文件
                                    print(f"\033[92m    {lang_dock_complex_suc}\033[0m")
                                    # writer energy to csv
                                    # 将能量数据准备写入csv文件
                                    # read csv_data_2d git positioning
                                    # 获取csv文件对应二维列表的相关信息
                                    x_coordinates = first_line_list.index(protein_name) # 获取蛋白质所对应的列坐标
                                    y_coordinates = first_column_list.index(ligand_name) # 获取小分子所对应的行坐标
                                    csv_data_2d[y_coordinates][x_coordinates] = energy # writer energy to csv 将自由能数据写入对应坐标
                                else: # 若对接出现错误
                                    energy = "Not found"
                                    dock_err_number += 1 # 错误计数器+1，用于该模块运行完毕后的总结输出
                                    print(f"\033[31m{lang_dock_err.format(ligand_name, dock_out)}\033[0m")
                    elif '#' in pdbqt_name: # 如果文件被“#”注释则停止执行操作
                        break
                    else:
                        error_pdbqt_path = os.path.join(ligand_pdbqt_path, pdbqt_name)  # fund error file path 获取错误分子路径
                        error_pqbqt_name = error_pdbqt_path.rsplit('/', 1)[-1]  # set error file name 获取错误分子名称
                        dock_war_number += 1 # 错误计数器+1，用于该模块运行完毕后的总结输出
                        print(f"\033[33m    {lang_dock_war}\033[95m{error_pqbqt_name}\033[0m")  # print red error
                else: # 如果文件被“#”注释
                    no_work_txt = pdbqt_name.replace("#", "") # 获取被注释的文件名称
                    print(f"\033[92m    {lang_dock_pdbqt_commend}\033[95m{no_work_txt}\033[0m") # 打印注释信息
    print(f"\033[92m{lang_dock_main_end}\033[0m") # 打印对接主程序执行完毕信息

    # Energy result (csv_data_2d) writer to csv file
    # 将含有自由能结果的二维数组写入csv文件作为结果输出
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data_2d)
    return dock_number, dock_war_number, dock_err_number, csv_name # 将运行次数，错误数，警告数，结果csv文件名称打包为元组

if __name__ == '__main__':
    result = dock # 将元组作为函数的输出
    dock()

# # 输出总结信息
# print(f'\n\033[92m    {lang_dock_csv_suc} "{csv_name}"\033[0m')
# if dock_war_number + dock_err_number == 0: # 判断异常计数是否为0
#     print(f'\n\033[92m    {lang_dock_summary_suc.format(dock_number)}\033[0m') # 输出无异常结束语句
# else: # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
#     print(f'\n\033[91m{lang_dock_summary_failure.format(dock_number, dock_err_number, dock_war_number)}\033[0m')
