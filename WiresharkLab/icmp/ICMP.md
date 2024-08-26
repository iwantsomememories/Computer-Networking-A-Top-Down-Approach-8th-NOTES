# Wireshark实验 - ICMP

**官方英文文档：[Wireshark_ICMP_v8.0.pdf](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_ICMP_v8.0.pdf)**

## ICMP和Ping

<img src='.\Figure\ICMP-1.png'>

**1.你的主机的IP地址是什么？目标主机的IP地址是什么？**

<img src='.\Figure\ICMP-2.png'>

答：源主机IP地址为192.168.31.199，目标主机IP地址为182.61.200.7。

**2.为什么ICMP数据包没有源端口号和目标端口号？**

答：因为ICMP并不运行在任何运输层协议之上，ICMP报文直接通过IP运输。

**3.检查由你的主机发送的一个ping请求包。ICMP的类型和代码号是多少？这个ICMP包还有哪些其他字段？校验和、序列号和标识符字段分别是多少字节？**

<img src='.\Figure\ICMP-3.png'>

答：如图，类型号为8，代码号为0；还包括校验和、标识符和序列号三个字段；校验和、标识符和序列号均为两个字节。

**4.检查相应的ping回复包。ICMP的类型和代码号是多少？这个ICMP包还有哪些其他字段？校验和、序列号和标识符字段分别是多少字节？**

<img src='.\Figure\ICMP-4.png'>

答：如图，类型号为0，代码号为0；还包括校验和、标识符和序列号三个字段；校验和、标识符和序列号均为两个字节。

## ICMP和Traceroute

<img src='.\Figure\ICMP-5.png'>

**5.你的主机的IP地址是什么？目标主机的IP地址是什么？**

<img src='.\Figure\ICMP-6.png'>

答：如图，源主机IP地址为192.168.31.199，目标主机IP地址为128.93.162.83。

**6.如果ICMP发送的是UDP数据包（如在Unix/Linux中），探测数据包的IP协议号是否仍然为01？如果不是，它会是什么？**

答：不是，它会是17（UDP协议号）。

**7.检查截图中的ICMP回显数据包。它与本实验前半部分的ICMP ping查询数据包不同吗？如果是，如何不同？**

<img src='.\Figure\ICMP-7.png'>

答：不同，如图，图中的数据报没有收到回应，且data字段更长。

**8.检查截图中的ICMP错误数据包。它比ICMP回显数据包包含更多字段。这些字段中包含了什么？**

<img src='.\Figure\ICMP-8.png'>

答：它还包含对应ICMP回显数据包的IP报头和ICMP报头。

**9.检查源主机接收到的最后三个ICMP数据包。这些数据包与ICMP错误数据包有何不同？为什么它们不同？**

<img src='.\Figure\ICMP-9.png'>

答：如图，最后三个ICMP数据包的类型与代码字段与ICMP错误数据包不同。因为这三个ICMP数据包都是对echo request的reply，没有发生TTL超时。

**10.在tracert测量中，是否有一个链路的延迟明显比其他链路长？根据路由器名称，你能猜出该链路两端的路由器的位置吗？**

<img src='.\Figure\ICMP-5.png'>

答：如图，可知在`210.25.187.50`与`orientplus-gw.mx1.lon.uk.geant.net [62.40.125.101]`之间的链路延迟明显比其他链路长；猜测`210.25.187.50`位于中国，`orientplus-gw.mx1.lon.uk.geant.net [62.40.125.101]`位于英国。

