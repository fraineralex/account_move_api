# Account Move API

## Example Data

partner_id = 'Azure Interior'
currency_id = 'DOP'
company_id = 'YourCompany'
journal_id = 'Facturas de cliente'
TEMPLATE = [
  {
    "name": "API/2023/0001",
    "ref": "Asiento desde postman",
    "move_type": "entry",
    "posted_before": False,
    "journal_id": journal_id,
    "company_id": company_id,
    "currency_id": currency_id,
    "partner_id": partner_id,
    "payment_state": "not_paid",
    "invoice_date": "2023-06-27",
    "invoice_date_due": "2023-06-29",
    "invoice_line_ids": [
      [
        0,
        False,
        {
          "sequence": 100,
          "product_id": False,
          "name": False,
          "quantity": 1,
          "price_unit": 147,
          "discount": 0,
          "tax_ids": [
            [6, False, [3]]
          ],
          "partner_id": partner_id,
          "currency_id": currency_id,
          "product_uom_id": False
        }
      ]
    ]
  }
]