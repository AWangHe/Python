# -*- coding: utf-8 -*-
import telnetlib


def telnetDoSomething(IP,user,passwd,command):
    try:
        #连接服务器
        telnet = telnetlib.Telnet(IP)
        #设置调试级别
        telnet.set_debuglevel(2)
        #读取输入用户名信息
        rt = telnet.read_until("Login username:".encode("utf-8"))
        #写入用户名
        telnet.write((user + "\r\n").encode("utf-8"))
        return True
    except:
        return False
    

        
    






























