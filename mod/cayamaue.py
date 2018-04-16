#    本文件提供子菜单功能接口，具体功能请写到/mod/job 文件下
from mod import access,cayatools,settings
import time

def common_tab():
        #for test
    common_tab = {
        "maue": ('hahaha', test('haha')),
        #for common operation
        "无内容": ('', none),
        '返回上一菜单': ('back', back),
        '返回主页': ('home', home),
        '账户登录':('user login',login),
        '账户注销':('user logout',logout),
        '退出系统':('exit',exit),
        '修改密码': ('reset password', user_set('password')),
        '修改昵称': ('reset nickname', user_set('nickname'))
    }
    return common_tab

def maue_main(user,option_tab):        #主要工作为记录路径dir_history，调用
    '''菜单执行'''
    main_maue = make_maues('MAIN',option_tab)               #菜单函数名

    while 1:
        dir_history = [ main_maue ]                        #路径初始化
        current_manu = main_maue(user)                     #生成菜单字典同时打印

        while 1:
            get_res,point = get_input(current_manu,option_tab,user)

            if type(get_res) == dict:                        #进入下一级菜单
                dir_history.append(make_maues(current_manu[point],option_tab))
                current_manu = get_res
                continue

            elif get_res in settings.BACK and len(dir_history) > 1:  # 返回上一步
                dir_history.pop()
                time.sleep(1)
                current_manu = dir_history[-1](user)

            elif get_res in settings.HOME:                           # 回到主菜单
                break

            elif get_res in settings.EXIT:                           # 回到退出系统
                exit_mark = 1
                return exit_mark

            elif get_res in settings.LOGIN:                          # 回到登录系统
                exit_mark = 0
                return exit_mark

            elif get_res in settings.LOGOUT:                         # 回到注销用户
                user = access.login('skip')
                break

            else:
                time.sleep(1)                                #执行操作
                current_manu = dir_history[-1](user)


@cayatools.timeout(settings.USER_HANDLE_TIMEOUT)
def get_input(current_manu,option_tab,user):   #用户操作，如果长时间不进行输入操作则返回超时提示
    while 1:
        point = input('>>')  # 请求输入
        if point == '':
            continue
        elif point not in current_manu:
            print('无效输入')
        elif type(current_manu[point]) is str:
            get_res = make_maues(current_manu[point],option_tab)(user)
            return get_res,point
        else:
            get_res = current_manu[point](user)  # 执行目标函数， 返回执行结果
            return get_res,point
#############################################################
#                          菜单生成                         #
#############################################################
def make_maues(title,option_tab):
    def wapper_user(user):
        '''生成字典形式的二级菜单'''
        title_name = '%s_%s'%(user.type,title)
        sub_options = []

        get_option_titles = cayatools.get_paragraph_file(user.maue_file)
        maue_titles = get_option_titles(title_name)
        # print(maue_titles)

        for line in maue_titles:
            sub_options.append(line.strip().split('.')[1])

        maue_list = {
            "Title": maue_titles,
            "1": match_option(sub_options[1],option_tab),
            "2": match_option(sub_options[2],option_tab),
            "3": match_option(sub_options[3],option_tab),
            "4": match_option(sub_options[4],option_tab),
            "5": match_option(sub_options[5],option_tab),
            "6": match_option(sub_options[6],option_tab),
            "7": match_option(sub_options[7],option_tab),
            "8": match_option(sub_options[8],option_tab),
        }
        # print(maue_list)
        print_manu(user, *maue_list['Title'])
        return maue_list
    return wapper_user

def match_option(titlename,option_tab):
    '''根据菜单选项表（configs.option_tab）匹配出相应的工作'''

    local_tab = common_tab()
    for h in local_tab:
        if titlename == local_tab[h][0]:
            return local_tab[h][1]

    optiontab = option_tab()
    for j in optiontab:
        if titlename == optiontab[j][0]:
            return optiontab[j][1]

    return none

#############################################################
#                        菜单打印格式                       #
#############################################################
def print_manu(user,title,*args):
    '''打印菜单至屏幕，可改格式'''
    print_hello =  settings.HELLO_FORMAT.format(hello_time())

    name = user.nick.strip()
    title = title.split('.')[1]
    title_maue = settings.NAME_FORMAT.format(name)

    date = time.strftime("%Y-%m-%d", time.localtime())
    local_time= time.strftime("%H:%M:%S", time.localtime())
    time_print = settings.TIME_FORMAT.format(date,local_time)

    mauetitle = settings.MANUE_FORMAT.format(' %s '%title,*args)
    print(print_hello,title_maue,time_print,mauetitle)


def hello_time():
    '''按时间段区分打招呼'''
    time_tmp = time.strftime("%H", time.localtime()).strip()
    if time_tmp in ['5','6','7','8','9','10','11','12']:
        hello = 'good morning!'
    elif time_tmp in ['13','14', '15', '16','17', '18']:
        hello = 'good afternoon!'
    else:
        hello = 'good evening'
    return hello

#############################################################
#                         通用选项                          #
#############################################################

def user_set(work):
    def wapper(user):
        if work == 'password':
            user.reset_psw()
        elif work == 'nickname':
            user.reset_name()
    return wapper

def back(user):
    '''返回上一菜单'''
    print('go back')
    res = 'back'
    return res

def home(user):
    '''回到主菜单'''
    print('go home')
    res = 'home'
    return res

def login(user):
    '''登录用户'''
    print('user login')
    res = 'login'
    return res

def logout(user):
    '''注销用户'''
    print('user logout')
    res = 'logout'
    return res


def exit(user):
    '''退出系统'''
    print('good bye')
    res = 'exit'
    return res


def test(text):
    def wapper(user):
        print(text)
    return wapper

def none(user):
    def wapper(*args):
        print('无效的选项')
    return wapper


# import json
#
# if __name__ == '__main__':
#     with open("new_hello", "w") as f:
#         dic_str = json.dumps(option_tab)
#         f.write(dic_str)  # json.dump(dic,f)