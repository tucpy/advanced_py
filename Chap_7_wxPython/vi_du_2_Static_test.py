import wx
app = wx.App()
frame = wx.Frame(None, title = "wxPython Frame", size =(300,200))
panel = wx.Panel(frame)
wx.StaticText(panel, -1,"Trung tam tin hoc", size=(150,30), pos=(50,10))
frame.Show(True)
app.MainLoop() 
