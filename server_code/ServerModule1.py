import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_form1(name, email, feedback):
  app_tables.feedback.add_row(
    joborderstatus=joborderstatus, 
    numberofitem=numberofitem, 
    percentage=percentage, 
    picture=picture
  )

