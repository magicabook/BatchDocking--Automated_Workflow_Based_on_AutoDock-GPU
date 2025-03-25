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
protein_list_path = '../protein' # Protein .maps,fld path
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

print(f'\n\033[92m<<<=====================[ 正在拆分小分子输入文件 ]====================>>>\033[0m')
print(f'\033[92m<<<============[ Splitting small molecule input file ]============>>>\033[0m')
# Change to single_file
for file in os.listdir(ligand_smi):
    if file.endswith('.txt'):  # checking file type
        # read smi
        smi_path = os.path.join(ligand_smi, file)
        if os.path.isfile(smi_path):
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
        warning_number += 1
        error_smi_path = os.path.join(ligand_smi, file)  # fund error file list
        error_smi_name = error_smi_path.rsplit('/', 1)[-1]  # set error file name
        print('\033[93m' + '  WARNING: Pleace Clear Error Type File > ligand_smi_single > ' + error_smi_name + '\033[0m')  # print red error
print(f'\033[92m<<<=======================[ 输入文件拆分完成 ]=======================>>>\033[0m')
print(f'\033[92m<<<================[ Input file split completed ]=================>>>\033[0m')

print(f'\n\033[92m<<<===================[ 正在转换小分子为.PDB格式 ]===================>>>\033[0m')
print(f'\033[92m<<<=========[ Converting small molecules to .PDB format ]=========>>>\033[0m')
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
            #print(obabel_smi_cmd)
            obabel_out = subprocess.check_output(obabel_smi_cmd,shell=False,stderr=subprocess.STDOUT,text=True)
            os.system('killall -9 obabel')
            if (obabel_out.find('1 molecule converted') >= 0):
                print('\033[92m' + '  Successful change to .PDB > ' + ligand_smi_single_name + '\033[0m') # print green information
            else:
                error_number += 1
                error_smi_single_path = os.path.join(ligand_smi_single, file)  # fund error file list
                error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name
                print(f'\033[91mERROR: {error_smi_single_name} Change to PDB Failure!\n  Pleace Checking > {error_smi_single_name}\n<<<=====[Process out put:]=====>>>\n{obabel_out}\033[0m')
        else:
            warning_number += 1
            error_smi_single_path = os.path.join(ligand_smi_single, file)  # fund error file list
            error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name
            print('\033[93m' + '  WARNING: Pleace Clear Error Type File > ligand_smi_single > ' + error_smi_single_name + '\033[0m') # print red error
print(f'\033[92m<<<=================[ 已将小分子全部转换为.PDB格式 ]==================>>>\033[0m')
print(f'\033[92m<<<=========[ Small molecules converted to .PDB format. ]=========>>>\033[0m')