# Predict-Spotify-Top200
- This is a miniproject in which Spotify API is used to pull the audio features data of music tracks. That data is used to described what kind of features are present in hit songs and how those features have changed over a time period. 

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

## Notes

#### Used ImageMagick in bash for GIF
    convert -delay 15 *.jpg topfeatures.gif
