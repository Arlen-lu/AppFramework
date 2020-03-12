import yaml
import os
import sys
sys.path.append(os.getcwd())

class GetTestDatas(object):
    
    def get_testdatas(self):
        with open('TestDatas/testdatas.yaml','r',encoding='utf-8') as f:
            datas = yaml.load(f.read(),Loader=yaml.SafeLoader)
            return datas

if __name__ == "__main__":
    getdatas = GetTestDatas()
    print(getdatas.get_testdatas()['invest_wrong'][0])