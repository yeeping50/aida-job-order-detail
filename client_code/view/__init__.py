from ._anvil_designer import viewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view(viewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    #self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('get_joborder')


