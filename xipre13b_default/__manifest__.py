{
    'name': 'xipre13b',
    'version': '13.0.0.0',
    'category': 'Tools',
    'summary': "Odoo 13 test",
    'author': 'SDEH',
    'depends': [
        'base',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',
    #'dbfilter': 'odoo13test',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/concagabriel/cl-xipre13b.git',
        'https://github.com/regaby/odoo-custom.git',
        'https://github.com/regaby/sdeh-pos.git',
        'https://github.com/jobiols/odoo-addons.git',
        ## Modulo QR para pos
        'https://github.com/regaby/l10n_ar_fe_qr.git ctmil/l10n_ar_fe_qr',
        ## localización
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/odoo-argentina-ce.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/stock.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/website.git',
        'https://github.com/OCA/account-financial-reporting.git',
        'https://github.com/OCA/reporting-engine.git',
        'https://github.com/OCA/server-ux.git',
        'https://github.com/OCA/mis-builder.git',
        'https://github.com/OCA/sale-workflow.git',
        'https://github.com/OCA/web.git',
        ##
        'https://github.com/OCA/contract.git',
        ##'https://github.com/CybroOdoo/CybroAddons.git',
        'https://github.com/itpp-labs/pos-addons.git',
        'https://github.com/odoomates/odooapps.git',
        ##
       ## 'https://github.com/sistemasdehudson/sdehposaddons.git',
        'https://github.com/OCA/project.git',
        'https://github.com/dhongu/deltatech.git',
        ##
        'https://github.com/OCA/manufacture.git -b 13.0',
        'https://github.com/OCA/manufacture-reporting.git -b 13.0',
        ##
        'https://github.com/OCA/stock-logistics-barcode.git -b 13.0',
        'https://github.com/OCA/stock-logistics-warehouse.git -b 13.0',
        'https://github.com/ingadhoc/purchase -b 13.0',
        'https://github.com/ingadhoc/product -b 13.0',
        'https://github.com/OCA/wms.git -b 13.0',
        'https://github.com/filoquin/odoo_retail -b 13.0',
        'https://github.com/OCA/queue -b 13.0',
        'https://github.com/OCA/currency -b 13.0',
        'https://github.com/OCA/e-commerce -b 13.0',
        ##localizacion espana
        'https://github.com/OCA/l10n-spain.git',
        ##modulos stock para remito
        'https://github.com/OCA/stock-logistics-workflow.git -b 13.0',
        'https://github.com/OCA/project-reporting -b 13.0',
        'https://github.com/OCA/payroll -b 13.0',
        ##ee
        'https://github.com/odoo/enterprise -b 13.0',
        'https://github.com/odoo/odoo -b 13.0',
        'https://github.com/OCA/social -b 13.0',
        'https://github.com/ingadhoc/miscellaneous -b 13.0',
        'https://github.com/OCA/knowledge -b 13.0',
        'https://github.com/ingadhoc/project -b 13.0',
        'https://github.com/OCA/partner-contact -b 13.0',
    ],

    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
