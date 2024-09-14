# WireShark实验 - WIFI

**官方英文文档：[Wireshark_802.11_v8.1.doc](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_802.11_v8.1.doc)**

**trace文件：[Wireshark_801_11](http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces-8.1.zip)**

## 信标帧

**1.两个发出大多数信标帧的接入点（AP）的SSID是什么？[提示：查看 Info 字段。要仅显示信标帧，在Wireshark显示过滤器中输入 `wlan.fc.type_subtype == 8`。]**

<img src='.\Figure\wifi-1.png'>

答：如图，分别为"30 Munroe St"和"linksys12"。

**2.这两个接入点使用的802.11信道是什么？[提示：你需要查看802.11信标帧中的无线电信息。]**

<img src='.\Figure\wifi-2.png'>

<img src='.\Figure\wifi-3.png'>

答：如图，两个接入点使用的802.11信道号均为6。

**现在我们来看看在 t=0.085474 时发送的信标帧。**

**3.该接入点（AP）发送信标帧的时间间隔是多少？[提示：该时间间隔包含在信标帧的某个字段中。]**

<img src='.\Figure\wifi-4.png'>

答：如图，时间间隔为0.1024秒。

**4.该接入点信标帧的源MAC地址（十六进制表示）是什么？回忆一下，802.11帧使用了三个地址：源、目的地和BSS。有关802.11帧结构的详细讨论，请参见IEEE 802.11标准文档第9.2.3-9.2.4.1节。**

<img src='.\Figure\wifi-5.png'>

答：如图，源MAC地址为`00:16:b6:f7:1d:51`。

**5.30 Munroe St信标帧的目的MAC地址（十六进制表示）是什么？**

答：如上图，目的MAC地址为`ff:ff:ff:ff:ff:ff`。

**6.30 Munroe St信标帧的MAC BSS ID（十六进制表示）是什么？**

答：如上图，BSS ID为`00:16:b6:f7:1d:51`。

**7.30 Munroe St接入点的信标帧中广播显示该接入点支持四个数据速率和八个额外的“扩展支持速率”，这些速率是多少？[注意：这些跟踪是在一个较旧的AP上捕获的。]**

<img src='.\Figure\wifi-6.png'>

答：支持的四个数据速率分别为1Mb/s，2Mb/s，5.5Mb/s，11Mb/s，八个额外的扩展速率分别为6Mb/s，9Mb/s，12Mb/s，18Mb/s，24Mb/s，36Mb/s，48Mb/s，54Mb/s。

## 数据传输

**8.查找在 t=24.8110 时发出第一个TCP会话（即下载alice.txt）的 SYN TCP 段的802.11帧。这三个MAC地址字段是什么？哪个MAC地址对应无线主机？（给出该主机的MAC地址的十六进制表示）哪个MAC地址对应接入点？哪个MAC地址对应第一跳路由器？发送此TCP段的无线主机的IP地址是什么？该TCP SYN段的目标IP地址是什么？**

<img src='.\Figure\wifi-7.png'>

答：如图，1）三个MAC地址分别为`00:16:b6:f4:eb:a8`，`00:13:02:d1:b6:4f`，`00:16:b6:f7:1d:51`；2）源MAC地址`00:13:02:d1:b6:4f`对应无线主机；3）目的MAC地址`00:16:b6:f4:eb:a8`对应接入点；4）BSS Id `00:16:b6:f7:1d:51`对应第一跳路由器；5）无线主机IP地址为`192.168.1.109`；6）目的IP地址为`128.119.245.12`。

**9.该TCP SYN的目标IP地址对应主机、接入点、第一跳路由器还是目标Web服务器？**

答：对应于目标Web服务器。

**10.查找在 t=24.8277 时收到的此TCP会话的 SYNACK 段的802.11帧。这三个MAC地址字段是什么？哪个MAC地址对应主机？哪个MAC地址对应接入点？哪个MAC地址对应第一跳路由器？该帧中的发送者MAC地址是否与发送封装在该数据报中的TCP段的设备的IP地址对应？（提示：如果不确定如何回答这个问题，可以回顾教材中的图6.19，或上一问题中的相关部分。理解这一点非常重要。）**

<img src='.\Figure\wifi-8.png'>

答：如图，1）三个MAC地址分别为`91:2a:b0:49:b6:4f`，`00:16:b6:f4:eb:a8`，`00:16:b6:f7:1d:51`；2）目的MAC地址`91:2a:b0:49:b6:4f`对应无线主机；3）源MAC地址`00:16:b6:f4:eb:a8`对应接入点；4）BSS Id `00:16:b6:f7:1d:51`对应第一跳路由器；5）不对应。

## 解除关联/认证/关联

**11.在 t=49 后，主机为结束与最初关联的30 Munroe St AP的关联发送了哪两个动作（即帧）？（提示：其中一个是IP层动作，另一个是802.11层动作）**

<img src='.\Figure\wifi-9.png'>

<img src='.\Figure\wifi-10.png'>

答：如图，主机在约0.02s后发送了一个802.11 Deauthentication帧，然后过了约0.58s又发送了一个DHCP Release帧。

**12.让我们首先看看认证（AUTHENTICATION）帧。在 t = 63.1680 时，主机尝试与 30 Munroe St AP 进行关联。使用 Wireshark 显示过滤器 `wlan.fc.subtype == 11` 来显示主机与 AP 之间发送的认证帧。主机请求的是哪种形式的认证？**

<img src='.\Figure\wifi-11.png'>

答：如图，请求的是开放系统认证。

**13.该主机向 AP 发送的认证帧的**认证序列号（Authentication SEQ）**是多少？**

答：如上图，Authentication SEQ为1。

**14.AP 在 t = 63.1690 时对认证请求作出了响应。AP 是否接受了主机请求的认证形式？**

<img src='.\Figure\wifi-12.png'>

答：如图，Status code为0，表示AP接受了主机请求的认证。

**15.AP 向主机发送的认证帧的认证序列号（Authentication SEQ）是多少？**

答：如上图，认证序列号为2。



**现在让我们来看看在 t = 63.1699 发送的关联请求（ASSOCIATION REQUEST）和在 t = 66.1921 收到的关联响应（ASSOCIATION RESPONSE）。注意，您可以使用过滤表达式 `wlan.fc.subtype < 2 and wlan.fc.type == 0` 来显示关联请求和响应帧。**



**16.该帧中指示的支持速率（SUPPORTED RATES）是什么？在您的回答中不要包括任何标记为扩展支持速率（EXTENDED SUPPORTED RATES）的速率。**

<img src='.\Figure\wifi-13.png'>

答：如图，支持速率为1Mb/s，2Mb/s，5.5Mb/s，11Mb/s，6Mb/s，9Mb/s，12Mb/s，18Mb/s。

**17.关联响应（ASSOCIATION RESPONSE）是否表明关联成功或失败？**

<img src='.\Figure\wifi-14.png'>

答：如图，Status code为0，表明关联成功。

**18.主机提供的最快的（最大）扩展支持速率（Extended Supported Rate）是否与 AP 能提供的最快的（最大）扩展支持速率相匹配？**

<img src='.\Figure\wifi-15.png'>

<img src='.\Figure\wifi-16.png'>

答：关联请求与关联响应帧中最大扩展支持速率均为54Mb/s，因此可以匹配。