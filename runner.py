import os
import pytest
from utils.readYaml import datas

pytest.main(['cases/test_login.py','--alluredir','./temp','-s'])
os.system('allure generate ./temp -o ./report --clean')