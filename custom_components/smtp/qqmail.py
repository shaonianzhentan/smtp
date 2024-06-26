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

    # 发送
    def send(self, title, message, tolist=[]):
        try:
            tolist.insert(0, self.from_addr)

            password = self.password
            from_addr = self.from_addr
            smtp_server = 'smtp.qq.com'
            msg = MIMEText(message, 'html', 'utf-8')
            msg['From'] = _format_addr('HomeAssistant <%s>' % from_addr)
            msg['To'] = ','.join(tolist)
            msg['Subject'] = Header(title, 'utf-8').encode()
            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, tolist, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            _LOGGER.error(e)
            return False