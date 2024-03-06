import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_form1(jobordernumber,joborderstatus,numberofitem,kitted,percentage,file):
  app_tables.table1.add_row(
    jobordernumber=jobordernumber,
    joborderstatus=joborderstatus, 
    numberofitem=numberofitem,
    kitted=kitted,
    percentage=kitted/numberofitem, 
    #file = file
  )

