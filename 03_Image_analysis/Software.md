# Open source software

## Introduction

When it comes time to select a software program for your image analysis, there are many options, some more general and others highly specialized to specific image modalities or types of experiments. In general, a good place to start exploring is by examining papers in your field and seeing what others have used to analyze similar experiments to your own. It’s important to note that there isn’t one correct answer to "Which program should I use?" Depending on your biological question, your images, and your own comfort with coding, there are many options available. 

Below, we summarize the use-cases and limitations of some of the most common, free and open-source software for image analysis, this is a small list and more extensive ones exist like the [A Hitchhiker's guide through the bio-image analysis software universe](https://febs.onlinelibrary.wiley.com/doi/full/10.1002/1873-3468.14451) and the [BioImage Informatics Index](bii.eu). 

Whatever software you choose, be sure to include a detailed description of your analysis in your methods, with pipeline or workflow files if possible, so others can reproduce your work. Also be sure to cite the analysis software you use! This helps developers of the software get grant funding and helps others find useful tools.  


### General use software


#### ImageJ

[ImageJ](https://imagej.net/) is an imaging processing program that is capable of operating on a variety of images including multichannel, 3D and time series. It provides a variety of basic imaging processing operations, but it can be complemented with a variety of plugins for more complex tasks.


##### What are its disadvantages?



* Imaging processing operations are done one at a time, while it has the capability of batch processing and creating macros it does require some understanding of coding.
* But while it can open large images, there is a size limit to the size it can handle based on the available memory. And even if it can open large images it can slow down performance.


##### How to download/install and learn more?

To download ImageJ or its “batteries-included” distribution Fiji go to



* [web] [ImageJ download](https://imagej.net/downloads)

For documentation and tutorials on how to use ImageJ as well as a list of available plugins



* [web] [ImageJ basics](https://imagej.net/learn/)


#### CellProfiler

[CellProfiler](https://cellprofiler.org/) is a software designed for biologist by biologist, it creates a bridge between image analysis and scientist with no need of computational expertise. It was designed with the idea of an image analysis pipeline in mind, it allows you to take a series of interoperable modules to design your own custom analysis pipeline that can be applied to one or thousands of images, making it suitable for high throughput image analysis. 


##### What are its disadvantages?



* CellProfiler can’t handle large images, like whole tissue sections from histology experiments. The image size is currently limited by the available memory on your computer.
* While CellProfiler can perform analysis on 3D images the visualization is limited to a one z-plane at a time via a slider on the viewing window.
* Also several features of CellProfiler are only available for 2D images.


##### How to download/install and learn more?

To download CellProfiler



* [web] [CellProfiler download](https://cellprofiler.org/releases)

For documentation examples and  tutorials.



* [web] [CellProfiler user manual](https://cellprofiler-manual.s3.amazonaws.com/CellProfiler-4.2.4/index.html) 
* [web] [Examples](https://cellprofiler.org/examples)
* [web] [Tutorials](https://tutorials.cellprofiler.org/)
* [video] [Video tutorials and workshops](https://www.youtube.com/playlist?list=PLXSm9cHbSZBBy7JkChB32_e3lURUcT3RL) 


#### QuPath

[QuPath](https://qupath.github.io/) offers a wide set of image analysis tools that can be applied to whole slide images. For that reason it is widely utilized with pathology images, but it can be used with other images as well. QuPath also contains pixel classification tools and can integrate with ImageJ (e.g., for sending ROIs between the programs, or for accessing ImageJ plugins). 


##### What are its disadvantages?

* To get the most out of QuPath (especially when analyzing many images), some scripting and knowledge of coding (or adapting other’s code) is necessary


##### How to download/install and learn more?

To download QuPath



* [web] [QuPath download](https://qupath.github.io/)

For documentation examples and  tutorials.



* [web] [QuPath user manual](https://qupath.readthedocs.io/en/stable/) 
* [video] [Video tutorials and workshops](https://www.youtube.com/c/qupath) 


#### Icy

[Icy](https://icy.bioimageanalysis.org/) is an out of the box image analysis tools, it utilizes plugins to create visual image analysis protocols that can be shared with other users.


##### What are its disadvantages?



* Icy interoperability with other softwares is limited to ImageJ


##### How to download/install and learn more?

To download Icy



* [web] [Icy download](https://icy.bioimageanalysis.org/download/)

For documentation examples and  tutorials.



* [web] [Icy course and tutorial](https://icy.bioimageanalysis.org/trainings/) 
* [video] [Bioimage analysis with Icy ](https://www.youtube.com/watch?v=myal9BD6J-k) 


#### MIB (Microscopy Image Browser) 

[MIB](http://mib.helsinki.fi/index.html) is a user-friendly software for image analysis of multidimensional datasets for both light and electron microscopy. It allows you to use the whole acquired data for its analysis and extraction of morphological features.


##### What are its disadvantages?



* It was created using MATLAB, a standalone packaged version exist, but they do not use the most up-to-date MATLAB releases


##### How to download/install and learn more?

To download MIB



* [web] [MIB download](http://mib.helsinki.fi/downloads.html)

For documentation examples and  tutorials.



* [web] [MIB user guide](http://mib.helsinki.fi/help/main2/im_browser_user_guide.html) 
* [web] [Tutorials](http://mib.helsinki.fi/tutorials.html)
* [video] [Video tutorials](https://www.youtube.com/playlist?list=PLGkFvW985wz8cj8CWmXOFkXpvoX_HwXzj) 


#### Napari

[Napari](https://napari.org/) is being developed as a multi-dimensional image viewer that can be expanded via a variety of plugins to perform basic and complex image analysis tasks.


##### What are its disadvantages?



* Napari is still in the development stages, but it is a very popular platform and already has a variety of plugins and use cases with tutorials available.


##### How to download/install and learn more?

To download Napari



* [web] [Napari bundled app download ](https://napari.org/stable/tutorials/fundamentals/installation.html#install-as-a-bundled-app)

For documentation examples and  tutorials.



* [web] [New to Napari guide ](https://napari.org/stable/tutorials/fundamentals/getting_started.html) 
* [web] [Tutorials](https://napari.org/stable/tutorials/index.html)


### Specified use software 


#### Cellpose

[Cellpose](https://www.cellpose.org/) is a segmentation algorithm, it provides a graphical user interface that allows users to use trained models or train their own using their images and annotations.


##### What type of image analysis problem is it good for?

Object segmentation, most trained models are for cell segmentation but could be applied to segment other similar objects 


##### What are its disadvantages?



* Its use requires some computational knowledge. 
* Training a new model requires manual annotation correction that can be time consuming, but is likely less time consuming than other methods of training models.


##### How to download/install and learn more?



* [web] [Installation instructions](https://cellpose.readthedocs.io/en/latest/installation.html)
* [video] [How to use tutorial](https://www.youtube.com/watch?v=5qANHWoubZU)


#### Ilastik

[Ilastik](https://www.ilastik.org/) is a tool for interactive image classification, segmentation and analysis. It leverages machine-learning algorithms to perform pixel and object-level classification. Using it requires no experience in image processing.


##### What image analysis problem can it be used for?

It can be used for both instance segmentation and semantic segmentation 


##### What are its disadvantages?



* Sometimes loading or exporting images can require a bit of troubleshooting to get the dimensions correct.
* Ilastik is limited by your computer’s RAM so training a model with lots of features or working with very large images is likely to slow you down.


##### How to download/install and learn more?

To download ilastik:



* [web] [Ilastik download ](https://www.ilastik.org/download.html)

For documentation examples and  tutorials.



* [web] [User guide](https://www.ilastik.org/documentation/index.html#user-documentation) 


#### Piximi


##### [Piximi](https://www.piximi.app/) is an application for annotation and classification that runs entirely from your browser and requires no installation and minimal setup. 


##### What type of image analysis is it good for?

Piximi can do image classification using machine learning 


##### What are its disadvantages?



* It is still in the developing phases and some of its proposed features are not available yet


##### How to download/install and learn more?



* [web] [Piximi website ](https://www.piximi.app/)
* [web] [Piximi user guide ](https://documentation.piximi.app/intro.html)
