import wx

class WxWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(WxWindow, self).__init__(*args, **kw)
        
        self.SetSize(400, 600)
        self.panel = wx.Panel(self)
        self.dark = False
        
        self.cycle_color_button = wx.Button(self.panel, label='Cycle Color')
        self.cycle_color_button.SetBackgroundColour(wx.Colour(255, 111, 97))  # Bright red
        self.cycle_color_button.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        self.cycle_color_button.Bind(wx.EVT_BUTTON, self.cycle_color)
        
        self.exit_button = wx.Button(self.panel, label='Exit')
        self.exit_button.SetBackgroundColour(wx.Colour(255, 111, 145))  # Bright pink
        self.exit_button.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        self.exit_button.Bind(wx.EVT_BUTTON, self.on_exit)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.cycle_color_button, 0, wx.ALL, 5)
        sizer.Add(self.exit_button, 0, wx.ALL, 5)
        self.panel.SetSizer(sizer)
        
        self.SetTitle('wxPython Window')
        self.Centre()
        self.panel.SetBackgroundColour(wx.Colour(137, 207, 240))  # Bright blue
        
    def cycle_color(self, event):
        if self.dark:
            self.panel.SetBackgroundColour(wx.Colour(137, 207, 240))  # Bright blue
            self.cycle_color_button.SetBackgroundColour(wx.Colour(255, 111, 97))  # Bright red
        else:
            self.panel.SetBackgroundColour(wx.Colour(10, 116, 218))  # Dark blue
            self.cycle_color_button.SetBackgroundColour(wx.Colour(214, 65, 97))  # Dark red
        self.dark = not self.dark
        self.panel.Refresh()

    def on_exit(self, event):
        self.Close(True)

def run_wx():
    app = wx.App()
    window = WxWindow(None)
    window.Show()
    app.MainLoop()

if __name__ == "__main__":
    run_wx()
