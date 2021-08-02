# Construction Progress

The project monitors the construction progress at a construction site.

## Description
The script takes in a video input of the construction site, frame by frame. Based on the changes in the pixel intensities the progress of the construction site is monitored. For this script, my region of interest had pixels which were roughly yellow in color therefore I chose relevant pixel boundaries as a check to monitor the progress.

## Requirements
- python 3
```bash
conda create -n env_name python=3.6
```
- cv2
```bash
conda install -c conda-forge opencv
```
- numpy
```bash
conda install -c anaconda numpy
```
