#News program 

from newsapi import NewsApiClient

def getNews():
    newsapi = NewsApiClient(api_key = "cc030e0254b443dc8d65a1f7c09b3794")


    data = newsapi.get_top_headlines(q='coronavirus updates',language = 'en')

    articles = data['articles']


    f = open('/Users/adarshbulusu/Desktop/Kivy_News/update_links.txt','w')
    g = open('/Users/adarshbulusu/Desktop/Kivy_News/updates_headers.txt','w')
    
    for a,b in enumerate(articles):
        f.write(f'{a}  {b["url"]} ') 
        f.write('\n')

    for a,b in enumerate(articles):
        g.write(f'{a}  {b["title"]} ')
        g.write('\n')

    f.close()
    g.close()

