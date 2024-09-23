# Wireshark实验 - DNS

**官方英文文档：[Wireshark_DHCP_v8.1.doc](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_DHCP_v8.1.doc)**

**trace文件：[Captured on my laptop](.\dhcp-trace1.pcapng)**

## DHCP问题

**让我们首先来看 DHCP Discover 消息。在你的跟踪文件中找到包含第一个 Discover 消息的 IP 数据报。**



**1.这个 DHCP Discover 消息是使用 UDP 还是 TCP 作为底层传输协议发送的？**

<img src='.\Figure\dhcp-1.png'>

答：如图，DHCP DIscover消息使用UDP传输。

**2.在包含 Discover 消息的 IP 数据报中使用的源 IP 地址是什么？这个地址有什么特别之处吗？请解释。**

答：如上图，源IP地址为`0.0.0.0`，该地址仅仅表示本机，并不是具体的IP地址。

**3.在包含 Discover 消息的数据报中使用的目标 IP 地址是什么？这个地址有什么特别之处吗？请解释。**

答：如上图，目的IP地址为`255.255.255.255`，该地址表示本网段内的所有设备。

**4.这个 DHCP Discover 消息的事务 ID 字段中的值是什么？**

<img src='.\Figure\dhcp-2.png'>

答：如图，事务ID值为`0x0fc07446`。

**5.现在检查 DHCP Discover 消息中的选项字段。除了 IP 地址之外，客户端在此 DHCP 交易中建议或请求从 DHCP 服务器接收的五条信息是什么？**

<img src='.\Figure\dhcp-3.png'>

答：如图，还包括子网掩码、广播地址、时间差、路由器、域名等信息。



**现在让我们看看 DHCP Offer 消息。在你的跟踪文件中找到 DHCP 服务器发送的 DHCP Offer 消息的数据报，该消息是对你在问题 1-5 中研究的 DHCP Discover 消息的响应。**



**6.你怎么知道此 Offer 消息是对你在问题 1-5 中研究的 DHCP Discover 消息的响应？**

<img src='.\Figure\dhcp-4.png'>

答：如图，Offer消息中的事务ID与Discover消息中的事务ID相同，故确定为对该消息的响应。

**7.在包含 Offer 消息的 IP 数据报中使用的源 IP 地址是什么？这个地址有什么特别之处吗？请解释。**

答：如上图，源IP地址为`192.168.31.1`，该地址为路由器地址。

**8.在包含 Offer 消息的数据报中使用的目标 IP 地址是什么？这个地址有什么特别之处吗？请解释。[提示：仔细查看你的跟踪文件。此问题的答案可能与教材中的图 4.24 所显示的不同。如果你真的想深入研究，请查阅 DHCP RFC，第 24 页。]**

答：如上图，目的IP地址为`192.168.31.167`，该地址为主机即将被分配的地址。原因在于DHCP Discover消息中将Broadcast标志位置为0，如图。

<img src='.\Figure\dhcp-5.png'>

RFC 2131关于这部分具体解释如下：

通常情况下，DHCP 服务器和 BOOTP 中继代理会尝试使用单播传输将 DHCPOFFER、DHCPACK 和 DHCPNAK 消息直接传递给客户端。在 IP 头中，IP 目标地址被设置为 DHCP 的 `yiaddr` 地址，而链路层目标地址被设置为 DHCP 的 `chaddr` 地址。不幸的是，一些客户端实现无法接收这样的单播 IP 数据报，直到其实现已经被配置了有效的 IP 地址（这可能导致死锁，因为在客户端被配置了 IP 地址之前，无法将 IP 地址传递给客户端）。

一个无法在其协议软件被配置 IP 地址之前接收单播 IP 数据报的客户端**应该**在其发送的任何 DHCPDISCOVER 或 DHCPREQUEST 消息中，将 `flags` 字段中的 BROADCAST 位设置为 1。BROCAST 位将向 DHCP 服务器和 BOOTP 中继代理提示，将任何消息广播给客户端所在的子网。一个能够在其协议软件被配置 IP 地址之前接收单播 IP 数据报的客户端**应该**将 BROADCAST 位清为 0。BOOTP 解释文档讨论了使用 BROADCAST 位的影响【21】。

当服务器或中继代理直接向 DHCP 客户端（即，不是向 `giaddr` 字段中指定的中继代理）发送或中继 DHCP 消息时，**应该**检查 `flags` 字段中的 BROADCAST 位。如果该位被设置为 1，DHCP 消息**应该**以 IP 广播的方式发送，使用 IP 广播地址（最好是 0xffffffff）作为 IP 目标地址，并使用链路层广播地址作为链路层目标地址。如果 BROADCAST 位被清为 0，则该消息**应该**以单播 IP 方式发送到 `yiaddr` 字段中指定的 IP 地址，并将链路层地址设置为 `chaddr` 字段中指定的地址。如果单播传输不可行，该消息**可以**使用 IP 广播地址（最好是 0xffffffff）作为 IP 目标地址，并使用链路层广播地址作为链路层目标地址进行广播。

**9.现在检查 DHCP Offer 消息中的选项字段。DHCP 服务器在 DHCP Offer 消息中向 DHCP 客户端提供了哪些五条信息？**

<img src='.\Figure\dhcp-6.png'>

答：如图，提供信息包括DHCP服务器标识符、IP地址租用期、恢复时间值、重新绑定时间值、子网掩码、广播地址、路由器IP、域名服务器、主机名等信息。



**在你的跟踪文件中找到包含第一个 DHCP Request 消息的 IP 数据报，并回答以下问题。**



**10.在你的跟踪文件中，包含第一个 DHCP Request 消息的 IP 数据报的 UDP 源端口号是多少？使用的 UDP 目标端口号是多少？**

<img src='.\Figure\dhcp-7.png'>

答：如图，源端口号为68，目的端口号为67。

**11.在包含此 Request 消息的 IP 数据报中的源 IP 地址是什么？这个地址有什么特别之处吗？请解释。**

答：如上图，源IP地址为`0.0.0.0`，该地址仅仅表示本机，并不是具体的IP地址。

**12.在包含此 Request 消息的数据报中使用的目标 IP 地址是什么？这个地址有什么特别之处吗？请解释。**

答：如上图，目的IP地址为`255.255.255.255`，该地址表示本网段内的所有设备。

**13.此 DHCP Request 消息的事务 ID 字段中的值是多少？它是否与之前的 Discover 和 Offer 消息的事务 ID 相匹配？**

<img src='.\Figure\dhcp-8.png'>

答：如图，事务ID值为`0x0fc07446`，与之前消息相匹配。

**14.现在检查 DHCP Discover 消息中的选项字段，并仔细查看“参数请求列表”。DHCP RFC 说明： “客户端可以通过包含‘参数请求列表’选项通知服务器客户端感兴趣的配置参数。此选项的数据部分明确列出了按标签编号请求的选项。” 你在此 Request 消息中的“参数请求列表”选项与之前的 Discover 消息中的相同列表选项之间看到了哪些差异？**

<img src='.\Figure\dhcp-9.png'>

答：如图，两者完全相同。



**在你的跟踪文件中找到包含第一个 DHCP ACK 消息的 IP 数据报，并回答以下问题。**



**15.在包含此 ACK 消息的 IP 数据报中的源 IP 地址是什么？这个地址有什么特别之处吗？请解释。**

<img src='.\Figure\dhcp-10.png'>

答：如图，源IP地址是`192.168.31.1`，为DHCP服务器也即路由器地址。

**16.在包含此 ACK 消息的数据报中使用的目标 IP 地址是什么？这个地址有什么特别之处吗？请解释。**

答：目的IP地址为`192.168.31.167`，是即将分配给主机的IP地址。

**17.DHCP ACK 消息中包含分配给客户端 IP 地址的字段名称是什么（在 Wireshark 窗口中显示）？**

<img src='.\Figure\dhcp-11.png'>

答：如图，字段名称为`dhcp.ip.your`。

**18.DHCP 服务器将此 IP 地址分配给客户端的时间（即所谓的“租赁时间”）是多长？**

<img src='.\Figure\dhcp-12.png'>

答：如图，IP地址租用期为12小时。

**19.DHCP ACK 消息中，DHCP 服务器返回给 DHCP 客户端的默认路径上第一跳路由器的 IP 地址是什么（即客户端通向互联网其他部分的第一跳路由器）？**

<img src='.\Figure\dhcp-13.png'>

答：如图，第一跳路由器IP地址为`192.168.31.1`。