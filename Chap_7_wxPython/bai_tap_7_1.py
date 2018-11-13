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
## Class Cong_ty
###########################################################################

class Cong_ty ( wx.Panel ):
	
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 633,521 ), style = wx.TAB_TRAVERSAL )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Media/berry.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 600,300 ), 0 )
        gbSizer1.Add( self.m_bitmap1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        gbSizer1.Add( self.m_staticText1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
        gbSizer1.Add( self.m_Ten, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        gbSizer1.Add( self.m_staticText2, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_btn_CapNhat = wx.Button( self, wx.ID_ANY, u"Cập nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_btn_CapNhat, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_Ma_so = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_Ma_so, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Địa chỉ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        gbSizer1.Add( self.m_staticText3, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Dia_chi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_Dia_chi, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Điện thoại", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        gbSizer1.Add( self.m_staticText4, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Dien_thoai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_Dien_thoai, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Mail", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        gbSizer1.Add( self.m_staticText5, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Mail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_Mail, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( gbSizer1 )
        self.Layout()

        # Connect Events
        self.m_btn_CapNhat.Bind( wx.EVT_BUTTON, self.OnClick_btn_CapNhat )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnClick_btn_CapNhat( self, event ):
        # Cap nhat thong tin vua nhap
        Ten=self.m_Ten.GetValue()
        Ma_so=self.m_Ma_so.GetValue()
        Dia_chi=self.m_Dia_chi.GetValue()
        Dien_thoai=self.m_Dien_thoai.GetValue()
        Mail=self.m_Mail.GetValue()
        # Mo file
        f = open('Du_lieu/Cong_ty.json', encoding='utf-8')
        noi_dung = json.load(f)
        f.close()
        # Cap nhat
        noi_dung['Ten']=Ten
        noi_dung['Dia_chi']=Dia_chi
        noi_dung['Dien_thoai']=Dien_thoai
        noi_dung['Mail']=Mail
        # Ghi file
        f = open('Du_lieu/Cong_ty.json','w', encoding='utf-8')
        json.dump(noi_dung,f,indent=4,ensure_ascii=False)
        f.close()
        wx.MessageBox('Da cap nhat file', 'Thong bao')                       
	

if __name__=="__main__":
    app = wx.App()
    frame = wx.Frame(None, size=( 633,521))
    panel_cong_ty= Cong_ty(frame)
    f = open('Du_lieu/Cong_ty.json', encoding='utf-8')
    noi_dung = json.load(f)
    f.close()

    # Hien thi noi dung trong file json len panel(nho go dung ten Key)
    panel_cong_ty.m_Ten.SetValue(noi_dung['Ten'])
    panel_cong_ty.m_Ma_so.SetValue(noi_dung['Ma_so'])
    panel_cong_ty.m_Dia_chi.SetValue(noi_dung['Dia_chi'])
    panel_cong_ty.m_Dien_thoai.SetValue(noi_dung['Dien_thoai'])
    panel_cong_ty.m_Mail.SetValue(noi_dung['Mail'])

    frame.Show (True)
    app.MainLoop()
