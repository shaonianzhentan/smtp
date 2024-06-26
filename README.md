# smtp
使用QQ邮箱替换掉官方的邮箱通知服务

[![hacs_badge](https://img.shields.io/badge/Home-Assistant-%23049cdb)](https://www.home-assistant.io/)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
![visit](https://visitor-badge.laobi.icu/badge?page_id=shaonianzhentan.smtp&left_text=visit)

## 使用方式

安装完成重启HA，刷新一下页面，在集成里搜索`QQ邮箱`即可

[![Add Integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=smtp)


**通知服务**
```yaml
service: notify.smtp
data:
  title: 标题
  message: 内容
```

**链接跳转**
```yaml
service: notify.smtp
data:
  title: 标题
  message: 内容
  data:
    url: https://github.com/shaonianzhentan/smtp
```

**多邮箱通知**
```yaml
service: notify.smtp
data:
  title: 标题
  message: 内容
  target:
    - xxxxx@qq.com
    - xxxxx@sina.cn
    - xxxxx@163.cn
```

## 如果这个项目对你有帮助，请我喝杯<del style="font-size: 14px;">咖啡</del>奶茶吧😘
|支付宝|微信|
|---|---|
<img src="https://ha.jiluxinqing.com/img/alipay.png" align="left" height="160" width="160" alt="支付宝" title="支付宝">  |  <img src="https://ha.jiluxinqing.com/img/wechat.png" align="left" height="160" width="160" alt="微信支付" title="微信">

#### 关注我的微信订阅号，了解更多HomeAssistant相关知识
<img src="https://ha.jiluxinqing.com/img/wechat-channel.png" height="160" alt="HomeAssistant家庭助理" title="HomeAssistant家庭助理"> 