import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="Calculator")
        panel=wx.Panel(self)
        equal=wx.Button(parent=panel,label="=",pos=(290,180))
        self.text=wx.TextCtrl(panel)
        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text,0,wx.ALL|wx.EXPAND,10)
        panel.SetSizer(sizer)
        self.Show()

if __name__ == "__main__":
    app=wx.App()
    frame=MyFrame()
    app.MainLoop()
