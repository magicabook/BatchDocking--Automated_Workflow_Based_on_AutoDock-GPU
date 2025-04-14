lang_inter_describe = '''
欢迎使用批量对接程序！ 版本号：[1.4.1]
项目地址：https://github.com/magicabook/Batch_Docking--Automated_Workflow_Based_on_AutoDock-GPU.git
作者：附魔书  通讯地址：magica_book@qq.com  保留该程序的一切权益。'''



lang_inter_select = '''
<<<=========================[ 模式选择 ]==========================>>>
[0] 设置界面
[1] 仅将输入的.txt拆分为单个.smiles小分子
[2] 仅将单个.smiles小分子转换为.PDB格式
[3] 仅将.PDB格式的小分子转换为.PDBQT配体格式
[4] 仅运行批量自动对接
[a] 运行小分子前处理的全部流程（ 1 ~ 3 ）
[b] 运行分子对接的全部流程（ 1 ~ 4 ）
[x] 文件补全
[z] 退出程序'''
lang_inter_function_number = '请选择您需要运行的功能：'
lang_inter_function_err = '警告：请输入正确的参数！'
lang_inter_suc = '您选择的工作模式是：{}'
lang_inter_select_1 = '仅将输入的.txt拆分为单个.smiles小分子'
lang_inter_select_2 = '仅将单个.smiles小分子转换为.PDB格式'
lang_inter_select_3 = '仅将.PDB格式的小分子转换为.PDBQT配体格式'
lang_inter_select_4 = '仅运行批量自动对接'
lang_inter_select_a = '运行小分子前处理的全部流程（ 1 ~ 3 ）'
lang_inter_select_b = '运行分子对接的全部流程（ 1 ~ 4 ）'
lang_inter_select_x = '文件补全'
lang_inter_select_z = '退出程序'
lang_inter_quit = '程序已退出，感谢使用！'
lang_return_list = '已返回上级列表'

lang_inter_select_0 = '设置界面\n'
lang_inter_set = '''\
[模式选择]-[设置界面]:
    [1] 语言
    [2] 单次对接迭代次数
    [3] 默认结果文件名
    [4] 对接程序运行种子
    [z] 返回上级目录'''
lang_inter_set_select = '请选择您需要设置的内容：'
lang_inter_set_select_1 = '语言'
lang_inter_set_select_2 = '设置单次对接迭代次数'
lang_inter_set_select_3 = '设置默认结果文件名'
lang_inter_set_select_4 = '设置对接程序运行种子'
lang_inter_set_select_z = '返回上级目录'
lang_inter_set_end = '设置已应用'

lang_inter_set_lang = '''
    \033[92m[z] 返回上级目录\033[0m
    存在的语言包列表：\033[92m{}\033[0m
    
请选择您需要的语言：'''
lang_inter_set_lang_suc = '成功设置语言为：'

lang_inter_set_nrun = '''
    \033[92m[z] 返回上级目录\033[0m
    此前程序默认的单次对接迭代次数为 \033[92m{}\033[0m
    注意：请输入整数
    
请输入在一对分子的对接工作中您希望的默认迭代次数：'''
lang_inter_set_nrun_suc = '成功设置默认对接次数为：'
lang_inter_set_nrun_war = '警告：请输入整数'
lang_inter_set_nrun_none = '警告：请输入对接次数'

lang_inter_set_name = '''
    \033[92m[z] 返回上级目录\033[0m
    此前程序默认的结果文件名为 \033[92m{}\033[0m
    注意：文件名称不要使用除下划线 _ 以外的特殊字符
    
请输入您希望的默认结果文件名：'''
lang_inter_set_name_suc = '成功设置默认结果文件名为：'

lang_inter_set_seed = '''
    \033[92m[z] 返回上级目录\033[0m
    此前程序默认的种子为 \033[92m{}\033[0m
    留空则使用AutoDock-GPU程序默认的种子（ 系统时间 + 进程PID ）
    注意：请输入整数
    
请输入您希望的默认种子：'''
lang_inter_set_seed_suc = '成功设置默认种子为：'
lang_inter_set_seed_suc1 = '种子已恢复为AutoDock-GPU默认的值'
lang_inter_set_seed_war = '警告：请输入整数或留空（直接回车）！'



lang_inter_make_began = '<<<====================[ 正在进行工作目录完整性校验 ]====================>>>'
lang_inter_make_file_dir_yes = '已存在目录 {}'
lang_inter_make_file_dir_make = '正在创建目录 {}'
lang_inter_make_file_dir_suc = '目录 {} 已成功创建！'
lang_inter_make_work_path_yes = '成功找到工作目录 {}'
lang_inter_make_work_path_make = '正在创建工作目录 {}'
lang_inter_make_work_path_suc = '工作目录 {} 已成功创建！'
lang_inter_make_end = '<<<======================[ 工作目录完整性校验通过 ]=====================>>>'



lang_smi_began = '<<<===================[ 正在拆分输入的小分子集合 ]===================>>>'
lang_smi_suc = '已提取小分子 >'
lang_smi_war = '警告：请检查或清除格式错误的文件，问题所在目录 > ligand_smi 问题文件名：'
lang_smi_end = '<<<=======================[ 输入文件拆分完成 ]=======================>>>'
lang_smi_commend = '找到被注释的小分子集合：'
lang_smi_summary_suc = '本次工作共提取 {} 个分子，产生 0 个错误与 0 个警告\n    圆满完成预期任务！'
lang_smi_summary_failure = '''\
本次工作共提取 {} 个分子，产生 {} 个错误与 {} 个警告
你可以查看终端中的红色错误信息与黄色警告信息以了解问题是如何发生的
如果需要寻求帮助，请把终端里的相关输出提供给对方，而不是发送这个窗口的照片或者截图……'''



lang_smi_sing_began = '<<<===================[ 正在转换小分子为.PDB格式 ]===================>>>'
lang_smi_sing_commend = '找到被注释的小分子：'
lang_smi_sing_suc = '成功将该小分子转换为.PDB格式 > '
lang_smi_sing_err = '''\
错误：该小分子转换为.PDB失败!
请检查： \033[95m{}\033[91m

                  vvvvv 请根据下列报错信息进行整改！ vvvvv
<<<==================[ OpenBaBel程序输出的错误报告: ]==================>>>

{}
                  ^^^^^ 请根据以上报错信息进行整改！ ^^^^^
'''
lang_smi_sing_war = '警告：请检查或清除格式错误的文件，问题所在目录 > ligand_smi_single 问题文件名：'
lang_smi_sing_end = '<<<==================[ 合格小分子已全部转换为.PDB格式 ]==================>>>'
lang_smi_sing_summary_suc = '本次工作共转换 {} 个分子，产生 0 个错误与 0 个警告\n    圆满完成预期任务！'
lang_smi_sing_summary_failure = '''\
本次工作共转换 {} 个分子，产生 {} 个错误与 {} 个警告
你可以查看终端中的红色错误信息与黄色警告信息以了解问题是如何发生的
如果需要寻求帮助，请把终端里的相关输出提供给对方，而不是发送这个窗口的照片或者截图……'''



lang_pdb_began = '<<<======================[ 正在设置小分子为配体 ]======================>>>'
lang_pdb_commend = '找到被注释的小分子：'
lang_pdb_suc = '成功将该小分子转换为.PDBQT格式 > '
lang_pdb_err = '''\
错误：该小分子转换为.PDBQT失败
请检查： \033[95m{}\033[91m

                  vvvvv 请根据下列报错信息进行整改！ vvvvv
<<<===============[ Prepare_Ligand4程序输出的错误报告: ]===============>>>

{}
                  ^^^^^ 请根据以上报错信息进行整改！ ^^^^^
'''
lang_pdb_war = '警告：请检查或清除格式错误的文件，问题所在目录 > ligand_pdb 问题文件名：'
lang_pdb_end = '<<<===================[ 合格小分子已全部设置为配体 ]===================>>>'
lang_pdb_summary_suc = '本次工作共转换 {} 个分子，产生 0 个错误与 0 个警告\n    圆满完成预期任务！'
lang_pdb_summary_failure = '''\
本次工作共转换 {} 个分子，产生 {} 个错误与 {} 个警告
你可以查看终端中的红色错误信息与黄色警告信息以了解问题是如何发生的
如果需要寻求帮助，请把终端里的相关输出提供给对方，而不是发送这个窗口的照片或者截图……'''



lang_dock_inter_name = '请为本次工作的结果文件设置名称，若使用默认名称，请按回车：'
lang_dock_workfile_began = '<<<=====================[ 正在校验工作目录完整性 ]=====================>>>'
lang_dock_pro_commend = '找到被注释的蛋白：'
lang_dock_pdbqt_commend = '找到被注释的小分子：'
lang_dock_fld_err = '错误：未找到该蛋白质的网格文件！问题蛋白名称：'
lang_dock_complex = '最优对接复合体存放目录已创建，目录名称：'
lang_dock_dlg = '小分子构象存放一级目录已创建，目录名称：'
lang_dock_have_dlg = '已存在小分子构象目录：'
lang_dock_mk_dlg = '正在进行目录补全 > 小分子构象存放二级目录：'
lang_dock_mk_dlg_suc = '小分子构象存放二级目录已创建，目录名称：'
lang_dock_workfile_end = '<<<=====================[ 工作目录完整性校验通过！ ]=====================>>>'
lang_dock_csv_began = '<<<===================[ 正在初始化结果矩阵与CSV模块 ]===================>>>'
lang_dock_csv_end = '<<<=====================[ 结果矩阵与CSV模块就绪！ ]=====================>>>'
lang_dock_main_began = '''\
<<<=====================[ 正在运行分子对接主程序 ]=====================>>>\033[0m

单次对接迭代次数为：\033[92m{}
'''
lang_dock_mess = '正在运行第 {} 次对接，工作蛋白 \033[96m{}\033[0m 对接小分子 \033[95m{}\033[0m'
lang_dock_suc = '蛋白质 \033[96m{}\033[92m 与小分子 \033[95m{}\033[92m 对接成功！最优构象的结合自由能为：{}'
lang_dock_err = '''\
错误：发生一次对接失败！
问题分子： \033[95m{}\033[91m

                  vvvvv 请根据下列报错信息进行整改！ vvvvv
<<<=================[ AutoDock-GPU程序输出的错误报告: ]=================>>>

{}
                  ^^^^^ 请根据以上报错信息进行整改！ ^^^^^
'''
lang_dlg_err = '''\
错误：最优构象提取失败！
问题分子： \033[95m{}\033[91m

                  vvvvv 请根据下列报错信息进行整改！ vvvvv
<<<===============[ BatchDock构象提取模块输出的错误报告: ]===============>>>

{}
                  ^^^^^ 请根据以上报错信息进行整改！ ^^^^^
'''
lang_dock_war = '警告：请检查或清除格式错误的文件，问题所在目录 > ligand_pdbqt 问题文件名：'
lang_dock_complex_suc = '最优构象提取成功，复合物3D结构已生成！'
lang_dock_main_end = '<<<===================[ 分子对接主程序运行完毕 ]=====================>>>'
lang_dock_csv_suc = '所有最优构象的自由能提取并写入Excel成功！文件名称为'
lang_dock_summary_suc = '本次工作共运行 {} 次对接，产生 0 个错误与 0 个警告\n    圆满完成预期任务！'
lang_dock_summary_failure = '''\
本次工作共运行 {} 次对接，产生 {} 个错误与 {} 个警告
你可以查看终端中的红色错误信息与黄色警告信息以了解问题是如何发生的
如果需要寻求帮助，请把终端里的相关输出提供给对方，而不是发送这个窗口的照片或者截图……'''



cheese_bonus = '''\
    人：“小猫，你可以吃，芝士汉堡”
    猫：“mua~”
'''

nyan_cat_bonus = '''\
    您的小分子似乎有些多，分子对接需要的时间有些长，快来这个网站获取一些催化剂吧！
    https://www.bilibili.com/video/BV1vW411T7HM/?spm_id_from=333.337.search-card.all.click&vd_source=cacde7cc9cb211ea5af2636b44fc3c30
'''

homura_cat_bonus = '''\
    您的小分子似乎有些多，分子对接需要的时间有些长，快来这个网站获取一些催化剂吧！
    吼姆拉特供！！！
    https://www.bilibili.com/video/BV11x411c7xH?spm_id_from=333.788.recommend_more_video.10&vd_source=cacde7cc9cb211ea5af2636b44fc3c30
'''