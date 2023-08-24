# Account Move API
This module provides an API for creating accounting entries in the account.move model through HTTP requests.

### Example Request
```bash
  PATCH /api/v1/move/account.move/call/create_move
```

### Headers:
```bash
  Authorization: Basic base64(username:password)
  Content-Type: application/json
```

### Body:
##### raw > json
```json
  {
    "args": [
      [
        {
          "date": "2023-08-24",
          "ref": "Asiento desde postman",
          "journal_id": "Facturas de cliente",
          "currency_id": "DOP",
          "company_id": "RIBO (Venezuela)",
          "line_ids": [
            [
              0,
              "virtual_843",
              {
                "account_id": "CUENTA DE PRUEBA RIBO VENEZUELA",
                "partner_id": "Frainer Encarnacion",
                "currency_id": "DOP",
                "amount_currency": 0.0,
                "debit": 0.0,
                "credit": 0.0,
                "quantity": 1
              }
            ]
          ]
        }
      ]
    ]
  }
```
### Prerequisites
- Install the Open API module in your Odoo instance.
- Enable the account.move module.
- Add your user to the allowed users.
