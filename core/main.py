
from mod import cayatools,access,cayamaue
from core import job
from config import settings



#for test skip access:

skip = 'skip'
user_test = None
login = access.login(settings.DB_DIR,settings.PROCESS_PATH_TITLE,settings)

@cayatools.timeout(settings.TOTAL_TIME_OUT)  #总超时，但仅提示，没什么卵用
def run():
    '''主运行程序'''
    exit_mark = 0
    while 1:
        if exit_mark == 1:
            break
        else:
            user = login(user_test)
            exit_mark = cayamaue.maue_main(user,job.option_tab)
            user = None

