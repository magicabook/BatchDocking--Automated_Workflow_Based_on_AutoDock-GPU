# -*- coding: utf-8 -*-
### 这是BatchDock的配置文件
### This Batch_Docking .configure file



### 导入运行库
### Import Runtime Library
import os
import re
import csv
import random
import shutil
import datetime
import subprocess
import importlib
import traceback
ver = '1.7.2'



### ！！！重要设置！！！【无法在软件中更改】
### !!! IMPORTANT SETTINGS !!! 【Cannot be changed in the software】
# 这里是BatchDock的父目录，若您的BatchDock在/home/user1/Batchdock，则修改为program_path = '/home/user1/'
# BatchDock parent directory (e.g., if BatchDock is at /home/user1/Batchdock, set: program_path = '/home/user1/')
program_path = '/root'
# 这里是BatchDock的工作目录，由于工作过程中产生的文件较多，我们建议您新建一个目录，例如mkdir /home/user1/docking_test。此时则修改为work_path = '/home/user1/docking_test'
# Working directory (create new directory, e.g.: mkdir /home/user1/docking_test → work_path = '/home/user1/docking_test')
work_path = '/root/test'
# 这里需要修改为您的Python2路径，由于AutoDockTools还停留在Python2，因此需要您提供Python2运行环境
# Python2 path (required for AutoDockTools)
py2 = '/usr/bin/python2.7'
# 这里需要将第一个？修改为您的AutoDock-GPU程序所在路径，第二个？修改为您自己编译后的可执行文件名称
# AutoDock-GPU path (replace first ? with path, second ? with compiled executable name)
AD_GPU = '/root/AutoDock-GPU-1.6/bin/autodock_gpu_128wi'



### 一般设置【可在软件中更改】
### General Settings 【Can be changed in the software】
# Your Language
language = 'zh_cn'
# OpenBabel Molecular Mechanics and Force Fields
fields = 'gaff'
# Whether to output .mol2 files for molecular dynamics simulation
out_mol2 = 'false'
# Docking run number
nrun = '20'
# AutoDock-GPU seed
seed = ''
# Show docking details
print_details = 'false'
# Your result file name
result_name_hat = ''
# Delete old ligand file
delete = 'true'



### 定义基础路径与功能，请不要更改！！！
### Base Path and Functionality Definition 【!!!DO NOT CHANGE!!!】
module_name = f"language.{language}"
module = __import__(module_name, fromlist=["*"])
globals().update({k: getattr(module, k) for k in dir(module) if not k.startswith("__")})
# Your work path
path = subprocess.check_output('pwd',shell=False,stderr=subprocess.STDOUT,text=True).replace("\n", "")
# Protein .maps,fld path
protein_path = work_path + '/protein'
#.smi path
ligand_smi_path = work_path + '/ligand_smi'
# .mol2 path
ligand_mol2_path = work_path +'/ligand_mol2'
# .pdb path
ligand_pdb_path = work_path + '/ligand_pdb'
# .pdbqt path
ligand_pdbqt_path = work_path + '/ligand_pdbqt'
# AutoDock-GPU run docking output for path
result_dlg_path = work_path + '/result_dlg'
# result csv path
result_csv_path = work_path + '/result_csv'
result_complex_path = work_path + '/result_complex'
result_mol2_path = work_path + 'result_mol2'
# Your AutoDockTools about prepare_receptor4.py path
Grid = program_path + '/BatchDock-' + ver + '/prepare_ligand4.py'
ligand_tools = 'obabel'
