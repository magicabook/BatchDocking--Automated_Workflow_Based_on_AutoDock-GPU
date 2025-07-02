# Batch Docking: Automated Workflow Based on AutoDock-GPU (V 1.5.0)
这是一个基于AutoDock-GPU的自动化批量对接程序，只需输入小分子的smiles结构文档（支持批量输入）并且提供蛋白质的网格文件（maps.fld）即可自动完成小分子预处理，分子对接，结果提取等步骤。<br>
This project is an automated batch docking pipeline built on AutoDock-GPU, designed to streamline virtual screening workflows.<br>

更多完善的功能和用户手册在将来的更新中被加入！<br>
More complete features and a user manual will be added in future updates!<br>

## 联系作者 Correspoonding Author
```
magica_book@qq.com
```

## 更新日志
### 紧急修复
紧急修复了小分子预处理时ADT模块调用错误，旧版本BatchDock错误调用了ADT的prepare_receptor4.py模块，正确的调用应为prepare_ligand4.py，1.5.0版本修复了这个BUG。

## Changelog
### Emergency Repair
An urgent remediation was implemented to correct an erroneous invocation of the ADT module during small-molecule preprocessing. In previous iterations of BatchDock, the prepare_receptor4.py module was improperly executed, whereas the appropriate procedure requires utilization of prepare_ligand4.py. This software defect was systematically resolved in version 1.5.0.

## 运行环境需求
1. 装有Ubuntu的WSL2环境或其他Linux发行版<br>
2. 已编译的AutoDock-GPU程序<br>
3. 安装OpenBaBel<br>
4. 安装AutoDockTools<br>
5. 安装Python3<br>
6. 安装Python2并且具备numpy库<br>
7. 上述软件及相关环境变量设置正确<br>

## System Requirements
1. A WSL2 environment running Ubuntu, or another Linux distribution.<br>
2. The pre-compiled AutoDock-GPU program.<br>
3. Installation of OpenBaBel.<br>
4. Installation of AutoDockTools.<br>
5. Installation of Python3.<br>
6. Install Python 2 with the numpy library.<br>
7. Ensure that the above software and related environment variables are set up correctly.<br>

## 操作简述
#### ！重要提醒 ！虽然我们充分理解非英语母语研究者的困难，但为了考虑到系统和软件的兼容性，我们强烈不建议您使用英语以外的其他语言命名任何文件！包括特殊字符和空格！您可以使用驼峰命名法加编号以区分不同的分子。
1. **修改BatchDock配置文件**
将BatchDock的GitHub仓库克隆到本地，或在Releases下载最新版本的压缩包后解压。进入BatchDock，您可以看到一系列.py文件、运行库和语言包。<br>
您需要打开`batchDock[版本号]`目录下的`properties.py`文件完成配置。<br>
```
vim properties.py
```
您需要修改配置文件第11~19行的内容：<br>
```
# 这里是BatchDock的父目录，若您的BatchDock在/home/user1/Batchdock，则修改为program_path = '/home/user1/'
program_path = ''
# 这里是BatchDock的工作目录，由于工作过程中产生的文件较多，我们建议您新建一个目录，例如mkdir /home/user1/docking_test。此时则修改为work_path = '/home/user1/docking_test'
work_path = ''
# 这里需要修改为您的Python2路径，由于AutoDockTools还停留在Python2，因此需要您提供Python2运行环境
py2 = '/usr/bin/python2.7'
# 这里需要将第一个？修改为您的AutoDock-GPU程序所在路径，第二个？修改为您自己编译后的可执行文件名称
AD_GPU = '？/AutoDock-GPU-1.6/bin/autodock_gpu_？wi'
# 这里需要将？修改为您的mgltools_x86_64Linux2_1.5.7所在路径
Grid = '？/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py'
```
编辑完成后保存并退出文本编辑器。<br>
2. **运行BatchDock主程序**
BatchDock中的所有模块和语言包受到主模块`main.py`的统一调度，您需要为该文件赋予可执行权限，随后运行主模块`main.py`。<br>
赋予`main.py`可执行权限：<br>
```
chmod +x main.py
```
执行`main.py`<br>
```
./main.py
```
您也可以将其写入环境变量中<br>
1）使用文本编辑器修改shell配置文件<br>
```
vim ~/.bashrc
```
2）在末尾加入环境变量<br>
```
alias batchdock="python3 YourBatchDockPath/main.py"
```
3）保存关闭文本编辑器后，刷新使环境变量生效<br>
```
source ~/.bashrc
```
4）现在您可以直接在控制台输入batchdock以运行BatchDock<br>
```
batchdock
```
3. **进行初始设置**
软件默认语言为英文，软件主程序运行后您可以看到以下内容：<br>
```
<<================[ Mode Selection ]================>>>
[0] Settings Interface
[1] Split input .TXT into individual .SMILES molecules
[2] Convert .SMILES to .PDB format
[3] Convert .PDB to .PDBQT ligand format 
[4] Run batch docking automation
[a] Run full preprocessing workflow (Steps 1-3)
[b] Run complete docking pipeline (Steps 1-4)
[x] File complement
[z] Exit program
Please select the function to run:
```
您需要输入`0`后`回车`进入设置模式：<br>
```
[Mode Selection]-[Settings]:
    [1] Language
    [2] Docking iterations per run
    [3] Default result filename
    [4] Docking seed
    [z] Return to main menu
Please select the function to run:
```
您需要输入`1`后`回车`进入语言设置：<br>
```
Selected workflow: Language
    [z] Return to parent menu
    Available language packs: ['华夏(文言)', 'en', 'zh_cn', 'en(Australia)']
Select language:
```
您需要输入您需要的语言，如`zh_cn`后`回车`，随后**一直输入`z`并`回车`直到软件完全退出，此时您的设置才会生效！！！**<br>
再次进入软件，设置单次工作中LGA运行次数（AutoDock-GPU默认20次）与随机数种子（AutoDock-GPU默认系统时间+进程PID），结果文件的默认名称。<br>
**切记每次修改默认设置后需一直`返回上级目录`直到软件完全退出，此时您的设置才会生效！！！**
4. **文件补全**
在终端输入`batchdock`进入BatchDock的主目录<br>
```
batchdock
```
输入`x`后`回车`，BatchDock会自动补全缺失的文件，运行完成后进入BatchDock的目录您将会看到下列文件：<br>
```工作目录下完整文件展示
工作目录/
├── ligand_smi/             # 输入小分子smiles文件的目录
├── ligand_smi_single/      # 软件自动识别并拆分的小分子存储目录
├── ligand_pdb/             # 软件自动转换3D小分子存储目录
├── ligand_pdbqt/           # 软件自动设置的配体小分子目录
├── protein/                # 输入蛋白质的目录
├── result_complex/         # 最优构型复合物的存储目录
├── result_csv/             # 结合自由能的存储目录
└── result_dlg/             # 对接产生的所有构象存储目录
```
5. **蛋白质准备**
预先用Pymol或AutoDockTools去除蛋白质的水、离子和共结晶化合物，然后用AutoDockTools生成网格文件（.map和.maps.fld与.maps.xyz）
6. **小分子准备**
绘制小分子的smiles结构式，并保存在一个.txt文件中，一个.txt支持存储多个小分子，示例如下：（smiles结构语法为：[smiles字符串][空格][自定义名称]）
```smiles.txt
CC(=O)NC1=CC=C(O)C=C1 Paracetamol
CC(C)CC1=CC=C(C=C1)[C@H](C)C(O)=O S-Ibuprofen
CC(=O)OC1=CC=CC=C1C(O)=O Aspirin
```
7. **蛋白质文件就位**
在`protein`目录下创建用于存放蛋白质网格文件（.map和.maps.fld与.maps.xyz）的目录，例如`pro1`，随后将该蛋白质的所有网格文件（.map和.maps.fld与.maps.xyz）复制到`pro1`目录下。<br>
BatchDock支持批量对接，因此您可以为多个蛋白创建目录`pro2`、`pro3`、`pro4`……请注意，您需要确保所有的蛋白质目录都被正确存放在`protein`目录下，即：<br>
```protein目录结构示例
工作目录/
├── protein/                # 用于存储多个蛋白质的集中目录
│   ├── pro1/               # 蛋白质1相关文件存储的目录
│   │   ├── pro1.maps.fld   # 蛋白质1的索引文件
│   │   ├── pro1.maps.xyz   # 蛋白质1的网格坐标文件
│   │   ├── pro1.C.map      # 蛋白质1的C原子网格文件
│   │   ├── pro1.N.map      # 蛋白质1的N原子网格文件
│   │   └── ……
│   │
│   ├── pro2/               # 蛋白质2相关文件存储的目录
│   │   ├── pro2.maps.fld   # 蛋白质2的索引文件
│   │   ├── pro2.maps.xyz   # 蛋白质2的网格坐标文件
│   │   ├── pro2.C.map      # 蛋白质2的C原子网格文件
│   │   ├── pro2.N.map      # 蛋白质2的N原子网格文件
│   │   └── ……
│   │
……  └── ……
```
8. **小分子文件就位**
复制第2步中创建的小分子smiles.txt文件到`ligand_smi`目录下，支持存放多个smiles.txt文件，其目录结构为：<br>
```ligand_smi目录结构示例
工作目录/
├──ligand_smi/              # 用于存储多个小分子smiles结构集的集中目录
│   ├── lead.txt            # 先导化合物的smiles集
│   ├── drug.txt            # 成品药的smiles集
│   ├── Method1.txt         # 使用方法1改造的小分子的smiles集
│   ├── Method2.txt         # 使用方法2改造的小分子的smiles集
……  └── ……
```
9. **分子对接**
进入BatchDock主程序，选择对应的功能键即可完成分子对接，其结果会自动整合输出到**result**相关目录下。
10. **注释功能**
BatchDock提供了注释功能，若您不希望某个小分子或蛋白质参与对接工作，只需在该分子或蛋白对应的名称前加入前缀`#`，BatchDock在运行时便会自动跳过。<br>
如果您进行了小分子abc和蛋白质ABC的对接，但由于一些问题导致小分子c和蛋白质B对接失败，那么您在修正问题后只需要用小分子c和蛋白质B重新对接，而不必做其他工作。<br>
此时您只需要进入`ligand_pdbqt`目录将小分子ab的名称打上前缀`#`，随后进入`protein`目录将蛋白质AC的名称打上前缀`#`，再运行BatchDock，选择功能**[4] 仅运行批量自动对接**即可完成补充工作。
11. **错误追踪**
BatchDock提供了非严重错误追踪与处理功能，当检测到目录下有不支持的文件（通常情况下是文件误移动导致），软件会跳过一次相关操作并抛出一个**警告**，当检测到运行失败，软件会跳过一次相关操作并抛出一个**错误**，同时会打印**系统输出的错误信息**以便于您检查与调试。<br>
**请注意！该功能并不能避免int3指令和环境缺失、环境变量错配、配置文件错误书写导致的软件崩溃！**

## Operation Overview
#### ! Important Notice ! While we fully understand the challenges faced by non-native English-speaking researchers, for optimal system and software compatibility, we strongly advise against using any language other than English for file naming! This includes avoiding special characters and spaces! You may use camelCase naming with numbering to distinguish different molecules.
1. **Configure BatchDock Settings**
Clone the BatchDock GitHub repository locally, or download and extract the latest release package. Navigate to the BatchDock directory where you will find .py files, libraries, and language packs.<br>
Edit the `properties.py` file located in the `batchDock[version]` directory:<br>
```
vim properties.py
```
You need to modify the content of lines 11 to 19 in the configuration file:<br>
```
# BatchDock parent directory (e.g., if BatchDock is at /home/user1/Batchdock, set: program_path = '/home/user1/')
program_path = ''
# Working directory (create new directory, e.g.: mkdir /home/user1/docking_test → work_path = '/home/user1/docking_test')
work_path = ''
# Python2 path (required for AutoDockTools)
py2 = '/usr/bin/python2.7'
# AutoDock-GPU path (replace first ? with path, second ? with compiled executable name)
AD_GPU = '？/AutoDock-GPU-1.6/bin/autodock_gpu_？wi'
# MGLTools path (replace ? with actual mgltools_x86_64Linux2_1.5.7 path)
Grid = '？/mgltools_x86_64Linux2_1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py'
```
Save changes and exit the editor.<br>
2. **Run BatchDock Main Program**
All modules and language packs in BatchDock are centrally managed by the main module `main.py`. You need to grant executable permission to this file and then run the main module `main.py`.<br>
Grant executable permission to `main.py`:<br>
```
chmod +x main.py
```
Execute`main.py`<br>
```
./main.py
```
You can also add it to environment variables<br>
1) Use a text editor to modify the shell configuration file<br>
The default language of the software is English. After running the main program, you will see the following content:<br>
```
vim ~/.bashrc
```
2) Add alias at end:<br>
```
alias batchdock="python3 YourBatchDockPath/main.py"
```
3) Reload configuration:<br>
```
source ~/.bashrc
```
4) Now you can directly enter `batchdock` in the console to run BatchDock<br>
```
batchdock
```
3. **Initial Setup**
Default language is English. After launch, you'll see:<br>
```
<<================[ Mode Selection ]================>>>
[0] Settings Interface
[1] Split input .TXT into individual .SMILES molecules
[2] Convert .SMILES to .PDB format
[3] Convert .PDB to .PDBQT ligand format 
[4] Run batch docking automation
[a] Run full preprocessing workflow (Steps 1-3)
[b] Run complete docking pipeline (Steps 1-4)
[x] File complement
[z] Exit program
Please select the function to run:
```
Enter `0` to access settings:<br>
```
[Mode Selection]-[Settings]:
    [1] Language
    [2] Docking iterations per run
    [3] Default result filename
    [4] Docking seed
    [z] Return to main menu
Please select the function to run:
```
Enter `1` for language settings:<br>
```
Selected workflow: Language
    [z] Return to parent menu
    Available language packs: ['华夏(文言)', 'en', 'zh_cn', 'en(Australia)']
Select language:
```
Enter preferred language (e.g., `zh_cn`), then **enter `z` repeatedly until full exit to apply settings!**<br>
Configure docking iterations (default:20) and random seed (default: system time + PID).<br>
**Always exit completely after configuration changes!**
4. **File Completion**
Run `batchdock`, then enter `x` to auto-generate directory structure:<br>
```
batchdock
```
After entering `x` followed by `Enter`, BatchDock will automatically complete missing files. Upon completion, navigate to the BatchDock directory and you will see the following files:<br>
```Complete File Structure in Working Directory
Working Directory/
├── ligand_smi/             # Directory for input small molecule SMILES files
├── ligand_smi_single/      # Directory for automatically split individual molecules
├── ligand_pdb/             # Directory for 3D-converted small molecules
├── ligand_pdbqt/           # Directory for prepared ligand molecules in PDBQT format
├── protein/                # Directory for input protein files
├── result_complex/         # Directory for optimal conformation complexes
├── result_csv/             # Directory for binding free energy results
└── result_dlg/             # Directory for all generated docking conformations
```
5. **Protein Preparation**
Preprocess proteins with PyMOL/AutoDockTools:<br>
- Remove water/ions/co-crystallized ligands<br>
- Generate grid files (.map, .maps.fld, .maps.xyz)<br>
6. **Ligand Preparation**
Create SMILES file format:<br>
```smiles.txt
CC(=O)NC1=CC=C(O)C=C1 Paracetamol
CC(C)CC1=CC=C(C=C1)[C@H](C)C(O)=O S-Ibuprofen
CC(=O)OC1=CC=CC=C1C(O)=O Aspirin
```smiles.txt
CC(=O)NC1=CC=C(O)C=C1 Paracetamol
CC(C)CC1=CC=C(C=C1)[C@H](C)C(O)=O S-Ibuprofen
CC(=O)OC1=CC=CC=C1C(O)=O Aspirin
```
7. Protein Deployment
Place grid files in protein/[name]/ directories:
```Protein Directory Structure e.g.
Working Directory/
├── protein/                # Central directory for storing multiple proteins
│   ├── pro1/               # Directory for Protein 1 related files
│   │   ├── pro1.maps.fld   # Index file for Protein 1
│   │   ├── pro1.maps.xyz   # Grid coordinate file for Protein 1
│   │   ├── pro1.C.map      # Carbon atom grid file for Protein 1
│   │   ├── pro1.N.map      # Nitrogen atom grid file for Protein 1
│   │   └── ...
│   │
│   ├── pro2/               # Directory for Protein 2 related files
│   │   ├── pro2.maps.fld   # Index file for Protein 2
│   │   ├── pro2.maps.xyz   # Grid coordinate file for Protein 2
│   │   ├── pro2.C.map      # Carbon atom grid file for Protein 2
│   │   ├── pro2.N.map      # Nitrogen atom grid file for Protein 2
│   │   └── ……
│   │
……  └── ……
```
8. **Ligand File Deployment**
Copy the small molecule SMILES.txt file created in Step 2 to the `ligand_smi` directory. Multiple SMILES.txt files are supported, with the directory structure as follows:<br>
```ligand_smi Directory Structure e.g.
Working Directory/
├── ligand_smi/              # Central directory for storing SMILES sets
│   ├── lead.txt            # SMILES collection for lead compounds
│   ├── drug.txt            # SMILES collection for approved drugs
│   ├── Method1.txt         # SMILES collection for molecules modified by Method 1
│   ├── Method2.txt         # SMILES collection for molecules modified by Method 2
……  └── ……
```
9. **Molecular Docking**
Launch the BatchDock main program and select the corresponding function key to perform molecular docking. The results will be automatically consolidated and output to relevant **result** directories.
10. **Comment Functionality**
BatchDock provides a comment feature. To exclude specific small molecules or proteins from docking, simply prefix their names with `#`. BatchDock will automatically skip these during execution.<br>
If docking fails for molecule *c* with protein *B* after processing molecules *abc* and proteins *ABC*, you only need to re-dock molecule *c* with protein *B* after fixing the issue.<br>
Navigate to the `ligand_pdbqt` directory and prefix molecule names *a* and *b* with `#`. Go to the `protein` directory and prefix protein names *A* and *C* with `#`
Run BatchDock and select function **[4] Run batch docking automation only** to complete supplementary docking.
11. **Error Tracking**
BatchDock provides non-critical error tracking and handling. When unsupported files are detected (typically caused by accidental file movement), the software skips the operation and throws a **warning**. For runtime failures, it skips the operation and throws an **error** while printing **system error messages** for inspection and debugging.<br>
**Note: This functionality cannot prevent crashes caused by int3 instructions, missing environments, environment variable mismatches, or configuration file errors!**

## 未来的方向
1. **进一步优化程序运行的逻辑** 让转化失败的可疑分子在结果文件中单独标识出来<br>
2. **优化软件输出** 添加可视化的进度条、进程监视与看门狗<br>
3. **蛋白质预处理和盲对接的支持** 自动识别蛋白质的大小并完成除水、除离子、除共结晶化合物、设置为配体，并自动计算对接盒子的参数，完成盲对接操作，助力高通量筛选和超前期药物研究工作

## Future Directions
1. **Optimize Program Execution Logic**Flag suspicious molecules that fail conversion in result files for separate identification.
2. **Enhance Software Output**Introduce visual progress bars, process monitoring, and watchdog functionality.
3. **Support Automated Protein Preprocessing and Blind Docking**Automatically detect protein dimensions to perform: Removal of water molecules, ions, and co-crystallized compounds, Ligand parameterization, Autonomous calculation of docking box parameters. Enable blind docking operations to facilitate high-throughput screening and ultra-early-stage drug discovery research.
