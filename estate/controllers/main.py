from odoo import http
from odoo.http import request


class Estate(http.Controller):
    @http.route('/',website=True,auth='public')
    def estate_porperty_show(self,**kw):
        # return "Hello This is property page"

        properties = request.env['estate.property'].sudo().search([])
        return request.render("estate.property",{

                'properties':properties,
               


        })