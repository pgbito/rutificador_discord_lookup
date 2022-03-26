import random
import bs4, html, requests, html_to_json as htj, json

def prepared_request(q):
          term = '+'.join(q.split(' '))
          print(term)
          request = requests.Request(url="https://www.nombrerutyfirma.com/buscar",method='POST',data=f"term={term}", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded",
        "Alt-Used": "www.nombrerutyfirma.com",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin"
    })
          request = request.prepare()
          return request

def html_to_json(content: bytes):
    ####### Config ######
    contentclass='table table-hover'
    content=content.decode('utf-8',errors='ignore')
    """obj = htj.convert(content)['html'][0]['body'][0]['div'][1]['div']\
    [0]['table'][0]"""
    obj = htj.convert_html_tables.convert_tables(content)[0]

    
    return json.dumps(obj,indent=4)
def search(query):
    session = requests.Session()
    pr = prepared_request(query)
    response = session.send(pr)

    return html_to_json(response.content)

import http.server

def embedify(content, blockcode=False, blockcodeFormat=None):
    if blockcode is True:
        if blockcodeFormat is None:
            useblockcode = False
        useblockcode = True
    else: useblockcode = False
    if useblockcode is True:
        nl='\n'
        content = f'```{blockcodeFormat}{nl}{content}```'
    em = discord.Embed()
    em.description = content
    em.color = client.user.color
    return em
