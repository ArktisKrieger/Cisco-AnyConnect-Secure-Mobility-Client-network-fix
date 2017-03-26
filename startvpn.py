#coding=utf-8
import win32gui
import win32api
import time
import os
child_handles=[]
def allelement(hwnd,param):
    child_handles.append(hwnd)
endp=0
btndhl=0

while endp==0:
    mainw=win32gui.FindWindow('#32770','Cisco AnyConnect Secure Mobility Client')
    btndhl=0
    btnhdl = win32gui.FindWindowEx(mainw, 0, "Button", "Connect Anyway")
    if btnhdl!=0:
        endp=1
win32api.SendMessage(btnhdl,245,0,0)
pwddlg=0
while pwddlg==0:
    pwddlg=win32gui.FindWindow('#32770','Cisco AnyConnect | '+'Name VPN')

time.sleep(10)
win32gui.EnumChildWindows(pwddlg,allelement,None)
win32gui.SendMessage(child_handles[7],12,0,"Password")
win32api.SendMessage(child_handles[8],245,0,0)




