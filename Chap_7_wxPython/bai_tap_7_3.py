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
## Class bai_tap_7_3
###########################################################################

class bai_tap_7_3 ( wx.Panel ):
	
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,250 ), style = wx.TAB_TRAVERSAL )

        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"THÔNG TIN NHÂN VIÊN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetFont( wx.Font( 14, 74, 90, 92, False, "Arial" ) )

        gbSizer3.Add( self.m_staticText11, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Họ tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        gbSizer3.Add( self.m_staticText13, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ho_ten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        gbSizer3.Add( self.m_Ho_ten, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ho_ten_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Ho_ten_err.Wrap( -1 )
        self.m_Ho_ten_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer3.Add( self.m_Ho_ten_err, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        gbSizer3.Add( self.m_staticText14, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ma_so = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_Ma_so, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_Ma_so_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Ma_so_err.Wrap( -1 )
        self.m_Ma_so_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer3.Add( self.m_Ma_so_err, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Tên đăng nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        gbSizer3.Add( self.m_staticText16, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ten_dang_nhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_Ten_dang_nhap, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_Ten_dang_nhap_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Ten_dang_nhap_err.Wrap( -1 )
        self.m_Ten_dang_nhap_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer3.Add( self.m_Ten_dang_nhap_err, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        gbSizer3.Add( self.m_staticText18, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Mat_khau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        self.m_Mat_khau.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )

        gbSizer3.Add( self.m_Mat_khau, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_Mat_khau_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Mat_khau_err.Wrap( -1 )
        self.m_Mat_khau_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer3.Add( self.m_Mat_khau_err, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Xác nhận MK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        gbSizer3.Add( self.m_staticText19, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Mat_khau_XN = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        gbSizer3.Add( self.m_Mat_khau_XN, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_Mat_khau_XN_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Mat_khau_XN_err.Wrap( -1 )
        self.m_Mat_khau_XN_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer3.Add( self.m_Mat_khau_XN_err, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_btnThem = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_btnThem, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( gbSizer3 )
        self.Layout()

        # Connect Events
        self.m_btnThem.Bind( wx.EVT_BUTTON, self.OnClick_Them )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnClick_Them( self, event ):
        Ten = self.m_Ho_ten.GetValue()
        Ma_so = self.m_Ma_so.GetValue()
        Ten_dang_nhap = self.m_Ten_dang_nhap.GetValue()
        Mat_khau = self.m_Mat_khau.GetValue()
        Mat_khau_xn = self.m_Mat_khau_XN.GetValue()
        flag=1
        if len(Ten)==0:
            self.m_Ho_ten_err.SetLabel('*')
            flag=0
        if len(Ma_so)==0:
            self.m_Ma_so_err.SetLabel('*')
            flag=0
        if len(Ten_dang_nhap)==0:
            self.m_Ten_dang_nhap_err.SetLabel('*')
            flag=0
        if len(Mat_khau)==0:
            self.m_Mat_khau_err.SetLabel('*')
            flag=0
        if len(Mat_khau_xn)==0:
            self.m_Mat_khau_XN_err.SetLabel('*')
            flag=0

        if Mat_khau_xn != Mat_khau:
            self.m_Mat_khau_XN_err.SetLabel('*')
            flag=0
        
        if flag ==1:
            wx.MessageBox('cho luu', 'Thong bao')



if __name__=="__main__":
    app = wx.App()
    frame = wx.Frame(None, size=(400,250), title="Thong tin nhan vien")
    panel = bai_tap_7_3(frame)



    frame.Show(True)
    app.MainLoop()

	

