from odoo import models, fields, api
import requests

class ResPartner(models.Model):
    _inherit = 'res.partner'

    latitude = fields.Float(string="Latitude", digits=(16, 6))
    longitude = fields.Float(string="Longitude", digits=(16, 6))
    map_url = fields.Char(string="Map URL", compute="_compute_map_url")

    @api.depends('street', 'street2', 'zip', 'city', 'country_id')
    def _compute_map_url(self):
        # Lire la config globale : activé/désactivé
        show_map = self.env['ir.config_parameter'].sudo().get_param('address_map.show_map', default='True')
        for record in self:
            if show_map == 'True':
                address = ', '.join(filter(None, [
                    record.street,
                    record.street2,
                    record.zip,
                    record.city,
                    record.country_id and record.country_id.name or ''
                ]))
                lat, lng = None, None
                if address:
                    # Géocode avec OSM/Nominatim
                    response = requests.get(
                        'https://nominatim.openstreetmap.org/search',
                        params={'q': address, 'format': 'json', 'limit': 1},
                        headers={'User-Agent': 'odoo_address_map_example'}
                    )
                    if response.ok:
                        data = response.json()
                        if data:
                            lat = float(data[0]['lat'])
                            lng = float(data[0]['lon'])
                            record.latitude = lat
                            record.longitude = lng

                if lat and lng:
                    url = (
                        f"https://staticmap.openstreetmap.de/staticmap.php?"
                        f"center={lat},{lng}&zoom=15&size=600x300&markers={lat},{lng},red-pushpin"
                    )
                    record.map_url = url
                else:
                    record.map_url = False
            else:
                record.map_url = False
