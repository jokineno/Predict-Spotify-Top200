# Predict-Spotify-Top200

```
git clone https://github.com/hd4niel/Predict-Spotify-Top200.git
```

## TODO
- [ ] Analyze features' correlation with streams and position
- [ ] Timeline of features over time
- [ ] Feature timeseries forecasting
- [x] Extra: Generate lyrics

## File structure

#### data
Data files, .csv etc...

#### notebooks
Jupyter notebooks

#### src
Code, .py files

#### results
Analysis docs

## Example workflow using virtual environment in python

#### Initialize virtual env in venv/ (it is ignored by gitignore)
    virtualenv -p python3 venv

#### Activate virtual env
    source venv/bin/activate

#### Install dependencies
    pip install -r requirements.txt

#### Install package
    pip install package

#### Add to the requirements
    pip freeze > requirements.txt
    
#### Deactivate environment
    deactivate

#### Use jupyter
    ipython kernel install --user --name=.venv
    jupyter notebook
choose kernel .venv