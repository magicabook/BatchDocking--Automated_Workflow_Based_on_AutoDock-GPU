# Batch Docking: Automated Workflow Based on AutoDock-GPU (V 1.2.4)
这是一个基于AutoDock-GPU的自动化批量对接程序，只需输入小分子的smiles结构文档（支持批量输入）并且提供蛋白质的网格文件（maps.fld）即可自动完成小分子预处理，分子对接，结果提取等步骤。<br>
This project is an automated batch docking pipeline built on AutoDock-GPU, designed to streamline virtual screening workflows.<br>

本程序暂处于早期测试版，作者不太熟悉GitHub的使用，请见谅。<br>
更多完善的功能和用户手册在将来的更新中被加入！<br>
This program is currently in an early beta phase. The author is not very familiar with GitHub usage, so please excuse any shortcomings.<br>
More complete features and a user manual will be added in future updates!<br>

## 更新日志
### 奇迹，魔法都是存在的！
1）正式实装“语言包”，您可以更改`properties.py`文件来改变程序默认的输出语言，目前支持简体中文和英文<br>
2）您可以在`language`目录下新建您像添加语言的.py文件，文件内容请参考`zh_cn.py`与`en.py`<br>
3）更加规范化代码的接口，变量名称，为后一个版本的协同工作和终端交互做了铺垫<br>
4）玩了几乎一天魔法少女小圆 MagiaExedra，开服刷号非常痛苦<br>
5）没有抽到晓美焰，没有抽到环彩羽，要魔女化了<br>
6）引入配置文件，您可以更方便地设置全局变量与参数，不必再对每一个文件进行调整<br>
7）引入语言包，您可以通过配置文件选择您的语言，所有的输出均进行了标准化命名，为汉化提供了接口和参考<br>
8）更为标准和一目了然的变量名称，避免了命名含糊不清的变量被错误使用造成灾难性后果<br>
9）更简洁的输出<br>
10）自动捕获软件错误与有问题的文件，让您调试更省心<br>
11）扩展注释范围，现在您可以对小分子进行注释<br>
12）优化了部分代码<br>
13）移除了Herobrine<br>

## Changelog<br>
### Miracles and Magic do Exist!
1. Implemented localization support – Customize output language via `properties.py` (currently supports Simplified Chinese & English)<br>
2. Add new `languages` – Create .py files in /language directory following `zh_cn.py`/`en.py` templates<br>
3. Standardized code interfaces & naming – Layered groundwork for future collaborative development and CLI interactions<br>
4. PlayedPuella Magi Madoka Magica Magia Exedra all day – Suffered through endless rerolls for starter accounts<br>
5. Gacha tragedy – No Homura, no Iroha... now turning into a witch (salty edition 🧂)<br>
6. Introduced configuration files – Easily set global variables and parameters without manual adjustments to individual files<br>
7. Added language packs – Select your language via the configuration file. All outputs now follow standardized naming conventions, enabling seamless localization (e.g zh-cn)<br>
8. Standardized and intuitive variable names – Eliminates ambiguous naming to prevent catastrophic misuse<br>
9. Simplified output – Cleaner logs and results for improved readability<br>
10. Automatic error and file validation – Catches software crashes and malformed inputs to streamline debugging<br>
11. Extended commenting scope – Now supports annotations for small molecule(e.g #ligand.zip)<br>
12. Fixed known bugs<br>
13. Removed Herobrine – Because even digital realms need pest control.<br>


## 运行环境需求
1）装有Ubuntu的WSL2环境或其他Linux发行版<br>
2）已编译的AutoDock-GPU程序<br>
3）安装OpenBaBel<br>
4）安装AutoDockTools<br>
5）安装Python3<br>
6）上述软件及相关环境变量设置正确<br>

## 在确保您的软件安装和环境变量无误后，请您在工作目录下新建下列目录（这一部分内容会在将来加入的初始化功能中代替人工操作）
1）`ligand_smi` # 用于批量输入小分子的smiles结构<br>
2）`ligand_smi_single` # 用于存放软件拆分后单个小分子的smiles结构<br>
3）`ligand_pdb` # 用于存放软件根据smiles生成的`.pdb`格式分子<br>
4）`ligand_pdbqt` # 用于存放软件完成预处理后的`.pdbqt`格式分子<br>
5）`protein` #用于存放您的蛋白质文件<br>
6）`result_dlg` # 用于存放每一个蛋白质-小分子对接后产生的结果文件<br>
7）`result_csv` # 用于存放每一次虚拟筛选工作后所有对接的最优构象自由能数据，以便于您快速查阅结果和定位潜在的活性分子<br>
8）`python` # 将您从这个仓库下载的代码全部放到这个目录下，以保证代码中路径定义正确。如果您有开发能力，可自行定义其中的路径<br>

## 工作流程
1）假设您有A、B两个蛋白，请在`protein`目录下分别创建`A`、`B`两个目录<br>
2）蛋白质预处理完毕后将AutoDockTools生成的`.maps`和`.maps.fld`文件剪贴到相关蛋白质的目录下<br>
3）在`ligand_smi`目录下新建一个`.txt`文件，并且按照smiles格式规则将您的小分子粘贴到这个`.txt`文件中，例如： <br>
    ```
    CC(=O)OC1=CC=CC=C1C(O)=O Aspirin
    ```<br>
    ```
    CC(=O)NC1=CC=C(O)C=C1 Paracetamol
    ```<br>
    ```
    CC(C)CC1=CC=C(C=C1)[C@@H](C)C(O)=O Ibuprofen
    ```<br>
4）运行`change_smi.py`，程序会自动读取您`ligand_smi`目录下的所有`.txt`文件，并将每一个分子提取出来单独保存至`ligand_smi_single`目录下，稍后程序将会把`ligand_smi_single`目录下的所有小分子转化为`.pdb`格式，同时完成加氢，加G电荷与根据gaff力场完成构象能量最低化 <br>
5）运行`change_pdb.py`，程序会自动将`ligand_pdb`目录下的所有小分子转化为`.pdbqt`格式并设置为配体，这一过程依赖ADT的子模块完成<br>
6）运行`dock.py`，程序会自动对每一个蛋白质-小分子组合进行对接，同时将获取的最低自由能保存到`.csv`文件中，您可以在开发环境中自定义`.csv`文件的名称，未来将添加交互式功能以便用户在终端中自定义<br>
7）运行`run_all.py`运行（4）~（6）<br>
8）在`result_dlg`目录下有与您蛋白质目录同名的目录，分别保存了该蛋白与每一个小分子对接的结果文件<br>
9）在`result_csv`目录下保存了本次对接工作的所有最优自由能数据，您可根据这一`.csv`文件寻找潜在的成药化合物<br>

## 未来的发展方向
1）**自动初始化（包括目录检查和依赖库下载）** 让用户上手后无需调整工作目录与下载python运行效果库文件即可直接使用<br>
2）**交互式服务** 让用户在终端即可自定义结果文件名称<br>
3）**进一步优化程序运行的逻辑** 让转化失败的可疑分子在结果文件中单独标识出来<br>
4）**自动提取最优构象的复合物结构** 用户无需再次进入ADT提取结构<br>
5）**优化软件输出** 添加可视化的进度条和进程监视与看门狗<br>
6）**更好的用户手册**<br>

## System Requirements
1. A WSL2 environment running Ubuntu, or another Linux distribution.<br>
2. The pre-compiled AutoDock-GPU program.<br>
3. Installation of OpenBaBel.<br>
4. Installation of AutoDockTools.<br>
5. Installation of Python3.<br>
6. Ensure that the above software and related environment variables are set up correctly.<br>

After confirming that your software installations and environment variables are correctly configured, please create the following directories in your working directory (this manual step will be replaced by an initialization feature in future updates)<br>

1. **ligand_smi** – For batch input of small molecules’ SMILES strings.<br>
2. **ligand_smi_single** – To store the individual SMILES strings of small molecules after the software splits them.<br>
3. **ligand_pdb** – To store molecules in the .pdb format generated from SMILES.<br>
4. **ligand_pdbqt** – To store molecules in the .pdbqt format after preprocessing.<br>
5. **protein** – To store your protein files.<br>
6. **result_dlg** – To store the result files produced from each protein–small molecule docking.<br>
7. **result_csv** – To store the best binding free energy data for all docked conformations from each virtual screening session, allowing you to quickly review results and identify potential active compounds.<br>
8. **python** – Place all the code you download from this repository in this directory to ensure that path definitions in the code are correct. If you have development skills, you may customize the paths as needed.<br>

## Workflow
1. If you have proteins A and B, please create two directories named “A” and “B” under the **protein** directory.<br>
2. After protein preprocessing, move the `.maps` and `.maps.fld` files generated by AutoDockTools into the corresponding protein directories.<br>
3. Create a new `.txt` file in the **ligand_smi** directory and paste your small molecules in SMILES format into this file. For example:<br>
    ```
    CC(=O)OC1=CC=CC=C1C(O)=O Aspirin
    CC(=O)NC1=CC=C(O)C=C1 Paracetamol
    CC(C)CC1=CC=C(C=C1)[C@@H](C)C(O)=O Ibuprofen
    ```
4. Run `change_smi.py`. The program will automatically read all `.txt` files in the **ligand_smi** directory, extract each molecule, and save them individually in the **ligand_smi_single** directory. Later, the program will convert all small molecules in **ligand_smi_single** to the `.pdb` format, add hydrogens, assign G charges, and perform conformational energy minimization according to the GAFF force field.<br>
5. Run `change_pdb.py`. The program will automatically convert all small molecules in the **ligand_pdb** directory to `.pdbqt` format and set them as ligands; this process relies on a submodule of ADT.<br>
6. Run `dock.py`. The program will automatically perform docking for each protein–small molecule pair and save the best (lowest) binding free energy into a `.csv` file. You can customize the `.csv` file name in the development environment; interactive features for custom naming will be added in future updates.<br>
7. Run `run_all.py`. Run 4 ~ 6 all process.<br>
8. In the **result_dlg** directory, directories named after your proteins will be created, each containing the docking result files for that protein with every small molecule.<br>
9. The **result_csv** directory will store the best binding free energy data for all docking sessions, which you can use to identify potential drug-like compounds.<br>

## Future Development Directions
1. **Automatic Initialization:** Including directory checks and dependency downloads, so users can start without manually adjusting the working directory or downloading Python libraries.<br>
2. **Interactive Service:** Allowing users to customize result file names directly from the terminal.<br>
3. **Workflow Optimization:** Improving the program’s logic to mark molecules that fail conversion separately in the result files.<br>
4. **Automated Extraction:** Automatically extracting the best binding complex structure, eliminating the need to extract structures via ADT.<br>
5. **Enhanced Output:** Adding visual progress bars, process monitoring, and a watchdog.<br>
6. **Improved User Manual.**<br>

The English portion of this project's README was generated by DeepSeek and ChatGPT.







