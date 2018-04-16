welcome = \
'''欢迎使用ATM系统！(作者caya)
本系统仅仅用于测试！
操作过程中您可以随时输入quit取消操作
管理员请登录：admin password
一般用户请登录：caya abc123
进入游客状态请输入：skip
'''
#words
SKIP = ['quit','q','QUIT','Q','skip','SKIP']
ALL = ['a','all','ALL']
BACK = ['BACK','back']
HOME = ['HOME','home']
EXIT = ['EXIT','exit']
LOGIN = ['LOGIN','login']
LOGOUT = ['LOGOUT','logout']

#account for test
TESTACCOUNT = ['E:\\PycharmProjects\\py_fullstack\\3.函数\\作业\\ATM\\home\\ATMadmin',
              'E:\\PycharmProjects\\py_fullstack\\3.函数\\作业\\ATM\\home\\normal']

DEFAULT_USER = 'default user'
TOTAL_TIME_OUT = 1000
USER_HANDLE_TIMEOUT = 60

#filenames
PROCESS_PATH_TITLE = 'ATM'

DB_DIR = 'J:\\PycharmProjects\\ATM\\home'
PSW_FILE = 'password.txt'
PM_FILE = 'permission.txt'
INFO_FILE = 'information.txt'
MANUE_TITLE_FILE = 'mauetitle.txt'
SA_FILE = 'savings_account.txt'
CCA_FILE = 'credit_card_account.txt'
LOG_FILE = 'log.txt'
GENERALLOG_FILE = 'generallog.txt'

#formats
HELLO_FORMAT = '''\r{0:^62}\n'''
NAME_FORMAT =  '''\r{0:^62}\n'''
TIME_FORMAT =  '''\r {0:<29}{1:>31}\n'''
MANUE_FORMAT = \
'''\r{0:=^62}
\r‖{1:<29}{2:<29}‖
\r‖{3:<29}{4:<29}‖
\r‖{5:<29}{6:<29}‖
\r‖{7:<29}{8:<29}‖
 \r%s'''%('='*62)
LOG_FORMAT =  '''\r{0:<22}{1:<12}{2:<18}{3:<12}{4:<12}{5:<12}{6:<12}'''
USER_INFO_FORMAT =  '''\r|{0:^10}|{1:^12}|{2:^10}|{3:^10}|{4:^10}|'''
BILL_FORMAT = \
'''本月{0}账单：{1}元
\r可用额度：{2}元
\r总额度：{3}元
\r账单结算日：{4} 日
\r最后还款日：{5} 日
\r自动还款日：{6} 日
\r自动还款账户：{7}
\r账户权益为：{8}元'''

