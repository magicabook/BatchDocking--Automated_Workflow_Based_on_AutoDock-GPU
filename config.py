### Batch_Docking--Automated_Workflow_Based_on_AutoDock-GPU .PROPERTIES file
# -*- coding: utf-8 -*-
import os
import re
import csv
import random
import datetime
import subprocess
import importlib
import traceback
import pandas as pd
ver = '1.6.1'

program_path = '/root'
work_path = '/root/test'

# Your python2 path
py2 = '/usr/bin/python2.7'
# Your AutoDock-GPU path
AD_GPU = '/root/AutoDock-GPU-1.6/bin/autodock_gpu_128wi'


# Your result file name
result_name_hat = ''
#Docking run number
nrun = '20'
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
protein_path = work_path + '/protein'
#.smi path
ligand_smi_path = work_path + '/ligand_smi'
# single.smi path
ligand_smi_single_path = work_path + '/ligand_smi_single'
# .pdb path
ligand_pdb_path = work_path + '/ligand_pdb'
# .pdbqt path
ligand_pdbqt_path = work_path + '/ligand_pdbqt'
# AutoDock-GPU run docking output for path
result_dlg_path = work_path + '/result_dlg'
# result csv path
result_csv_path = work_path + '/result_csv'
result_complex_path = work_path + '/result_complex'
# Your AutoDockTools about prepare_receptor4.py path
Grid = work_path + 'BatchDock-' + ver + '/prepare_ligand4.py'
ligand_tools = 'obabel'