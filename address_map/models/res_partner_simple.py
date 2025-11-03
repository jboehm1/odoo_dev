from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    latitude = fields.Float(string="Latitude", digits=(16, 6))
    longitude = fields.Float(string="Longitude", digits=(16, 6))
    # Champ HTML pour afficher la carte OSM
    map_html = fields.Html(string="Carte OpenStreetMap", compute="_compute_map_html", sanitize=False)

    @api.depends('latitude', 'longitude')
    def _compute_map_html(self):
        for record in self:
            # Test hardcodé pour démo (à remplacer par les valeurs DB)
            lat =  48.8566     # Paris
            lng =  2.3522

            # Génération du code HTML avec l'iframe OSM
            record.map_html = (
                f'<iframe width="600" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" '
                f'src="https://www.openstreetmap.org/export/embed.html?bbox={lng-0.01},{lat-0.01},{lng+0.01},{lat+0.01}'
                f'&layer=mapnik&marker={lat},{lng}"></iframe>'
            )
