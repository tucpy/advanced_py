import wx
app = wx.App()
frame = wx.Frame(None, title="Vi du TextCtrl", size=(300,150))
panel = wx.Panel(frame, -1)

# 4 cach nhap mau: hexa, color name, RGB hoac mau trong wx(wx.RED)

stHoTen = wx.StaticText(panel,-1,label="Ho ten: ", pos=(10,10), size=wx.DefaultSize)
stHoTen.SetForegroundColour("#8f3d5e")
txtHoTen = wx.TextCtrl(panel, -1, value="Nhap ho ten", pos=(100,10), size=(250,30))
txtHoTen.SetForegroundColour("red")
txtHoTen.SetBackgroundColour("yellow")


_color = wx.Colour(143,61,94) # tuong duong voi #8f3d5e
stLop=wx.StaticText(panel, -1, label="Lớp:",pos=(10,50), size=wx.DefaultSize)
stLop.SetForegroundColour(_color)
txtLop = wx.TextCtrl(panel, -1, value="nhập lớp", pos=(100,50), size=(250,30))
txtLop.SetForegroundColour(wx.RED)
txtLop.SetBackgroundColour(wx.GREEN)


frame.Show(True)
app.MainLoop()