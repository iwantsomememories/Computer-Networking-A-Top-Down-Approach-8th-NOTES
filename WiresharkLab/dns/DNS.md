# Wireshark实验 - DNS

**官方英文文档：[Wireshark_DNS_v8.0.pdf](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_DNS_v8.0.pdf)**

## 1.nslookup

**1.运行*nslookup*以获取一个亚洲的Web服务器的IP地址。该服务器的IP地址是什么？**

<img src=".\Figure\DNS-1.png" />

答：以www.baidu.com为例，可以看到，其规范主机名为www.a.shifen.com，ip地址包括182.61.200.7以及182.61.200.6。

**2.运行*nslookup*来确定一个欧洲的大学的权威DNS服务器。**

<img src=".\Figure\DNS-2.png" />

答：以牛津大学为例，可以看到，牛津大学共有三个权威DNS服务器，分别为dns0.ox.ac.uk，dns1.ox.ac.uk，dns2.ox.ac.uk。

**3.运行*nslookup*，使用问题2中一个已获得的DNS服务器，来查询Yahoo!邮箱的邮件服务器。它的IP地址是什么？**

<img src=".\Figure\DNS-3-1.png" />

答：多次尝试发现似乎不支持通过权威DNS查询邮件服务器，直接查询可以。

<img src=".\Figure\DNS-3-2.png" />

## 2.ipconfig

值得注意的是ifconfig并没有查询以及刷新dns记录的功能。

## 3.使用Wireshark追踪DNS

**4.找到DNS查询和响应消息。它们是否通过UDP或TCP发送？**

<img src=".\Figure\DNS-4.png" />

答：UDP。

**5.DNS查询消息的目标端口是什么？ DNS响应消息的源端口是什么？**

<img src=".\Figure\DNS-5.png" />

答：查询消息的目标端口为53，响应消息的源端口为53。

**6.DNS查询消息发送到哪个IP地址？使用ipconfig来确定本地DNS服务器的IP地址。这两个IP地址是否相同？**

<img src=".\Figure\DNS-6.png" />

答：发送到192.168.31.1，与本地DNS的IP地址相同。

**7.检查DNS查询消息。DNS查询是什么"Type"的？查询消息是否包含任何"answers"？**

答：type A，查询消息不包含answer。

**8.检查DNS响应消息。提供了多少个"answers"？这些答案具体包含什么？**

<img src=".\Figure\DNS-8.png" />

答：提供了2个answer，两个answer相同都是A类型，显示www.ietf.org的ip地址包括104.16.45.99以及104.16.44.99。

**9.考虑从您主机发送的后续TCP SYN数据包。 SYN数据包的目的IP地址是否与DNS响应消息中提供的任何IP地址相对应？**

<img src=".\Figure\DNS-9.png" />

答：是的。

**10.这个网页包含一些图片。在获取每个图片前，您的主机是否都发出了新的DNS查询？**

答：发出来对static.ietf.org的DNS查询。

**使用nslookup查询 www.mit.edu **

<img src=".\Figure\DNS-10.png" />

**11.DNS查询消息的目标端口是什么？ DNS响应消息的源端口是什么？**

答：查询消息的目标端口为53，响应消息的源端口为53。

**12.DNS查询消息的目标IP地址是什么？这是你的默认本地DNS服务器的IP地址吗？**

答：目标IP地址为192.168.31.1，是默认本地DNS服务器的IP地址。

**13.检查DNS查询消息。DNS查询是什么"Type"的？查询消息是否包含任何"answers"？**

<img src=".\Figure\DNS-11.png" />

答：type AAAA，不包含任何answer。

**14.检查DNS响应消息。提供了多少个"answers"？这些答案包含什么？**

<img src=".\Figure\DNS-12.png" />

答：提供了4个answer，包含CNAME类型回复，指明了www.mit.edu的规范名称为www.mit.edu.edgekey.net，而www.mit.edu.edgekey.net的规范名称为e9566.dscb.akamaiedge.net；包含AAAA类型回复，指明e9566.dscb.akamaiedge.net的IPv6地址为2600:1417:8400:988::255e以及2600:1417:8400:9bb::255e。

**15.提供屏幕截图。**

答：如上图。

**输入`nslookup -type=NS mit.edu`命令**

<img src=".\Figure\DNS-13.png" />

**16.DNS查询消息发送到的IP地址是什么？这是您的默认本地DNS服务器的IP地址吗？**

<img src=".\Figure\DNS-14.png" />

答：192.168.31.1，是默认本地本地DNS服务器的IP地址。

**17.检查DNS查询消息。DNS查询是什么"Type"的？查询消息是否包含任何"answers"？**

答：type NS，不包含任何answer。

**18.检查DNS响应消息。响应消息提供的MIT域名服务器是什么？此响应消息还提供了MIT域名服务器的IP地址吗？**

<img src=".\Figure\DNS-15.png" />

答：一共提供了8个MIT域名服务器，分别为：ns1-173.akam.net，asia2.akam.net，eur5.akam.net，use5.akam.net，ns1-37.akam.net，usw2.akam.net，asia1.akam.net，use2.akam.net；并没有提供MIT域名服务器的IP地址。

**19.提供屏幕截图。**

答：如上图。

**输入`nslookup www.aiit.or.kr bitsy.mit.edu`命令**

**此处因`bitsy.mit.edu`已弃用，直接分析作者追踪结果。**

**20.DNS查询消息发送到的IP地址是什么？这是您的默认本地DNS服务器的IP地址吗？如果不是，这个IP地址是什么？**

(网页暂时打不开)