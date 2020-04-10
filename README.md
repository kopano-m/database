# database
This Python module holds a model used for uploading data related to the COVID-19 pandemic onto am AWS hosted database. This module is used hand in hand with the sqlalchemy package. The model code was taken from a repository created by Rhida Moosa [here](https://github.com/ridha-explore/coronasa.git) that will house COVID-19 data.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the database package.
```bash
pip install git+https://github.com/kopano-m/database.git
```

## Update
```bash
pip install --upgrade git+https://github.com/kopano-m/database.git
```

## Usage
To import the package along with other essential packages:
```python
from database import model as m
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
```
To refer to the database tables use the following syntax:
```python
m.'table_name'

```
Syntax for referring to the respective table columns:
```python
m.'table_name'.'column_name'
```

Syntax for uploading data into a database table:
```python
session = sessionmaker()(bind=engine)
for i in range(df):
  table_name = m.table_name(
        column1_name = df['df_column1'][i],  ## Assuming your db table has 2 columns
        column2_name = df['df_column2'][i]
  )
  session.add(table_name)
session.commit()
session.close()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Authors
Kopano Monyobo kopanomonyobo@gmail.com<br/>
