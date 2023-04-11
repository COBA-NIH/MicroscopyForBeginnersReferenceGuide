# Open source software

## Introduction

When it comes time to select a software program for your image analysis, there are many options, some more general and others highly specialized to specific image modalities or types of experiments. In general, a good place to start exploring is by examining papers in your field and seeing what others have used to analyze similar experiments to your own. It’s important to note that there isn’t one correct answer to "Which program should I use?" Depending on your biological question, your images, and your own comfort with coding, there are many options available. 

Below, we summarize the use-cases and limitations of some of the most common, free and open-source software for image analysis, this is a small list and more extensive ones exist like the [A Hitchhiker's guide through the bio-image analysis software universe](https://febs.onlinelibrary.wiley.com/doi/full/10.1002/1873-3468.14451) {cite}`Haase2022-ad` and the [BioImage Informatics Index](https://biii.eu) {cite}`Paul-Gilloteaux2021-vw`. 

Whatever software you choose, be sure to include a detailed description of your analysis in your methods, with pipeline or workflow files if possible, so others can reproduce your work. Also be sure to cite the analysis software you use! This helps developers of the software get grant funding and helps others find useful tools.  



::::{grid}
:gutter: 3

:::{grid-item-card}
:columns: 4
:img-top: https://imagej.net/media/icons/imagej2.png
```{dropdown} ImageJ
[ImageJ](https://imagej.net/) is an imaging processing program that is capable of operating on a variety of images including multichannel, 3D and time series. It provides basic imaging processing operations and has a variety of plugins for more complex tasks.
[Read more...](content/imagej)
```
:::

:::{grid-item-card}
:columns: 4
:img-top: https://global.discourse-cdn.com/business4/uploads/imagej/original/2X/b/bcdcd5ba157e07e74dd1964ec81765e708455ed9.png
```{dropdown} CellProfiler
[CellProfiler](https://cellprofiler.org/) was designed with the idea of an image analysis pipeline in mind; it allows you to take a series of interoperable modules to design your own custom analysis pipeline that can be applied to one or thousands of images, making it suitable for high throughput image analysis.
[Read more...](content/cellprofiler)
```
:::

:::{grid-item-card}
:columns: 4
:img-top: https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/6/0/6039b2daa4b6b1c32943f63f464cf3c477898bfe_2_750x750.png
```{dropdown} QuPath
[QuPath](https://qupath.github.io/) offers a wide set of image analysis tools that can be applied to whole slide images like pathology images, but it can be used with other images as well. QuPath also contains pixel classification tools and can integrate with ImageJ.
[Read more...](content/qupath)
```
:::

:::{grid-item-card}
:columns: 4
:img-top: https://icy.bioimageanalysis.org/wp-content/uploads/2018/07/logo_full_notext600px.png
```{dropdown} Icy
[Icy](https://icy.bioimageanalysis.org/) is an out of the box image analysis tools, it utilizes plugins to create visual image analysis protocols that can be shared with other users.
[Read more...](content/icy)
```
:::

:::{grid-item-card}
:columns: 4
:img-top: https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/7/4/74273a1f9a663b52053d44c9767ed49193f2170f_2_787x750.png
```{dropdown} MIB
[MIB](http://mib.helsinki.fi/index.html) is a user-friendly software for image analysis of multidimensional datasets for both light and electron microscopy. It allows you to use the whole acquired data for its analysis and extraction of morphological features.
[Read more...](content/mib)
```
:::

:::{grid-item-card}
:columns: 4
:img-top: https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/7/7/775e83f70639e1cb7cb299d8681d272e18718089_2_750x750.png
```{dropdown} napari
[napari](https://napari.org/) is being developed as a multi-dimensional image viewer that can be expanded via a variety of plugins to perform basic and complex image analysis tasks.
[Read more...](content/napari)
```
:::

:::{grid-item-card}
:columns: 4
:img-top: https://www.cellpose.org/static/images/cellpose_transparent.png
```{dropdown} Cellpose
[Cellpose](https://www.cellpose.org/) is a {term}`segmentation` algorithm, it provides a graphical user interface that allows users to use trained models or train their own using their images and annotations.
[Read more...](content/cellpose)
```
:::

:::{grid-item-card}
:columns: 4
:img-top: https://global.discourse-cdn.com/business4/uploads/imagej/original/3X/9/f/9f5be5e138c63bc6a50be0bb0027b8eef0194935.png
```{dropdown} ilastik
[ilastik](https://www.ilastik.org/) is a tool for interactive image classification, {term}`segmentation` and analysis. It leverages machine-learning algorithms to perform pixel and object-level classification. Using it requires no experience in {term}`image processing`.
[Read more...](content/ilastik)
```
:::

:::{grid-item-card}
:columns: 4
:img-top: https://global.discourse-cdn.com/business4/uploads/imagej/original/3X/3/f/3fe4d974194caabdb61a5574e24402db8484ab9b.png
```{dropdown} Piximi
[Piximi](https://www.piximi.app/) is an application for annotation and classification that runs entirely from your browser and requires no installation and minimal setup. 
[Read more...](content/piximi)
```
:::

::::
