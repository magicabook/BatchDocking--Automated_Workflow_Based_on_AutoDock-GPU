import os
import re
import csv
import numpy
import datetime
import subprocess

# Define and Set Your Work_Path and Basic Function
csv_name_hat = 'work1'
nrun = '100' #Docking run number
py2 = '/usr/bin/python2.7'
AD_GPU = '/root/AutoDock-GPU-1.6/bin/autodock_gpu_128wi' # AutoDock-GPU path
Grid = '/root/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py'
protein_list_path = '../protein/' # Protein .maps,fld path
ligand_smi = '../ligand_smi' #.smi path
ligand_smi_single = '../ligand_smi_single' # single.smi path
ligand_pdb = '../ligand_pdb' # .pdb path
ligand_pdbqt_path = '../ligand_pdbqt' # .pdbqt path
result_dlg = '../result_dlg/' # AutoDock-GPU run docking output for path
result_csv = "../result_csv/" # sult csv path
time_raw = datetime.datetime.now() # get system time to make file sign
time_str = time_raw.strftime('%Y-%m-%d %H-%M-%S') # change to str
ligand_number = 0 # give ligand a number , to save as csv

# Checking protein.maps.fld
for protein_name in os.listdir(protein_list_path): # make protein list
    if os.system(f'find {protein_list_path}{protein_name}/ -type f -name "*.maps.fld" | grep -q .;') != 0:
        print(f'\033[91mERROR: Not Find .maps.fld > {protein_name}\033[0m')

# Make result_dlg/protein
for protein_name in os.listdir(protein_list_path): # make protein list
    # checking do .result_dlg have protein ?
    checking_protein_cmd = f'ls {result_dlg}'
    checking_protein_out = subprocess.check_output(checking_protein_cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    if protein_name in checking_protein_out:
        print(f'\033[92m  have result catalog > {protein_name}\033[0m')  # print result catalog
    else:
        os.system(f'mkdir {result_dlg}{protein_name}') #make result file
        print(f'\033[92m  make result catalog > {protein_name}\033[0m')  # print result catalog

# Set result csv file
csv_name = f'[{csv_name_hat}] {time_str}.csv'
csv_path = os.path.join(result_csv, csv_name) # important! use save as docking cent(Best_Low_Energy)!
# make protein list (line)
first_line_list = ['Ligand_name']
for protein_name in os.listdir(protein_list_path):
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

# Make AutoDock-GPU docking
# matrix dot product
for protein_name in os.listdir(protein_list_path): # make protein list
    for pdbqt_name in os.listdir(ligand_pdbqt_path): # make ligand list
        # docking
        if pdbqt_name.endswith('.pdbqt'): # checking file type
            # define protein.maps.fld and ligand.pdbqt path
            # find and define protein.maps.fld path
            for protein_maps_fld_find in os.listdir(f'{protein_list_path}{protein_name}'):
                if protein_maps_fld_find.endswith('.maps.fld'):
                    protein_maps_fld = protein_maps_fld_find
                    protein_path = os.path.join(protein_list_path, protein_name, protein_maps_fld) # define protein.maps.fld path
                    pdbqt_path = os.path.join(ligand_pdbqt_path, pdbqt_name) # define ligand.pdbqt path
                    # abstracting ligand name
                    start = pdbqt_path.rfind('/')
                    end = pdbqt_path.rfind('.')
                    ligand_name = pdbqt_path[start + 1:end]
                    ligand_number += 1  # give ligand number
                    print(f'Docking proceece number : {ligand_number} Factor : {protein_name} and {ligand_name}')
                    result_path = f'{result_dlg}{protein_name}/'
                    dock_cmd = [AD_GPU,
                                '--ffile', protein_path,
                                '--lfile', pdbqt_path,
                                '-nrun', nrun,
                                '-resnam', result_path]
                    dock_out = subprocess.check_output(dock_cmd, shell=False, stderr=subprocess.STDOUT, text=True)
                    pattern = r'([-+]?[0-9]*\.?[0-9]+)\s*kcal/mol'  # fund *kcal/mol
                    # fund all *kcal/mol
                    result_class = re.findall(pattern, dock_out)  # all docking energy result
                    if result_class:
                        # abstracting(extracted) last
                        energy = result_class[-1]
                        energy_unit = f'{energy} kcal/mol'
                        print(f'\033[92m  {ligand_name} Doking {protein_name} Successful! > Bast_Low_Energy: {energy}\033[0m')  # print docking result
                        # writer energy to csv
                        # read csv_data_2d git positioning
                        x_coordinates = first_line_list.index(protein_name)
                        y_coordinates = first_column_list.index(ligand_name)
                        csv_data_2d[y_coordinates][x_coordinates] = energy # writer energy to csv
                    else:
                        energy = "Not found"
                        print(f'\033[91mERROR: docking Failure! Error Molecular > {ligand_name}\n vvvvv Pleace Read more Information! vvvvv \n<<<=====[Process out put:]=====>>>\n{dock_out}\033[0m')  # print red error
        else:
            error_pdbqt_path = os.path.join(ligand_pdbqt_path, ligand_name)  # fund error file list
            error_pqbqt_name = error_pdbqt_path.rsplit('/', 1)[-1]  # set error file name
            print('\033[93m' + '  WARNING: Pleace Clear Error Type File > ligand_pdbqt >' + error_pqbqt_name + '\033[0m')  # print red error
# Energy result (csv_data_2d) writer to csv file
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data_2d)
print(f'\033[92m  Energy result (csv_data_2d) writer to csv Successful! > {csv_name}\033[0m')