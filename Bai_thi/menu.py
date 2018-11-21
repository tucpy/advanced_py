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
from new_form_ptbac2 import *

###########################################################################
## Class menu_PT
###########################################################################

class menu_PT ( wx.Frame ):
	
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar4 = wx.MenuBar( 0 )
        self.m_menu4 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Giai phuong trinh bac 2", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.AppendItem( self.m_menuItem5 )

        self.m_menubar4.Append( self.m_menu4, u"Python NC" ) 

        self.SetMenuBar( self.m_menubar4 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.OnClick_giaiPT, id = self.m_menuItem5.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnClick_giaiPT( self, event ):
        frame = wx.Frame(None, size=(480,250), title="Giai phuong trinh bac 2")
        panel = giai_pt(frame)
        frame.Show(True)
        app.MainLoop()

if __name__=="__main__":
    app = wx.App()
    frame = menu_PT(None)
    frame.Maximize(True)
    frame.Show(True)
    app.MainLoop()

	

