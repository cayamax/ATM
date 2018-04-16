
ATM
   |
   ——bin  #执行文件存放
   |    |
   |    ——ATM系统.py   #开始调用主程序main
   |
   |
   ——config
   |   |
   |   ——settings.py #存放全局变量，包括数据库路径，操作的关键字等
   |
   |
   ——profiles  #存放用户数据库
   |    |
   |    ——用户文件夹
   |        |
   |        ——permission.txt #用户权限，可加密
   |        |
   |        ——information.txt       #用户基本信息
   |        |
   |        ——password.txt   #存放密码、登录锁，文件可加密
   |        |
   |        ——savings_account.log   #储蓄账户流水记录
   |        |
   |        ——credit_card_account.log  #信用卡账户流水记录
   |        |
   |        ——log.txt       #存放用户操作日志
   |
   |
   ——logs    #日志文件夹
   |    |
   |    ——errlog    #错误日志，通过errtry装饰器返回
   |    |
   |    ——accesslog #登录日志，通过access装饰器返回
   |
   |
   ——mod    #增加模块，封装功能性函数，方便阅读
   |    |
   |    ——find.py   #access的功能模块，用于查找账户名对应的用户数据文件
   |    |   |
   |    |   ——name()    #匹配用户名并返回用户目录
   |    |   |
   |    |   ——match()   #匹配文件内容用的,保留
   |    |
   |    ——msg.py
   |    |   |
   |    |   ——err()#错误返回
   |    |   |
   |    |   ——info()#信息返回
   |    |   |
   |    |   ——warning()#警告返回
   |    |   |
   |    |   ——box()#装载消息，根据不同情况返回给log
   |
   |
   ——Core
   |    |
   |    ——main.py
   |    |   |
   |    |   ——run()
   |    |   |
   |    |   ——print_manu()    #打印选项菜单
   |    |   |
   |    |   ——atm_draw()      #取款
   |    |   |
   |    |   ——atm_deposit()   #存款
   |    |   |
   |    |   ——atm_repayment() #定期还款
   |    |   |
   |    |   ——atm_bill()      #定期出账单
   |    |   |
   |    |   ——transfer()      #转账
   |    |   |
   |    |   ——su_adduser(）   #添加账户
   |    |   |
   |    |   ——su_set_limit(） #指定用户额度
   |    |   |
   |    |   ——su_freeze_user(）  #冻结用户
   |    |
   |    ——class.py  #管理员与一般用户不共用类的原因是避免因权限修改而让一般用户变成管理员的风险
   |    |   |
   |    |   ——class super_usr  #管理员，存放超级权限的令牌
   |    |   |
   |    |   ——class usr        #一般用户，存放一般权限的令牌
   |    |   |
   |    |   ——


