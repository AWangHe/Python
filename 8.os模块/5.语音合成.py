# -*- coding: utf-8 -*-
#系统客户端
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SPVOICE")
speaker.Speak("今天是个好日子，所有的事儿都能成")
























