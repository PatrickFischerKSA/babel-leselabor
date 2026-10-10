"""Import public Gutenberg title/author/link metadata, never full texts."""
import concurrent.futures,html,json,re,urllib.request,urllib.parse
from pathlib import Path
BASE='https://projekt-gutenberg.org'
def fetch(url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'BabelLeselabor/1.0 (public title catalogue)'}),timeout=45) as r:return r.read().decode()
def parse(page):
 result=[]
 for item in re.findall(r'<li class="book-app__index-item">(.*?)</li>',page,re.S):
  link=re.search(r'class="book-app__index-link" href="([^"]+)"',item)
  title=re.search(r'class="book-app__index-title">(.*?)</span>',item,re.S)
  author=re.search(r'book-app__index-meta--author">(.*?)</span>',item,re.S)
  if link and title:result.append({'title':html.unescape(re.sub('<[^>]+>','',title[1])).strip(),'author':html.unescape(author[1]).strip() if author else '', 'url':html.unescape(link[1])})
 return result
initial=fetch(BASE+'/bibliothek/')
letters=list(dict.fromkeys(html.unescape(x).split('#')[0] for x in re.findall(r'class="book-app__az-link[^"]*" href="([^"]+)"',initial)))
# The site's # link is malformed; numeric titles are requested explicitly.
letters=[x if 'gl_letter=' in x else '/bibliothek/?gl_letter=%23' for x in letters]
books=[];pending=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for path,page in zip(letters,pool.map(fetch,[BASE+x for x in letters])):
  books.extend(parse(page));m=re.search(r'Seite\s+1\s+von\s+(\d+)',page)
  pages=int(m[1]) if m else 1
  pending.extend(BASE+path+'&gl_page='+str(i) for i in range(2,pages+1))
 print('Letters parsed; additional pages:',len(pending),flush=True)
 for page in pool.map(fetch,pending):books.extend(parse(page))
unique={b['url']:b for b in books};books=sorted(unique.values(),key=lambda b:b['title'].casefold())
assert len(books)>10000,len(books)
Path('assets/gutenberg-catalog.json').write_text(json.dumps({'updated':'2026-10-10','source':BASE+'/bibliothek/','count':len(books),'books':books},ensure_ascii=False,separators=(',',':')))
print('Imported',len(books),'unique works',flush=True)
