from mod import cayatools,settings

def login(db_dir,db_title,set):
    def login2(user_login):
        find_name = cayatools.search_file(db_dir,db_title)
        SKIP = settings.SKIP
        TESTACCOUT = settings.TESTACCOUNT

        if user_login in SKIP:
            logout_user = C_user(find_name('default'),set)
            return logout_user

        elif user_login in TESTACCOUT:
            test_user = C_user(user_login)
            return test_user

        else:
            print(settings.welcome)

            while 1:
                name=input('请输入账号>>')

                if name in SKIP:
                    logout_user = C_user(find_name('default'), set)
                    return logout_user

                else:
                    psw = input('请输入密码>>')
                    user_file_path = find_name(name)
                    # print(user_file_path)
                    if user_file_path == None:
                        print('密码错误或用户名错误')
                        continue
                    else:
                        user = C_user(user_file_path,set)
                        if user.lock == '0':
                            print('该用户已被锁定，请联系管理员！\n')
                            continue
                        else:
                            if  user.psw_match(psw):
                                print('密码正确')
                                return user
                            else:
                                print('密码错误或用户名错误')
    return login2

class C_user():
    def __init__(self,user_file_path,set):
        #paths
        self.path = user_file_path
        self.maue_file = '%s\\%s' % (user_file_path,set.MANUE_TITLE_FILE)      # 用户菜单文件
        self.pm_file = '%s\\%s' % (user_file_path,set.PM_FILE)                 # 用户权限文件
        self.info_file = '%s\\%s' % (user_file_path,set.INFO_FILE)             # 用户信息文件
        self.credit_file = '%s\\%s' % (user_file_path, set.CCA_FILE)           # 用户信用卡文件
        self.saving_file = '%s\\%s' % (user_file_path, set.SA_FILE)            # 用户储蓄账户文件
        self.log_file = '%s\\%s' % (user_file_path, set.LOG_FILE)              # 用户日志文件
        self.general_log = '%s\\%s' % (set.DB_DIR, set.GENERALLOG_FILE)              # 总账

        #infos
        self.type = cayatools.get_line_word('TYPE')(self.info_file)                     # 用户类型
        self.nick =  cayatools.get_line_word('NICK')(self.info_file)                     # 用户昵称
        self.name = cayatools.get_line_word('NAME')(self.info_file)                     # 用户账号
        self.lock = cayatools.get_line_word('LOCK')(self.info_file)                     # 用户登录锁

        #permissions
        self.pm1 = cayatools.get_line_word('PERMISSION1')(self.pm_file)            #用户权限(预留)
        self.pm2 = cayatools.get_line_word('PERMISSION2')(self.pm_file)
        self.pm3 = cayatools.get_line_word('PERMISSION3')(self.pm_file)
        self.sets = set

    def psw_match(self, patten):
        '''匹配关键字'''
        # print('match')
        psw_file = '%s\\%s' % (self.path, self.sets.PSW_FILE)  # 用户密码文件
        if not psw_file:
            return False
        else:
            decode = cayatools.try_decode
            code = decode(psw_file)
            with open(psw_file, encoding=code) as f:
                for line in f:
                    if patten == line.strip():
                        return True

    def reset_psw(self):
        psw_file = '%s\\%s' % (self.path, settings.PSW_FILE)  # 用户密码文件
        old = input('输入原密码:')
        if old in ['q','quit','QUIT','Q']:
            return
        if self.psw_match(old):
            while 1:
                new = input('输入新密码：')
                new_match = input('再次输入新密码：')
                if new == new_match:
                    print('开始修改',new)
                    cayatools.write_to_disk(psw_file, new)
                    print('修改成功！')
                    return
                else:
                    print('两次密码输入不一致，请重新输入')

    def reset_name(self):
        old = input('输入账户密码:')
        if self.psw_match(old):
            name = input('输入新的账户昵称：')
            set_info = cayatools.change_caya_value(self.info_file)
            set_info('NICK',name)
            print('修改成功！')





