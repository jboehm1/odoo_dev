from odoo import models, fields, api
import requests

class ResPartner(models.Model):
    _inherit = 'res.partner'

    latitude = fields.Float(string="Latitude", digits=(16, 6))
    longitude = fields.Float(string="Longitude", digits=(16, 6))
    map_html = fields.Html(string="Carte OpenStreetMap", compute="_compute_map_html", sanitize=False)

    @api.depends('street', 'street2', 'zip', 'city', 'country_id', 'latitude', 'longitude')
    def _compute_map_html(self):
        for record in self:
            show_map = self.env['ir.config_parameter'].sudo().get_param('address_map.show_map', default='True')
            iframe = False

            lat = record.latitude if record.latitude else None
            lng = record.longitude if record.longitude else None
            
            # Si pas de coordonnées, tente de géocoder
            if show_map == 'True':
                if not (lat and lng) and (record.street or record.city):
                    address = ', '.join(filter(None, [
                        record.street,
                        record.street2,
                        record.zip,
                        record.city,
                        record.country_id and record.country_id.name or ''
                    ]))
                    try:
                        response = requests.get(
                            'https://nominatim.openstreetmap.org/search',
                            params={'q': address, 'format': 'json', 'limit': 1},
                            headers={'User-Agent': 'odoo_address_map_example'}
                        )
                        if response.ok and response.json():
                            lat = float(str(response.json()[0]['lat']).replace(',', '.'))
                            lng = float(str(response.json()[0]['lon']).replace(',', '.'))
                            record.latitude = lat
                            record.longitude = lng
                    except Exception:
                        lat = None
                        lng = None

                # Si on a des coordonnées, formatte toujours en point !
                if lat and lng:
                    lat_str = "{:.6f}".format(float(lat)).replace(",", ".")
                    lng_str = "{:.6f}".format(float(lng)).replace(",", ".")
                    bbox_lng_min = "{:.6f}".format(float(lng) - 0.01).replace(",", ".")
                    bbox_lat_min = "{:.6f}".format(float(lat) - 0.01).replace(",", ".")
                    bbox_lng_max = "{:.6f}".format(float(lng) + 0.01).replace(",", ".")
                    bbox_lat_max = "{:.6f}".format(float(lat) + 0.01).replace(",", ".")
                    
                    iframe = (
                        f'<iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" '
                        f'src="https://www.openstreetmap.org/export/embed.html?bbox={bbox_lng_min},{bbox_lat_min},{bbox_lng_max},{bbox_lat_max}'
                        f'&layer=mapnik&marker={lat_str},{lng_str}"></iframe>'
                    )
            record.map_html = iframe or "<p>Aucune carte disponible</p>"
