import wx
app = wx.App()
frame = wx.Frame(None, title = "wxPython Frame", size =(300,200))
panel = wx.Panel(frame)
wx.TextCtrl(panel,-1,"nhap ho ten", pos=(50,10),size=(175,30))

frame.Show(True)
app.MainLoop() 
