# -*- coding: utf-8 -*-
{
    'name': "Custom Templates",

    'summary': """
        A custom module to update legacy pdf reports""",

    'description': """
        This module inherits legacy pdf reports and update them to company's default pdf report
    """,

    'author': "Vaibhavnath Jha",
    'website': "",

    'category': 'Uncategorized',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'views/DeliveryNotesTemplate.xml',
        'views/InvoiceTemplate.xml',
        'views/OrderQuotationTemplate.xml',
        'views/PurchaseOrderTemplate.xml',
        'views/RemittanceTemplate.xml',
        'views/RFQTemplate.xml',
        'views/Commercial_InvoiceTemplate.xml',
        'views/stock_report.xml'
    ],
}
