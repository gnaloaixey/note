# JAVA开发回顾

## 一、maven

## 二、软件测试

* 在规定条件下对程序操作，以致发现程序错误，衡量软件质量，对设计要求进行评估

1. 单元测试&集成测试
2. 白盒测试&黑盒测试
3. 自动测试&手动测试
4. 回归测试
5. 压力测试
6. 。。。

* Junit

## 三、高级文本处理

## 四、高级文件处理

### 图像文件处理:

* 图形:Graphm,矢量图
* 图像:Image,
  1. 由像素点组成
  2. 格式:jpg,png,bmp,gif等
  3. 颜色:RGB(Red,Green,Blue)
* 条形码识别和生成
* 二维码识别和生成

### word 文档处理

### 表格文件处理

* xls/xlsx 文件(Microsoft Excel)
* CSV文件(Comma Seperated Values)

## 五、java多线程和并发编程

### 多线程概念:

* 当前的操作系统都是多任务OS
* 每个独立执行的任务就是一个进程
* OS将时间划分为多个时间片(时间很短)
* 每个时间片将CPU分配给某一任务。时间片结束，CPU将自动回收，再分配给另外任务。从外部看，所有任务同时进行，但在CPU上，任务是按照串行依次运行(单核，多核可以并行)

### java实现 

* java.lang.Thread，继承Tread类
* java.lang.Runnable接口，实现run()方法
* start()方法线程启动，run()方法结束即线程结束

### 信息共享处理

* volatile 关键词,公用工作缓存

* 关键步骤加锁
  1. 互斥(synchronized):代码关键区,线程不能同时修改这个代码块
  2. 同步:多个线程运行，必须按照某一种先后顺序来执行
  3. 互斥是同步的一种特例

### 多线程管理

* 线程状态
  1. new 刚创建
  2. runnable就绪态
  3. running运行中
  4. block阻塞(sleep)
  5. terminated结束
* Tread部分API
  1. sleep,睡眠
  2. wait/notify/notifyAll,等待
  3. join,等待另一个线程结束
  4. interrupt,向另外一个线程发送中断信号

### 并发

* 共享线程池原理，
* executor框架(java5)，fork-joi
* n框架(java7)



## 六、网络编程

### UDP

* DatagramSocket:send(),receive()
* DatagramPacket

### TCP





