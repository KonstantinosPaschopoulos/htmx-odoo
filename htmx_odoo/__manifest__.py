{
    "name": "HTMX-ODOO",
    "summary": """Testing HTMX inside the Odoo website/frontend.""",
    "version": "16.0.1.0.0",
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "license": "OEEL-1",
    "depends": [
        "website_sale",
    ],
    "data": [
        "views/product_template_views.xml",
        "views/htmx_list.xml",
        "data/website_menus.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "htmx_odoo/static/lib/htmx/htmx.min.js",
        ],
    },
}
