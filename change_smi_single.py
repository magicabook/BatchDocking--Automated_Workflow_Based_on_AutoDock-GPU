from properties import *

# Make ligand_single.SMI change to ligand.PDB
print(f'\n\033[92m{lang_smi_sing_began}\033[0m')
for smi_sing in os.listdir(ligand_smi_single):
    no_work = '#' in smi_sing  # the protein to_work or no_work ?
    if no_work != True:
        if smi_sing.endswith('.smi'): # checking file type
            smi_single_path = os.path.join(ligand_smi_single, smi_sing) # fund file list
            ligand_smi_single_name = smi_single_path.rsplit('/', 1)[-1]  # abstracting smi file name
            # set pdb file name
            start = ligand_smi_single_name.rfind('/')
            end = ligand_smi_single_name.rfind('.')
            ligand_pdb_name = ligand_smi_single_name[start + 1:end]
            obabel_smi_cmd = ['obabel',
                            '-ismi', smi_single_path,
                            '-opdb',
                            '-O', f"{ligand_pdb}/{ligand_pdb_name}.pdb",
                            '-h',
                            '--gen3D',
                            '--partialcharge', 'gasteiger',
                            '--minimize',
                            '--ff', 'gaff']
            #print(obabel_smi_cmd)
            obabel_out = subprocess.check_output(obabel_smi_cmd,shell=False,stderr=subprocess.STDOUT,text=True)
            os.system('killall -9 obabel')
            if (obabel_out.find('1 molecule converted') >= 0):
                pdb_number += 1
                print(f'    \033[92m{lang_smi_sing_suc}\033[95m{ligand_smi_single_name}\033[0m') # print green information
            elif '#' in smi_sing:
                break
            else:
                error_number += 1
                error_smi_single_path = os.path.join(ligand_smi_single, smi_sing)  # fund error file list
                error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name
                print(f'\033[91m{lang_smi_sing_err1}\033[95m{error_smi_single_name}\n\033[91m{lang_smi_sing_err2}\n{obabel_out}\n{lang_smi_sing_err3}\033[0m')
        else:
            warning_number += 1
            error_smi_single_path = os.path.join(ligand_smi_single, smi_sing)  # fund error file list
            error_smi_single_name = error_smi_single_path.rsplit('/', 1)[-1]  # set error file name
            print(f'    \033[93m{lang_smi_sing_war}\033[95m{error_smi_single_name}\033[0m') # print red error
    else:
        no_work_txt = smi_sing.replace("#", "")
        print(f'\033[92m    {lang_smi_sing_commend}：\033[95m{no_work_txt}\033[0m')
print(f'\033[92m{lang_smi_sing_end}\033[0m')

if error_number+warning_number == 0:
    print(f'\033[92m\n    {lang_smi_sing_summary_suc1}{pdb_number}{lang_smi_sing_summary_suc2}\033[0m')
else:
    print(f'\033[91m\n{lang_smi_sing_summary_failure1}{pdb_number}{lang_smi_sing_summary_failure2}{error_number}{lang_smi_sing_summary_failure3}{warning_number}{lang_smi_sing_summary_failure4}\033[0m')