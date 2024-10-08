# Wireshark实验 - TCP

**官方英文文档：[Wireshark_TCP_v8.0.pdf](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_TCP_v8.0.pdf)**

## 1.捕获从本地到远程服务器的批量 TCP 传输

<img src=".\Figure\TCP1.png" />

## 2.查看捕获的trace文件

**1.客户端计算机（源）使用的IP地址和TCP端口号是什么？**

<img src=".\Figure\TCP2.png" />

答：ip地址为10.12.178.169，端口号为56784。

**2.`gaia.cs.umass.edu` 的IP地址是什么？它正在使用哪个端口号来发送和接收此连接的TCP段？**

答：观察上图可知，`gaia.cs.umass.edu`的ip地址为128.119.245.12，所使用端口号为80。

**3.你的客户端计算机（源）使用的IP地址和TCP端口号是什么？**

答：答案同1。

## 3.TCP基础

**4.用于在客户端计算机与 `gaia.cs.umass.edu` 之间启动 TCP 连接的 TCP SYN 段的序列号是什么？该段中标识该段为 SYN 段的内容是什么？**

<img src=".\Figure\TCP3.png" />

答：序号为1237079799，标志位为0x002，其中SYN位置为1，标识出该段为SYN段。有趣的是，客户端计算机还通过本地端口56785与 `gaia.cs.umass.edu` 建立了另一个TCP连接。通过追踪流发现，该连接仅仅完成了3次握手，并未实际传输数据。

**5.`gaia.cs.umass.edu` 发送给客户端计算机的 SYNACK 段的序列号是多少？SYNACK 段中确认字段的值是多少？`gaia.cs.umass.edu` 是如何确定该值的？该段中标识该段为 SYNACK 段的内容是什么？**

<img src=".\Figure\TCP4.png" />

答：序列号为3065315417；确认号为1237079800，这是由客户端发送的SYN段中的序号加1得到的；标志位为0x012，其中SYN位与ACK位置为1，标识出该段为SYNACK段。

**6.包含 HTTP POST 命令的 TCP 段的序列号是多少？**

<img src=".\Figure\TCP5.png" />

答：观察DATA段首部可以看到`POST`命令，序列号为1237079800。

**7.将包含 HTTP POST 的 TCP 段视为 TCP 连接中的第一个段。TCP 连接中前六个段的序列号是什么（包括包含 HTTP POST 的段）？每个段是什么时间发送的？每个段的 ACK 是什么时候收到的？考虑每个 TCP 段发送的时间与收到确认之间的时间差，每个段的 RTT 值是多少？在每个 ACK 收到后，估计的 RTT 值是多少（参见课本第 242 页的 3.5.3 节）？假设估计的 RTT 值等于第一个段的测量 RTT，然后使用第 242 页的估计 RTT 方程计算所有后续段的 RTT 值。**

<img src=".\Figure\TCP6.png" />

答：如上图，可知如下结果。前六个段几乎同时发出，且TCP采用累计确认机制，于22.966838确认了如下数据段，确认号为1237091480。

| 序列号     | 发送时间（秒） | ACK到达时间 | RTT  | 估计RTT |
| ---------- | -------------- | ----------- | ---- | ------- |
| 1237079800 | 22.693747      | 22.966838   |      |         |
| 1237081260 | 22.693747      | 22.966838   |      |         |
| 1237082720 | 22.693747      | 22.966838   |      |         |
| 1237084180 | 22.693747      | 22.966838   |      |         |
| 1237085640 | 22.693747      | 22.966838   |      |         |
| 1237087100 | 22.693747      | 22.966838   |      |         |

**8.前六个 TCP 段的长度是多少？**

答：长度均为1514字节。

**9.在整个跟踪中接收方所宣告的可用缓冲区空间的最小值是多少？接收方缓冲区空间的不足是否曾经限制了发送方？**

<img src=".\Figure\TCP7.png" />

<img src=".\Figure\TCP8.png" />

答：`gaia.cs.umass.edu` 作为接收方宣告的最小窗口为29200，帧序号为48；本地计算机作为接收方宣告的最小窗口为64240，帧序号为46。两者都大于0，并未触发TCP的查询等待机制。

**10.在捕获的trace文件中是否有任何重传的段？你在trace中检查什么来回答这个问题？**

<img src=".\Figure\TCP9.png" />

答：并没有重传的段。观察上图可知序号一直在增大。

**11.接收方通常在一个ACK（确认）中确认多少数据？你能识别出接收方是否在每隔一个接收到的段时发送ACK吗（参见教材第250页的表格3.2）？**

<img src=".\Figure\TCP10.png" />

答：确认数据量一般为MSS（本例中为1460）的整数倍。

**12.这个TCP连接的吞吐量是多少（每单位时间传输的字节数）？请解释你是如何计算这个值的。**

<img src=".\Figure\TCP11.png" />

答：追踪流发现整个会话传输数据量为153KB，会话开始与结束时间分别为23.836140与22.426896，则吞吐量 = 153KB/(23.836140-22.426896)s = 108.57KB/s。

## 4.TCP拥塞控制的实际应用

<img src=".\Figure\TCP12.png" />

**13.使用 Time-Sequence-Graph(Stevens) 绘图工具查看从客户端发送到 gaia.cs.umass.edu 服务器的数据包段的序列号与时间的关系图。你能识别出 TCP 的慢启动（slowstart）阶段的开始和结束以及拥塞避免（congestion avoidance）何时接管吗？请评论测量数据与我们在课本中学习的 TCP 理想行为的差异。**

答：本例中报文段长度均为1460字节，由上图可知，各个时间点发送报文段数量如下：

| 时间  | 报文段数目 |
| ----- | ---------- |
| 22.69 | 10         |
| 22.97 | 20         |
| 23.24 | 40         |
| 23.52 | 35         |

根据以上结果，推测慢启动从22.69开始，于23.24结束，拥塞避免从23.24开始。与课本中的

不同在于，拥塞避免开始后，窗口大小发生了减小（23.52降为35）。

