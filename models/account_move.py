from odoo import fields,models,api
import convert_numbers
# from deep_translator import GoogleTranslator
from uuid import uuid4
import qrcode
from odoo.exceptions import UserError

import base64
import logging

from lxml import etree

logger = logging.getLogger(__name__)




class AccountMove(models.Model):
    _inherit = 'account.move'

    so_number = fields.Char(string='SO Number')
    customer_po = fields.Char(string='Customer PO Number')
    contact = fields.Char(string='Contact Eng')
    contact_address = fields.Char(string='Contact Address')
    datetime_field = fields.Datetime(string="Create Date", default=lambda self: fields.Datetime.now())
    decoded_data = fields.Char('Decoded Data')
    ubl_preview = fields.Integer(string="Test")
    debit_note = fields.Boolean(default=False)
    credit_note = fields.Boolean(default=False)
    qr_image = fields.Binary(string="QR Image")
    uuid = fields.Char('UUID', size=50, index=True, default=lambda self: str(uuid4()), copy=False)
    a_total_amount = fields.Char(string="A Total Value")
    a_net_amount = fields.Char(string="A Net Value")
    a_vat_value = fields.Char(string="A VAT Value")
    a_net_with_value = fields.Char(string="A NET WITH Value")