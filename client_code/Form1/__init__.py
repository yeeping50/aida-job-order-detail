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
    self.repeating_panel_employees.items = anvil.server.call('get_joborder')

  def file_loader_1_change(self, file, **event_args):
    file = self.file_loader_1
  

  def button_click(self, **event_args):
    
    jobordernumber = self.order_box.text
    joborderstatus = self.status_box.text
    numberofitem = int(self.number_box.text)
    kitted = int(self.kitted_box.text)
    percentage = (kitted/numberofitem)*100
    file = self.file_loader_1.file
    anvil.server.call('add_form1', jobordernumber,joborderstatus,numberofitem,kitted,percentage,file)


    