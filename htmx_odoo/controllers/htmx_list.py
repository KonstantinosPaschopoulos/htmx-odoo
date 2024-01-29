from odoo import http
from odoo.http import Response, request


class HtmxList(http.Controller):
    @http.route("/htmx_list", type="http", auth="user", website=True)
    def htmx_list(self, **kw):
        products = request.env["product.template"].search([("on_list", "=", True)])
        return request.render("htmx_odoo.htmx_list", {"products": products})

    @http.route("/htmx_list/duplicate/<model('product.template'):product>", type="http", auth="user", website=True)
    def htmx_list_duplicate(self, product, **kw):
        new_product = product.copy()
        new_product.name = f"{product.name} Duplicated from frontend"
        return request.render("htmx_odoo.htmx_list_row", {"product": new_product})

    @http.route("/htmx_list/remove/<model('product.template'):product>", type="http", auth="user", website=True)
    def htmx_list_remove(self, product, **kw):
        product.on_list = False
        return Response(status=200)

    @http.route("/htmx_list/delete/<model('product.template'):product>", type="http", auth="user", website=True)
    def htmx_list_delete(self, product, **kw):
        product.unlink()
        return Response(status=200)

    @http.route("/htmx_list/info/<model('product.template'):product>", type="http", auth="user", website=True)
    def htmx_list_info(self, product, **kw):
        similar_products = request.env["product.template"].sudo().search([("name", "ilike", product.name)])
        return request.render("htmx_odoo.modal_info", {"product": product, "similar_products": similar_products})
