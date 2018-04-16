import os
import sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #输出本项目路径
sys.path.append(base_dir)

# 把本项目目录写入配置文件，本应该是setup文件的工作，首次执行运行以下部分，之后请注释掉
db_dir = '%s\\%s' % (base_dir, 'home')
set_dir = '%s\\%s' % (base_dir,'config\\settings.py')
from mod import cayatools
cayatools.change_caya_value(set_dir)('DB_DIR','%r'%db_dir)

from core import main
if __name__ == '__main__':             #当本程序被执行，则…
    main.run()
