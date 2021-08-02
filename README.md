# Construction Progress

The project monitors the construction progress at a construction site.

![caption](https://github.com/hamza9305/Construction-Progress/blob/main/output/progress.gif)

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
## Region of Interest
The region of interest that is to be monitored can be selected by drawing a bounding box or elsewise a polygon of any shape that can help us to monitor the construction area more closely. The accurate parameters of the polygon can be selected particularly in this project using the [Find_coordinates.py](https://github.com/hamza9305/Construction-Progress/blob/main/Find_coordinates.py) which takes in an input image and based on the curser clicks, you can get the image coordinates of the region of interest.

<img src="https://github.com/hamza9305/Construction-Progress/blob/main/data/Images/image0.png" width="320" height="180" img align="center">
<img src="https://github.com/hamza9305/Construction-Progress/blob/main/data/Images/mask.png" width="320" height="180" img align="right">


