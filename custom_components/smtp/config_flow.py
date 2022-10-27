from __future__ import annotations

from typing import Any
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN
from .qqmail import QQMail

DATA_SCHEMA = vol.Schema({
    vol.Required("qq"): str,
    vol.Required("code"): str
})

class SimpleConfigFlow(ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        errors = {}
        if user_input is not None:
            qq = user_input['qq']
            code = user_input['code']
            # 安装校验
            qm = QQMail(self.hass, qq, code)
            result = qm.send('HomeAssistant插件安装成功', '''
            插件地址：https://github.com/shaonianzhentan/smtp

            关注微信公众号，了解更多HomeAssistant信息
            <br/><img src="https://ha.jiluxinqing.com/img/wechat-channel.png" height="160" alt="HomeAssistant家庭助理" title="HomeAssistant家庭助理">
            ''', qm.from_addr)

            if result == True:
                return self.async_create_entry(title=DOMAIN, data=user_input)
            else:
                errors['base'] = 'failed'
                DATA_SCHEMA = vol.Schema({
                    vol.Required("qq", default=qq): str,
                    vol.Required("code", default=code): str
                })

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)

        
            
        