import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Pages import ws_front_shopbag

# TC 6
ws_front_shopbag.ws_shopbag()

