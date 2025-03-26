### Batch_Docking--Automated_Workflow_Based_on_AutoDock-GPU .PROPERTIES file
import os
import re
import csv
import datetime
import subprocess
from zh_cn import *
## Define and Set Your Work_Path and Basic Function

# Your result file name
result_name_hat = 'test'
#Docking run number
nrun = '1'
py2 = '/usr/bin/python2.7'
# AutoDock-GPU path
AD_GPU = '/root/AutoDock-GPU-1.6/bin/autodock_gpu_128wi'
Grid = '/root/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py'
# Protein .maps,fld path
protein_list_path = '../protein'
#.smi path
ligand_smi = '../ligand_smi'
# single.smi path
ligand_smi_single = '../ligand_smi_single'
# .pdb path
ligand_pdb = '../ligand_pdb'
# .pdbqt path
ligand_pdbqt_path = '../ligand_pdbqt'
# AutoDock-GPU run docking output for path
result_dlg = '../result_dlg'
# result csv path
result_csv = '../result_csv'
result_complex = '../result_complex'
# get system time to make file sign
time_raw = datetime.datetime.now()
# change to str
time_str = time_raw.strftime('%Y-%m-%d %H-%M-%S')
time_str_file = time_raw.strftime('%Y-%m-%d\ %H-%M-%S')
# give ligand a number , to save as csv
smi_number = 0
smi_war_number = 0
smi_err_number = 0
pdb_number = 0
pdb_war_number = 0
pdb_err_number = 0
pdbqt_number = 0
pdbqt_war_number = 0
pdbqt_err_number = 0
dock_number = 0
dock_war_number = 0
dock_err_number = 0
error_number = smi_err_number + pdb_err_number + pdbqt_err_number + dock_err_number
warning_number = smi_war_number + pdb_war_number + pdbqt_war_number +dock_war_number