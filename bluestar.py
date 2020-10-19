from twilio.rest import Client 
import pandas as pd
df=pd.read_excel('avocado.xlsx')
import datetime
from datetime import datetime
account_sid = 'AC94ce801ff997bb1445cfed69e3a3dfa9' 
auth_token = '6ceb6ae04c2755405e8d51f0513b1a70' 
client = Client(account_sid, auth_token) 
def alert():
  from datetime import date, timedelta
  dt = date.today() - timedelta(1009)
  t2=df['Date']
  t2=pd.to_datetime(t2,format='%Y-%m-%d')

  for i in range(0,len(df['crop'])):
    if(t2[i]==dt):
      a=df['region'][i]
      body='Hi the client for today is{}'.format(a)
      message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=body,      
                              to='whatsapp:+919819354506' 
                          ) 
