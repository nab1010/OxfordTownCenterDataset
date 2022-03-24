# Oxford Town Center Dataset YOLO Format Convert

[***@nabang1010***](https://github.com/nabang1010)


### Oxford Town Center Dataset Type

**TownCentre-groundtruth.top** file 

| **personNumber** | **frameNumber** | **headValid** | **bodyValid** | **headLeft** | **headTop** | **headRight** | **headBottom** | **bodyLeft** | **bodyTop** | **bodyRight** | **bodyBottom** |
|---|---|---|---|---|---|---|---|---|---|---|---|


### YOLO Dataset Format

file **image.txt**:

| **class** | **xCenterBBoxYOLO** | **yCenterBBoxYOLO** | **wBBoxYOLO** | **hBBoxYOLO** | 
|---|---|---|---|---|

while:

\begin{equation*}
xCenterBBoxYOLO & = xCenterBBox/imageWidth 
\end{equation*}
```math
yCenterBBoxYOLO = yCenterBBox/imageHeight
```
```math
wBBoxYOLO = wBBox/imageWidth
```
```math
yBBoxYOLOYOLO = yBBox/imageHeight
```