from homeassistant.helpers import template
import logging

_LOGGER = logging.getLogger(__name__)
from .const import DOMAIN

# ----------邮件相关---------- #
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# ----------邮件相关---------- #

class QQMail:

    # 初始化
    def __init__(self, hass, from_addr, password):
        self.hass = hass
        self.from_addr = f'{from_addr}@qq.com'
        self.password = password
        # 设置QQ邮箱通知服务
        if hass.services.has_service(DOMAIN, 'notify') == False:
            hass.services.async_register(DOMAIN, 'notify', self.notify)

    # 发送邮件
    def sendMail(self, to_addr, title, message):
        try:
            from_addr = self.from_addr
            smtp_server = 'smtp.qq.com'
            msg = MIMEText(message, 'html', 'utf-8')
            msg['From'] = _format_addr('HomeAssistant <%s>' % from_addr)
            #msg['To'] = _format_addr('智能家居 <%s>' % to_addr)
            msg['To'] = ','.join(to_addr)
            msg['Subject'] = Header(title, 'utf-8').encode()
            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, self.password)
            server.sendmail(from_addr, to_addr, msg.as_string())
            server.quit()
        except Exception as e:
            _LOGGER.error(e)

    # 通知服务
    def notify(self, call):
        data = call.data
        # 读取收件人
        email = data.get('email', self.from_addr)
        if not isinstance(email, list):
            email = [ email ]
        title = data.get('title', '消息来自HomeAssistant')
        message = self.template(data.get('message', ''))
        self.sendMail(email, title, message)

    # 模板解析
    def template(self, _message):
        tpl = template.Template(_message, self.hass)
        _message = tpl.async_render(None)
        return _message
