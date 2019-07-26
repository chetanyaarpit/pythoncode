import os
from flask import Flask,request
import pandas as pd
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.file import Storage
import json
import re
import httplib2 
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client
import requests
from datetime import datetime
from datetime import timedelta
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import cv2
from flask import send_file
from jsonmerge import merge

stopwords = set(STOPWORDS)
#from flask import jsonify

app = Flask(__name__)
@app.route('/dash', methods=['POST','GET'])
def entry_page():
    # print("get hello")
    if request.method == 'GET':
            start_date = int(request.args.get('start_date'))
            print('raw timestamp_start:',start_date)
            start_date = datetime.utcfromtimestamp(start_date).strftime('%Y-%m-%d')
            start_date = str(datetime.strptime(start_date,'%Y-%m-%d')+ timedelta(days=1))
            start_date = start_date[0:10]
            
            
            end_date = int(request.args.get('end_date'))
            print('raw timestamp_end:',end_date)
            end_date = datetime.utcfromtimestamp(end_date).strftime('%Y-%m-%d')
            end_date = str(datetime.strptime(end_date,'%Y-%m-%d')+ timedelta(days=1))
            end_date = end_date[0:10]
            
            
            print('start_date:',start_date)
            
            print('end_date:',end_date)
    
    #if request.method == 'POST':
            #print('in POST')

            '''function check whether file exist in the path or not'''
            
            def where_json(file_name):return os.path.exists(file_name)
            
            ''' function return the refresh token '''
            
            def get_refresh_token(client_id,client_secret):
                CLIENT_ID = client_id
                CLIENT_SECRET = client_secret
                SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'
                REDIRECT_URI = 'http:localhost:8080'
              
                flow = OAuth2WebServerFlow(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,scope=SCOPE,redirect_uri=REDIRECT_URI)
                if where_json('credential.json')==False:
                   storage = Storage('credential.json') 
                   credentials = run_flow(flow, storage)
                   refresh_token=credentials.refresh_token
                   
                elif where_json('credential.json')==True:
                   with open('credential.json') as json_file:  
                       refresh_token=json.load(json_file)['refresh_token']
              
                return(refresh_token)
                
            client_id = '864316075373-o6fr2afsvb6hh0c1lgchvo5brm0uh3pq.apps.googleusercontent.com'
            client_secret = 'MVNrkrHeeKP8WdNgygLSJ8a5'
            refresh_token=get_refresh_token(client_id,client_secret)
            
            ''' function return the google analytics data for given dimension, metrics, start data, end data access token, type,goal number, condition'''
            
            def google_analytics_reporting_api_data_extraction(viewID,dim,met,start_date,end_date,refresh_token,transaction_type,goal_number,condition):
                
                viewID=viewID;dim=dim;met=met;start_date=start_date;end_date=end_date;refresh_token=refresh_token;transaction_type=transaction_type;condition=condition
                goal_number=goal_number
                viewID="".join(['ga%3A',viewID])
                
                if transaction_type=="Goal":
                    met1="%2C".join([re.sub(":","%3A",i) for i in met]).replace("XX",str(goal_number))
                elif transaction_type=="Transaction":
                    met1="%2C".join([re.sub(":","%3A",i) for i in met])
                    
                dim1="%2C".join([re.sub(":","%3A",i) for i in dim])
                
                if where_json('credential.json')==True:
                   with open('credential.json') as json_file:  
                       storage_data = json.load(json_file)
                   
                   client_id=storage_data['client_id']
                   client_secret=storage_data['client_secret']
                   credentials = client.OAuth2Credentials(
                            access_token=None, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token,
                            token_expiry=3600,token_uri=GOOGLE_TOKEN_URI,user_agent='my-user-agent/1.0',revoke_uri=GOOGLE_REVOKE_URI)
            
                   credentials.refresh(httplib2.Http())
                   rt=(json.loads(credentials.to_json()))['access_token']
              
                   api_url="https://www.googleapis.com/analytics/v3/data/ga?ids="
                
                   url="".join([api_url,viewID,'&start-date=',start_date,'&end-date=',end_date,'&metrics=',met1,'&dimensions=',dim1,'&max-results=1000000',condition,'&access_token=',rt])
                
                   data=pd.DataFrame()
                
                   try:
                     r = requests.get(url)
                            
                     try:
                        data=pd.DataFrame(list((r.json())['rows']),columns=[re.sub("ga:","",i) for i in dim+met])
                        #data['date']=start_date
                        print("data extraction is successfully completed")
                       
                        return data
                     except:
                        print((r.json()))
                   except:
                     print((r.json()))
                     print("error occured in the google analytics reporting api data extraction")
            
            viewID='166538351'
            dim=['ga:userType','ga:sessionCount','ga:pagePath','ga:browser','ga:sourceMedium','ga:country','ga:date']
            met=['ga:users','ga:newUsers','ga:bounceRate','ga:organicSearches','ga:avgSessionDuration']
            transaction_type='Transaction'
            goal_number=''
            refresh_token=refresh_token
            condition='&sort=-ga%3Ausers'
            
            data=google_analytics_reporting_api_data_extraction(viewID,dim,met,start_date,end_date,refresh_token,transaction_type,goal_number,condition)
            data.date.apply(str)
            def clean(x):
                x = x[:4]+ '/' + x[4:6] + '/' + x[6:]
                return str(x)
            data['date'] = data['date'].apply(clean)
            data = data[['userType','sessionCount','pagePath','browser','sourceMedium','country','users','newUsers','bounceRate','organicSearches','avgSessionDuration','date']]
            data.to_excel("/home/adventum/Documents/Google_Analytics_API_Data/output.xlsx")
            
            data['users']=pd.to_numeric(data['users'])
            
            group1 = data.groupby(['userType']).sum()
            group1.reset_index(inplace=True)
            
            group2 = data.groupby(['date']).sum()
            group2.reset_index(inplace=True)
            
            group3 = data.groupby(['country']).sum()
            group3.reset_index(inplace=True)
            
            group4 = data.groupby(['browser']).sum()
            group4.reset_index(inplace=True)
            
            group5 = data.groupby(['pagePath']).sum()
            group5.reset_index(inplace=True)
            group5 = group5.sort_values(['users'],ascending=False)
            group5 = group5.head(5)
            
            g1 = group1.to_json(orient='records')
            g2 = group2.to_json(orient='records')
            g3 = group3.to_json(orient='records')
            g4 = group4.to_json(orient='records')
            g5 = group5.to_json(orient='records')
            out = data.to_json(orient='records')
            
            out = out.replace('\\','')
            out = out.replace('}]','},')
            
            #New Visitor/Existing Visitor
            g1 = g1.replace('"userType":"New Visitor","users"','"New_Visitor"')
            g1 = g1.replace('"userType":"Returning Visitor","users"','"Returning_Visitor"')
            g1 = g1.replace('[{','{')
            g1 = g1.replace(':',':"')
            g1 = g1.replace('}','"}')
            g1 = g1.replace('},{',',')
            g1 = g1.replace('}]','},')
            
            g2 = g2.replace('"date":','')
            g2 = g2.replace('"userType":"Returning Visitor","users"','"Returning Visitor"')
            g2 = g2.replace('[{','{')
            g2 = g2.replace(':',':"')
            g2 = g2.replace('}','"}')
            g2 = g2.replace('},{',',')
            g2 = g2.replace('\/','/')
            g2 = g2.replace(',"users"','')
            g2 = g2.replace('}]','},')
            
            g3 = g3.replace('"country":','')
            g3 = g3.replace(',"users"','')
            g3 = g3.replace('[{','{')
            g3 = g3.replace(':',':"')
            g3 = g3.replace('}','"}')
            g3 = g3.replace('},{',',')
            g3 = g3.replace('\/','/')
            g3 = g3.replace(',"users"','')
            g3 = g3.replace('}]','},')
            
            g4 = g4.replace('"browser":','')
            g4 = g4.replace(',"users"','')
            g4 = g4.replace('[{','{')
            g4 = g4.replace(':',':"')
            g4 = g4.replace('}','"}')
            g4 = g4.replace('},{',',')
            g4 = g4.replace('\/','/')
            g4 = g4.replace(',"users"','')
            g4 = g4.replace('}]','},')
            
            g5 = g5.replace('"pagePath":','')
            g5 = g5.replace(',"users"','')
            g5 = g5.replace('[{','{')
            g5 = g5.replace(':',':"')
            g5 = g5.replace('}','"}')
            g5 = g5.replace('},{',',')
            g2 = g2.replace(',"users"','')
            g5 = g5.replace('\/','/')
            g5 = g5.replace('/','/home')
            
            
            #print(type(out))
            with open('/home/adventum/Documents/Google_Analytics_API_Data/out_json.txt', 'w') as f:
                f.write(out)
            with open('/home/adventum/Documents/Google_Analytics_API_Data/g1_json.txt', 'w') as f:
                f.write(g1)     
            with open('/home/adventum/Documents/Google_Analytics_API_Data/g2_json.txt', 'w') as f:
                f.write(g2)
            with open('/home/adventum/Documents/Google_Analytics_API_Data/g3_json.txt', 'w') as f:
                f.write(g3)
            with open('/home/adventum/Documents/Google_Analytics_API_Data/g4_json.txt', 'w') as f:
                f.write(g4)
        
            def show_wordcloud(data, title = None):
                            wordcloud = WordCloud(
                                background_color='black',
                                height = 200,
                                width = 300,
                                stopwords=stopwords,
                                max_words=2000,
                                max_font_size=50,
                                scale=3,
                                random_state=1,collocations=False
                            ).generate(str(data))
                        
                            fig = fig = plt.figure(
                                figsize = (10, 10),
                                facecolor = 'k',    
                                edgecolor = 'k')
                            plt.axis('off')
                            if title: 
                                fig.suptitle(title, fontsize=20)
                                fig.subplots_adjust(top=2.3)
                        
                            #plt.imshow(wordcloud,interpolation = 'bilinear')
                            #plt.tight_layout(pad=0)
                            #plt.show()
                            wordcloud.to_file("/home/adventum/Documents/Google_Analytics_API_Data/wc.jpg")
            text = " ".join(country for country in data.country)
            text = text.replace('United States','United_States')
            text = text.replace('Hong Kong','Hong_Kong')
            text = text.replace('South Africa','South_Africa')
            text = text.replace('United Arab Emirates','UAE')
            text = text.replace('United States','United_States')
            text = text.replace('United Kingdom','United_Kingdom')
            
            show_wordcloud(text)
            
            new = out+g1+g2+g3+g4+g5
            with open('/home/adventum/Documents/Google_Analytics_API_Data/new.txt','w') as f:
                f.write(new)
            #c = {key: value for (key, value) in (out.items() + g1.items())}
            #print(new)
            return new
            
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')