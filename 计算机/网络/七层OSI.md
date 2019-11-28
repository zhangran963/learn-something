<style>img {max-width: 400px} .w4{max-width: 400px}.w5{max-width: 500px}</style>



## OSI七层模型

### OSI中的层 功能 TCP/IP协议族

* 应用层 文件传输，电子邮件，文件服务，虚拟终端 TFTP，HTTP，SNMP，FTP，SMTP，DNS，Telnet
* 表示层 数据格式化，代码转换，数据加密 没有协议
* 会话层 解除或建立与别的接点的联系 没有协议
* 传输层 提供端对端的接口 TCP，UDP
* 网络层 为数据包选择路由 IP，ICMP，RIP，OSPF，BGP，IGMP
* 数据链路层 传输有地址的帧以及错误检测功能 SLIP，CSLIP，PPP，ARP，RARP，MTU
* 物理层 以二进制数据形式在物理媒体上传输数据 ISO2110，IEEE802，IEEE802.2

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g9dg27xd0zj30fy0bzq41.jpg)




### TCP/IP五层模型的协议

应用层
传输层
网络层
数据链路层
物理层

* 物理层：中继器、集线器、还有我们通常说的双绞线也工作在物理层
* 数据链路层：网桥（现已很少使用）、以太网交换机（二层交换机）、网卡（其实网卡是一半工作在物理层、一半工作在数据链路层）
* 网络层：路由器、三层交换机
* 传输层：四层交换机、也有工作在四层的路由器

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g9dgrz8nvhj30fw09hdgc.jpg)