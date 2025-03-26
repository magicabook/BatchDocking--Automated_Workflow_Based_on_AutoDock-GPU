from properties import *

# Checking protein.maps.fld
print(f'\n\033[92m{lang_dock_workfile_began}\033[0m')
for protein_name in os.listdir(protein_list_path): # make protein list
    if os.system(f'find {protein_list_path}/{protein_name}/ -type f -name "*.maps.fld" | grep -q .;') != 0:
        if '#' in protein_name:
            break
        else:
            error_number += 1
            print(f'\033[91m{lang_dock_fld_err}\033[96m{protein_name}\033[0m')
# Make result_complex/name_time
os.system(f'mkdir {result_complex}/{result_name_hat}\ {time_str_file}')
print(f'\033[92m    {lang_dock_complex} "{result_name_hat} {time_str}"\033[0m')
# Make result_dlg/name_time
os.system(f'mkdir {result_dlg}/{result_name_hat}\ {time_str_file}')
print(f'\033[92m    {lang_dock_dlg} "{result_name_hat} {time_str}"\033[0m')
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
    no_work_pro = '#' in protein_name  # the protein to_work or no_work ?
    if no_work_pro != True:
        for pdbqt_name in os.listdir(ligand_pdbqt_path): # make ligand list
            no_work_pdbqt = '#' in pdbqt_name  # the pdbqt to_work or no_work ?
            if no_work_pdbqt != True:
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
                            print(f'{lang_dock_mess1}{dock_number}{lang_dock_mess2} \033[96m{protein_name} \033[0m{lang_dock_mess3} \033[95m{ligand_name}\033[0m')
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
                                print(f'    \033[96m{protein_name} \033[92m{lang_dock_suc1} \033[95m{ligand_name} \033[92m{lang_dock_suc2}{energy}\033[0m')  # print docking result
                                # abstracting dlg and out put complex pdbqt
                                dlg_path = f'{result_dlg}/{result_name_hat} {time_str}/{protein_name}/{ligand_name}.dlg' # find dlg file
                                ER_bast = fr'Estimated Free Energy of Binding\s*=\s*{energy}\s*kcal/mol(.*?)(?=DOCKED: ENDMDL)' # Expression for find bast low energy data
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
                                print(f'\033[92m    {lang_dock_complex_suc}\033[0m')
                                # writer energy to csv
                                # read csv_data_2d git positioning
                                x_coordinates = first_line_list.index(protein_name)
                                y_coordinates = first_column_list.index(ligand_name)
                                csv_data_2d[y_coordinates][x_coordinates] = energy # writer energy to csv
                            else:
                                energy = "Not found"
                                error_number += 1
                                print(f'\033[91m{lang_dock_err1} \033[95m{ligand_name}\n \033[91m{lang_dock_err2}\n{dock_out}\n{lang_dock_err3} \033[0m')
                elif '#' in pdbqt_name:
                    break
                else:
                    error_pdbqt_path = os.path.join(ligand_pdbqt_path, pdbqt_name)  # fund error file list
                    error_pqbqt_name = error_pdbqt_path.rsplit('/', 1)[-1]  # set error file name
                    warning_number += 1
                    print(f'\033[93m    {lang_dock_war}\033[95m{error_pqbqt_name}\033[0m')  # print red error
            else:
                no_work_txt = pdbqt_name.replace("#", "")
                print(f'\033[92m    {lang_dock_pdbqt_commend}\033[95m{no_work_txt}\033[0m')
print(f'\033[92m{lang_dock_main_end}\033[0m')

# Energy result (csv_data_2d) writer to csv file
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data_2d)
print(f'\n\033[92m    {lang_dock_csv_suc} "{csv_name}"\033[0m')
if error_number+warning_number == 0:
    print(f'\n\033[92m    {lang_dock_summary_suc1} {dock_number} {lang_dock_summary_suc2}\033[0m')
else:
    print(f'\n\033[91m{lang_dock_summary_failure1} {dock_number} {lang_dock_summary_failure2} {error_number} {lang_dock_summary_failure3} {warning_number} {lang_dock_summary_failure4}\033[0m')
