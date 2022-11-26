## linux tomcat服务器安装和配置服务

### 安装

* cd /usr/local
* mkdir tomcat

* [tomcat tar包下载](https://tomcat.apache.org/download-90.cgi)，可以直接wget 

* 解压    tar -xvf 包名

* 环境变量   export CATALINA_HOME=/usr/local/文件名

  ​				   export PATH=$PATH:$CATALINA_HOME/bin

#### 配置服务

* cd /etc/init.d
* touch tomcat
* vi tomcat

```shell
#!/bin/bash
JAVA_HOME=/usr/local/java/jdk-13.0.1
CATALINA_HOME=/usr/local/tomcat/apache-tomcat-9.0.27

case $1 in
	start)
		sh $CATALINA_HOME/bin/startup.sh
		;;
	stop)
		sh $CATALINA_HOME/bin/shutdown.sh
		;;
	restart)
		sh $CATALINA_HOME/bin/shutdown.sh
		sh $CATALINA_HOME/bin/startup.sh
		;;
	*)
		echo 'please use : tomcat {start | stop | restart}'
		;;
esac
exit 0

```

* 将文件设置为可执行文件  chmod a+x tomcat
* update-rc.d tomcat defaults