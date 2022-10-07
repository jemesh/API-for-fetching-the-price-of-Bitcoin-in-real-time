# care
open the project in pycharm<br/>
**Activate virtual Enviornment**
  open terminal and run<br/>
  cd env/Scripts/.\acitvate<br/>
  cd ..<br/>
  cd ..<br/>
**Run the project by following command**<br/>
  python manage.py runserver<br/>
  now go to this link<br/>
  http://127.0.0.1:8000/<br/>
**Below link gives the current bitcoin price and it's automatically added to the database ,and every time we refersh page or get request,will current bitcoin price **<br/>
  http://127.0.0.1:8000/priceofbitcoin/<br/>
**list of the price that we have previously fetched (10 data per page)**<br/>
  http://127.0.0.1:8000/list/<br/>
** fetch the data using id and delete**
  http://127.0.0.1:8000/list/1 </br>
**Note** : only authorised person can delete the data ,for that you need to login<br/>
       Before you try to login create super user by run this command<br/>
       python manage.py createsuperuser<br/>
