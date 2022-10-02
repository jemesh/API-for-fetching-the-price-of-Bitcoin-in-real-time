# care
open the project in pycharm
**Activate virtual **
  open terminal and run
  cd env/Scripts/.\acitvate
  cd ..
  cd ..
**Run the project by following command**
  python manage.py runserver
  now go to this link
  http://127.0.0.1:8000/
**get current bitcoin price and add this price to the database**
  http://127.0.0.1:8000/add
**list of the price that we have previously fetched**
  http://127.0.0.1:8000/priceofbitcoin/
  
Note : only authorised person can delete,put,patch the data ,for that you need to login
       Before you try to login create super user
       python manage.py createsuperuser
