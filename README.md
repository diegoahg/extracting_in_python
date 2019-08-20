# Scraping in Wikipedia using panda

This is a simple example to use pandas to scrap in the web by getting data and then clean it to obtain the necessary data.

In this case, It gets the data from the table of the Territorial organization of Chile in the website https://es.wikipedia.org/wiki/Chile. Then, It adds a new column of population percentages each Region. Finally, The program export to CSV file with the data.

## Pre-requisites
- Python >=3.6.8
- Pip for Python3
- Python Environment. This is optional but I recommended use it. You can follow this [guide]( https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Installation

Into the python env, you need to run this command. It has all of the package necessaries to run the application.

```bash
pip install -r requirements.txt
```

If you find a problem with the installation you can create a new Issue.

## Usage

```python
python main.py
```

## Output waited
```bash
Getting data from wiki Chile...
Cleaning the data
Calculating the population percentage...
Exporting to CSV...
The Program has finished
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Next Steps
- Dockerized
- Add Test