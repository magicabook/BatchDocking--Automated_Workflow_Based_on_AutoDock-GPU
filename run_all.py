import os
import re
import csv
import datetime
import subprocess

# Define and Set Your Work_Path and Basic Function
csv_name_hat = 'test' # Your result file name
nrun = '1' #Docking run number
py2 = '/usr/bin/python2.7'
AD_GPU = '/root/AutoDock-GPU-1.6/bin/autodock_gpu_128wi' # AutoDock-GPU path
Grid = '/root/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py'
protein_list_path = '../protein/' # Protein .maps,fld path
ligand_smi = '../ligand_smi' #.smi path
ligand_smi_single = '../ligand_smi_single' # single.smi path
ligand_pdb = '../ligand_pdb' # .pdb path
ligand_pdbqt_path = '../ligand_pdbqt' # .pdbqt path
result_dlg = '../result_dlg' # AutoDock-GPU run docking output for path
result_csv = '../result_csv' # sult csv path
result_complex = '../result_complex'
time_raw = datetime.datetime.now() # get system time to make file sign
time_str = time_raw.strftime('%Y-%m-%d %H-%M-%S') # change to str
ligand_number = 0 # give ligand a number , to save as csv
error_number = 0
warning_number = 0

# Change to single_file
for file in os.listdir(ligand_smi):
    if file.endswith('.txt'):  # checking file type
        # read smi
        smi_path = os.path.join(ligand_smi, file)
        if os.path.isfile(smi_path):
            print(f"\033[92m--- Reading {smi_path} ---\033[0m")
            # line read
            with open(smi_path, "r", encoding="utf-8") as f:
                for line in f:
                    smi_all = (line.strip()) # delete \n
                    # abstracting structure and name
                    parts = smi_all.split()
                    smi_str, smi_name = parts[0], parts[1] # abstracting and set
                    # make file and rename
                    out_smi =  os.path.join(ligand_smi_single, smi_name + ".smi") # define out_file name
                    with open(out_smi,'w') as f: # define out_fine content
                        f.write(smi_str)
                    print(f'\033[92m'f"  make {smi_name} \033[0m")
    else:
        error_smi_path = os.path.join(ligand_smi, file)  # fund error file list
        error_smi_name = error_smi_path.rsplit('/', 1)[-1]  # set error file name
        print('\033[93m' + '  WARNING: Pleace Clear Error Type File > ligand_smi_single > ' + error_smi_name + '\033[0m')  # print red error

# Make ligand_single.SMI change to ligand.PDB
for file in os.listdir(ligand_smi_single):
        if file.endswith('.smi'): # checking file type
            smi_single_path = os.path.join(ligand_smi_single, file) # fund file list
            ligand_smi_single_name = smi_single_path.rsplit('/', 1)[-1]  # abstracting smi file name
            # set pdb file name
            start = ligand_smi_single_name.rfind('/')
            end = ligand_smi_single_name.rfind('.')
            ligand_pdb_name = ligand_smi_single_name[start + 1:end]
            obabel_smi_cmd = ['obabel',
                            '-ismi', smi_single_path,
                            '-opdb',
                            '-O', f"{ligand_pdb}/{ligand_pdb_name}.pdb",
                            '-h',
                            '--gen3D',
                            '--partialcharge', 'gasteiger',
                            '--minimize',
                            '--ff', 'gaff']
            obabel_out = subprocess.check_output(obabel_smi_cmd,shell=False,stderr=subprocess.STDOUT,text=True)
            os.system('killall -9 obabel')
            if (obabel_out.find('1 molecule converted') >= 0):
                print('\033[92m' + '  Successful change to .PDB > ' + ligand_smi_single_name + '\033[0m') # print green information
            else:
                error_smi_single_path = os.path.join(ligand_smi_single, file)  # fund error file list
                error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name
                print(f'\033[91mERROR: {error_smi_single_name} Change to PDB Failure!\n  Pleace Checking > {error_smi_single_name}\n<<<=====[Process out put:]=====>>>\n{obabel_out}\033[0m')
        else:
            error_smi_single_path = os.path.join(ligand_smi_single, file)  # fund error file list
            error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name
            print('\033[93m' + '  WARNING: Pleace Clear Error Type File > ligand_smi_single > ' + error_smi_single_name + '\033[0m') # print red error

# Make ligand.PDB change to ligand.PDBQT and setting ligand
for file in os.listdir(ligand_pdb):
    if file.endswith('.pdb'):  # checking file type
        pdb_path = os.path.join(ligand_pdb, file)  # fund file list
        ligand_pdbqt_name = pdb_path.rsplit('/', 1)[-1]  # set pdbqt file name
        change_pdbqt_cmd = [py2, Grid,
                            '-r', pdb_path,
                            '-o', f'{ligand_pdbqt_path}/{ligand_pdbqt_name}qt']
        change_pdbqt_out = subprocess.check_output(change_pdbqt_cmd,shell=False,stderr=subprocess.STDOUT,text=True)
        if (len(change_pdbqt_out) < 1):
            print('\033[92m' + '  Successful change to .PDBQT > ' + ligand_pdbqt_name + '\033[0m')  # print green information
        else:
            error_pdb_path = os.path.join(ligand_pdb, file)  # fund error file list
            error_pdb_name = error_pdb_path.rsplit('/', 1)[-1]  # set error file name
            print(f'\033[91mERROR: {error_pdb_name} Change to PDBQT and Setting Ligand Failure!\n  Pleace Checking > {error_pdb_name}.pdb\n<<<=====[Process out put:]=====>>>\n{change_pdbqt_out}\033[0m')
    else:
        error_pdb_path = os.path.join(ligand_pdbqt_path, file)  # fund error file list
        error_pdb_name = error_pdb_path.rsplit('/', 1)[-1]  # set error file name
        print('\033[93m' + '  WARNING: Pleace Clear Error Type File > ligand_pdb > ' + error_pdb_name + '\033[0m')  # print red error

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
        print(f'\033[92m  have result catalog > {protein_name}[0m')  # print result catalog
    else:
        os.system(f'mkdir {result_dlg}{protein_name}') #make result file
        print(f'\033[92m  make result catalog > {protein_name}[0m')  # print result catalog

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