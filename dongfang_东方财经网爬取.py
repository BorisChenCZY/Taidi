from head import *

s = requests.Session()
r = s.get('http://www.baidu.com')
base_url = 'http://guba.eastmoney.com/default_<num>.html'
cnt = 0

df = pd.DataFrame(pandas_head)
# print(df)
# quit()
for i in range(1, 11):
    url = base_url.replace('<num>', str(i))
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    spans = soup.find_all('span', class_ = 'sub')
    cnt = 0
    total = len(spans)
    for span in spans:
        cnt += 1
        if span.a:
            inner_url = 'http://guba.eastmoney.com' + span.find_all('a')[1].get('href')
            r = s.get(inner_url)
            soup = BeautifulSoup(r.text, 'lxml')
            div = soup.find_all('div', class_ = 'stockcodec')[0]
            content = div.get_text()
            content_tag = get_tag(div)
            content_parent_tags = find_parent(div)
            author_div = soup.find(id = 'zwconttbn')
            author = author_div.get_text()
            author_tag = get_tag(author_div)
            author_parent_tags = find_parent(author_div)
            df = add_row(df, r.text, content, content_tag, *content_parent_tags, author, author_tag, *author_parent_tags)
            # print(df)
            # quit()
            print('{}/{}'.format(cnt, total))

df.to_csv('./东方财经.csv')


