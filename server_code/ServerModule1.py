import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_form1(jobordernumber,joborderstatus,numberofitem):
  app_tables.table1.add_row(
    jobordernumber=jobordernumber,
    joborderstatus=joborderstatus, 
    numberofitem=numberofitem,
    #kitted=kitted,
    #percentage=str(kitted/numberofitem), 
    #file = file
  )
@anvil.server.callable
def get_joborder():
  return app_tables.table1.search()

@anvil.server.callable
def update_article(article, article_dict):
  # check that the article given is really a row in the ‘articles’ table
  if app_tables.table1.has_row(tables):
    article_dict['updated'] = datetime.now()
    article.update(**article_dict)
  else:
    raise Exception("Article does not exist")