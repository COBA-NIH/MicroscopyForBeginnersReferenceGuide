# Presentation of microscopy images

## What is it?

Microscopy images are often shown in scientific papers to illustrate a particular conclusion. While qualitative conclusions are not a subsitute for quantitative comparisons (see next section), images can certainly guide our reasoning and our conclusions. Following a few consistent best practices ensures that these conclusions are correct and robust.

```{figure} ../images/10TipsHowToNotLieWithImages.png
---
alt: 10 tips for image presentation
width: 100%
align: center
---
**A brief visual summary of image presentation tips.** Figure by Helena Jambor. [Source](https://doi.org/10.5281/zenodo.7750259)
```

````{dropdown} Adjust the image crop, orientation, and size. 
For any adjustments, work with an image copy and do not alter the original file. Note, do not use adjusted images for quantitative image data analyses 
Adjustments to effectively communicate the image content may include removing uninformative image regions (crop), changing the image orientation, and adjusting the size. Note that rotation and re-sizing may change the image data when pixel information is redistributed. 
```{image} ../images/rotation.png
:alt: rotation
:align: center
```
```{dropdown} 🤔 How do I do it?
See the [cheat-sheet below](image-cheat-sheet) for more information. 
```
```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
Any adjustments that alter the conclusions are not permitted. 
```
```{dropdown} 📚🤷‍♀️ Where can I learn more?
* 📄 <!--(Miura and Norrelykke, 2021).--> 
* 📄 <!--(Cromey DW).-->
```
````

````{dropdown} Enhance visibility of image content
Images often do not have regular spaced intensity values. To still display the data visible on a screen/in a figure, adjustments of brightness and contrast are usually necessary.
```{image} ../images/inversion.png
:alt: image adjustment
:align: center
```
```{dropdown} 🤔 How do I do it?
See the [cheat-sheet below](image-cheat-sheet) for more information. 
```
```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
Any adjustments that result in the disappearance of image details are considered misleading  <!--(Cromey DW).-->. Note that many nonlinear transformations of brightness and contrast are available in image processing software, before using these users should ensure that they faithfully represent the data to avoid accidentally misleading audiences and disclose them as annotations.
```
```{dropdown} 📚🤷‍♀️ Where can I learn more?
* 📄 <!--(Cromey DW).-->
```
````

````{dropdown} Use accessible colors
Fluorescent microscope images are often composed of data from multiple wavelengths/color channels. To best visualize molecular structures, individual channels can be shown in separate grayscale images. When colors are chosen to represent the illumination wavelength (blue, green, red, far-red), for example Green-Fluorescent Protein is shown in green color, be reminded that intensity values on a black background reduces the level of detail.

When channels are over-laid in ‘composite’ images, authors should ensure that structures are visible, i.e., that the overlay does not obstruct features and that the colors used are clearly distinguishable. 
```{image} ../images/multichannel.png
:alt: multicolor image composition
:align: center
```
```{dropdown} 🤔 How do I do it?
See the [cheat-sheet below](image-cheat-sheet) for more information. 
```
```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
For composite images consider if color combinations are accessible to color-blind audiences (e.g. not combine red with green, but rather magenta and green, see reference below for examples) and possibly additionally show individual channels in grayscale for maximizing accessibility and detail. 
Tools for color blindness simulation of the images exist in image processing software (ImageJ/Fiji) and visibility of colors in final image figures can be tested with applications such as ColorOracle. 
```
```{dropdown} 📚🤷‍♀️ Where can I learn more?
* 📄 <!--(Jambor et al PLosBio).--> 
```
````

````{dropdown} Annotate key image features
Each image needs a reference to its physical dimensions. This is typically achieved by including a scale bar with dimensions annotated in the image or the figure legend.

In addition, authors should remember to annotate the colors used, any symbols and arrows used to guide readers, and, if used, the origin of any zoom/inset. If specialized images are shown (time-lapse, volumes, reconstructions) authors are encouraged to consider annotating important information in the figures. 
```{image} ../images/crosstalk.png
:alt: speech bubbles
:align: center
```
```{dropdown} 🤔 How do I do it?
See the [cheat-sheet below](image-cheat-sheet) for more information. 
```
```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
Lack of details and missing of key explanations will make it impossible for audiences to interpret image data in figures. 
To unambiguously reference probes consider using terms from the ISAC Probe Tag Dictionary, a standardized nomenclature for probers used in cytometry and microscopy. 
```
```{dropdown} 📚🤷‍♀️ Where can I learn more?
* 📄 <!--(Blenman et al, Cytometry, 2021).--> 
```
````

````{dropdown} Explain the image 
To rapidly orient audiences, a minimal explanatory text should be presented along with images. This includes the figure legend and the methods section in scientific papers or the title of figures in posters and slides.
Consider using a controlled vocabulary to reduce ambiguity and increase machine-readability of the descriptions of specimens, tissues, cell lines, and proteins etc. A useful tool is the [RRID (Reseach Resource Identifying Data)index](https://scicrunch.org/resources) , which provides indices for commonly used biological reagents and resources, e.g., plasmids, cell lines and antibodies . 
```{dropdown} 🤔 How do I do it?
See the [cheat-sheet below](image-cheat-sheet) for more information. 
```
```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
Missing explanations of image details/methods may result in non-reproducible data and limits the insights from the data. 
```
```{dropdown} 📚🤷‍♀️ Where can I learn more?
* 📄 <!--(Sheen et al for the consequences of unintelligible images in research.).--> 
* 📄 <!--(Marques et al for a survey of method statements in papers with image data.).-->
* 📄 <!--(Yu, Agarwal, Johnston and Cohen for a user analysis of the understandability of figure legends in the literature ).-->
```
````

A cheat sheet on how to do basic image preparation with open source software: 


```{figure} ../images/processing_images_cheatsheet.gif
---
alt: Instructions for common image processing operations in Fiji
width: 100%
align: center
name: image-cheat-sheet
---
**How to correctly perform various image manipulations in Fiji.** Figure by Christopher Schmied and Helena Jambor. [Source](https://doi.org/10.12688/f1000research.27140.2)
```