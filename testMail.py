#coding:utf-8

from smtplib import SMTP
from poplib import POP3
from time import sleep

print("=====================SMTP发邮件和POP3收邮件=====================");

SMTPSVR = 'smtp.163.com'  #smtp服务器地址
POP3SVR = 'pop.163.com'  #pop3服务器地址
SENDER="aaaaaaa@163.com"                           #用户名，换成自己的
PASSWORD=""                             #授权码，需自己去设置开启smtp和pop3服务
RECIPS=["aaaaaaaa@163.com"]      #这里接收人也设置为自己
origmsg = '''\
From: %(who)s
To: %(who)s
Subject: first test

Hello World!
''' % {'who': SENDER}

#使用SMTP完成邮件的发送
sendSvr = SMTP(SMTPSVR)   #创建一个smtp发送对象
sendSvr.login(SENDER, PASSWORD)  # 登录操作
errs = sendSvr.sendmail(SENDER,RECIPS,origmsg) #参数：发件人，收件人，邮件整体（消息头和消息体的字符串表示）
sendSvr.quit()
assert len(errs) == 0, errs  #,assert返回为假就会触发异常
print("smtp发送邮件完成")
sleep(10)    # 睡眠10秒钟，等待邮件被投递，让服务器完成消息的发送和接收。sleep单位秒


#使用pop3完成邮件的获取
recvSvr = POP3(POP3SVR)  #创建一个pop3接收对象
recvSvr.user(SENDER)  #设置用户名
recvSvr.pass_(PASSWORD)  #设置密码
emailist = recvSvr.stat()  #获取邮件列表
rsp, msg, siz = recvSvr.retr(emailist[0]) #下载第一个邮件
print(msg)
#sep = msg.index('')  #查找列表中""空白元素，空白元素后面为邮件正文
#recvBody = msg[sep+1:]  #根据空白元素定位获取邮件正文
print("pop3接收邮件完成")