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
from class_ptbac2 import *

###########################################################################
## Class giai_pt
###########################################################################

class giai_pt ( wx.Panel ):
	
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 480,250 ), style = wx.TAB_TRAVERSAL )

        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_Pt = wx.StaticText( self, wx.ID_ANY, u"(ax^2 +bx + c = 0)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Pt.Wrap( -1 )
        self.m_Pt.SetFont( wx.Font( 14, 74, 90, 92, False, "Arial" ) )

        gbSizer2.Add( self.m_Pt, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 6 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_a = wx.StaticText( self, wx.ID_ANY, u"a =", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_a.Wrap( -1 )
        gbSizer2.Add( self.m_a, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_txt_a = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_txt_a, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_b = wx.StaticText( self, wx.ID_ANY, u"b =", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_b.Wrap( -1 )
        gbSizer2.Add( self.m_b, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_txt_b = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_txt_b, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_c = wx.StaticText( self, wx.ID_ANY, u"c =", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_c.Wrap( -1 )
        gbSizer2.Add( self.m_c, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_txt_c = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_txt_c, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_btn_Tim_nghiem = wx.Button( self, wx.ID_ANY, u"Tìm nghiệm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_btn_Tim_nghiem, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 6 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_giaiPT = wx.StaticText( self, wx.ID_ANY, u"Giải phương trình bậc 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_giaiPT.Wrap( -1 )
        self.m_giaiPT.SetFont( wx.Font( 14, 74, 90, 92, False, "Arial" ) )

        gbSizer2.Add( self.m_giaiPT, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 6 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_ket_qua = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_ket_qua.Wrap( -1 )
        gbSizer2.Add( self.m_ket_qua, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 6 ), wx.ALL, 5 )


        self.SetSizer( gbSizer2 )
        self.Layout()

        # Connect Events
        self.m_btn_Tim_nghiem.Bind( wx.EVT_BUTTON, self.OnClick_Tim_Nghiem )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnClick_Tim_Nghiem( self, event ):
        a = self.m_txt_a.GetValue()
        b = self.m_txt_b.GetValue()
        c = self.m_txt_c.GetValue()

        flag=1
        if len(a)==0 or len(b)==0 or len(c)==0:
            wx.MessageBox('Phai nhap du cac he so')
            flag=0
        a = int(a)
        b = int(b)
        c = int(c)
        if type(a) != 'int' or type(b) !='int' or type(c) != 'int':
            wx.MessageBox('Vui long nhap du lieu hop le')
            flag =0
        if type(a) == 'int' and type(b) =='int' and type(c) == 'int':
            flag =1
        if flag ==1:
            ptb2 = PTbac2(a,b,c)
            nghiem = ptb2.phuong_trinh_bac_hai()
            self.m_ket_qua.SetLabel(nghiem)

        # Tao file json
        DS_Nhom=[]
        noi_dung = {"danh_sach_phuong_trinh": DS_Nhom}
        f = open("pt.json", 'w')
        json.dump(noi_dung, f,indent = 4, ensure_ascii=False)
        f.close()

        # Luu ket qua giai phuong trinh
        kq = {"a":a, "b":b, "c": c, "nghiem": nghiem}
        DS_Nhom.append(kq)

        noi_dung.update(DS_Nhom)
        f = open("pt.json", 'w', encoding='utf-8')
        json.dump(noi_dung, f, indent=4, ensure_ascii=False) 


if __name__=="__main__":
    app = wx.App()
    frame = wx.Frame(None, size=(480,250), title="Giai phuong trinh bac 2")
    panel = giai_pt(frame)

    frame.Show(True)
    app.MainLoop()