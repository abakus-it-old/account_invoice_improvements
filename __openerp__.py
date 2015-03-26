{
    'name': "AbAKUS invoice improvements",
    'version': '1.0',
    'depends': ['account'],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Accounting',
    'description': """This modules adds some functionalities to the invoicing process for AbAKUS. 
- it adds a field in the invoice form with the next invoice number
- it auto copies the supplier ref number to the bank transfer communication field
- it checks if the supplier invoice number already exists

This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.""",
    'data': ['account_invoice_view.xml',],
    'demo': [],
}
