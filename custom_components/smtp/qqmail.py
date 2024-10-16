import logging

_LOGGER = logging.getLogger(__name__)

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

    # 通知服务
    def notify(self, call):
        data = call.data
        title = str(data.get('title', '消息来自HomeAssistant'))
        message = str(data.get('message', ''))
        email = data.get('email', self.from_addr)
        self.send(title, message, email)

    # 发送
    def send(self, title, message, to_addr):
        try:
            tolist = list(map(lambda x: x.strip(), to_addr.split(',')))
            
            password = self.password
            from_addr = self.from_addr
            smtp_server = 'smtp.qq.com'
            msg = MIMEText(message, 'html', 'utf-8')
            msg['From'] = _format_addr('HomeAssistant <%s>' % from_addr)
            msg['To'] = ','.join(tolist)
            msg['Subject'] = Header(title, 'utf-8').encode()
            server = smtplib.SMTP_SSL(smtp_server, 465)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, tolist, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            _LOGGER.error(e)
            return False