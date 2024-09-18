# Wireshark实验 - NAT

**官方英文文档：[Wireshark_NAT_v8.1.doc](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_NAT_v8.1.doc)**

**trace文件：[nat-inside-wireshark-trace1-1.pcapng](http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces-8.1.zip), [nat-outside-wireshark-trace1-1.pcapng](http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces-8.1.zip)**

## NAT测量场景

**1.发送 HTTP GET 请求的客户端的 IP 地址是什么？在 `nat-inside-wireshark-trace1-1.pcapng` 跟踪中的包含 HTTP GET 请求的 TCP 段的源端口号是什么？该 HTTP GET 请求的目标 IP 地址是什么？包含 HTTP GET 请求的 TCP 段的目标端口号是什么？**

<img src='.\Figure\nat-1.png'>

答：如图，客户端IP地址为`192.168.10.11`，源端口号为53924，目的IP地址为`138.76.29.8`，目的端口号为80。

**2.NAT 路由器将 Web 服务器的对应 HTTP 200 OK 消息转发到路由器 LAN 侧的客户端的时间是什么？**

<img src='.\Figure\nat-2.png'>

答：如图，时间是0.030672101ms。

**3.携带 HTTP 200 OK 消息的 IP 数据报的源和目标 IP 地址以及 TCP 段的源和目标端口是什么？**

<img src='.\Figure\nat-3.png'>

答：如图，源IP地址为`138.76.29.8`，目的IP地址为`192.168.10.11`，源端口为80，目的端口为53924。



**在 `nat-outside-wireshark-trace1-1.pcapng` 跟踪文件中，找到与在时间 `t=0.027362245` 发送的 HTTP GET 消息对应的 HTTP GET 消息，其中 `t=0.027362245` 是消息发送的时间，这个时间记录在 `nat-inside-wireshark-trace1-1.pcapng` 跟踪文件中。**



**4.此 HTTP GET 请求消息出现在 `nat-outside-wireshark-trace1-1.pcapng` 跟踪文件中的时间是什么时候？**

<img src='.\Figure\nat-4.png'>

答：如图，对应时间是0.027356291ms。

**5.在 `nat-outside-wireshark-trace1-1.pcapng` 跟踪文件中，承载此 HTTP GET 请求的 IP 数据报的源 IP 地址和目的 IP 地址是什么？TCP 源端口和目的端口号是什么？**

<img src='.\Figure\nat-5.png'>

答：如图，源IP地址为`10.0.1.254`，目的IP地址为`138.76.29.8`，源端口号为53924，目的端口号为80。

**6.与问题 1 中的答案相比，这四个字段中有哪些字段发生了变化？**

答：源IP地址发生了变化。

**7.HTTP GET 消息中的任何字段发生了变化吗？**

<img src='.\Figure\nat-6.png'>

答：如图，并未发生任何变化。

**8.承载 HTTP GET 请求的 IP 数据报从局域网（内部）接收到的报文到在 NAT 路由器上转发到互联网端（外部）的对应报文中，下列哪个字段发生了变化：版本、首部长度、标志、校验和？**

<img src='.\Figure\nat-7.png'>

答：如图，仅有首部校验和发生了变化。



**让我们继续查看 `nat-outside-wireshark-trace1-1.pcapng` 跟踪文件。找到 HTTP 响应，其中包含对上面问题 4 到 8 中检查的 HTTP GET 请求的 "200 OK" 响应消息。**



**9.此消息出现在 `nat-outside-wireshark-trace1-1.pcapng` 跟踪文件中的时间是什么时候？**

<img src='.\Figure\nat-8.png'>

答：如图，出现时间为0.030625966ms。

**10.在 `nat-outside-wireshark-trace1-1.pcapng` 跟踪文件中，承载此 HTTP 响应 ("200 OK") 消息的 IP 数据报的源 IP 地址和目的 IP 地址是什么？TCP 源端口和目的端口号是什么？**

<img src='.\Figure\nat-9.png'>

答：源IP地址为`138.76.29.8`，目的IP地址为`10.0.1.254`，源端口为80，目的端口为53924。

**11.承载 HTTP 响应 ("200 OK") 的 IP 数据报的源 IP 地址和目的 IP 地址是什么？TCP 源端口和目的端口号是什么？当数据报从路由器转发到图 1 右侧的目标主机时，这些字段的值是什么？**

答：转发到目标主机时，源IP地址为`138.76.29.8`，目的IP地址为`192.168.10.11`，源端口号为80，目的端口号为53924。