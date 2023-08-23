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
          "date": "2023-06-28",
          "ref": "API",
          "journal_id": "Operaciones varias",
          "currency_id": "DOP",
          "line_ids": [
            [
              0,
              "virtual_843",
              {
                "account_id": "Cuenta de prueba",
                "partner_id": "Azure Interior",
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
