import sys, os # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Pages import ws_front_consolidate_order

# TC 19
ws_front_consolidate_order.ws_consolidate_order()