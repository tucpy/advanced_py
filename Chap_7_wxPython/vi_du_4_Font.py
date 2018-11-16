import wx
app = wx.App()
frame = wx.Frame(None, title="Vi du TextCtrl", size=(300,150))
panel = wx.Panel(frame, -1)
str = "Thong tin cong ty"
text = wx.StaticText(panel,-1,str,(20,20))
font = wx.Font(18,wx.DECORATIVE, wx.ITALIC, wx.BOLD)
text.SetFont(font)
wx.StaticText(panel,-1,"Cong ty trach nhiem huu han", (20,50))
frame.Show(True)
app.MainLoop()