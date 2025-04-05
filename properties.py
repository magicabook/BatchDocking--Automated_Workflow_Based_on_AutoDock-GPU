### Batch_Docking--Automated_Workflow_Based_on_AutoDock-GPU .PROPERTIES file
import os
import re
import csv
import datetime
import subprocess
import importlib

program_path = '/root/CPT'
ver = '1.3.3'
work_path = '/root/test'

# Your python2 path
py2 = '/usr/bin/python2.7'
# Your AutoDock-GPU path
AD_GPU = '/root/AutoDock-GPU-1.6/bin/autodock_gpu_128wi'
# Your AutoDockTools about prepare_receptor4.py path
Grid = '/root/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py'

# Your result file name
result_name_hat = 'test'
#Docking run number
nrun = '1'
# AutoDock-GPU seed
seed = ''

## Define and Set Your Work_Path and Basic Function

# Your Language
language = 'zh_cn'
module_name = f"language.{language}"
module = __import__(module_name, fromlist=["*"])
globals().update({k: getattr(module, k) for k in dir(module) if not k.startswith("__")})
# Your work path
path = subprocess.check_output('pwd',shell=False,stderr=subprocess.STDOUT,text=True).replace("\n", "")
# Protein .maps,fld path
protein_list_path = work_path + '/protein'
#.smi path
ligand_smi = work_path + '/ligand_smi'
# single.smi path
ligand_smi_single = work_path + '/ligand_smi_single'
# .pdb path
ligand_pdb = work_path + '/ligand_pdb'
# .pdbqt path
ligand_pdbqt_path = work_path + '/ligand_pdbqt'
# AutoDock-GPU run docking output for path
result_dlg = work_path + '/result_dlg'
# result csv path
result_csv = work_path + '/result_csv'
result_complex = work_path + '/result_complex'