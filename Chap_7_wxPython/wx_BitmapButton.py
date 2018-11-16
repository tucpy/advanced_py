import wx
def OnClick(self):
    frame.Destroy()

app = wx.App()
frame = wx.Frame(None, title="Vi du TextCtrl", size =(300,150))
panel = wx.Panel(frame, -1)
close = wx.Image("Media/close.png",wx.BITMAP_TYPE_ANY).ConvertToBitmap()
button = wx.BitmapButton(panel, -1, close, pos=(50,20))
frame.Bind(wx.EVT_BUTTON, OnClick, button)
button.SetDefault()
frame.Show(True)
app.MainLoop()