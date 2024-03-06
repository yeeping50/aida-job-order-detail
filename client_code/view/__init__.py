from ._anvil_designer import viewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view(viewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def refresh_articles(self):
    # Load existing articles from the Data Table, 
    # and display them in the RepeatingPanel
    self.label_2 = anvil.server.call('get_joborder')
    self.refresh_articles()
    print(self.label_2)

    # Any code you write here will run before the form opens.
