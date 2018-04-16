from config import settings
from core import cayatools

class short_user():
    def __init__(self,user_file_path):
        self.path = user_file_path
        self.pm_file = '%s\\%s' % (user_file_path,settings.PM_FILE)                 # 用户权限文件
        self.info_file = '%s\\%s' % (user_file_path,settings.INFO_FILE)             # 用户信息文件
        self.credit_file = '%s\\%s' % (user_file_path, settings.CCA_FILE)           # 用户信用卡文件

        self.name = cayatools.get_line_word('NAME')(self.info_file)                 # 用户账号
        self.lock = cayatools.get_line_word('LOCK')(self.info_file)                 # 用户登录锁
        self.type = cayatools.get_line_word('TYPE')(self.info_file)                 # 用户类型
        self.rmb_total_limit = cayatools.get_line_word('TOTAL_LIMIT_RMB')(self.credit_file)       # 人民币总额度
        self.rmb_current_limit = cayatools.get_line_word('CREDIT_LIMIT_RMB')(self.credit_file)    # 人民币目前额度
        self.usd_total_limit = cayatools.get_line_word('TOTAL_LIMIT_USD')(self.credit_file)       # 美元总额度
        self.usd_current_limit = cayatools.get_line_word('CREDIT_LIMIT_USD')(self.credit_file)    # 美元目前额度

        #permissions
        self.pm1 = cayatools.get_line_word('PERMISSION1')(self.pm_file)                  #用户权限(预留)
        self.pm2 = cayatools.get_line_word('PERMISSION2')(self.pm_file)
        self.pm3 = cayatools.get_line_word('PERMISSION3')(self.pm_file)


    def admin_reset_psw(self):
        psw_file = '%s\\%s' % (self.path, settings.PSW_FILE)  # 用户密码文件
        do = input('该用户密码将被重置为初始密码，是否继续（yes）?')
        if do in ['yes']:
            cayatools.write_to_disk(psw_file, 'abc123')
            print('修改成功！')
