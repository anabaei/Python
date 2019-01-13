# Crawler
#### Python

<details>
      <summary> Crawlers </summary>

* Speed up crawling [link](https://stackoverflow.com/questions/8888454/where-to-store-web-crawler-data)
* Crawlers
```python

```
</details>

<details>
      <summary> Settings sqlite to Mysql </summary>


* To change from sqlite to mysql got to `/user/local/lib/python3.7/site-packages/memorious-0.7.20-py3.7.egg/memorious/settings.py`

```python
#DATASTORE_FILE = os.path.join(BASE_PATH, 'datastore.sqlite3')
#DATASTORE_URI = env('DATASTORE_URI', 'sqlite:///%s' % 'datastore.sqlite3')
to 
DATASTORE_URI = env('DATASTORE_URI', 'mysql+pymysql://root:password@localhost/aml')
```
where root is our username and password is our password and aml is our database name
* Common Error install pymsql for the specific version of python as well
```python
pip install pymysql   // if you use python2
pip3 install pymysql  //if you use python3
```
* Notice: in order to know which python are you  when run `memorious run crawl` it shows on top 
* `gb_coh_disqualified` gave error

</details>

<details>
      <summary> MySQL </summary>

* Show all attributes from a table
```mysql
SHOW COLUMNS FROM table_name;
OR 
Describe table;
```
* display attributes from tables
```mysql
select id from table_name;
show tables;
```
</details>

<details>
      <summary> Install </summary>

* Use this [link](https://www.slothparadise.com/how-to-install-django-on-mac/)
```java
brew install python3
```
* If error happen
```java
sudo chown -R $(whoami) $(brew --prefix)/*
sudo install -d -o $(whoami) -g admin /usr/local/Frameworks
```

```java
python3
sudo easy_install pip
sudo pip install virtualenv
virtualenv thanos
```
* Then track to it
```java
cd thanos
sudo pip install Django
```
* If error happen
```java
curl https://bootstrap.pypa.io/get-pip.py | python
pip install --upgrade setuptools
```
* Create Project Blog use [this](https://www.youtube.com/watch?v=pjkZCQTfneQ) 
```java
django-admin.py startproject blog
cd blog 
python manage.py runserver
```
Then check the port 8000 as `http://127.0.0.1:8000`

</details>

<details>
      <summary> Memorius  Start Sanctions</summary>
 
* Git clone from [here](https://github.com/alephdata/memorious) 
* Then make sure the version of python u are using and then if you want use mysql change this
```java
`/user/local/lib/python3.7/site-packages/memorious-0.7.20-py3.7.egg/memorious/settings.py`
```
as when `aml` is our database name and root and passwords are user and password for mysql
```java
DATASTORE_URI = env('DATASTORE_URI', 'mysql+pymysql://root:password@localhost/aml')
```
* now it is ready to run it as 
* A [link](https://github.com/alephdata/memorious)
```python
memorious list
memorious run crawl_name
```
</details>

<details>
      <summary> Versions </summary>
      
  * To find a file in command line
  ```java
  sudo find . -name "SQLALCHEMY_DATABASE_URI"
  ```
  * Change version got to ~/.bash_profile and edit it as 
  ```java
    alias python='python2'
  ```
  </details>  
  
  <details>
      <summary> Run Sanction </summary>
   
```java   
  python setup.py --help-commands
  python setup.py build
  python setup.py install
  memorious list
  memorious run crawler_name
```  
   </details>  
   <details>
      <summary> Open Sanctions </summary>
   
   * [open sanctions](https://github.com/alephdata/opensanctions)
   * After cloning 
 ```python
 python3 setup.py --help-commands
 ```
   </details>
   
### Create a Crawler 

<details>
      <summary> Create a file </summary>
      
* followed [this](https://www.youtube.com/watch?v=Eis9vu4XiNI)      
```python      
import os
def create_project_dir(directory):
    if not os.path.exists(directory):
       print('Creating Project'+ directory)
       os.makedirs(directory)
       
create_project_dir('thenewboston2')       
```
</details>

<details>
      <summary> HTML Parser tags </summary>
     
* Html parser allows to read pages as here. It is go through the feed and everytime saw a tag it prints it out!
* Remember it is python 3
```python
from html.parser import HTMLParser
from urllib import parse 
class LinkFinder(HTMLParser):

    def __init__(self):
         super().__init__() 
 
    def error(self, message):
        pass
   

    def handle_starttag(self, tag, attrs):
        print(tag)


finder = LinkFinder()
finder.feed(
    '<html><head> aaaaa </head><body>bbbb <h1>hhh 111</h1></body></html>'
)
```
</details> 

<details>
      <summary> Address which page to Crawl </summary>
      
* Queue keeps all hyper links inside page 
```python
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue): 
           write_file(queue, base_url)
    if not os.path.isfile(crawled): 
           write_file(crawled, '')

## Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
 
Then to call it we have 
create_data_files(
  'thenewboston', 'https://eli17.herokuapp.com/'     
)
```
</details>
 <details>
      <summary> Search Engine (spider) </summary>

* 
</details>     


 <details>
      <summary> Links </summary>
      
  * [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)
  * [MySQL DBAPI](https://docs.sqlalchemy.org/en/latest/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqldb)
  * [build crawler](https://memorious.readthedocs.io/en/latest/buildingcrawler.html)

</details>
