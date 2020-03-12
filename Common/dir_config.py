import os


#获取project的根目录
base_dir = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0]
dir_log = os.path.join(base_dir,'Outputs\TestLogs')
dir_report = os.path.join(base_dir,'Outputs\Reports')
dir_screen = os.path.join(base_dir,'Outputs\Screen_Shots')
dir_data = os.path.join(base_dir,'TestDatas')


print(base_dir)