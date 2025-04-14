lang_inter_describe = '''
恭迎大人使用批量對接之程式！ 版本號：[1.4.1]
項目之所在：https://github.com/magicabook/Batch_Docking--Automated_Workflow_Based_on_AutoDock-GPU.git
作者：附魔書  通訊之所：magica_book@qq.com  此程式之一切權益，悉皆保留。
明嘉靖廿一年乃生命科學之年矣。'''



lang_inter_select = '''
<<<=========================[ 模式揀選 ]==========================>>>
[0] 設置介面
[1] 僅將輸入之.txt拆分為獨立.smiles小分子
[2] 僅將單個.smiles小分子轉為.PDB格式
[3] 僅將.PDB格式之小分子轉為.PDBQT配體格式
[4] 僅行批量自動對接
[a] 行小分子前置處理之全程（ 1 ～ 3 ）
[b] 行分子對接之全過程（ 1 ～ 4 ）
[x] 文件補全
[z] 退程式'''
lang_inter_function_number = '請擇君所欲運之功能：'
lang_inter_function_err = '警告：宜輸正確參數！'
lang_inter_suc = '君所揀之作業模式為：{}'
lang_inter_select_1 = '僅將輸入之.txt拆分為獨立.smiles小分子'
lang_inter_select_2 = '僅將單個.smiles小分子轉為.PDB格式'
lang_inter_select_3 = '僅將.PDB格式之小分子轉為.PDBQT配體格式'
lang_inter_select_4 = '僅行批量自動對接'
lang_inter_select_a = '行小分子前置處理之全程（ 1 ～ 3 ）'
lang_inter_select_b = '行分子對接之全過程（ 1 ～ 4 ）'
lang_inter_select_x = '文件補全'
lang_inter_select_z = '退程式'
lang_inter_quit = '程式既退，謝君惠顧！'
lang_return_list = '已還返上層目錄'

lang_inter_select_0 = '設置介面\n'
lang_inter_set = '''\
[模式選擇]－[設置介面]:
    [1] 語言
    [2] 單次對接迭代次數
    [3] 預設結果檔名
    [4] 對接程式運行之種子
    [z] 還返上層目錄'''
lang_inter_set_select = '請擇所欲設之內容：'
lang_inter_set_select_1 = '語言'
lang_inter_set_select_2 = '設置單次對接迭代次數'
lang_inter_set_select_3 = '設置預設結果檔名'
lang_inter_set_select_4 = '設置對接程式運行之種子'
lang_inter_set_select_z = '還返上層目錄'
lang_inter_set_end = '設置已應用'

lang_inter_set_lang = '''
    \033[92m[z] 還返上層目錄\033[0m
    有存之語言包列表：\033[92m{}\033[0m

請擇所欲之語言：'''
lang_inter_set_lang_suc = '語言設定成功，為：'

lang_inter_set_nrun = '''
    \033[92m[z] 還返上層目錄\033[0m
    先前程式預定之單次對接迭代次數為 \033[92m{}\033[0m
    請注：宜輸整數

請輸於一對分子對接之作業中君所欲之預設迭代次數：'''
lang_inter_set_nrun_suc = '預設對接次數設定成功，為：'
lang_inter_set_nrun_war = '警告：宜輸整數'
lang_inter_set_nrun_none = '警告：請輸對接次數'

lang_inter_set_name = '''
    \033[92m[z] 還返上層目錄\033[0m
    先前程式所定之結果檔名為 \033[92m{}\033[0m
    請注：檔名毋用下劃線 _ 之外之異字

請輸君欲之預設結果檔名：'''
lang_inter_set_name_suc = '預設結果檔名定矣，為：'

lang_inter_set_seed = '''
    \033[92m[z] 還返上層目錄\033[0m
    先前程式所定之種子為 \033[92m{}\033[0m
    如空留，則用AutoDock-GPU程式預設之種子（系統時刻加進程PID）
    請注：宜輸整數

請輸君所欲之預設種子：'''
lang_inter_set_seed_suc = '預設種子定矣，為：'
lang_inter_set_seed_suc1 = '種子已復原為AutoDock-GPU預設之值'
lang_inter_set_seed_war = '警告：宜輸整數或空留（直接回車）！'



lang_inter_make_began = '<<<====================[ 正審工作目錄之完善否 ]====================>>>'
lang_inter_make_file_dir_yes = '目錄 {} 已存'
lang_inter_make_file_dir_make = '正建目錄 {}'
lang_inter_make_file_dir_suc = '目錄 {} 已建成！'
lang_inter_make_work_path_yes = '工作目錄 {} 已覓得'
lang_inter_make_work_path_make = '正建工作目錄 {}'
lang_inter_make_work_path_suc = '工作目錄 {} 建成矣！'
lang_inter_make_end = '<<<======================[ 工作目錄完善否審核通矣 ]=====================>>>'



lang_smi_began = '<<<===================[ 正審拆分輸入之小分子集 ]===================>>>'
lang_smi_suc = '小分子已擷取 >'
lang_smi_war = '警告：請審核或清除格式失誤之檔，處於目錄 > ligand_smi 之案：'
lang_smi_end = '<<<=======================[ 輸入檔拆分完畢 ]=======================>>>'
lang_smi_commend = '覓得所註解之小分子集：'
lang_smi_summary_suc = '此次作業共擷取 {} 分子，無錯誤、無警告，圓滿遂志！'
lang_smi_summary_failure = '''\
此次作業共擷取 {} 分子，生 {} 錯誤及 {} 警告
君可閱終端紅錯及黃警，以知是何故生
若欲求援，請將終端之相關輸出轉交彼方，毋以窗內照或擷圖相付……'''



lang_smi_sing_began = '<<<===================[ 正審轉換小分子為.PDB格式 ]===================>>>'
lang_smi_sing_commend = '覓得所註解之小分子：'
lang_smi_sing_suc = '該小分子轉為.PDB格式已成 > '
lang_smi_sing_err = '''\
錯誤：該小分子轉為.PDB未成！
請檢： \033[95m{}\033[91m

                  vvvvv 請據下列報錯宜行整頓！ vvvvv
<<<==================[ OpenBaBel程式所出錯報： ]==================>>>

{}
                  ^^^^^ 請據上報錯宜行整頓！ ^^^^^
'''
lang_smi_sing_war = '警告：請審或清格式失誤之檔，處於目錄 > ligand_smi_single 之案：'
lang_smi_sing_end = '<<<==================[ 合格小分子皆轉為.PDB格式 ]==================>>>'
lang_smi_sing_summary_suc = '此次作業共轉換 {} 分子，零錯零警，圓滿遂志！'
lang_smi_sing_summary_failure = '''\
此次作業共轉換 {} 分子，生 {} 錯誤及 {} 警告
君可閱終端紅錯及黃警，以知是何因生
若欲求援，請將終端相關輸出轉付他人，毋以窗中照或擷圖相付……'''



lang_pdb_began = '<<<======================[ 正審設小分子為配體 ]======================>>>'
lang_pdb_commend = '覓得所註解之小分子：'
lang_pdb_suc = '該小分子轉為.PDBQT格式已成 > '
lang_pdb_err = '''\
錯誤：該小分子轉為.PDBQT未成
請檢： \033[95m{}\033[91m

                  vvvvv 請據下列報錯宜行整頓！ vvvvv
<<<===============[ Prepare_Ligand4程式所出錯報： ]===============>>>

{}
                  ^^^^^ 請據上報錯宜行整頓！ ^^^^^
'''
lang_pdb_war = '警告：請審或清格式失誤之檔，處於目錄 > ligand_pdb 之案：'
lang_pdb_end = '<<<===================[ 合格小分子皆設為配體 ]===================>>>'
lang_pdb_summary_suc = '此次作業共轉換 {} 分子，零錯零警，圓滿遂志！'
lang_pdb_summary_failure = '''\
此次作業共轉換 {} 分子，生 {} 錯誤及 {} 警告
君可閱終端紅錯與黃警，以識原由
若欲求援，請將終端相關輸出轉付彼方，毋以窗中照或擷圖相付……'''



lang_dock_inter_name = '請為此次作業之結果檔命名，若用預設名，則按回車：'
lang_dock_workfile_began = '<<<=====================[ 正審校工作目錄完善否 ]=====================>>>'
lang_dock_pro_commend = '覓得所註蛋白：'
lang_dock_pdbqt_commend = '覓得所註小分子：'
lang_dock_fld_err = '錯誤：未覓該蛋白之網格檔！ 問題蛋白名：'
lang_dock_complex = '最優對接合體之存目錄已建，名曰：'
lang_dock_dlg = '小分子構象之首目錄已建，名曰：'
lang_dock_have_dlg = '小分子構象目錄已存：'
lang_dock_mk_dlg = '正補目錄以全：小分子構象之次目錄：'
lang_dock_mk_dlg_suc = '小分子構象之次目錄已建，名曰：'
lang_dock_workfile_end = '<<<=====================[ 工作目錄完善否審校通矣！ ]=====================>>>'
lang_dock_csv_began = '<<<===================[ 正審初設結果矩陣與CSV模組 ]===================>>>'
lang_dock_csv_end = '<<<=====================[ 結果矩陣與CSV模組就緒！ ]=====================>>>'
lang_dock_main_began = '''\
<<<=====================[ 正行分子對接主程式 ]=====================>>>\033[0m

單次對接迭代次數為：\033[92m{}\033[0m
'''
lang_dock_mess = '正行第 {} 次對接：工作蛋白 \033[96m{}\033[0m 對接小分子 \033[95m{}\033[0m'
lang_dock_suc = '蛋白 \033[96m{}\033[92m 與小分子 \033[95m{}\033[92m 對接成功！最優構象之結合自由能為：{}'
lang_dock_err = '''\
錯誤：一次對接失誤！
問題分子： \033[95m{}\033[91m

                  vvvvv 請據下列報錯宜行整頓！ vvvvv
<<<=================[ AutoDock-GPU程式所出錯報： ]=================>>>

{}
                  ^^^^^ 請據上報錯宜行整頓！ ^^^^^
'''
lang_dlg_err = '''\
錯誤：最優構象提取未成！
問題分子： \033[95m{}\033[91m

                  vvvvv 請據下列報錯宜行整頓！ vvvvv
<<<===============[ BatchDock構象提取模組出錯報： ]===============>>>

{}
                  ^^^^^ 請據上報錯宜行整頓！ ^^^^^
'''
lang_dock_war = '警告：請審或清除格式失誤之檔，處於目錄 > ligand_pdbqt 之案：'
lang_dock_complex_suc = '最優構象提取成矣，合體3D構造已成！'
lang_dock_main_end = '<<<===================[ 分子對接主程式運行畢矣 ]=====================>>>'
lang_dock_csv_suc = '各最優構象之自由能已擷取並入Excel，檔名為'
lang_dock_summary_suc = '此次作業共行 {} 次對接，無錯誤、無警告，圓滿遂志！'
lang_dock_summary_failure = '''\
此次作業共行 {} 次對接，生 {} 錯誤及 {} 警告
君可閱終端紅錯及黃警，以知故因
若欲求援，請轉交終端相關輸出，毋以窗內照或擷圖相付……'''



cheese_bonus = '''\
    人：“狸，食堡。”
    猫：“善哉”
'''

nyan_cat_bonus = '''\
    汝之小分子似多，分子對接所需之時日較長，速來此網頁取些催化劑吧！
    https://www.bilibili.com/video/BV1vW411T7HM/?spm_id_from=333.337.search-card.all.click&vd_source=cacde7cc9cb211ea5af2636b44fc3c30
'''

homura_cat_bonus = '''\
    汝之小分子似多，分子對接所需之時日較長，速來此網頁取些催化劑吧！
    吼姆拉特供！！！
    https://www.bilibili.com/video/BV11x411c7xH?spm_id_from=333.788.recommend_more_video.10&vd_source=cacde7cc9cb211ea5af2636b44fc3c30
'''