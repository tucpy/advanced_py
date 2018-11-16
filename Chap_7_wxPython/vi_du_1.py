import wx
print (wx.__file__) # check which wx package it imports
#/Users/tp10/anaconda3/lib/python3.6/site-packages/wx/__init__.py 

app = wx.App()
frame = wx.Frame(None, title = "wxPython Frame", size = (300,200))
panel = wx.Panel(frame)
label = wx.StaticText(panel, label="Hello World!", pos = (100,50))
frame.Show(True)
app.MainLoop() 
