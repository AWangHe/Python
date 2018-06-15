# -*- coding: utf-8 -*-
from card import Card
from user import User
import random

class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers
        
    #开户
    def createUser(self):
        #向用户字典中添加一对键值对（卡号---用户）
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")
        prestoreMoney = int(input("请输入您的预存款金额："))
        if prestoreMoney < 0:
            print("预存款输入有误！！！开户失败………………")
            return -1
        onePasswd = input("请设置密码：")
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！！！开户失败………………")
            return -1
        #所有需要的信息就齐全了
        cardStr = self.randomCardId()
        
        card = Card(cardStr, onePasswd, prestoreMoney)
        user = User(name, idCard, phone, card)
        #存到字典
        self.allUsers[cardStr] = user
        print("开户成功！！！请牢记密码 （%s）………………" % (cardStr))
        
    #查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")
        #验证是存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在！！！查询失败………………")
            return -1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作………………")
            return -1      
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！！该卡已被锁定，请解锁后再进行其他操作………………")
            user.card.cardLock = True
            return -1
        print("账号：%s  余额：%d " % (user.card.cardId, user.card.cardMoney))
    #取款
    def getMoney(self):
        cardNum = input("请输入您的卡号：")
        #验证是存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在！！！取款失败………………")
            return -1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作………………")
            return -1      
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！！该卡已被锁定，请解锁后再进行其他操作………………")
            user.card.cardLock = True
            return -1
        money = int(input("请输入你的取款金额："))
        if money > user.card.cardMoney:
            print("余额不足，无法进行取款………………")
            return -1
        if money < 0:
            print("输入错误，无法进行取款………………")
            return -1
        user.card.cardMoney -= money
        print("取款成功！！！余额：%d" % (user.card.cardMoney))
    #存款
    def saveMoney(self):
        pass
    #转账
    def transferMoney(self):
        pass
    #改密
    def changePasswd(self):
        pass
    #锁定
    def lockUser(self):
        cardNum = input("请输入您的卡号：")
        #验证是存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在！！！查询失败………………")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定！！！请解锁后再使用其它功能………………")
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！！锁定失败………………")
            return -1
        #验证身份证号
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入有误！！！锁定失败………………")
            return -1
        #锁定
        user.card.cardLock = True
        print("锁定成功………………")
            
            
    #解锁
    def unlockUser(self):
        cardNum = input("请输入您的卡号：")
        #验证是存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在！！！解锁失败………………")
            return -1
        if not user.card.cardLock:
            print("该卡未被锁定！！！无需解锁………………")
            return -1
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！！解锁失败………………")
            return -1
        #验证身份证号
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入有误！！！解锁失败………………")
            return -1
        #锁定
        user.card.cardLock = False
        print("解锁成功………………")
        
    #补卡
    def newCard(self):
        pass
    #销户
    def killUser(self):
        pass
    
    
    #验证密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False
    
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1 ))
                str += ch
            #判断是否重复
            if not self.allUsers.get(str):
                return str
    


































