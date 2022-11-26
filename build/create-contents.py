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

sortBy = lambda e:os.path.getmtime(e)
# 遍历root下的目录
def dfs(path,relative_path,deep):
	global target
	d, f = os.path.split(path)
	if(isfile(path) and sum((path[-len(suf):] == suf for suf in suffixs)) >=1):
		d, f = os.path.split(path)
		target += '  '*(deep) +  f'- [{f}]({relative_path}/{f})\n'
		pass
	else:
		if deep == 0:
			target += '#'*(deep+2) + f' {f}\n'
		else:
			target += '  '*(deep) + f'- {f}\n'
		dirs = glob.glob(path + '/*');
		dirs.sort(key = sortBy,reverse=True)
		for new_path in dirs:
			dfs(new_path,relative_path+f'/{f}',deep + 1)
# 可以限制根目录只识别子文件
dirs = glob.glob(root + '/*');
dirs.sort(key = sortBy,reverse=True)
for dir in dirs:
	dfs(dir,'.',0)
f = os.open(os.path.join(root, './index.md'),os.O_RDWR)
os.write(f,str.encode(target,'utf-8'))
os.close(f)
