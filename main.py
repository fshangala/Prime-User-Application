from kivymd.app import MDApp

class PrimesUserApp(MDApp):
  def build(self):
    return MainWindow()

PrimesUserApp().run()
