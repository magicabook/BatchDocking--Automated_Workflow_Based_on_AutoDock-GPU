import re
smi_txt_raw = ' '

smi_txt_data = re.sub(r'[\t]', ' ', smi_txt_raw)
for smi_txt_line in smi_txt_data: # 读取每一行
    smi_txt_line = (smi_txt_line.strip()) # delete \n 删除所有换行符
    if not smi_txt_line:
        print('no')
    else:
        print('yes')


print(smi_txt_data)