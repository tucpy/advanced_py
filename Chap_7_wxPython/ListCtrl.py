import sys
import wx

players = [('TV001', 'Tivi Sony 49 inch', '12000000'), ('TV002', 'Tivi Sony 50inch', '15000000'),\
            ('TV003', 'Tivi Sony 32 inch', '7000000'), ('TV004', 'Tivi LG 50 inch', '13000000'), ('TV005', 'Tivi Samsung 50 inch', '13500000')]

app = wx.App()
frame = wx.Frame(None,title="Vi du Choice", size=(450,200))
panel = wx.Panel(frame,-1)
list = wx.ListCtrl(panel,-1,style=wx.LC_REPORT, size=(450,200))
list.InsertColumn(0,'Ma so', width=100)
list.InsertColumn(1,'Ten', wx.LIST_FORMAT_LEFT, 200)
list.InsertColumn(2,'Gia', wx.LIST_FORMAT_RIGHT, 100)
index = 0
for i in players:
    list.InsertStringItem(index,i[0])
    list.SetStringItem(index,1,i[1])
    list.SetStringItem(index,2,i[2])

frame.Show(True)
app.MainLoop()