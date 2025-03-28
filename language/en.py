lang_smi_began = '<<<===============[ Validating Workspace Integrity ]===============>>>'
lang_smi_suc = 'Molecules extracted >'
lang_smi_war = 'Warning: Please check or remove malformed files | Directory > ligand_smi | File:'
lang_smi_end = '<<<==============[ Input File Splitting Completed ]================>>>'
lang_smi_commend = 'Found commented molecules:'
lang_smi_summary_suc = 'Processed {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!'
lang_smi_summary_failure = '''\
Processed {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...'''

lang_smi_sing_began = '<<<============[ Converting Molecules to .PDB Format ]============>>>'
lang_smi_sing_commend = 'Found commented molecule:'
lang_smi_sing_suc = 'Successfully converted to .PDB > '
lang_smi_sing_err = '''\
Error: Conversion to .PDB failed!
Check: \033[95m{}\033[91m
vvvvv Please rectify based on following errors vvvvv
<<<==================[ OpenBaBel Error Report: ]==================>>>
{}
^^^^^ Please rectify based on above errors ^^^^^'''
lang_smi_sing_war = 'Warning: Malformed files detected | Directory > ligand_smi_single | File:'
lang_smi_sing_end = '<<<===========[ All Valid Molecules Converted to .PDB ]===========>>>'
lang_smi_sing_summary_suc = 'Converted {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!'
lang_smi_sing_summary_failure = '''\
Converted {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...'''

lang_pdb_began = '<<<=============[ Configuring Molecules as Ligands ]==============>>>'
lang_pdb_commend = 'Found commented molecule:'
lang_pdb_suc = 'Successfully converted to .PDBQT > '
lang_pdb_err = '''\
Error: Conversion to .PDBQT failed
Check: \033[95m{}\033[91m
vvvvv Please rectify based on following errors vvvvv
<<<==============[ Prepare_Ligand4 Error Report: ]================>>>
{}
^^^^^ Please rectify based on above errors ^^^^^'''
lang_pdb_war = 'Warning: Malformed files detected | Directory > ligand_pdb | File:'
lang_pdb_end = '<<<===============[ All Valid Ligands Configured ]================>>>'
lang_pdb_summary_suc = 'Converted {} molecules with 0 errors and 0 warnings\n    All tasks completed successfully!'
lang_pdb_summary_failure = '''\
Converted {} molecules with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...'''

lang_dock_workfile_began = '<<<==============[ Validating Workspace Integrity ]===============>>>'
lang_dock_pro_commend = 'Found commented protein:'
lang_dock_pdbqt_commend = 'Found commented ligand:'
lang_dock_fld_err = 'Error: Missing grid file for protein | Target:'
lang_dock_complex = 'Docking complex directory created:'
lang_dock_dlg = 'Primary conformation directory created:'
lang_dock_have_dlg = 'Existing conformation directory:'
lang_dock_mk_dlg = 'Complementing directories > Secondary conformation directory:'
lang_dock_mk_dlg_suc = 'Secondary conformation directory created:'
lang_dock_workfile_end = '<<<===============[ Workspace Validation Passed! ]================>>>'
lang_dock_csv_began = '<<<=========[ Initializing Result Matrix & CSV Module ]===========>>>'
lang_dock_csv_end = '<<<=============[ Result Matrix & CSV Module Ready! ]=============>>>'
lang_dock_main_began = '<<<==============[ Running Molecular Docking Core ]===============>>>'
lang_dock_mess = 'Docking attempt {} | Protein \033[96m{}\033[0m vs Ligand \033[95m{}\033[0m'
lang_dock_suc = 'Successful docking: \033[96m{}\033[92m & \033[95m{}\033[92m | Binding energy: {}'
lang_dock_err = '''\
Error: Docking failure!
Problematic ligand: \033[95m{}\033[91m
vvvvv Please rectify based on following errors vvvvv
<<<================[ AutoDock-GPU Error Report: ]=================>>>
{}
^^^^^ Please rectify based on above errors ^^^^^'''
lang_dock_war = 'Warning: Malformed files detected | Directory > ligand_pdbqt | File:'
lang_dock_complex_suc = 'Optimal conformation extracted! 3D complex structure generated.'
lang_dock_main_end = '<<<================[ Molecular Docking Completed ]================>>>'
lang_dock_csv_suc = 'All binding energies extracted and written to Excel:'
lang_dock_summary_suc = 'Completed {} docking attempts with 0 errors and 0 warnings\n    All tasks completed successfully!'
lang_dock_summary_failure = '''\
Completed {} docking attempts with {} errors and {} warnings
Check terminal for RED errors and YELLOW warnings
When seeking help, please share terminal output instead of window screenshots...'''