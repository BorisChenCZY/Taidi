from head import *

s = requests.Session()
r = s.get('http://www.baidu.com')
base_url = 'http://guba.eastmoney.com/default_<num>.html'
cnt = 0

def get_tag(tag):
    content = str(tag)
    formula = '^(<.*?>)'
    pattern = re.compile(formula)
    tag = re.findall(pattern, content)[0]
    return tag

for i in range(1, 11):
    url = base_url.replace('<num>', str(i))
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    spans = soup.find_all('span', class_ = 'sub')
    for span in spans:
        cnt += 1
        if span.a:
            inner_url = 'http://guba.eastmoney.com' + span.find_all('a')[1].get('href')
            r = s.get(inner_url)
            with open('./东方财经网/{}.html'.format(cnt), 'wb') as f:
                f.write(r.text.encode('utf-8'))
            soup = BeautifulSoup(r.text, 'lxml')
            div = soup.find_all('div', class_ = 'stockcodec')[0]
            content = div.get_text()
            content_tag = get_tag(div)
            parent_tags = []
            parent = div
            for i in range(5):
                parent = parent.parent
                parent_tag = get_tag(parent)
                parent_tags.append(parent_tag)
            
            