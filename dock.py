from properties import *

# Checking protein.maps.fld
print(f'\n\033[92m{lang_dock_workfile_began}\033[0m')
for protein_name in os.listdir(protein_list_path): # make protein list
    if os.system(f'find {protein_list_path}/{protein_name}/ -type f -name "*.maps.fld" | grep -q .;') != 0:
        error_number += 1
        print(f'\033[91m{lang_dock_fld_err}\033[96m{protein_name}\033[0m')
# Make result_complex/name_time
os.system(f'mkdir {result_complex}/{result_name_hat}\ {time_str_file}')
print(f'\033[92m    {lang_dock_complex}{result_name_hat} {time_str_file}\033[0m')
# Make result_dlg/name_time
os.system(f'mkdir {result_dlg}/{result_name_hat}\ {time_str_file}')
print(f'\033[92m    {lang_dock_dlg}{result_name_hat} {time_str_file}\033[0m')
# Make result_dlg/protein
for protein_name in os.listdir(protein_list_path): # make protein list
    no_work = '#' in protein_name # the protein to_work or no_work ?
    if no_work != True:
        # checking do .result_dlg have protein ?
        checking_protein_cmd = f'ls {result_dlg}/{result_name_hat}\ {time_str_file}'
        checking_protein_out = subprocess.check_output(checking_protein_cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        if protein_name in checking_protein_out:
            print(f'\033[92m  {lang_dock_have_dlg}\033[96m{protein_name}\033[0m')  # print result catalog
        else:
            print(f'\033[92m    {lang_dock_mk_dlg}\033[0m')
            os.system(f'mkdir {result_dlg}/{result_name_hat}\ {time_str_file}/{protein_name}') #make result file
            print(f'\033[92m    {lang_dock_mk_dlg_suc}\033[96m{protein_name}\033[0m')  # print result catalog
    else:
        no_work_protein = protein_name.replace("#", "")
        print(f'\033[92m    {lang_dock_pro_commend}\033[96m{no_work_protein}\033[0m')
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
print(f'\033[92m{lang_dock_workfile_end}\033[0m')

# Set result csv file
print(f'\n\033[92m{lang_dock_csv_began}\033[0m')
csv_name = f'{result_name_hat} {time_str}.csv'
csv_path = os.path.join(f'{result_csv}/', csv_name) # important! use save as docking cent(Best_Low_Energy)!
# make protein list (line)
first_line_list = ['Ligand_name']
for protein_name in os.listdir(protein_list_path):
    no_work = '#' in protein_name  # the protein to_work or no_work ?
    if no_work != True:
        first_line_list.append(protein_name)
# make ligand list (column)
first_column_list = ['Ligand_name']
for pdbqt_name in os.listdir(ligand_pdbqt_path):
    # abstracting ligand name
    start = pdbqt_name.rfind('/')
    end = pdbqt_name.rfind('.')
    ligand_name = pdbqt_name[start + 1:end]
    first_column_list.append(ligand_name)
# make csv_data_2d
num_rows = len(first_column_list)
num_cols = len(first_line_list)
csv_data_2d = [[None] * num_cols for _ in range(num_rows)]
if num_cols > 1:
    csv_data_2d[0][1:] = first_line_list[1:]
for i in range(1, num_rows):
    csv_data_2d[i][0] = first_column_list[i]
csv_data_2d[0][0] = first_line_list[0]
print(f'\033[92m{lang_dock_csv_end}\033[0m')

# Make AutoDock-GPU docking
print(f'\n\033[92m{lang_dock_main_began}\033[0m')
# matrix dot product
for protein_name in os.listdir(protein_list_path): # make protein list
    no_work = '#' in protein_name  # the protein to_work or no_work ?
    if no_work != True:
        for pdbqt_name in os.listdir(ligand_pdbqt_path): # make ligand list
            # docking
            if pdbqt_name.endswith('.pdbqt'): # checking file type
                # define protein.maps.fld and ligand.pdbqt path
                # find and define protein.maps.fld path
                for protein_maps_fld_find in os.listdir(f'{protein_list_path}/{protein_name}'):
                    if protein_maps_fld_find.endswith('.maps.fld'):
                        protein_maps_fld = protein_maps_fld_find
                        protein_path = os.path.join(protein_list_path, protein_name, protein_maps_fld) # define protein.maps.fld path
                        pdbqt_path = os.path.join(ligand_pdbqt_path, pdbqt_name) # define ligand.pdbqt path
                        # abstracting ligand name
                        start = pdbqt_path.rfind('/')
                        end = pdbqt_path.rfind('.')
                        ligand_name = pdbqt_path[start + 1:end]
                        dock_number += 1  # give ligand number
                        print(f'{lang_dock_mess1}{dock_number}{lang_dock_mess2}\033[96m{protein_name}\033[0m{lang_dock_mess3}\033[95m{ligand_name}\033[0m')
                        result_path = f'{result_dlg}/{result_name_hat} {time_str}/{protein_name}/'
                        dock_cmd = [AD_GPU,
                                    '--ffile', protein_path,
                                    '--lfile', pdbqt_path,
                                    '-nrun', nrun,
                                    '-resnam', result_path]
                        dock_out = subprocess.check_output(dock_cmd, shell=False, stderr=subprocess.STDOUT, text=True)
                        result_energy = r'([-+]?[0-9]*\.?[0-9]+)\s*kcal/mol'  # fund *kcal/mol
                        # fund all *kcal/mol
                        result_class = re.findall(result_energy, dock_out)  # all docking energy result
                        if result_class:
                            # abstracting(extracted) last
                            energy = result_class[-1]
                            energy_unit = f'{energy} kcal/mol'
                            print(f'    \033[95m{ligand_name} \033[92mDoking \033[96m{protein_name} \033[92mSuccessful! > Bast_Low_Energy: {energy}\033[0m')  # print docking result
                            # abstracting dlg and out put complex pdbqt
                            dlg_path = f'{result_dlg}/{result_name_hat} {time_str}/{protein_name}/{ligand_name}.dlg' # find dlg file
                            ER_bast = fr"Estimated Free Energy of Binding\s*=\s*{energy}\s*kcal/mol(.*?)(?=DOCKED: ENDMDL)" # Expression for find bast low energy data
                            with open(dlg_path, "r", encoding="utf-8") as f_dlg:
                                dlg_data = f_dlg.read()
                            match = re.search(ER_bast, dlg_data, re.DOTALL)
                            extracted = match.group(1)
                            ligand_pdbqt_data = extracted.replace("DOCKED: ", "") # this complex.pdbqt in ligand part
                            # find and read protein.pdbqt
                            for f in os.listdir(f'{protein_list_path}/{protein_name}/'):
                                if f.endswith('.pdbqt'):
                                    protein_pdbqt_name = f
                            with open(f'{protein_list_path}/{protein_name}/{protein_pdbqt_name}', "r", encoding="utf-8") as protein_pdbqt:
                                protein_pdbqt_data = protein_pdbqt.read()
                            complex_data = protein_pdbqt_data + "\n" + ligand_pdbqt_data
                            with open(f'{result_complex}/{result_name_hat} {time_str}/{protein_name}-{ligand_name}-complex.pdbqt', "w", encoding="utf-8") as fout:
                                fout.write(complex_data)
                            print(f'\033[92m    complex file make Successful!\033[0m')
                            # writer energy to csv
                            # read csv_data_2d git positioning
                            x_coordinates = first_line_list.index(protein_name)
                            y_coordinates = first_column_list.index(ligand_name)
                            csv_data_2d[y_coordinates][x_coordinates] = energy # writer energy to csv
                        else:
                            energy = "Not found"
                            error_number += 1
                            print(f'\033[91m错误：发生一次对接失败！问题分子 \033[95m{ligand_name}\n \033[91mvvvvv 请根据下列错误信息进行整改！ vvvvv \n<<<=====[ AutoDock-GPU程序输出的错误报告: ]=====>>>\n{dock_out}\n^^^^^ 请根据以上错误信息进行整改！ ^^^^^ \033[0m')
                            print(f'\033[91mERROR: docking Failure! Error Molecular > \033[95m{ligand_name}\n \033[91mvvvvv Pleace Read more Information! vvvvv \n<<<=====[AutoDock-GPU Process out put:]=====>>>\n{dock_out}\n^^^^^ Pleace Read more Information! ^^^^^ \033[0m')  # print red error
        else:
            error_pdbqt_path = os.path.join(ligand_pdbqt_path, pdbqt_name)  # fund error file list
            error_pqbqt_name = error_pdbqt_path.rsplit('/', 1)[-1]  # set error file name
            warning_number += 1
            print(f'\033[93m    WARNING: Pleace Clear Error Type File > ligand_pdbqt > \033[95m{error_pqbqt_name}\033[0m')  # print red error
print(f'\033[92m<<<===================[ 分子对接主程序运行完毕 ]=====================>>>\033[0m')
print(f'\033[92m<<<=======[ Molecular docking main program has completed. ]======>>>\033[0m')

# Energy result (csv_data_2d) writer to csv file
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data_2d)
print(f'\n\033[92m    所有最优构象的自由能提取并写入Excel成功！文件名称为 {csv_name}\033[0m')
print(f'\033[92m    Energy result writer to csv Successful! > {csv_name}\033[0m')
if error_number+warning_number == 0:
    print(f'\n\033[92m    本次工作共运行{dock_number}次对接，产生0个错误与0个警告\n    圆满完成预期任务！\033[0m')
    print(f'\033[92m    In this operation, a total of {dock_number} docking runs were performed, resulting in 0 errors and 0 warnings\nsuccessfully completing the expected tasks!\033[0m')
else:
    print(f'\n\033[91m本次工作共运行{dock_number}次对接，产生{error_number}个错误与{warning_number}个警告\n你可以查看终端中的红色错误信息与黄色警告信息以了解问题是如何发生的\n如果需要寻求帮助，请把终端里的相关输出提供给对方，而不是发送这个窗口的照片或者截图……\033[0m')
    print(f'\033[91mIn this operation, a total of {dock_number} docking runs were performed, resulting in {error_number} errors and {warning_number} warnings\nYou can check the red error messages and yellow warning messages in the terminal to understand how the issues occurred\nIf you need assistance, please provide the relevant terminal output to others, instead of sending photos or screenshots of the window...\033[0m')