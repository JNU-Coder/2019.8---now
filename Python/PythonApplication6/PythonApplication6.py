d={'中国':'北京','法国':'巴黎','英国':'伦敦'}
print('中国'in d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get('中国',2))
print(d.pop('中国',2))
print(d)
print(len(d))
dist={}
dist['1']='2'
dist['6']='9'
dist['6']='2'
print(dist)
print('a'in dist)  