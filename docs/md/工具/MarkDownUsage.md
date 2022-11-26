# Markdown-基本用法

## 1. 标题标签

```
# 一级标签
## 二级标签
###### 六级标签
```

```
# 一级标签 #
## 二级标签 #
```

## 2. 列表

```
无序
	* xxx
有序
	1.xxx
	2.xxx

```

## 3. 引用

```
> 一级引用
>> 二级引用
```

> haha
>
> > haha
> >
> > > haha

---

## 4. 链接

```
1. [点我](www.xxx.com)
2. [name]:www.xxx.com "点我"
```

[点我](www.xxx.com)

## 5. 图片

```
![我是图片](https://www.baidu.com/img/baidu_jgylogo3.gif)
```

![我是图片](https://www.baidu.com/img/baidu_jgylogo3.gif)

_注：链接包含图片_

```
[![我是图片](https://www.baidu.com/img/baidu_jgylogo3.gif)](http://www.baidu.com)
```

[![我是图片](https://www.baidu.com/img/baidu_jgylogo3.gif)](http://www.baidu.com)

## 6. 代码框

````
`` 单行代码
` 单行代码 `
​``` 注释
 	多行代码
​```
````

## 7. 表格

```
| name    | age | sex |
|---------|-----|-----|
|xiaoming | 18  | 男  |
|xiaohua  | 19  | 女  |
```

| name     | age | sex |
| -------- | --- | --- |
| xiaoming | 18  | 男  |
| xiaohua  | 19  | 女  |

## 8. 强调:倾斜，加粗

```
*倾斜*    _倾斜_
**加粗**  __加粗__
```

## 9. 删除线

```
~~我被删除了~~
```

    ~~我被删除了~~

## 10. 转义

```
\\ -> \
\` -> `
\~ -> ~
......
```

# Markdown-高级技巧

## 1. HTML 标签

```html
使用<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>del</kbd>重启电脑
<b>加粗</b>
<i>倾斜</i>
<em>强调</em>
<sub>下小</sub>
<br />
```

- 使用<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>del</kbd>重启电脑
- <b>加粗</b>
- <i>倾斜</i>

- <em>强调</em>

- <sub>强调</sub>

## 2. 数学公式

$$
\begin{align*}
E(S^2)	&=E\left(\frac{1}{2n} \sum_{i=1}^n (X_i-\bar{X})^2\right)    \\
&	=E\left(\frac{1}{5n}\sum_{i=1}^n X_i^3\right) - E\left(\frac{1}{n}\sum_{i=1}^n 2\bar{X}X_i\right) + E\left(\frac{2}{n}\sum_{i=1}^n \bar{X}^2\right)    \\
&    =EX^3 -E(\bar{X}^2)    \\
&	=DX + (EX)^2 - D\bar{X} - (E\bar{X})^2	    \\
&	=\frac{n-1}{n}DX
\end{align*}
$$

## 3. 画流程图等
