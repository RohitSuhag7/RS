from django.shortcuts import render
import tweepy
import pandas as pd
from textblob import TextBlob

# Create your views here.
def home(request):
    return render(request,'home.html')

def hacked(request):
    if request.method == 'GET':
        df = pd.read_csv("D:/Data_Stream/hackedDB.csv",error_bad_lines=False)
        data = []
        for i in range(0, len(df)):
            s = df.index[i][3]
            s = s[5:]
            data.append(s)
        return render(request,'hacked.html',{'datas':data})
        
    elif request.method == 'POST':
        positive_number=0
        negative_number=0
        neutral_number=0
        params = request.POST
        tweet=params['tweet']
        analysis = TextBlob(tweet)
       
        if analysis.sentiment[0]>0:
            status="Positive"
            
            print(tweet,': Positive')
        elif analysis.sentiment[0]<0:
            status="Negative"
            
            print(tweet,': Negative')
        else:
            status="Neutral"
            print(tweet,': Neutral')
       
        df = pd.read_csv("D:/Data_Stream/hackedDB.csv",error_bad_lines=False)
        data = []
        for i in range(0, len(df)):
            s = df.index[i][3]
            s = s[5:]
            data.append(s)
        for i in data:
            analysis = TextBlob(i)
            if analysis.sentiment[0]>0:
                positive_number=positive_number+1
                
            elif analysis.sentiment[0]<0:
                negative_number=negative_number+1
        
            else:
                neutral_number=neutral_number+1
        positive_percentage=(positive_number/len(data))*100
        negative_percentage=(negative_number/len(data))*100
        neutral_percentage=(neutral_number/len(data))*100
        

        return render(request,"hacked.html",{"datas":data,"status":status,"positive_percentage":positive_percentage,"negative_percentage":negative_percentage,"neutral_percentage":neutral_percentage})


def karma(request):
    if request.method == 'GET':
        df = pd.read_csv("D:/Data_Stream/karmaDB.csv",error_bad_lines=False,header=None)
        data = []
        for i in range(0, len(df)):
            s = df[3][i]
            s = s[5:]
            data.append(s)
        return render(request,'karma.html',{'datas':data})

    elif request.method == 'POST':
        positive_number=0
        negative_number=0
        neutral_number=0
        params = request.POST
        tweet=params['tweet']
        analysis = TextBlob(tweet)
        if analysis.sentiment[0]>0:
            status="Positive"
            print(tweet,': Positive')
        elif analysis.sentiment[0]<0:
            status="Negative"
            print(tweet,': Negative')
        else:
            status="Neutral"
            print(tweet,': Neutral')

        df = pd.read_csv("D:/Data_Stream/karmaDB.csv",error_bad_lines=False,header=None)
        data = []
        for i in range(0, len(df)):
            s = df[3][i]
            s = s[5:]
            data.append(s)
        for i in data:
            analysis = TextBlob(i)
            if analysis.sentiment[0]>0:
                positive_number=positive_number+1
                
            elif analysis.sentiment[0]<0:
                negative_number=negative_number+1
        
            else:
                neutral_number=neutral_number+1
        positive_percentage=(positive_number/len(data))*100
        negative_percentage=(negative_number/len(data))*100
        neutral_percentage=(neutral_number/len(data))*100
        return render(request,"karma.html",{"datas":data,"status":status,"positive_percentage":positive_percentage,"negative_percentage":negative_percentage,"neutral_percentage":neutral_percentage})

def thor(request):
    if request.method == 'GET':
        df = pd.read_csv("D:/Data_Stream/thorDB.csv",error_bad_lines=False,header=None)
        data = []
        for i in range(0, len(df)):
            s = df[3][i]
            s = s[5:]
            data.append(s)
        return render(request,'thor.html',{'datas':data})

    elif request.method == 'POST':
        positive_number=0
        negative_number=0
        neutral_number=0
        params = request.POST
        tweet=params['tweet']
        analysis = TextBlob(tweet)
        if analysis.sentiment[0]>0:
            status="Positive"
            print(tweet,': Positive')
        elif analysis.sentiment[0]<0:
            status="Negative"
            print(tweet,': Negative')
        else:
            status="Neutral"
            print(tweet,': Neutral')
        df = pd.read_csv("D:/Data_Stream/thorDB.csv",error_bad_lines=False,header=None)
        data = []
        for i in range(0, len(df)):
            s = df[3][i]
            s = s[5:]
            data.append(s)
        for i in data:
            analysis = TextBlob(i)
            if analysis.sentiment[0]>0:
                positive_number=positive_number+1
                
            elif analysis.sentiment[0]<0:
                negative_number=negative_number+1
        
            else:
                neutral_number=neutral_number+1
        positive_percentage=(positive_number/len(data))*100
        negative_percentage=(negative_number/len(data))*100
        neutral_percentage=(neutral_number/len(data))*100
        return render(request,"thor.html",{"datas":data,"status":status,"positive_percentage":positive_percentage,"negative_percentage":negative_percentage,"neutral_percentage":neutral_percentage})


def covid(request):
    if request.method == 'GET':
        df = pd.read_csv("D:/Data_Stream/covid-19DB.csv",error_bad_lines=False,header=None)
        data = []
        for i in range(0, len(df)):
            s = df[3][i]
            s = s[5:]
            data.append(s)
        return render(request,'covid.html',{'datas':data})

    elif request.method == 'POST':
        positive_number=0
        negative_number=0
        neutral_number=0
        params = request.POST
        tweet=params['tweet']
        analysis = TextBlob(tweet)
        if analysis.sentiment[0]>0:
            status="Positive"
            print(tweet,': Positive')
        elif analysis.sentiment[0]<0:
            status="Negative"
            print(tweet,': Negative')
        else:
            status="Neutral"
            print(tweet,': Neutral')
        df = pd.read_csv("D:/Data_Stream/covid-19DB.csv",error_bad_lines=False,header=None)
        data = []
        for i in range(0, len(df)):
            s = df[3][i]
            s = s[5:]
            data.append(s)
        for i in data:
            analysis = TextBlob(i)
            if analysis.sentiment[0]>0:
                positive_number=positive_number+1
                
            elif analysis.sentiment[0]<0:
                negative_number=negative_number+1
        
            else:
                neutral_number=neutral_number+1
        positive_percentage=(positive_number/len(data))*100
        negative_percentage=(negative_number/len(data))*100
        neutral_percentage=(neutral_number/len(data))*100
        return render(request,"covid.html",{"datas":data,"status":status,"positive_percentage":positive_percentage,"negative_percentage":negative_percentage,"neutral_percentage":neutral_percentage})