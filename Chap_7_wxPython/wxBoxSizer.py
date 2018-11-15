import wx
app = wx.App()
frame = wx.Frame(None,title="Vi du ListBox", size=(500,400))
panel = wx.Panel(frame, -1)
vbox = wx.BoxSizer(wx.VERTICAL)


stHoten = wx.StaticText(panel,label="Ho ten")
vbox.Add(stHoten,0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,5)
txtHoTen = wx.TextCtrl(panel,-1,size=(100,20))
vbox.Add(txtHoTen,0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,5)
panel.SetSizer(vbox)

stNghenghiep = wx.StaticText(panel,label="Nghe nghiep")
vbox.Add(stNghenghiep,0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,5)
txtNghenghiep = wx.TextCtrl(panel,-1,size=(100,20))
vbox.Add(txtNghenghiep,0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,5)
panel.SetSizer(vbox)


frame.Show(True)
app.MainLoop()