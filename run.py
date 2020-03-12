import os
import sys
sys.path.append(os.getcwd())
from Common import dir_config
import pytest
import time


test_log = os.path.join(dir_config.dir_log,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+'-test_log.txt')
test_report = os.path.join(dir_config.dir_report,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+'-test_report.html')
mark_name = 'testinvest'
text = '-m {} -s'.format(mark_name)
text1 = '--capture=no'
# text_rerun = '--reruns 2'
text_log = '--report-log={}'.format(test_log)
text_report = '--html={}'.format(test_report)
# pytest.main([text,text1,text_log,text_report])
pytest.main()
# for i in range(1,10):
#     pytest.main([text,text1,text_log,text_report])
#     time.sleep(5)

