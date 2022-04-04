**Bruker2csv**

# Description
Python script I've been using to convert Bruker's NMR files into csv files. Currently, the script takes Bruker's binary file and converts it into a csv file containing three columns with the ppm scale, intensity and normalized intensity.

# Requirements
This script requires the following Python packages:
- NMRglue : https://github.com/jjhelmus/nmrglue
- Numpy : https://github.com/numpy/numpy
- Pandas : https://github.com/pandas-dev/pandas

# Usage
As provided, you should open the script `bruker2csv.py` and add the directory to the file you want to extract

`data_dir = os.path.normpath('C:/Bruker/TopSpin4.1.3/data/400/Sample/10/pdata/1')`

You should also choose the filename of the exported file. Usually I add the nucleus and the sample id.

`sample_name = '1H_zeolite'`

Then you should run on your command line

`python bruker2csv.py`

and a new csv file will be created

## Using Jupyter Notebooks
In my workflow, I use this script in [Jupyter Notebook](https://github.com/jupyter/notebook) and plot the NMR spectrum using [Matplotlib](https://github.com/matplotlib/matplotlib). See the `bruker2csv_JN.ipynb` file.

Feel free to contact me if you need any help using this!
