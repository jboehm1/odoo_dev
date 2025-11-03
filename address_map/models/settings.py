from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_map = fields.Boolean(
        string="Display Map on Partner Form",
        default=True,
        config_parameter="address_map.show_map"
    )
