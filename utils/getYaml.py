import yaml
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml")

class getyaml:
    def __init__(self,filepath):
        filepath = os.path.join(BASE_DIR,filepath)
        self.path = filepath

    def get_yaml(self):
        '''
        加载yaml文件数据
        :param path: 文件路径
        :return:返回数据
        '''
        try:
            f = open(self.path,encoding='utf-8')
            data =yaml.load(f)
            f.close()
            return data
        except Exception as msg:
            print("异常消息-> {0}".format(msg))

    def alldata(self):
        """
        读取yaml文件数据
        :return: 返回数据
        """
        data =self.get_yaml()
        return data
    if __name__ == '__main__':
        path= "material_manage_video.yaml"
        a = get_yaml(self=path)
        print(a)
