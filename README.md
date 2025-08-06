Setup for uv .....  

uv add google-generativeai python-dotenv

rm -rf myfirstproject

sudo apt-get update
sudo apt-get install -y gnome-keyring
nvm install node
npm install -g typescript
npm -v  
node -v  
tsc -v

sudo apt-get install -y python3-pip python3-dev python3-venv build-essential libssl-dev libffi-dev

source my_env/bin/activate
python3 -m venv myfirstproject
source myfirstproject/bin/activate
pip install cowsay
deactivate

mkdir myproject && cd myproject
uv init .
uv venv
source .venv/bin/activate
uv add openai-agents
uv add python-dotenv
uv run main.py
uv run app.py

chainlit run main.py -w



# for Linux Creating chromeos developer    chromebook developer mode


sudo apt update && sudo apt dist-upgrade -y
python3 --version
sudo apt install python3 python3-pip -y
python3 --version
pip3 --version
dpkg --print-architecture
# My-first-agent
