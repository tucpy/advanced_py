import wx
def OnXem(event):
    kq = wx.MessageBox("Ban co chac chan muon xoa khong", "Thong bao",\
    wx.YES_NO|wx.ICON_INFORMATION)
    if wx.YES==kq:
        stTraLoi.SetLabel("Ban chon button YES")
    else:
        stTraLoi.SetLabel("Ban chon button NO")

app = wx.App()
frame = wx.Frame(None,title="Vi du MessageBox", size=(300,150))
panel = wx.Panel(frame,-1)
btnChon = wx.Button(panel,-1,label="Click vao de xem Message",pos=(10,10))
frame.Bind(wx.EVT_BUTTON, OnXem, btnChon)
stTraLoi = wx.StaticText(panel,-1,pos=(10,50))
frame.Show(True)
app.MainLoop()