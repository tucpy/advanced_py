# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import json

###########################################################################
## Class nhom_tivi
###########################################################################

class nhom_tivi ( wx.Panel ):
	
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nhóm Tivi" ), wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_Ma = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Mã", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.m_Ma.Wrap( -1 )
        bSizer3.Add( self.m_Ma, 0, wx.ALL, 5 )

        self.m_textCtrl9 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

        self.m_Ten = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.m_Ten.Wrap( -1 )
        bSizer3.Add( self.m_Ten, 0, wx.ALL, 5 )

        self.m_textCtrl10 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_textCtrl10, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )

        self.m_btnThem = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_btnThem, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        sbSizer2.Add( bSizer2, 1, wx.EXPAND, 5 )


        bSizer1.Add( sbSizer2, 0, wx.EXPAND, 5 )

        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Danh sách nhóm" ), wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_lstDSNhom = wx.Listbook( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LB_DEFAULT )

        bSizer7.Add( self.m_lstDSNhom, 1, wx.EXPAND |wx.ALL, 5 )


        sbSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )


        bSizer1.Add( sbSizer6, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        # Connect Events
        self.m_btnThem.Bind( wx.EVT_BUTTON, self.OnClick_Them )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnClick_Them( self, event ):
        Ma = self.m_Ma.GetValue()
        Ten = self.m_Ten.GetValue()
        # Mo file de lay noi dung cu
        f = open('Du_lieu/Cong_ty.json', encoding='utf-8')
        noi_dung = json.load(f)
        f.close()
        # Bo sung noi dung
        noi_dung['Danh_sach_Nhom_Tivi'].append({'Ten':Ten,'Ma_so':Ma})
        # Luu noi dung moi
        f = open('Du_lieu/Cong_ty.json','w', encoding='utf-8')
        json.dump(noi_dung,f,indent=4,ensure_ascii=False)
        f.close()
        # Load lai noi dung cho List
        f = open('Du_lieu/Cong_ty.json', encoding='utf-8')
        noi_dung = json.load(f)
        f.close()
        ds_nhom_tivi=[]
        for item in noi_dung['Danh_sach_Nhom_Tivi']:
            ds_nhom_tivi.append(item['Ten'])
        # Clear noi dung cu truoc khi append noi dung moi
        self.m_lstDSNhom.Clear()
        self.m_lstDSNhom.AppendItems(ds_nhom_tivi)


if __name__=="__main__":
    app = wx.App()
    frame = wx.Frame(None, size=(600,400), title="Nhom tivi")
    panel_nhom_tivi= nhom_tivi(frame)
    f = open('Du_lieu/Cong_ty.json', encoding='utf-8')
    noi_dung = json.load(f)
    f.close()
    ds_nhom_tivi=[]
    # Hien thi noi dung
    for item in noi_dung['Danh_sach_Nhom_Tivi']:
        ds_nhom_tivi.append(item['Ten'])
    #panel_nhom_tivi.m_lstDSNhom.AppendItems(ds_nhom_tivi)

    frame.Show(True)
    app.MainLoop()



