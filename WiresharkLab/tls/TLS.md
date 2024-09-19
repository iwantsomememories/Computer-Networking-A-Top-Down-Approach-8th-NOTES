# WiresharkLab - TLS

**官方英文文档：[Wireshark_TLS_v8.1.doc](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_TLS_v8.1.doc)**

**trace文件：[tls-wireshark-trace1](http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces-8.1.zip)**

## 查看trace

**1.在你的抓包记录中，包含初始 TCP SYN 消息的包号是什么？（“包号”是指 Wireshark 显示左侧 "No." 列中的数字，而不是 TCP 段中的序列号）。**

<img src='.\Figure\tls-1.png'>

答：如图，包号为17。

**2.TCP 连接是在客户端发送给服务器的第一个 TLS 消息之前还是之后建立的？**

答：如上图，在发送第一个TLS消息之前就完成了TCP三次握手，因此TCP 连接是在客户端发送给服务器的第一个 TLS 消息之前建立的。

## TLS握手：客户端Hello消息

**3.在你的抓包记录中，包含 TLS 客户端 Hello 消息的包号是什么？**

答：如上图，包号为28。

**4.在客户端 Hello 消息中声明的，你的客户端运行的 TLS 版本是什么？**

<img src='.\Figure\tls-2.png'>

答：如图，版本为1.0。

**5.在客户端 Hello 消息中声明的，你的客户端支持多少个加密套件？加密套件是一组相关的加密算法，它决定了会话密钥如何生成，以及如何通过 HMAC 算法对数据进行加密和数字签名。**

<img src='.\Figure\tls-3.png'>

答：如图，共支持17个加密套件。

**6.在客户端 Hello 消息中，你的客户端生成并发送了一串“随机字节”给服务器。客户端 Hello 消息的随机字节字段中的前两个十六进制数字是什么？输入两个十六进制数字（不带空格、无前导 '0x'，并在需要时使用小写字母）。提示：仔细深入查看随机字段以找到随机字节子字段（不要考虑随机字段中的 GMT UNIX 时间子字段）。**

<img src='.\Figure\tls-4.png'>

答：如图，前两个十六机制数字为4b。

**7.客户端 Hello 消息中的“随机字节”字段的作用是什么？提示：你需要做一些搜索和阅读才能找到此问题的答案；请参阅第 8.6 节以及 RFC 5246（特别是 RFC 5246 的第 8.1 节）。**

答：用于计算主密钥（MS）。

## TLS 握手：服务器 Hello 消息

**8.在你的抓包记录中，包含 TLS 服务器 Hello 消息的包号是什么？**

<img src='.\Figure\tls-5.png'>

答：如图，包号为32。

**9.服务器从早期客户端 Hello 消息中提供的加密套件中选择了哪个加密套件？**

<img src='.\Figure\tls-6.png'>

答：如图，选择的加密套件为TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)。

**10.服务器 Hello 消息是否包含随机字节，类似于客户端 Hello 消息中的随机字节？如果是，它们的作用是什么？**

答：如上图，包含随机字节，它们均用于计算主密钥。

**11.在你的抓包记录中，包含 [www.cics.umass.edu](http://www.cics.umass.edu) 服务器（实际上是 [www.cs.umass.edu](http://www.cs.umass.edu) 服务器）公钥证书的 TLS 消息部分的包号是什么？**

<img src='.\Figure\tls-7.png'>

答：如图，包号为37。

**12.服务器可能会返回多个证书。如果返回了多个证书，它们是否都属于 www.cs.umass.edu？如果不是，它们属于谁？你可以通过检查返回证书中的 id-at-commonName 字段确定证书的所属。**

<img src='.\Figure\tls-8.png'>

答：如图，共有三个证书，第一个属于www.cs.umass.edu，第二个属于InCommon RSA Server CA，第三个属于USERTrust RSA Certification Authority。

**13.为 id-at-commonName=[www.cs.umass.edu](http://www.cs.umass.edu) 颁发证书的认证机构名称是什么？**

<img src='.\Figure\tls-9.png'>

答：如图，认证机构为InCommon RSA Server CA。

**14.CA 用于签署此证书的数字签名算法是什么？提示：此信息可以在 [www.cs.umass.edu](http://www.cs.umass.edu) 证书的 SignedCertificate 字段的 signature 子字段中找到。**

<img src='.\Figure\tls-10.png'>

答：如图，算法Id为1.2.840.113549.1.1.11 (sha256WithRSAEncryption)。

**15.让我们看看真实的公钥是什么样子的！[www.cics.umass.edu](http://www.cics.umass.edu) 使用的公钥模数的前四个十六进制数字是什么？请输入四个十六进制数字（不带空格、无前导 '0x'，并在需要时使用小写字母，包括 '0x' 之后的任何前导 0）。提示：此信息可以在 [www.cs.umass.edu](http://www.cs.umass.edu) 证书的 SignedCertificate 字段的 subjectPublicKeyInfo 子字段中找到。**

<img src='.\Figure\tls-11.png'>

答：如图，前四个十六进制数为00b3。

**16.查看你的抓包记录，查找客户端与 CA 之间的消息，以获取 CA 的公钥信息，以便客户端验证服务器发送的由 CA 签署的证书确实有效，并且没有被伪造或篡改。你在抓包记录中是否看到了这样的消息？如果有，抓包记录中客户端发送给 CA 的第一个包的包号是什么？如果没有，请解释为什么客户端没有联系 CA。**

答：没有看到这样的消息，因为客户端可以依赖本地存储的受信任 CA 列表来验证服务器证书的真实性。这种本地存储的 CA 列表已经包含了各大 CA 的公钥，因此，客户端可以使用这些公钥验证服务器证书的签名。

**17.在你的抓包记录中，包含 Server Hello Done TLS 记录的 TLS 消息部分的包号是什么？**

<img src='.\Figure\tls-12.png'>

答：如图，包号为37。

## TLS 握手：总结握手过程

**18.你的抓包中，客户端发送包含公钥信息、`Change Cipher Spec` 和加密握手消息的 TLS 消息的包号是多少？**

<img src='.\Figure\tls-13.png'>

答：如图，包号为39。

**19.客户端是否向服务器提供了由 CA 签署的公钥证书？如果是，包含客户端证书的抓包中的包号是多少？**

答：并未向服务器提供公钥证书。

## 应用数据

**20.客户端和服务器用来加密应用数据（此处为 HTTP 消息）的对称密钥加密算法是什么？**

答：对称密钥加密算法是AES_128_GCM。

**21.该对称密钥加密算法最终在哪条 TLS 消息中被决定并声明？**

答：在包号为32的“Server Hello”消息中被决定并声明。

**22.你的抓包中，携带从客户端到服务器的第一个加密应用数据的包号是多少？**

<img src='.\Figure\tls-14.png'>

答：如图，包号为41。

**23.考虑到此抓包是通过访问 [www.cics.umass.edu](http://www.cics.umass.edu) 的主页生成的，你认为这个加密的应用数据内容是什么？**

答：内容是客户端发往服务器的“HTTP GET”消息。

## 关闭TLS连接

**24.包含从客户端到服务器的关闭 TLS 连接消息的包号是多少？由于在 Wireshark 抓包中 TLS 消息是加密的，我们无法直接查看 TLS 消息的内容，因此需要做出合理的猜测。**

<img src='.\Figure\tls-15.png'>

答：如图，最后一个目的IP为`128.119.240.84`且TCP标志位FIN为1的消息包号为503，故可知503号包包含关闭TLS连接消息。