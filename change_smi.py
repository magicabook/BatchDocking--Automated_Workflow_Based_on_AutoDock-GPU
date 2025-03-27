from properties import *

# Change to single_file
# 将ligand_smi目录下的.txt文件拆分为单个.smi文件存储到ligand_smi_single目录下，并以小分子名称命名
print(f'\033[92m{lang_smi_began}\033[0m')
for smi_txt in os.listdir(ligand_smi):  # make ligand list 阅读该目录下的所有文件并存储到一个list中
    no_work_smi = '#' in smi_txt  # the ligand to_work or no_work ? 通过“#”判断该小分子集是否参与工作
    if no_work_smi != True:
        if smi_txt.endswith('.txt'):  # checking file type 检查文件后缀是否正确
            # read smi.txt
            # 开始阅读小分子集的.txt文件
            smi_path = os.path.join(ligand_smi, smi_txt) # 该目录下所有.txt文件的路径
            if os.path.isfile(smi_path):
                # line read
                # 每次读取一行
                with open(smi_path, "r", encoding="utf-8") as smi_txt_data: # 开始阅读.txt文件
                    for line in smi_txt_data: # 读取每一行
                        smi_txt_all = (line.strip()) # delete \n 删除所有换行符
                        # abstracting structure and name
                        # 分别提取结构字符串和名称字符串
                        parts = smi_txt_all.split() # 按行进行切片
                        smi_str, smi_name = parts[0], parts[1] # abstracting and set 第一个空格前切片为结构字符串，第二个空格前切片为名称字符串
                        # make file and rename
                        # 新建只包含一个结构的smi文件
                        out_smi =  os.path.join(ligand_smi_single, smi_name + ".smi") # define out_file path 定义新建smi文件的路径
                        with open(out_smi,'w') as smi_sing_file: # define out_fine content 读取新建的smi文件，进入写模式
                            smi_sing_file.write(smi_str) # 将结构字符串写入smi文件
                        print(f'\033[92m    {lang_smi_suc} \033[95m{smi_name}\033[0m') # 打印成功信息
                        smi_number += 1 # smi计数器+1，用于该模块运行完毕后的总结
        elif '#' in smi_txt: # 若该文件被“#”注释，则停止执行对该文件的操作
            break
        else: # 文件后缀错误，停止执行操作并输出警告
            smi_war_number += 1 # 警告计数器+1，用于该模块运行完毕后的总结输出
            error_smi_path = os.path.join(ligand_smi, smi_txt)  # fund error file list # 获取错误文件的路径
            error_smi_name = error_smi_path.rsplit('/', 1)[-1]  # set error file name # 提取错误文件的名称
            print(f'\033[93m    {lang_smi_war} {error_smi_name}\033[0m')  # print yellow warning # 打印文件类型警告
    else: # 如果文件被“#”注释
        no_work_txt_name = smi_txt.replace("#", "") # 获取被注释的文件名称
        print(f'\033[92m    {lang_smi_commend} \033[95m{no_work_txt_name}\033[0m') # 打印注释信息
print(f'\033[92m{lang_smi_end}\033[0m') # 打印提取单个smi模块执行结束信息

if smi_err_number + smi_war_number == 0: # 判断异常计数是否为0
    print(f'\033[92m\n    {lang_smi_summary_suc.format(smi_number)}\033[0m') # 输出无异常结束语句
else: # 若异常计数器不为零，则将异常输出计数打印并调用异常提示信息
    print(f'\033[91m\n{lang_smi_summary_failure.format(smi_number, smi_err_number, smi_war_number)}\033[0m')