import os



def search_file(path,TITLE=''):
    def wapper(usrname):
        '''找到文件绝对路径'''
        tar_file = '%s\\%s%s' % (path,TITLE,usrname)
        # print(path)
        # print(tar_file)
        g = os.walk(path)
        for i in g:
            if i[0] == tar_file:
                return tar_file
    return  wapper


def try_decode(filename):
    '''未知文件编码方式，试试出编码'''
    try:
        with open(filename, encoding='utf-8') as f:
            return 'utf-8'
    except:
        with open(filename, encoding='gbk') as f:
            return 'gbk'
    else:
        return 'none'


def get_paragraph_file(filename):
    '''从预指定文件中打印目标段落'''
    def wapper(word):
        res = []
        with open(filename,encoding='utf-8') as f:
            set_p = 0
            for line in f:
                if line.strip() == word :
                    set_p = 1
                elif line.strip() == '':
                    set_p = 0
                else:
                    if set_p == 1:
                        res.append(line.strip())
            return res
    return wapper

def get_line_word(word):
    '''根据预指定关键字打印目标文件的对应行'''
    def wapper(filename):
        with open(filename,encoding='utf-8') as f:
            for line in f:
                if word in line :
                    res = line.strip().split('=')[-1].strip()
                    break
        return res
    return wapper

def get_line_file(file_path):
    '''从预指定文件中打印目标行'''
    def wapper(word):
        with open(file_path,encoding='utf-8') as f:
            # print(word)
            for line in f:
                if word in line :
                    res = line.strip().split('=')[-1].strip()
                    break
        return res
    return wapper

def error(func):
    '''fegnm'''
    def wapper(*args, **kwargs):
        try:
            res = func(*args,**kwargs)
            return res
        except:
            print('报错啦！')
    return wapper


def timeout(seconds):
    from threading import Timer
    '''超时计时器'''
    def wraps(func):
        def time_out():   #生成一个运行异常
            print('time out %s seconds'%seconds)   #ps:要找到杀死进程的方法

        def deco(*args, **kwargs):
            timer = Timer(seconds, time_out)   #倒数时间，当计时结束，执行timer_out
            timer.start()
            res = func(*args, **kwargs)
            timer.cancel()
            return res

        return deco
    return wraps


def read_to_memory(file_path):
    '''文件读到内存'''
    file_encode = try_decode(file_path)
    with open(file_path,'r',encoding=file_encode) as f_r:
        lines = f_r.readlines()
        return lines

def write_to_disk(file_path,file_in_memory):
    '''文件写到磁盘'''
    file_encode = try_decode(file_path)
    with open(file_path,'w',encoding=file_encode) as f_w:
        for line in file_in_memory:
            f_w.write(line)

def replace_word_line(file,old_word,new_word):
    '''替换符合的行，输出新的行列表'''
    lines = file
    line_num = 0
    mark = 0
    for line in lines:
        if old_word in line:
            newline = line.replace(old_word,new_word)
            lines[line_num]=newline
            mark = 1
        line_num += 1
    if mark == 0:
        print('chang error:cant find word')
    return lines

def change_num_line(file,word,value):
    '''修改符合对应行的值，输出新的行列表'''
    lines = file
    line_num = 0
    mark = 0
    for line in lines:
        if word in line:
            newline =  '%s = %s\n' % (word,value)
            lines[line_num]=newline
            mark = 1
        line_num += 1
    if mark == 0:
        print('chang error:cant find word')
    return lines

def change_caya_value(file_path):
    def wapper(word,value):
        temp_file = read_to_memory(file_path)
        temp_file = change_num_line(temp_file,word,value)
        write_to_disk(file_path, temp_file)
    return wapper

