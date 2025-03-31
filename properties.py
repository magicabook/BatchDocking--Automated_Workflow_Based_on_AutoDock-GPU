### Batch_Docking--Automated_Workflow_Based_on_AutoDock-GPU .PROPERTIES file
import os
import re
import csv
import datetime
import subprocess
import importlib

## Define and Set Your Work_Path and Basic Function

# Your Language
language = 'zh_cn'
module_name = f"language.{language}"
module = __import__(module_name, fromlist=["*"])
globals().update({k: getattr(module, k) for k in dir(module) if not k.startswith("__")})
# Your result file name
result_name_hat = 'work'
#Docking run number
nrun = '1'
seed = ''
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