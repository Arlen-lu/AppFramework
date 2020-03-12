import yaml
import os
import sys
sys.path.append(os.getcwd())

class GetCaps(object):
    def __init__(self):
        pass

    def get_caps(self):
        with open('Caps/caps.yaml','r',encoding='utf-8') as f:
            datas = yaml.load(f.read(),Loader=yaml.SafeLoader)
            # phone_info= datas[datas['inuse']]
            descired_caps =dict(datas[datas['inuse']['platform']],**datas[datas['inuse']['apk_name']])
            server_port = datas['inuse']['server_port']
            return [descired_caps,server_port]

    


if __name__ == "__main__":
    getcaps = GetCaps()
    data1 = getcaps.get_caps()
    print(data1)