import requests
from lxml import etree
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
         }
def get_data() :

        url = 'https://www.liepin.com/zhaopin/?key='
        insult_job = input('请输入要查找的职位：')
        url = url + insult_job
        for pagenum in range(0, 30):
            pagenum = str(pagenum)
            new_url = url + "&curPage="+pagenum
            insult_job = str(insult_job)
            print(new_url)
            fp = open('./HTML.html', 'wb')
            response = requests.get(url=new_url, headers=headers).text
            fp.write(response.encode(encoding='utf-8'))
        return response

if __name__ == '__main__':

    response = get_data()
    parser = etree.HTMLParser()
    tree = etree.parse('HTML.html', parser)
    with open('note.txt','w',encoding='utf-8') as fp:
        url = tree.xpath('/html/body//h3/a/@href')
        text = tree.xpath('/html/body//h3//a/text()')
        length = len(text)
        for a in range (0,length):
            fp.write(text[a])
            fp.write(url[a])



