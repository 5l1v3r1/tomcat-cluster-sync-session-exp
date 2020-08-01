

**工具仅用于安全研究以及内部自查，禁止使用工具发起非法攻击，造成的后果使用者负责**

**工具仅用于安全研究以及内部自查，禁止使用工具发起非法攻击，造成的后果使用者负责**

**工具仅用于安全研究以及内部自查，禁止使用工具发起非法攻击，造成的后果使用者负责**

脚本基于<https://github.com/threedr3am/tomcat-cluster-session-sync-exp>，采用多进程调用`tomcat-cluster-session-sync-exp-1.0-SNAPSHOT-jar-with-dependencies.jar`，通过ceye.io来证明漏洞是否真实存在。

**注意：脚本还未经过测试，可能不可用**

1. 资产文件格式说明：`IP<空格>PORT`，可参考ips.txt；
2. 修改脚本中的ceye.io地址为自己账号对应的地址；
3. 多进程数量修改`pool = ProcessPoolExecutor(10)`，默认10个进程数;

