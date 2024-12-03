# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api
from odoo.models import AbstractModel
from odoo.tools import cloc

from ast import literal_eval

class PublisherWarrantyContract(AbstractModel):
    _inherit = "publisher_warranty.contract"

    @api.model
    def _get_message(self):
        return {}
    
    @api.model
    def _get_sys_logs(self):
        """
        Utility method to send a publisher warranty get logs messages.
        """
        msg = self._get_message()
        arguments = {'arg0': ustr(msg), "action": "update"}

        #url = config.get("publisher_warranty_url")

        #r = requests.post(url, data=arguments, timeout=30)
        #r.raise_for_status()
        return literal_eval('')
    
    def update_notification(self, cron_mode=True):
        return True