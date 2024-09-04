import pytest
import os

from Test.Interface.Common.handle_data import replace_case_by_regular
from Test.Interface.Common.handle_data_from_response import data_from_response
from Test.Interface.Common.handle_excel import HandleExcel
from Test.Interface.Common.handle_path import data_dir
from Test.Interface.Common.handle_request import send_request

filename=os.path.join(data_dir,'萤火商城接口自动化测试用例.xlsx')
excel=HandleExcel(filename,'收货地址模块业务流')
data=excel.read_datas()

class TestAddressBusiness():

    @pytest.mark.parametrize('case',data)
    def test(self,case):
        # 1. 替换数据---#变量#
        case=replace_case_by_regular(case)
        #2. 发送接口请求
        res = send_request(case['url'],case['method'],case['data'],case['json_type'],case['login_status'])
        #3. 是否需要提取值，放入  全局变量中
        if case['jsonpath']:
            data_from_response(res.json(),case['jsonpath'])
