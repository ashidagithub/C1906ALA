# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习使用 csv 文件写一副牌
#   学习使用 加密技术 文件写一副牌
# ------------------------(max to 80 columns)-----------------------------------

#from binascii import b2a_hex

msg = '啊'
byte_msg = msg.encode()
print ('-- default: [%s]' % byte_msg)
new_msg = byte_msg.decode()
print ('-- default: [%s]' % new_msg)

byte_msg = msg.encode('utf-8')
print ('-- utf-8: [%s]' % byte_msg)
new_msg = byte_msg.decode('utf-8')
print ('-- utf-8: [%s]' % new_msg)

byte_msg = msg.encode('gbk')
print ('-- gbk: [%s]' % byte_msg)
new_msg = byte_msg.decode('gbk')
print ('-- gbk: [%s]' % new_msg)

byte_msg = msg.encode('gb2312')
print ('-- gb2312: [%s]' % byte_msg)
new_msg = byte_msg.decode('gb2312')
print ('-- gb2312: [%s]' % new_msg)

# test for error
msg='啊'
byte_msg = msg.encode('gbk')
new_msg = byte_msg.decode('utf-8')
print('-- test for error: [%s]' % new_msg)
