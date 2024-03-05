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

  def submit_button_1_click(self, **event_args):

    joborderstatus = self.order_box.text
    numberofitem = self.number_box.text
    kitted = self.kitted_box.text
    percentage = kitted/numberofitem
    picture = download()
    anvil.server.call('add_form1', joborderstatus, numberofitem, kitted)


    