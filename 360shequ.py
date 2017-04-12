# encode = utf-8

from head  import *

s=requests.Session()
base_url='http://bbs.360.cn/forum-140-<num>.html'
cnt=0

df=pd.DataFrame(pandas_head)
for i in range(1,11):
#for i in range(1,3):
    url=base_url.replace('<num>', str(i))
    r=s.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    divs=soup.find_all('div',class_='tl_ct')
    cnt=0
    total=len(divs)
    for div in divs:
        cnt+=1
        if div.a:
            inner_url=div.find_all('a')[0].get('href')
            r=s.get(inner_url)
            soup=BeautifulSoup(r.text,'lxml')
            div=soup.find_all('td',class_='t_f postmessage-top')[0]
            content=div.get_text()
            content_tag=get_tag(div)
            content_parent_tags=find_parent(div)
            #这个论坛主贴发布没作者信息。。要么没有，要么和正文一体
            #author_div=soup.find('',class_='')
            #author=author_div.find_all('a')[0].get('')
            #author_tag=get_tag(author_div)
            #author_parent_tags=find_parent(author_div)
            author=''
            author_tag=''
            author_parent_tags=('','','','','')
            df=add_row(df,r.text,content,content_tag,*content_parent_tags,author,author_tag,*author_parent_tags)
            print(df)
            quit()
            print('{}/{}'.format(cnt, total))
            
df.to_csv('./360社区.csv')