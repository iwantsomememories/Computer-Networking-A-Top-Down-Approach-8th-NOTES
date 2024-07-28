# Wireshark实验 - HTTP

**官方英文文档：[Wireshark_HTTP_v8.0.pdf](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_HTTP_v8.0.pdf)**

## 1.基本HTTP GET/response交互

<img src=".\Figure\HTTP-1.png" />

<img src=".\Figure\HTTP-1-1.png" />



<img src=".\Figure\HTTP-1-2.png" />

**1.您的浏览器是否运行HTTP版本1.0或1.1？服务器运行什么版本的HTTP？**

答：我的浏览器运行HTTP1.1，服务器运行HTTP1.1。

**2.您的浏览器会从接服务器接受哪种语言（如果有的话）？**

答：简体/繁体中文，美式/英式英语。

**3.您的计算机的IP地址是什么？ gaia.cs.umass.edu服务器地址呢？**

答：192.168.31.199，128.119.245.12。

**4.服务器返回到浏览器的状态代码是什么?**

答：200 OK。

**5.服务器上HTML文件的最近一次修改是什么时候？**

答：Fri, 26 Jul 2024 05:59:02 GMT。

**6.服务器返回多少字节的内容到您的浏览器?**

答：128字节。

**7.通过检查数据包内容窗口中的原始数据，你是否看到有协议头在数据包列表窗口中未显示？ 如果是，请举一个例子。**

答：有，浏览器还请求了一个名为favicon.icon的文件（手动忽略掉了）。

## 2.HTTP条件Get/response交互

<img src=".\Figure\HTTP-2.png" />

**8.检查第一个从您浏览器到服务器的HTTP GET请求的内容。您在HTTP GET中看到了“IF-MODIFIED-SINCE”行吗？**

<img src=".\Figure\HTTP-2-1.png" />

答：没有。

**9.检查服务器响应的内容。服务器是否显式返回文件的内容？ 你是怎么知道的？**

<img src=".\Figure\HTTP-2-2.png" />

答：如图所示，显式返回了html文件内容。

**10.现在，检查第二个HTTP GET请求的内容。 您在HTTP GET中看到了“IF-MODIFIED-SINCE:”行吗？ 如果是，“IF-MODIFIED-SINCE:”头后面包含哪些信息？**

<img src=".\Figure\HTTP-2-3.png" />

答：是，包含信息: Fri, 26 Jul 2024 05:59:02 GMT。

**11.针对第二个HTTP GET，从服务器响应的HTTP状态码和短语是什么？服务器是否明确地返回文件的内容？请解释。**

<img src=".\Figure\HTTP-2-4.png" />

答：304 Not Modified；没有明确返回文件内容，因为文件并未修改，直接调用本地缓存即可。

##3.HTTP条件Get/response交互

<img src=".\Figure\HTTP-3.png" />

**12.您的浏览器发送多少HTTP GET请求消息？哪个数据包包含了请求美国权利法案的消息？**

<img src=".\Figure\HTTP-3-1.png" />

答：发送了1个GET请求消息，96号数据包包含该消息。

**13.哪个数据包包含响应HTTP GET请求的状态码和短语?**

答：103号数据包。

**14.响应中的状态码和短语是什么？**

答：200 OK。

**15.需要多少包含数据的TCP段来执行单个HTTP响应和权利法案文本？**

<img src=".\Figure\HTTP-3-2.png" />

答：需要4个TCP协议段。

## 4.具有嵌入对象的HTML文档

<img src=".\Figure\HTTP-4.png" />

**16.您的浏览器发送了几个HTTP GET请求消息？ 这些GET请求发送到哪个IP地址？**

<img src=".\Figure\HTTP-4-1.png" />

答：共发送3个GET请求消息，目的IP地址分别为128.119.245.12，128.119.245.12以及178.79.137.164。

**17.浏览器从两个网站串行还是并行下载了两张图片？请说明。**

答：对第二个图片的请求在收到对第一个图片请求的回复后才发出，判断为串行下载。

## 5.HTTP认证

<img src=".\Figure\HTTP-5.png" />

**18.对于您的浏览器的初始HTTP GET消息，服务器响应（状态码和短语）是什么响应？**

<img src=".\Figure\HTTP-5-1.png" />

答：401 Unauthorized。

**19.当您的浏览器第二次发送HTTP GET消息时，HTTP GET消息中包含哪些新字段？**

<img src=".\Figure\HTTP-5-2.png" />

答：增加了Authorization字段，该字段的值为用户名和密码。