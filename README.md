# analysis_catalina
通过java的启动命令分析catalina的所在目录位置

## 假设启动命令为：
/usr/local/jdk1.6/bin/java -Djava.util.logging.config.file=/usr/local/tomcats/websso/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -javaagent:/usr/local/tomcats/jspAgent/JSPAgent.jar -Xms49152m -Xmx49152m -Xss1024K -XX:PermSize=512m -XX:MaxPermSize=2048m -Djdk.tls.ephemeralDHKeySize=2048 -Djava.endorsed.dirs=/usr/local/tomcats/websso/endorsed -classpath /usr/local/tomcats/websso/bin/bootstrap.jar -Dcatalina.base=/usr/local/tomcats/websso -Dcatalina.home=/usr/local/tomcats/websso -Djava.io.tmpdir=/usr/local/tomcats/websso/temp org.apache.catalina.startup.Bootstrap start


## 格式化：
/usr/local/jdk1.6/bin/java<br>
-Djava.util.logging.config.file=/usr/local/tomcats/websso/conf/logging.properties<br>
-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager<br>
-javaagent:/usr/local/tomcats/jspAgent/JSPAgent.jar<br>
-Xms49152m<br>
-Xmx49152m<br>
-Xss1024K<br>
-XX:PermSize=512m<br>
-XX:MaxPermSize=2048m<br>
-Djdk.tls.ephemeralDHKeySize=2048<br>
-Djava.endorsed.dirs=/usr/local/tomcats/websso/endorsed<br>
-classpath/usr/local/tomcats/websso/bin/bootstrap.jar<br>
-Dcatalina.base=/usr/local/tomcats/websso<br>
-Dcatalina.home=/usr/local/tomcats/websso<br>
-Djava.io.tmpdir=/usr/local/tomcats/websso/temporg.apache.catalina.startup.Bootstrapstart<br>




## 结果：
/usr/local/tomcats/websso



## 示例：

![示例图片](picture1.png)

