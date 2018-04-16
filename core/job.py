from mod import cayatools
from config import settings
import time

QUIT = settings.SKIP

def option_tab():
    option_tab = {
        #子菜单选项
        "子菜单 储蓄账户": ('savings account', 'SAVINGS_MAUE'),  # 理论上支持无限个子菜单
        "子菜单 信用卡账户": ('credit card account', 'CRADIT_CARD_MAUE'),
        "子菜单 取款": ('draw', 'DRAW_MAUE'),
        "子菜单 存款": ('deposit', 'DEPOSIT_MAUE'),
        "子菜单 转账": ('transfer', 'TRANSFER_MAUE'),
        "子菜单 账单": ('bills', 'CRADIT_CARD_BILL'),
        "子菜单 设置": ('credit card settings', 'CRADIT_CARD_SETTINGS'),
        '子菜单 还款': ('repay now', 'REPAY_NOW'),
        '子菜单 还款': ('views', 'VIEWS'),

        # 储蓄卡账户
        '查看余额': ('show balance',show_balance()),
        '查看账单': ('show user logs', show_logs()),
        '美元取款': ('draw(USD)',draw('USD')),
        '人民币取款': ('draw(RMB)', draw('RMB')),
        '人民币存款': ('deposit(RMB)', deposit('RMB')),
        '美元存款': ('deposit(USD)', deposit('USD')),
        '人民币转账': ('transfer(RMB)', transfer('RMB')),
        '美元转账': ('transfer(USD)',transfer('USD')),

        # 信用卡账户
        '查看人民币账单': ('current bill(RMB)', show_bill_info('RMB')),
        '查看美元账单': ('current bill(USD)', show_bill_info('USD')),
        '自动还款账户': ('set repay account', set_repayment('REPAY_ACCOUNT')),
        '美元立即还款': ('repay USD account',repay_now('USD')),
        '人民币立即还款': ('repay RMB account', repay_now('RMB')),
        '设置出账时间': ('set bill accout day', set_repayment('ACCOUNT_DAY')),
        # 邮寄账单是另外一个工作系统执行，本软件系统只作文件修改
        # administrator operation
        '添加账户': ('add user', adduser()),
        '设置额度': ('set user limit', admin_work('set limit')),
        '冻结账户': ('freeze user', admin_work('freeze user')),
        '解锁账户': ('unlock user', admin_work('unlock user')),
        '查看总账': ('transaction records', show_general_logs()),
        '查看用户信息表': ('account information tab', admin_work('view')),
        '重置目标用户密码': ('reset n_user password', admin_work('reset password'))
    }
    return option_tab

def write_log_file(filepath):
    def write_values(a,b,c,d,e,f):

        import time
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).strip()
        encode = cayatools.try_decode(filepath)
        new_log = settings.LOG_FORMAT.format(time_now,a,b,c,d,e,f)

        with open(filepath,'a',encoding=encode) as f:
            f.write(new_log)

    return write_values

def show_balance():
    '''查看余额'''
    def wapper(user):
        # print(user.saving_file)
        get_baleace = cayatools.get_line_file(user.saving_file)
        balacne_RMB = get_baleace('RMB')
        balacne_USD = get_baleace('USD')
        print('您的账户余额为：\n 人民币：￥%s\n 美元：$%s'%(balacne_RMB,balacne_USD))
        input('继续请输入任意字符>>')
    return wapper

def view_logs(work):
    def view_logs2():
        '''查看账单'''
        def wapper(user):
            # print(user.saving_file)
            read_file = cayatools.read_to_memory
            if work == 'user log':
                shows = read_file(user.log_file)
            elif work == 'general log':
                shows = read_file(user.general_log)
            for line in shows:
                print(line.strip())
            input('任意按键继续\n')
        return wapper
    return view_logs2

show_logs = view_logs('user log')
show_general_logs = view_logs('general log')

def saving_acount_work(work):
    def wapper1(currency):
        def wapper2(user):
            '''取款'''
            # print(user.saving_file)
            get_baleace = cayatools.get_line_file(user.saving_file)
            change_value = cayatools.change_caya_value(user.saving_file)
            get_info = cayatools.get_line_file(user.credit_file)
            set_credit_card_value = cayatools.change_caya_value(user.credit_file)
            log = write_log_file(user.log_file)
            general_log = write_log_file(user.general_log)
            YES = ['YES','yes']

            while 1:
                balacne = get_baleace(currency)
                print('您目前的储蓄账户%s余额为：%s元' % (currency, balacne))

                if work == 'draw':
                    draw_now = input('请输入您要取款的金额：')
                    new_balace = int(balacne) - int(draw_now)
                    work_value = draw_now
                    target_user = user.name
                    if new_balace < 0:
                        print('余额不足，请重新输入')
                        continue

                elif work == 'deposit':
                    deposit_now = input('请输入您要存款的金额：')
                    new_balace = int(balacne) + int(deposit_now)
                    work_value = deposit_now
                    target_user = user.name

                elif work == 'transfer':
                    target_user = input('请输入转入账号,核对无误请按ENTER：')
                    transfer_now = input('请输入您要转账的金额：')
                    new_balace = int(balacne) - int(transfer_now)
                    work_value = transfer_now
                    if new_balace < 0:
                        print('余额不足，请重新输入')
                        continue

                elif work == 'repayment':
                    bill_currency = 'CURRENT_BILL_%s' %(currency)
                    credit_card_balace_currency = 'BALANCE_%s' %(currency)

                    bill = get_info(bill_currency)
                    c_balance = get_info(credit_card_balace_currency)
                    print('您的本期%s账单总额为：%s元'%(currency,bill))
                    repay = input('请输入你要还款的金额：')
                    if repay in settings.ALL:
                        repay = bill
                    new_bill = int(bill) - int(repay) if int(bill) > int(repay) else 0
                    new_ccd_balace = int(c_balance) if int(bill) > int(repay) else \
                        int(c_balance) + (int(repay) - int(bill))  # 还多了就计入账户里
                    new_balace = int(balacne) - int(repay)

                    #下面留到自动还款用，主动还款是不会扣除信用卡账户余额的
                    # new_ccd_balace = int(c_balance) - int(repay) if int(repay) < int(c_balance) else 0
                    # new_balace = int(balacne) - (int(repay) - int(c_balance)) \
                    #     if int(repay) > int(c_balance) else int(balacne)

                    if new_balace < 0:
                        print('余额不足')
                        continue

                    set_credit_card_value(bill_currency,new_bill)
                    set_credit_card_value(credit_card_balace_currency, new_ccd_balace)

                    target_user = user.name
                    ccd_user = '%s:%s:%s'%(user.name,'ccd',currency)
                    work_value = (int(repay) - int(c_balance))if int(repay) > int(c_balance) else 0

                    log(work, ccd_user, repay, bill, new_bill, user.name)
                    general_log(work, ccd_user, repay, bill, new_bill, user.name)


                #修改文件
                print('请稍候。。。')
                change_value(currency, str(new_balace))

                #记录日志
                target_log = '%s:%s'%(target_user,currency)
                log(work,target_log, work_value, balacne, new_balace, user.name)
                general_log(work,target_log,work_value, balacne, new_balace, user.name)

                time.sleep(5)

                print('您目前的%s余额为：%s元' % (currency,get_baleace(currency)))
                continue_or_not = input('请问是否继续？(继续请输入yes):')
                if continue_or_not not in YES:
                    break
        return wapper2
    return wapper1

 #四个内容相近的函数，为了不全部修改原来的代码，就这样写了
draw = saving_acount_work('draw')
deposit =  saving_acount_work('deposit')
transfer =  saving_acount_work('transfer')
repay_now = saving_acount_work('repayment')

def show_bill_info(currency):
    '''查看账单信息'''
    def wapper(user):
        get_info = cayatools.get_line_file(user.credit_file)

        bill = get_info('CURRENT_BILL_%s' % (currency))
        limit = get_info('CREDIT_LIMIT_%s' % (currency))
        total_limit = get_info('TOTAL_LIMIT_%s' % (currency))
        remaining = get_info('BALANCE_%s' % (currency))

        account_day = get_info('ACCOUNT_DAY')
        auto_repay_day = get_info('AUTO_REPAYMENT_DAY')
        last_repay_day = get_info('LAST_REPAYMENT_DAY')
        repay_acount = get_info('REPAY_ACCOUNT')

        for_print = settings.BILL_FORMAT.format(\
            currency,bill,limit,total_limit,account_day,last_repay_day,auto_repay_day,repay_acount,remaining)
        print(for_print)
        input('任意按键继续\n')
    return wapper

def set_repayment(word):
    '''定期还款'''
    def wapper(user):
        get_info = cayatools.get_line_file(user.credit_file)
        set_value = cayatools.change_caya_value(user.credit_file)

        if word == 'ACCOUNT_DAY' :
            print(get_info(word))
            value = input('请输入自动结账的日期：')
        elif word == 'REPAY_ACCOUNT' :
            print(get_info(word))
            value = input('请输入自动还款的储蓄账户：')
        elif word == '':
            print(get_info(word))
            value = input('请输入需要修改的值：')
        if value in QUIT:
            return
        else:
            set_value(word, value)
            print('修改成功！')
    return wapper



def admin_work(work_type):
    def wapper(user):
        from core import classes
        import os
        print('用户类型：',user.type)
        if user.type != 'ADMIN':
            print('权限不足！')
            return
        else:
            print('权限认证成功！')
            db_dir = settings.DB_DIR
            g = os.walk(db_dir)
            next(g)
            paths = []
            user_tab = []
            for line in g:
                paths.append(line[0])
            for user_path in paths:
                user_tab.append(classes.short_user(user_path))


            line = settings.USER_INFO_FORMAT.format('user name',
                                                    'access lock',
                                                    'user type',
                                                    'RMB limit',
                                                    'USD limit')
            print(line)
            print('%s'%('='*58))
            for user_short in user_tab:
                if user_short.type == 'ADMIN':
                    continue
                else:
                    line = settings.USER_INFO_FORMAT.format(user_short.name,
                                                            user_short.lock,
                                                            user_short.type,
                                                            user_short.rmb_total_limit,
                                                            user_short.usd_total_limit)
                    print(line)

            if work_type == 'view':
                input('任意按键继续>>')

            elif work_type in['freeze user','unlock user']:
                while 1:
                    if work_type == 'freeze user':
                        user_name = input('输入你要冻结的用户:')
                        lock = 0
                    elif work_type == 'unlock user':
                        user_name = input('输入你要解锁的用户:')
                        lock = 3

                    if user_name in QUIT:
                        return

                    for user_short in user_tab:
                        if user_short.name == user_name:
                            freeze = cayatools.change_caya_value(user_short.info_file)
                            freeze('LOCK',lock)
                            print('操作成功')
                            return

                    print('用户不存在')

            elif work_type == 'set limit':
                while 1:
                    user_name = input('输入你要设置的用户:')
                    if user_name in QUIT:
                        return

                    currency = input('输入你要设置的货币类型(USD/RMB):')
                    if currency not in ['USD','RMB']:
                        print('货币类型输入错误')
                        continue

                    for user_short in user_tab:
                        if user_short.name == user_name:
                            new_total_limit = input('输入新的额度:')
                            set_limit = cayatools.change_caya_value(user_short.credit_file)

                            if currency == 'RMB':
                                old_total_limit = user_short.rmb_total_limit
                                set_limit('TOTAL_LIMIT_RMB', new_total_limit)
                                old_limit = user_short.rmb_current_limit
                                new_limit = int(new_total_limit)-int(old_total_limit)+int(old_limit)
                                set_limit('CREDIT_LIMIT_RMB', new_limit)
                                print('设置成功！')
                                return

                            elif currency == 'USD':
                                old_total_limit = user_short.usd_total_limit
                                set_limit('TOTAL_LIMIT_USD', new_total_limit)
                                old_limit = user_short.usd_current_limit
                                new_limit = int(new_total_limit)-int(old_total_limit)+int(old_limit)
                                set_limit('CREDIT_LIMIT_USD', new_limit)
                                print('设置成功！')
                                return

                    print('用户不存在')

            elif work_type == 'reset password':
                while 1:
                    user_name = input('输入你要重置的用户:')
                    for user_short in user_tab:
                        if user_short.name == user_name:
                            user_short.admin_reset_psw()
                            return
                    print('用户不存在')

    return wapper


def adduser():
    '''添加账户'''
    def wapper(user):
        import shutil
        import os
        from core import cayatools
        while 1:
            new_account = input('输入新的账户名：')
            if new_account in settings.SKIP:
                break

            DB_DIR = 'E:\\PycharmProjects\\py_fullstack\\3.函数\\作业\\ATM\\home'
            tar = '%s\\%s' % (DB_DIR, 'normal')
            new = '%s\\%s%s' % (DB_DIR, 'ATM', new_account)

            if os.path.exists(new):
                print('该用户已存在')
                continue
            else:
                shutil.copytree(tar, new)
                break

        set_info = cayatools.change_caya_value('%s\\%s' % (new, 'information.txt'))
        set_credit_card = cayatools.change_caya_value('%s\\%s' % (new, 'credit_card_account.txt'))

        set_info('TYPE', 'NORMAL')
        set_info('NAME', new_account)
        set_info('NICK', new_account)
        set_info('LOCK', 3)

        set_credit_card('TOTAL_LIMIT_RMB', 2000 )
        set_credit_card('TOTAL_LIMIT_USD', 2000 )
        set_credit_card('REPAY_ACCOUNT',new_account )
        print('新增用户成功！密码默认abc123')

    return wapper




        # none_func = none()
#
# TITLES=[
#     ['tf',transfer]
#     ['',none]
# ]
#
# def get_work():
#     def wapper(name,user):
#         for job in TITLES:
#             if name == job[0]:
#                 print(job[1])
#                 return job[1](user)
#     return wapper
#
# match_option=get_work()
# option1 = match_option('tf','haha')
# option1()