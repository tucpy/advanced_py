#wx.CheckBox, chon nhieu option cung luc
'''
import wx
app = wx.App()
frame = wx.Frame(None,title ="Vi du CheckBox", size=(300,150))
panel = wx.Panel(frame,-1)
wx.CheckBox(panel,-1,"Mot",(35,40),(150,20))
wx.CheckBox(panel,-1,"Hai",(35,60),(150,20))
wx.CheckBox(panel,-1,"Ba",(35,80),(150,20))
frame.Show(True)
app.MainLoop()
'''

#wx.RadioButton, chi duoc chon 1 option

import wx
app = wx.App()
frame = wx.Frame(None,title = "Vi du RadioButton", size=(300,150))
panel = wx.Panel(frame,-1)
radio1 = wx.RadioButton(panel,-1,"Nam", pos=(20,10), style=wx.RB_GROUP)
radio2 = wx.RadioButton(panel,-1,"Nu", pos=(20,40))
radio3 = wx.RadioButton(panel,-1,"Nu", pos=(20,70))
frame.Show(True)
app.MainLoop()