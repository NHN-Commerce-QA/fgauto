import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Libs import webdriver
from Pages import ws_front_login
## TC_4
ds_front_login.ds_login()