from config import ver

# 定义旋转180°的转换函数：首先颠倒字符串，再对其中的字母进行映射转换
def rotate180(s):
    mapping = {
        'a': 'ɐ',
        'b': 'q',
        'c': 'ɔ',
        'd': 'p',
        'e': 'ǝ',
        'f': 'ɟ',
        'g': 'ƃ',
        'h': 'ɥ',
        'i': 'ᴉ',
        'j': 'ɾ̣',
        'k': 'ʞ',
        'l': 'ן',
        'm': 'ɯ',
        'n': 'u',
        'o': 'o',
        'p': 'd',
        'q': 'b',
        'r': 'ɹ',
        's': 's',
        't': 'ʇ',
        'u': 'n',
        'v': 'ʌ',
        'w': 'ʍ',
        'x': 'x',
        'y': 'ʎ',
        'z': 'z',
        # 大写字母映射
        'A': '∀',
        'B': 'ꓭ',  # 部分字体支持该字符
        'C': 'Ɔ',
        'D': 'ᗡ',
        'E': 'Ǝ',
        'F': 'Ⅎ',
        'G': '⅁',
        'H': 'H',
        'I': 'I',
        'J': 'ſ',  # 通常采用长s表示
        'K': 'ꓘ',
        'L': 'ꓶ',
        'M': 'W',
        'N': 'N',
        'O': 'O',
        'P': 'Ԁ',
        'Q': 'Ό',  # 没有绝对标准，可根据实际效果调整
        'R': 'ᴚ',
        'S': 'S',
        'T': '┴',
        'U': '∩',
        'V': 'Λ',
        'W': 'M',
        'X': 'X',
        'Y': '⅄',
        'Z': 'Z',
        # 数字映射
        '0': '0',
        '1': 'Ɩ',
        '2': 'ᄅ',
        '3': 'Ɛ',
        '4': 'ㄣ',
        '5': 'ϛ',
        '6': '9',
        '7': 'ㄥ',
        '8': '8',
        '9': '6',
        # 常用符号映射
        ',': '\'',
        '.': '˙',
        '?': '¿',
        '!': '¡',
        '[': ']',
        ']': '[',
        '(': ')',
        ')': '(',
        '{': '}',
        '}': '{',
        '<': '>',
        '>': '<',
        '&': '⅋',
        '_': '‾',
        ';': '؛',
        ':': ':',
        '"': '„',
        '\'': ','
    }
    return "".join(mapping.get(ch, ch) for ch in s[::-1])



lang_inter_describe = rotate180('''
                                                Welcome to the Batch Docking Program!  Version:[''' + ver + ''']  
GitHub_Link: https://github.com/magicabook/Batch_Docking--Automated_Workflow_Based_on_AutoDock-GPU.git
               Author: Magica_Book  Contact_Address: magica_book@qq.com   License: All rights reserved.
                                  Second Author: ZhuErding   Contact_Address: zhuerding@zhuerding.top
                                                                             Third Author: Rex   Miya ''')



lang_inter_select = rotate180('''
<<<=========================[ Mode Selection ]=========================>>>
[0] Settings Interface                                                    
[1] Split input .TXT into individual .SMILES molecules                    
[2] Convert .SMILES to .PDB format                                        
[3] Convert .PDB to .PDBQT ligand format                                   
[4] Run batch docking automation                                          
[a] Run full preprocessing workflow (Steps 1-3)                           
[b] Run complete docking pipeline (Steps 1-4)                             
[x] File complement                                                       
[z] Exit program                                                          ''')
lang_inter_function_number = rotate180('Please select the function to run:')
lang_inter_function_err = rotate180('Warning: Please enter a valid option!')
lang_inter_suc = rotate180('Selected workflow: {}')
lang_inter_select_1 = rotate180('Split input .TXT into individual .SMILES molecules')
lang_inter_select_2 = rotate180('Convert .SMILES to .PDB format')
lang_inter_select_3 = rotate180('Convert .PDB to .PDBQT ligand format')
lang_inter_select_4 = rotate180('Run batch docking automation')
lang_inter_select_a = rotate180('Run full preprocessing workflow (Steps 1-3)')
lang_inter_select_b = rotate180('Run complete docking pipeline (Steps 1-4)')
lang_inter_select_x = rotate180('File complement')
lang_inter_select_z = rotate180('Exit program')
lang_inter_quit = rotate180('Program terminated. Thank you for using!')
lang_return_list = rotate180('Returned to parent menu')

lang_inter_select_0 = rotate180('Settings Interface (Language & Docking Iterations)')
lang_inter_set = rotate180('''
[Mode Selection]-[Settings]:          
    [1] Language                      
    [2] Docking iterations per run    
    [3] Default result filename       
    [4] Docking seed                  
    [z] Return to main menu''')
lang_inter_set_select = rotate180('Select setting to configure:')
lang_inter_set_select_1 = rotate180('Language')
lang_inter_set_select_2 = rotate180('Set docking iterations')
lang_inter_set_select_3 = rotate180('Set default result filename')
lang_inter_set_select_4 = rotate180('Set docking seed')
lang_inter_set_select_z = rotate180('Return to main menu')
lang_inter_set_end = rotate180('Settings applied')

lang_inter_set_lang = rotate180('''
    \033[92m[z] Return to parent menu\033[0m
    Available language packs: \033[92m{}\033[0m

Select language:''')
lang_inter_set_lang_suc = rotate180('Language set to: ')

lang_inter_set_nrun = rotate180('''
    \033[92m[z] Return to parent menu\033[0m
    Current default docking iterations: \033[92m{}\033[0m
    Note: Integer input required

Enter default iterations per docking run:''')
lang_inter_set_nrun_suc = rotate180('Default iterations set to:')
lang_inter_set_nrun_war = rotate180('Warning: Integer required!')
lang_inter_set_nrun_none = rotate180('Warning: Please enter iteration count')

lang_inter_set_name = rotate180('''\
    \033[92m[z] Return to parent menu\033[0m
    Current default filename: \033[92m{}\033[0m
    Note: Use only underscores (_) as special characters

Enter default result filename:''')
lang_inter_set_name_suc = rotate180('Default filename set to:')

lang_inter_set_seed = rotate180('''
    \033[92m[z] Return to parent menu\033[0m
    Current default seed: \033[92m{}\033[0m
    Empty = AutoDock-GPU default (system time + process PID)
    Note: Integer or blank

Enter default seed:''')
lang_inter_set_seed_suc = rotate180('Default seed set to:')
lang_inter_set_seed_suc1 = rotate180('Seed restored to AutoDock-GPU default')
lang_inter_set_seed_war = rotate180('Warning: Enter integer or leave blank!')



lang_inter_make_began = rotate180('<<<=================[ Validating Workspace Integrity ]=================>>>')
lang_inter_make_file_dir_yes = rotate180('Existing directory {}')
lang_inter_make_file_dir_make = rotate180('Creating directory {}')
lang_inter_make_file_dir_suc = rotate180('Directory {} created successfully!')
lang_inter_make_work_path_yes = rotate180('Found working directory {}')
lang_inter_make_work_path_make = rotate180('Creating working directory {}')
lang_inter_make_work_path_suc = rotate180('Working directory {} created successfully!')
lang_inter_make_end = rotate180('<<<===================[ Workspace Validation Passed ]===================>>>')



lang_smi_began = rotate180('<<<==============[ Splitting Input Molecular Collection ]==============>>>')
lang_smi_suc = rotate180('Molecules extracted >')
lang_smi_war = rotate180('Warning: Please check or remove malformed files | Directory > ligand_smi | File:')
lang_smi_end = rotate180('<<<================[ Input File Splitting Completed ]==================>>>')
lang_smi_commend = rotate180('Found commented molecules:')
lang_smi_summary_suc = rotate180('Processed {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!')
lang_smi_summary_failure = rotate180('''\
Processed {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...''')



lang_smi_sing_began = rotate180('<<<===============[ Converting Molecules to .PDB Format ]===============>>>')
lang_smi_sing_commend = rotate180('Found commented molecule:')
lang_smi_sing_suc = rotate180('Successfully converted to .PDB > ')
lang_smi_sing_err = rotate180('''\
Error: Conversion to .PDB failed!
Check: \033[95m{}\033[91m

           vvvvv Please rectify based on following errors! vvvvv
<<<=====================[ OpenBaBel Error Report: ]=====================>>>

{}
             ^^^^^ Please rectify based on above errors! ^^^^^
''')
lang_smi_sing_war = rotate180('Warning: Malformed files detected | Directory > ligand_smi_single | File:')
lang_smi_sing_end = rotate180('<<<==============[ All Valid Molecules Converted to .PDB ]==============>>>')
lang_smi_sing_summary_suc = rotate180('Converted {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!')
lang_smi_sing_summary_failure = rotate180('''\
Converted {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...''')



lang_pdb_began = rotate180('<<<=================[ Configuring Molecules as Ligands ]=================>>>')
lang_pdb_commend = rotate180('Found commented molecule:')
lang_pdb_suc = rotate180('Successfully converted to .PDBQT > ')
lang_pdb_err = rotate180('''\
Error: Conversion to .PDBQT failed
Check: \033[95m{}\033[91m

           vvvvv Please rectify based on following errors! vvvvv
<<<==================[ Prepare_Ligand4 Error Report: ]==================>>>

{}
             ^^^^^ Please rectify based on above errors! ^^^^^
''')
lang_pdb_war = rotate180('Warning: Malformed files detected | Directory > ligand_pdb | File:')
lang_pdb_end = rotate180('<<<===================[ All Valid Ligands Configured ]===================>>>')
lang_pdb_summary_suc = rotate180('Converted {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!')
lang_pdb_summary_failure = rotate180('''\
Converted {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...''')



lang_dock_inter_name = rotate180('Enter filename for this run (press Enter for default):')
lang_dock_workfile_began = rotate180('<<<==================[ Validating Workspace Integrity ]===================>>>')
lang_dock_pro_commend = rotate180('Found commented protein:')
lang_dock_pdbqt_commend = rotate180('Found commented ligand:')
lang_dock_fld_err = rotate180('Error: Missing grid file for protein | Target:')
lang_dock_complex = rotate180('Docking complex directory created:')
lang_dock_dlg = rotate180('Primary conformation directory created:')
lang_dock_have_dlg = rotate180('Existing conformation directory:')
lang_dock_mk_dlg = rotate180('Complementing directories > Secondary conformation directory:')
lang_dock_mk_dlg_suc = rotate180('Secondary conformation directory created:')
lang_dock_workfile_end = rotate180('<<<==================[ Workspace Validation Passed! ]===================>>>')
lang_dock_csv_began = rotate180('<<<=============[ Initializing Result Matrix & CSV Module ]=============>>>')
lang_dock_csv_end = rotate180('<<<================[ Result Matrix & CSV Module Ready! ]================>>>')
lang_dock_main_began = rotate180('''\
<<<==================[ Running Molecular Docking Core ]==================>>>\033[0m

Docking iterations per run: \033[92m{}\033[0m
''')
lang_dock_mess = rotate180('Docking attempt {} | Protein \033[96m{}\033[0m vs Ligand \033[95m{}\033[0m')
lang_dock_suc = rotate180('Successful docking: \033[96m{}\033[92m & \033[95m{}\033[92m | Binding energy: {}')
lang_dock_err = rotate180('''\
Error: Docking failure!
Problematic ligand: \033[95m{}\033[91m

           vvvvv Please rectify based on following errors! vvvvv
<<<====================[ AutoDock-GPU Error Report: ]====================>>>

{}
             ^^^^^ Please rectify based on above errors! ^^^^^
''')
lang_dlg_err = rotate180('''\
Error: Optimal conformation extraction failed!
Problematic molecule: \033[95m{}\033[91m

           vvvvv Please rectify based on following errors! vvvvv
<<<=====[ BatchDock Conformation Extraction Module Error Report: ]=====>>>

{}
             ^^^^^ Please rectify based on above errors! ^^^^^
''')
lang_dock_war = rotate180('Warning: Malformed files detected | Directory > ligand_pdbqt | File:')
lang_dock_complex_suc = rotate180('Optimal conformation extracted! 3D complex structure generated.')
lang_dock_main_end = rotate180('<<<===================[ Molecular Docking Completed ]===================>>>')
lang_dock_csv_suc = rotate180('All binding energies extracted and written to Excel:')
lang_dock_summary_suc = rotate180('Completed {} docking attempts with 0 errors and 0 warnings\n    All tasks completed successfully!')
lang_dock_summary_failure = rotate180('''\
Completed {} docking attempts with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...''')



cheese_bonus = rotate180('''\
    Human: Kitty, you can has Cheese Burger
    Cat: Mua~
''')

nyan_cat_bonus = rotate180('''\
    Your small molecules seem to be numerous, and the docking process will take a long time. Come to this website to get some catalysts!
    https://www.bilibili.com/video/BV1vW411T7HM/?spm_id_from=333.337.search-card.all.click&vd_source=cacde7cc9cb211ea5af2636b44fc3c30
''')

homura_cat_bonus = rotate180('''\
    Your small molecules seem to be numerous, and the docking process will take a long time. Come to this website to get some catalysts!
    Homura-taru provides!!!
    https://www.bilibili.com/video/BV11x411c7xH?spm_id_from=333.788.recommend_more_video.10&vd_source=cacde7cc9cb211ea5af2636b44fc3c30
''')