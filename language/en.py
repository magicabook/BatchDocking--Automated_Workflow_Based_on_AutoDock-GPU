from config import ver

lang_inter_describe = '''
Welcome to the Batch Docking Program!  Version:[''' + ver + ''']
GitHub_Link: https://github.com/magicabook/Batch_Docking--Automated_Workflow_Based_on_AutoDock-GPU.git
Author: Magica_Book  Contact_Address: magica_book@qq.com   License: All rights reserved.
Second Author: ZhuErding   Contact_Address: zhuerding@zhuerding.top
Third Author: Rex   Miya
 '''



lang_inter_select = '''
<<<=========================[ Mode Selection ]=========================>>>
[0] Settings Interface
[1] Split input .TXT into individual .SMILES molecules
[2] Convert .SMILES to .PDB format
[3] Convert .PDB to .PDBQT ligand format 
[4] Run batch docking automation
[a] Run full preprocessing workflow (Steps 1-3)
[b] Run complete docking pipeline (Steps 1-4)
[x] File complement
[z] Exit program'''
lang_inter_function_number = 'Please select the function to run:'
lang_inter_function_err = 'Warning: Please enter a valid option!'
lang_inter_suc = 'Selected workflow: {}'
lang_inter_select_1 = 'Split input .TXT into individual .SMILES molecules'
lang_inter_select_2 = 'Convert .SMILES to .PDB format'
lang_inter_select_3 = 'Convert .PDB to .PDBQT ligand format'
lang_inter_select_4 = 'Run batch docking automation'
lang_inter_select_a = 'Run full preprocessing workflow (Steps 1-3)'
lang_inter_select_b = 'Run complete docking pipeline (Steps 1-4)'
lang_inter_select_x = 'File complement'
lang_inter_select_z = 'Exit program'
lang_inter_quit = 'Program terminated. Thank you for using!'
lang_return_list = 'Returned to parent menu'

lang_inter_select_0 = 'Settings Interface (Language & Docking Iterations)'
lang_inter_set = '''
[Mode Selection]-[Settings]:
    [1] Language
    [2] Docking iterations per run
    [3] Default result filename
    [4] Docking seed
    [z] Return to main menu'''
lang_inter_set_select = 'Select setting to configure:'
lang_inter_set_select_1 = 'Language'
lang_inter_set_select_2 = 'Set docking iterations'
lang_inter_set_select_3 = 'Set default result filename'
lang_inter_set_select_4 = 'Set docking seed'
lang_inter_set_select_z = 'Return to main menu'
lang_inter_set_end = 'Settings applied'

lang_inter_set_lang = '''
    \033[92m[z] Return to parent menu\033[0m
    Available language packs: \033[92m{}\033[0m

Select language:'''
lang_inter_set_lang_suc = 'Language set to: '

lang_inter_set_nrun = '''
    \033[92m[z] Return to parent menu\033[0m
    Current default docking iterations: \033[92m{}\033[0m
    Note: Integer input required

Enter default iterations per docking run:'''
lang_inter_set_nrun_suc = 'Default iterations set to:'
lang_inter_set_nrun_war = 'Warning: Integer required!'
lang_inter_set_nrun_none = 'Warning: Please enter iteration count'

lang_inter_set_name = '''\
    \033[92m[z] Return to parent menu\033[0m
    Current default filename: \033[92m{}\033[0m
    Note: Use only underscores (_) as special characters

Enter default result filename:'''
lang_inter_set_name_suc = 'Default filename set to:'

lang_inter_set_seed = '''
    \033[92m[z] Return to parent menu\033[0m
    Current default seed: \033[92m{}\033[0m
    Empty = AutoDock-GPU default (system time + process PID)
    Note: Integer or blank

Enter default seed:'''
lang_inter_set_seed_suc = 'Default seed set to:'
lang_inter_set_seed_suc1 = 'Seed restored to AutoDock-GPU default'
lang_inter_set_seed_war = 'Warning: Enter integer or leave blank!'



lang_inter_make_began = '<<<=================[ Validating Workspace Integrity ]=================>>>'
lang_inter_make_file_dir_yes = 'Existing directory {}'
lang_inter_make_file_dir_make = 'Creating directory {}'
lang_inter_make_file_dir_suc = 'Directory {} created successfully!'
lang_inter_make_work_path_yes = 'Found working directory {}'
lang_inter_make_work_path_make = 'Creating working directory {}'
lang_inter_make_work_path_suc = 'Working directory {} created successfully!'
lang_inter_make_end = '<<<===================[ Workspace Validation Passed ]===================>>>'



lang_smi_began = '<<<==============[ Splitting Input Molecular Collection ]==============>>>'
lang_smi_suc = 'Molecules extracted >'
lang_smi_war = 'Warning: Please check or remove malformed files | Directory > ligand_smi | File:'
lang_smi_end = '<<<================[ Input File Splitting Completed ]==================>>>'
lang_smi_commend = 'Found commented molecules:'
lang_smi_summary_suc = 'Processed {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!'
lang_smi_summary_failure = '''\
Processed {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...'''



lang_smi_sing_began = '<<<===============[ Converting Molecules to .PDB Format ]===============>>>'
lang_smi_sing_commend = 'Found commented molecule:'
lang_smi_sing_suc = 'Successfully converted to .PDB > '
lang_smi_sing_err = '''\
Error: Conversion to .PDB failed!
Check: \033[95m{}\033[91m

           vvvvv Please rectify based on following errors! vvvvv
<<<=====================[ OpenBaBel Error Report: ]=====================>>>

{}
             ^^^^^ Please rectify based on above errors! ^^^^^
'''
lang_smi_sing_war = 'Warning: Malformed files detected | Directory > ligand_smi_single | File:'
lang_smi_sing_end = '<<<==============[ All Valid Molecules Converted to .PDB ]==============>>>'
lang_smi_sing_summary_suc = 'Converted {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!'
lang_smi_sing_summary_failure = '''\
Converted {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...'''



lang_pdb_began = '<<<=================[ Configuring Molecules as Ligands ]=================>>>'
lang_pdb_commend = 'Found commented molecule:'
lang_pdb_suc = 'Successfully converted to .PDBQT > '
lang_pdb_err = '''\
Error: Conversion to .PDBQT failed
Check: \033[95m{}\033[91m

           vvvvv Please rectify based on following errors! vvvvv
<<<==================[ Prepare_Ligand4 Error Report: ]==================>>>

{}
             ^^^^^ Please rectify based on above errors! ^^^^^
'''
lang_pdb_war = 'Warning: Malformed files detected | Directory > ligand_pdb | File:'
lang_pdb_end = '<<<===================[ All Valid Ligands Configured ]===================>>>'
lang_pdb_summary_suc = 'Converted {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!'
lang_pdb_summary_failure = '''\
Converted {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...'''



lang_dock_inter_name = 'Enter filename for this run (press Enter for default):'
lang_dock_workfile_began = '<<<==================[ Validating Workspace Integrity ]==================>>>'
lang_dock_pro_commend = 'Found commented protein:'
lang_dock_pdbqt_commend = 'Found commented ligand:'
lang_dock_fld_err = 'Error: Missing grid file for protein | Target:'
lang_dock_complex = 'Docking complex directory created:'
lang_dock_dlg = 'Primary conformation directory created:'
lang_dock_have_dlg = 'Existing conformation directory:'
lang_dock_mk_dlg = 'Complementing directories > Secondary conformation directory:'
lang_dock_mk_dlg_suc = 'Secondary conformation directory created:'
lang_dock_workfile_end = '<<<==================[ Workspace Validation Passed! ]===================>>>'
lang_dock_csv_began = '<<<=============[ Initializing Result Matrix & CSV Module ]=============>>>'
lang_dock_csv_end = '<<<================[ Result Matrix & CSV Module Ready! ]================>>>'
lang_dock_main_began = '''\
<<<==================[ Running Molecular Docking Core ]==================>>>\033[0m

Docking iterations per run: \033[92m{}
'''
lang_dock_mess = 'Docking attempt {} | Protein \033[96m{}\033[0m vs Ligand \033[95m{}\033[0m'
lang_dock_suc = 'Successful docking: \033[96m{}\033[92m & \033[95m{}\033[92m | Binding energy: {}'
lang_dock_err = '''\
Error: Docking failure!
Problematic ligand: \033[95m{}\033[91m

           vvvvv Please rectify based on following errors! vvvvv
<<<====================[ AutoDock-GPU Error Report: ]====================>>>

{}
             ^^^^^ Please rectify based on above errors! ^^^^^
'''
lang_dlg_err = '''\
Error: Optimal conformation extraction failed!
Problematic molecule: \033[95m{}\033[91m

           vvvvv Please rectify based on following errors! vvvvv
<<<=====[ BatchDock Conformation Extraction Module Error Report: ]=====>>>

{}
             ^^^^^ Please rectify based on above errors! ^^^^^
'''
lang_dock_war = 'Warning: Malformed files detected | Directory > ligand_pdbqt | File:'
lang_dock_complex_suc = 'Optimal conformation extracted! 3D complex structure generated.'
lang_dock_main_end = '<<<===================[ Molecular Docking Completed ]===================>>>'
lang_dock_csv_suc = 'All binding energies extracted and written to Excel:'
lang_dock_summary_suc = 'Completed {} docking attempts with 0 errors and 0 warnings\n    All tasks completed successfully!'
lang_dock_summary_failure = '''\
Completed {} docking attempts with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...'''



cheese_bonus = '''\
    Human: Kitty, you can has Cheese Burger
    Cat: Mua~
'''

nyan_cat_bonus = '''\
    Your small molecules seem to be numerous, and the docking process will take a long time. Come to this website to get some catalysts!
    https://www.bilibili.com/video/BV1vW411T7HM/?spm_id_from=333.337.search-card.all.click&vd_source=cacde7cc9cb211ea5af2636b44fc3c30
'''

homura_cat_bonus = '''\
    Your small molecules seem to be numerous, and the docking process will take a long time. Come to this website to get some catalysts!
    Homura-taru provides!!!
    https://www.bilibili.com/video/BV11x411c7xH?spm_id_from=333.788.recommend_more_video.10&vd_source=cacde7cc9cb211ea5af2636b44fc3c30
'''