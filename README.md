# agile Sentiment

## Create and execute the enviroment bellow <br>
- python -m venv agl <br>
- Windows .\agl\Scripts\activate <br>
- Ubuntun source ./agl/bin/activate <br>

Obs.: .gitignore will ignore the agl enviroment!!!

## Create and execute the requeriments.txt <br>
pip install -r requirements.txt <br>
If you receive a yellow WARNING about pip, I suggest to update your pip.

## Finaly execute the aplication
python .\main.py

## To update libraries usued in requeriments
- pip freeze > requirements.txt

## To use git to update the repository
- git init
- git add .
- git commit -m "msg"
- git push
- git stash push --include-untracked (AWS Machine)
- git pull (AWS Machine)

## Aws InfraStructure deploy
- pm2 delete agilim
- pm2 save
- git clone https://github.com/pedrosrk/agileSentiment.git
- cd agileSentiment
- pm2 start main.py --interpreter python3 --watch --name agilim
- pm2 save

## Aws InfraStructure database
- mysql -u root -p
- USE agilim
- SELECT * from users;
