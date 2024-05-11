• API Setup

* Go to http://my.telegram.org  and log in.
* Click on API development tools and fill the required fields.
* put app name you want & select other in platform Example :
* copy "api_id" & "api_hash" after clicking create app ( will be used in setup.py )

• How To Install and Use

* Install -y git python
* cd Telegram-group
* Install requierments
	-pip install telethon requests configparser
	-pip install cython numpy pandas
* python setup.py -i

• Setting up configration file (apiID, apiHASH)

* python setup.py -c

• Adding members to a group

* python AddToGroup.py members.csv
* Choose the group to add the members.csv contacts using the numbers as a guide
* Choose option 1 to add members by user ID