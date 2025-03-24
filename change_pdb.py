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
result_csv = '../result_csv' # result csv path
result_complex = '../result_complex'
time_raw = datetime.datetime.now() # get system time to make file sign
time_str = time_raw.strftime('%Y-%m-%d %H-%M-%S') # change to str
ligand_number = 0 # give ligand a number , to save as csv
error_number = 0
warning_number = 0

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
            error_number += 1
            error_pdb_path = os.path.join(ligand_pdb, file)  # fund error file list
            error_pdb_name = error_pdb_path.rsplit('/', 1)[-1]  # set error file name
            print(f'\033[91mERROR: {error_pdb_name} Change to PDBQT and Setting Ligand Failure!\n  Pleace Checking > {error_pdb_name}.pdb\n<<<=====[Process out put:]=====>>>\n{change_pdbqt_out}\033[0m')
    else:
        warning_number += 1
        error_pdb_path = os.path.join(ligand_pdbqt_path, file)  # fund error file list
        error_pdb_name = error_pdb_path.rsplit('/', 1)[-1]  # set error file name
        print('\033[93m' + '  WARNING: Pleace Clear Error Type File > ligand_pdb > ' + error_pdb_name + '\033[0m')  # print red error