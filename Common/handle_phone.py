import random
"""
第一行   移动
第二行   联通
第三行   电信
第四行   中国广电
"""

prefix=[
    134,135,136,137,138,139,144,147,148,150,151,152,157,158,159,178,182,183,184,187,188,195,197,198,

    130,131,132,140,145,146,155,156,166,167,175,176,185,186,

    133,141,149,153,173,177,180,181,189,191,193,199,

    192
]

def get_new_phone():


    #随机一个下标用于  取 手机号前缀
    index=random.randint(0,len(prefix)-1)
    #手机前缀
    phone=str(prefix[index])

    #后缀
    for i in range(8):

        phone+=str(random.randint(0,9))

    return phone