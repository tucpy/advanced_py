import wx
app = wx.App()
frame = wx.Frame(None, title = "wxPython Frame", size =
(300,200))
panel = wx.Panel(frame)
frame.Show(True)
app.MainLoop() 
