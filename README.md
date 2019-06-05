

<details>
    <summary> Abstact data type </summary>
    
* Abstract Data types ADTs means what kind of data a data structure can hold and what operations are allowed on that data.
* You may create a new ADT and define them or you can use already defined ADTs like linked list. 
* difference between ADT and data structure? Abstract Data Types express ideas about a collection of data. Data Structures implement those ideas using code.
</details>    

<details> 
    <summary> List and linkedlist</summary>

* Python list can contains different types of values
```python
a = [1, true. "amir", 43]
```
* Python uses  `dynamic array` to save data. Dynamic array uses contiguous chunk of memory to store data and save each item in its own slot and index counts from 0. So in Dynamic array we can access directly to memory located the item using an integer as its address. 
* in contrast `Linkedlist` has only a pointer to another node in memory.
* `linkedlist` has `head` to show the entry point. `Head` is just a reference and is not a seperate node and End of linkedlist is a node which points to `none`
* If head referecnce to `none` means empty linkedlist
* Linked lists are recursive DTS because each node points to another collection of nodes
#### When to Use Linked List
* When we want to insert items "in between" other items
* Collection size is unknown
* no need random access
* no concern about memory usage
</details>
<details>
    <summary> Node classes for single and dounle linked lists</summary>
    
*  A node class needs a data and put to none at first we create
```python
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

     # this method returns a readable anyobjest we have. It returns as string format our self.data
    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):  
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next"""
        self.next = new_next

```
* To run this command you can use `python3 -i filename.py` command then
```python
node = SLLNode('apple')
node.get_data()
node.set_data(7)
node2 = SLLNode(9)
node.set_next(node2)
node.get_next()  // return none
```
#### Double LinkedList 
* To have double linked list to traverse the list in both ways
```python
class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next
        parameter."""
        self.next = new_next

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute with
        new_previous parameter."""
        self.previous = new_previous
```
</details>

<details>
    <summary> Lambda </summary>

* Lambda is anonymouse functions like
```python
sum = lambda a, b, c: a + b + c
sum(1,2,3) #return 6
```
*  Lambda can be used inside lists and dictionaries
* Lambda is used with Map, filter and seduce. Filter is use to filterout the inputrs and seduce use to travers through inputs.
A good [resource](https://www.python-course.eu/python3_lambda.php)
```python
>>> even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
>>> print(even_numbers)
[0, 2, 8, 34]

>>> import functools
>>> functools.reduce(lambda x,y: x+y, [47,11,42,13])
113
```
</details>
<details>
    <summary> Regex </summary>
   
* Using regex [online](https://regex101.com)
```python
import re
re.search('/W','amir nabaei@vfd') # returns not charactors
re.search('[a-zA-Z0-9]','amir nabaei@vfd') # retun only numbers and charactors 
bool(re.search('[!@#$%^&*(),.?":{}|<>]','amir nabaei@vfd'))   #check for special charactors
/^([a-z0-9]{5,})$/.test('abc12');   // true
```
</details>
  
<details>
    <summary> Read and write into file </summary>
    
```python
# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 
```
* READ inputs in a line 
```python
# number of elements 
n = int(input("Enter number of elements : ")) 
  
# Below line read inputs from user using map() function  
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
  
print("\nList is - ", a) 
```
* Read unlimited inputs into array of unknown size
```python
  lst=list(map(int,input().split()))
```
* Write a program that adds two numbers and print the result out 

```
// inputs
3
1 5
3 10
999 -34343
// outputs
6
13
-33344
```
```python
n = int(raw_input())
for _ in xrange(n):
    a, b = map(int, raw_input().strip().split())
    print a + b
```
</details>
<details> 
    <summary> Basic </summary> 

#### Arrays
* To creaet array of a fixed size we can have
```python
>> lst = [None] * 5
>> [None, None, None, None, None]
>> aa = [[0,0]]*2
>> [[0, 0], [0, 0]]
>>  [[0] * (2)] * (2)
>> same result as above
To update an 2d array or matrix
aa[1] = [4,5]    # would update row 2 
aa[1][2] = 4 # does not do what you really expect! 
```
#### Map & Lambda
* Map is a function run on a list as 
```python
r = map(func, seq)
```
* For example
```python
temperatures = (36.5, 37, 37.5, 38, 39)

def celsius(T):
      return (float(5)/9)*(T-32)
      
c = list(map(celsius,temperatures))
```
#### Lambda 
* lambda is an anonymouse function in javascript
* Same map written with lambda
```python
temperatures = (36.5, 37, 37.5, 38, 39)
f = list(map(lambda x: (float(5)/9)*(x-32),temperatures)) 
```
* Also map can go through more than one list as [here](https://www.python-course.eu/python3_lambda.php)

```python
#print in same line
for i in range(len(a)):
    print( a[i], end =" ")

x,y = 10,100
print(x,y)
print("ssa"+str(12)) // convert int to string

// globale variable
globale f // make a variable global even inside a child function
del f     // undefined a variable 

// bitwise 
y = 0x0a
x = 0x02
z = x & y # means binary action
print(f' x as hexa with 2 character is {x:02x} and as binary with 8 charactor is {x:08b}') 
```
*
```python
lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)   
```
#### Functions
```python
def ome(arg1, arg2=1):   //with default value
    print("aa")
    return arg1
ome(1,2)

// function with variable number of args
def me(*args):
    result = 0
    for x in args:
        result += x
    return result

print(me(1,2,3,4)) 
```
#### Conditional
```python
  x,y = 10, 100
    if(x<y):
        print(x,y)
    elif (x>y):
        print(x,y)
    else:
        print(x,y)
/// 
st = "x is bigger than y" if(x>y) else "y is bigger"
```
#### Loops
```python
   while(x<5):
        print(x)
        x +=1
     // for loops 2..4   
    for x in range(2,5):
        print(x)
     games = ["aaa","bbb","ccc","ddd","eee","ffff","ggg"]
     print(games[1])
     print(games[1:6:2])  #print from 1 to 4 indexs as "bbb" "ddd" "ffff"
     i = games.index("aaa") # return 0
     games.append("rrr")    # add to the end
     games.insert(0,"vvv")  # add to index 0
     games.remove("aaa")
     games.pop() # remove from end of the list
     del games(2)
     print(', '.join(games)) #add , between members in array
     len(games)   # size of array
/// Skip the rest of the loop or break
       for x in range(1,10):
        if(x%2 == 0): continue
        print(x)  #prints odd numbers
        
        for x in range(1,10):
        if(x > 4): break
        print(x)  #only 1,2,3 and stop
        
/// geting index and values
     days = ["1","a","sd"]
     for i,d in enumerate(days):
         print(i,d)
```
* Hashes
```python
   hashes = {'a':1, 'b':2, 'c':3, 'd':4}
        hash2 = dict(a=1, b=2, c=3, d=4)
        for k,v in hash2.items():
            print(f'{k}, {v}')
         for k in hash2.keys(): print(k)
         for v in hash2.values(): print(v)
         hash2['f']=5 #assign new value
```
#### Classes
```python
class myclass():
    def method1(self):
        print("mehtod 1")

    def method2(self,somthing):
        print(somthing)

c = myclass()  // create object of the class 
c.method1()    // self refers to current object and never calls
c.method2("sss")

// inherite classes 
class second(myclass): 
      def somemethod(self):
          myclass.method1(self)
          print("done!")
          
```
</details>    

<details> 
    <summary> Run Scrapper </summary> 

* Creaet `configCredentials.py` from `configCredentialsExample.py` providing username and passwords for eventbrite
* change username to `username=anabaei` at `runScraper.sh` then run
```javacript
bash runScraper.sh
```

</details> 

## Run Python 

* on command line 
```python
python myhello.py
```
#### Read Json File
* To read json who file we have
```python
import json 
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)
    
pprint(data)
```
```python
#data is a list of hashes to read for example name of each object loop through as
for x in data:
  print(x['name'])
```
* To hit canvas we should change header with key `Authorization` and value `Bearer canvasToken`

## Scrape event CSVs from EventBrite with Python3 and Selenium

## Before running
- Python3 must be installed
- If not for mac you can `brew postinstall python3`
- if not working and gets error `Permissions issue when linking python3` use
```python
sudo mkdir /usr/local/Frameworks
sudo chown $(whoami):admin /usr/local/Frameworks
```
- Chrome must be installed
- Selenium must be installed, use: `pip3 install selenium`
- Pandas (python3 data library) must be installed, use `pip3 install pandas`
- Chromedriver must be in PATH, visit `https://sites.google.com/a/chromium.org/chromedriver/downloads`, download it and then place it into `usr/bin` or `usr/local/bin`.

## How to run
- Create a copy of `configCredentials.py.example`, fill it with the proper EventBrite details, then rename it to `configCredentials.py`
- Modify the username and directory variable in `runScraper.sh`
- Use `bash runScraper.sh` to collect the CSVs, process them and upload the combined json file to ftp server.

# Scrape event CSVs from EventBrite with Python3 and Selenium

## Before running
- Python3 must be installed
- Chrome must be installed
- Selenium must be installed, use: `pip3 install selenium`
- Pandas (python3 data library) must be installed, use `pip3 install pandas`
- Chromedriver must be in PATH, visit `https://sites.google.com/a/chromium.org/chromedriver/downloads`, download it and then place it into `usr/bin` or `usr/local/bin`.

## How to run
- Create a copy of `configCredentials.py.example`, fill it with the proper EventBrite details, then rename it to `configCredentials.py`
- Modify the username and directory variable in `runScraper.sh`
- Use `bash runScraper.sh` to collect the CSVs, process them and upload the combined json file to ftp server.

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
 
 * First make sure that you using python 3 
```java
/// rm if python2 
$ brew rm python 
$ rm -rf /usr/local/opt/python
$ brew prune 
$ brew install python3
```
 * 
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


