## Introduction
This repository contains scripts to collect basketball statistics from [Basketball Reference](https://basketball-reference.com) or [MySportsFeed](https://mysportsfeed.com). Th intent of this work was to provide an automated way this data for Fantasy Basketball competition.

To make it more easily accessible, the Basketball Reference script (which I use more) a Docker image is created. The script has been branded Basketball Statistics Collector, or BSC. 

## Usage
Using the script is very easy. For local use, setup a virtual environment, activate it and install the packages
```
# Setup environment
python3 -m venv .env

# Activate it
./.env/bin/activate

# Install requirements
pip3 install requirements
```

Create the folder 'logs' and run the script
```
# Create folder
mkdir logs

# Run the script
python3 basketball_reference.py
```

## Docker
You can also just pull the Docker image for easier use.
```
docker pull statixs/bsc
```

And run it with an attached folder of your choosing to store the CSV file. 
```
docker run --rm -v <ABSOLUTE_PATH>/logs:/app/logs statixs/bsc:latest
```

## Contributing
Contributions are very welcome! Make a PR with a clear description what you are adding and it'll be reviewed for merging :) 