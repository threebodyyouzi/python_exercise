import re
from collections import Counter
class Count():
    def __init__(self,patt):
        # self.path=path
        # self.patt=patt
        self.patt=re.compile(patt)
    #
    # def __str__(self):
    #     patt_dict = {}
    #     cpatt = re.compile(self.patt)
    #     with open(path) as fobj:
    #         for line in fobj:
    #             m = cpatt.search(line)
    #             if m:
    #                 key = m.group()
    #                 patt_dict[key] = patt_dict.get(key, 0) + 1
    #     return str(patt_dict)
    #
    # def count_patt(self,path):
    #     patt_dict = {}
    #     # cpatt = re.compile(self.patt)
    #     with open(path) as fobj:
    #         for line in fobj:
    #             m = self.patt.search(line)
    #             if m:
    #                 key = m.group()
    #                 patt_dict[key] = patt_dict.get(key, 0) + 1
    #     return patt_dict
    def count_patt(self,path):
        patt_dict={}
        result=Counter()
        with open(path) as fobj:
            for line in fobj:
                m=self.patt.search(line)
                if m:
                    key=m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1
                    result.update([m.group()])
        return result
if __name__ == '__main__':
    fname="/root/access_log"
    ip="^(\d+\.){3}(\d)"
    # print(Count(fname,ip))
    # print(Count.count_patt(fname))
    count_ip=Count(ip)
    print(count_ip.count_patt(fname))
    br="Chrome|Firefox|MSIE"
    count_br=Count(br)
    print(count_br.count_patt(fname))