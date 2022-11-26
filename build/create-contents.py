from array import array
from genericpath import isdir, isfile
import yaml
import os
import glob

dirname, filename = os.path.split(os.path.abspath(__file__))

config_file = open(os.path.join(dirname, './config.yaml'), encoding = 'utf-8')

# 用load加载配置
conf = yaml.load(config_file,Loader=yaml.SafeLoader)
config_file.close()

# 开始
# 目标字符串
target = f'# {conf["title"]}\n'

root = os.path.join(dirname,conf['root']);

suffixs =[s.strip() for s in str.split(conf['page-suffix'],',')] 

# 遍历root下的目录
def dfs(path,relative_path,deep):
	global target
	d, f = os.path.split(path)
	if(isfile(path)):
		d, f = os.path.split(path)
		target += '  '*(deep+1) +  f'- [{f}]({relative_path}/{f})\n'
		pass
	else:
		if deep == 0:
			target += '#'*(deep+2) + f' {f}\n'
		else:
			target += '  '*(deep) + f'- {f}\n'
		for new_path in glob.glob(path + '/*'):
			dfs(new_path,relative_path+f'/{f}',deep + 1)

for path in list(filter(lambda i:isdir(i), glob.glob(root + '/*'))):
	dfs(path,'.',0)

f = os.open(os.path.join(root, './index.md'),os.O_RDWR)
os.write(f,str.encode(target,'utf-8'))
os.close(f)
