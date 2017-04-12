# encode = utf-8
#7k7k网页游戏里面每个游戏都有论坛，这里是爬的“神仙道”的论坛 

from head  import *

s=requests.Session()
base_url='http://8.7k7k.com/forum-311-<num>.html'
cnt=0

df=pd.DataFrame(pandas_head)
for i in range(1,11):
#for i in range(1,4):
    url=base_url.replace('<num>', str(i))
    r=s.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    divs=soup.find_all('th',class_='common')#为什么第一页只找了前三个，其他页面都没问题哇？
    cnt=0
    total=len(divs)
    for div in divs:
        cnt+=1
        if div.a:
            inner_url='http://8.7k7k.com/'+div.find_all('a')[0].get('href')
            r=s.get(inner_url)
            soup=BeautifulSoup(r.text,'lxml')
            div=soup.find_all('td',class_='t_f')[0]
            content=div.get_text()
            content_tag=get_tag(div)
            content_parent_tags=find_parent(div)
            author_div=soup.find('div',class_='authi')
            author=author_div.find_all('a')[0].get_text()
            author_tag=get_tag(author_div)
            author_parent_tags=find_parent(author_div)
            df=add_row(df,r.text,content,content_tag,*content_parent_tags,author,author_tag,*author_parent_tags)
            #print(df)
            #quit()
            print('{}/{}'.format(cnt, total))
            
df.to_csv('./7k7k游戏.csv')