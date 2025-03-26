from properties import *

# Make ligand.PDB change to ligand.PDBQT and setting ligand
print(f'\n\033[92m{lang_pdb_began}\033[0m')
for pdb in os.listdir(ligand_pdb):
    no_work_pdb = '#' in pdb  # the protein to_work or no_work ?
    if no_work_pdb != True:
        if pdb.endswith('.pdb'):  # checking file type
            pdb_path = os.path.join(ligand_pdb, pdb)  # fund file list
            ligand_pdbqt_name = pdb_path.rsplit('/', 1)[-1]  # set pdbqt file name
            change_pdbqt_cmd = [py2, Grid,
                                '-r', pdb_path,
                                '-o', f'{ligand_pdbqt_path}/{ligand_pdbqt_name}qt']
            try:
                change_pdbqt_out = subprocess.check_output(change_pdbqt_cmd,shell=False,stderr=subprocess.STDOUT,text=True)
            except:
                change_pdbqt_out = 'No Error Messages'
                pass
            if (len(change_pdbqt_out) < 1):
                pdbqt_number += 1
                print(f'\033[92m    {lang_pdb_suc}\033[95m{ligand_pdbqt_name}\033[0m')  # print green information
            elif '#' in pdb:
                break
            else:
                error_number += 1
                error_pdb_path = os.path.join(ligand_pdb, pdb)  # fund error file list
                error_pdb_name = error_pdb_path.rsplit('/', 1)[-1]  # set error file name
                print(f'\033[91m{lang_pdb_err1}\033[95m{error_pdb_name}\033[91m\n{lang_pdb_err2}\n{change_pdbqt_out}\033[91m\n{lang_pdb_err3}\033[0m')
        else:
            warning_number += 1
            error_pdb_path = os.path.join(ligand_pdbqt_path, pdb)  # fund error file list
            error_pdb_name = error_pdb_path.rsplit('/', 1)[-1]  # set error file name
            print(f'    \033[93m{lang_pdb_war}\033[95m{error_pdb_name}\033[0m')  # print red error
    else:
        no_work_txt = pdb.replace("#", "")
        print(f'\033[92m    {lang_pdb_commend}：\033[95m{no_work_txt}\033[0m')
print(f'\033[92m{lang_pdb_end}\033[0m')

if error_number+warning_number == 0:
    print(f'\033[92m\n    {lang_pdb_summary_suc1}{pdbqt_number}{lang_pdb_summary_suc2}\033[0m')
else:
    print(f'\033[91m\n{lang_pdb_summary_failure1}{pdbqt_number}{lang_pdb_summary_failure2}{error_number}{lang_pdb_summary_failure3}{warning_number}{lang_pdb_summary_failure4}\033[0m')