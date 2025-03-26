from properties import *

# Change to single_file
print(f'\033[92m{lang_smi_began}\033[0m')
for smi_txt in os.listdir(ligand_smi):  # make protein list
    no_work_smi = '#' in smi_txt  # the protein to_work or no_work ?
    if no_work_smi != True:
        if smi_txt.endswith('.txt'):  # checking file type
            # read smi
            smi_path = os.path.join(ligand_smi, smi_txt)
            if os.path.isfile(smi_path):
                # line read
                with open(smi_path, "r", encoding="utf-8") as f:
                    for line in f:
                        smi_all = (line.strip()) # delete \n
                        # abstracting structure and name
                        parts = smi_all.split()
                        smi_str, smi_name = parts[0], parts[1] # abstracting and set
                        # make file and rename
                        out_smi =  os.path.join(ligand_smi_single, smi_name + ".smi") # define out_file name
                        with open(out_smi,'w') as f: # define out_fine content
                            f.write(smi_str)
                        print(f'\033[92m    {lang_smi_suc}\033[95m{smi_name}\033[0m')
                        smi_number += 1
        elif '#' in smi_txt:
            break
        else:
            warning_number += 1
            error_smi_path = os.path.join(ligand_smi, smi_txt)  # fund error file list
            error_smi_name = error_smi_path.rsplit('/', 1)[-1]  # set error file name
            print(f'\033[93m    {lang_smi_war}{error_smi_name}\033[0m')  # print red error
    else:
        no_work_txt = smi_txt.replace("#", "")
        print(f'\033[92m    {lang_smi_commend}\033[95m{no_work_txt}\033[0m')
print(f'\033[92m{lang_smi_end}\033[0m')

if error_number+warning_number == 0:
    print(f'\033[92m\n    {lang_smi_summary_suc1}{smi_number}{lang_smi_summary_suc2}\033[0m')
else:
    print(f'\033[91m\n{lang_smi_summary_failure1}{smi_number}{lang_smi_summary_failure2}{error_number}{lang_smi_summary_failure3}{warning_number}{lang_smi_summary_failure4}\033[0m')