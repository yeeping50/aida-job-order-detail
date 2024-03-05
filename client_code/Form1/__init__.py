from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_click(self, **event_args):
    
    jobordernumber = self.order_box.text
    joborderstatus = self.status_box.text
    #numberofitem = self.number_box.text
    #kitted = self.kitted_box.text
    #percentage = {kitted}/{numberofitem}
    #picture = download()
    anvil.server.call('add_form1', jobordernumber,joborderstatus)


    