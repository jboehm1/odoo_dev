from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_map = fields.Boolean(
        string="Afficher la carte sur le formulaire Contact",
        default=True,
        config_parameter="address_map.show_map"
    )
