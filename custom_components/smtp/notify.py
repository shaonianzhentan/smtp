"""Notify.Events platform for notify component."""
from __future__ import annotations

import logging

from homeassistant.components.notify import (
    ATTR_DATA,
    ATTR_TITLE,
    BaseNotificationService,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import DOMAIN
from .qqmail import QQMail

_LOGGER = logging.getLogger(__name__)


def get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> SmtpNotificationService:
    return SmtpNotificationService(hass, discovery_info)


class SmtpNotificationService(BaseNotificationService):

    def __init__(self, hass, config):
        self.hass = hass
        self.qm = QQMail(hass, config['qq'], config['code'])
        # 设置QQ邮箱通知服务
        if hass.services.has_service(DOMAIN, 'notify') == False:
            hass.services.async_register(DOMAIN, 'notify', self.qm.notify)

    def send_message(self, message, **kwargs):
        """Send a message."""
        data = kwargs.get(ATTR_DATA) or {}
        title = kwargs.get(ATTR_TITLE, message)
        url = data.get('url')
        if url is not None:
            message = f'<a href="{url}">{message}</a>'

        self.qm.send(title, message, self.qm.from_addr)