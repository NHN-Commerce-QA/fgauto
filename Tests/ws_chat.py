import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Libs import webdriver
from Pages import ws_front_chat
## TC_4
ws_front_chat.ws_chat()