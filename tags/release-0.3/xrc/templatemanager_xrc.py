# This file was automatically generated by pywxrc, do not edit by hand.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res


class xrcTemplateManager(wx.Dialog):
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle()."""
        pass

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "TemplateManager")
        self.PostCreate(pre)

        # Define variables for the controls
        self.movable_list_holder = xrc.XRCCTRL(self, "movable_list_holder")
        self.gui_preview = xrc.XRCCTRL(self, "gui_preview")
        self.tp_holder = xrc.XRCCTRL(self, "tp_holder")
        self.wxID_OK = xrc.XRCCTRL(self, "wxID_OK")
        self.wxID_CANCEL = xrc.XRCCTRL(self, "wxID_CANCEL")


class xrcTemplatePanel(wx.Panel):
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle()."""
        pass

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PrePanel()
        self.PreCreate(pre)
        get_resources().LoadOnPanel(pre, parent, "TemplatePanel")
        self.PostCreate(pre)

        # Define variables for the controls
        self.header = xrc.XRCCTRL(self, "header")
        self.body = xrc.XRCCTRL(self, "body")
        self.footer = xrc.XRCCTRL(self, "footer")
        self.headings = xrc.XRCCTRL(self, "headings")
        self.instructions = xrc.XRCCTRL(self, "instructions")



# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    __res.Load('templatemanager.xrc')
