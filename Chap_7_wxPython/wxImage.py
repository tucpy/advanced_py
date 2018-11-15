import wx
app = wx.App()
frame = wx.Frame(None, title="Vi du ListBox",size=(500,400))
panel = wx.Panel(frame,-1)
hinh = wx.Image("Media/hoa.jpg", wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
stStaticBitmal = wx.StaticBitmap(panel,-1,hinh)

frame.Show(True)
app.MainLoop()