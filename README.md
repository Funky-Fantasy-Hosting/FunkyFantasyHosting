# FunkyFantasyHosting
Our Software Engineering project. 

Link to our [SRS document](https://docs.google.com/document/d/1MxkAyRQ9vqesaHWG9CkF1JhxgJS4AfMEdNwubAL4py4/edit?usp=sharing)


Funky Fantasy Hosting is a new tool for playing fantasy football. It takes the form of a website that can take your rosters that were drafted on the Sleeper platform, and manages them according to new and unique rule sets. The site will pull real world NFL data from the ESPN API. This site will allow fantasy football to be played in novel ways to break the monotony of traditional leagues.


# How to run the actual site (Different sets of parenthesis are for different machines, if one doesn't work try another)
0. Create your python enviornment -ONLY DO THIS ONCE- (python3 -m venv nameOfEnviornment)
1. Run your python enviornment (source nameOfEnviornment/bin/activate)
2. Install Requirements.txt onto your python enviornment (pip install -r requirements.txt)
3. Set your FLASK_APP to main.py (set FLASK_APP=main.py) (export FLASK_APP=main.py)
3b. Set your FLASK_ENV to Development if you are changing code (set FLASK_ENV=Development) (export FLASK_ENV=Development)
3c. Set the GOOGLE_APPLICATION_CREDENTIALS (export GOOGLE_APPLICATION_CREDENTIALS=ffbigquery.json)
4. Run flask(flask run)
5. ctrl-click on the link provided in the terminal

