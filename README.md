# Account Move API
This module provides an API for creating accounting entries in the account.move model through HTTP requests.

### Example Request
```bash
  PATCH /api/v1/move/account.move/call/create_move
```

### Headers:
```bash
  Authorization: Basic base64(username: email, password: token)
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
          "journal_id": "Operaciones varias",
          "currency_id": "DOP",
          "company_id": "RIBOCAP SAS (Rep. Dom.)",
          "line_ids": [
            [
              0,
              0,
              {
                "account_id": "CUENTA DE PRUEBA PARA LA API",
                "partner_id": "Frainer Encarnacion",
                "currency_id": "DOP",
                "amount_currency": 0.0,
                "debit": 0.0,
                "credit": 0.0
              }
            ]
          ]
        }
      ]
    ]
  }
```
## :rocket: Main Technologies ##

<a href="https://python.org">
  <img width="50" title="Python" alt="Python Logo" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</a> &#xa0; &#xa0;

<a href="https://odoo.com">
  <img width="100" title="Odoo" alt="Odoo Logo" src="https://github.com/odoo/odoo/blob/17.0/addons/web/static/img/logo.png">
</a> &#xa0; &#xa0;

### Prerequisites
- Odoo 14 ot heigher
- Install the [Open API module](https://apps.odoo.com/apps/modules/14.0/openapi) in your Odoo instance.
- Enable the account.move module.
- Add your user to the allowed users.
