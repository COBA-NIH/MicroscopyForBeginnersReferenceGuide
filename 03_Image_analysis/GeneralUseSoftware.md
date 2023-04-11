# General Use Software

Tools on this page tend to be relatively multipurpose across a lot of kinds of analyses and/or images. For tools that specialize in certain analysis steps, see the [Specific Use Software](./SpecificUseSoftware.md) page.

(content/imagej)=
## <img src="https://imagej.net/media/icons/imagej2.png" alt="logo" width="30px"> ImageJ


[ImageJ](https://imagej.net/) {cite}`Schneider2012-gs,Schindelin2012-kk,Rueden2017-ku` is an imaging processing program that is capable of operating on a variety of images including multichannel, 3D and time series. It provides a variety of basic imaging processing operations, but it can be complemented with a variety of plugins for more complex tasks.

```{dropdown} What are its disadvantages?


* Imaging processing operations are done one at a time, while it has the capability of batch processing and creating macros it does require some understanding of coding.
* But while it can open large images, there is a size limit to the size it can handle based on the available memory. And even if it can open large images it can slow down performance.
```

```{dropdown} How to download/install and learn more?

To download ImageJ or its “batteries-included” distribution Fiji go to



* 🌐 [ImageJ download](https://imagej.net/downloads)

For documentation and tutorials on how to use ImageJ as well as a list of available plugins



* 🌐 [ImageJ basics](https://imagej.net/learn/)
```

(content/cellprofiler)=
## <img src="https://global.discourse-cdn.com/business4/uploads/imagej/original/2X/b/bcdcd5ba157e07e74dd1964ec81765e708455ed9.png" alt="logo" width="30px"> CellProfiler

[CellProfiler](https://cellprofiler.org/) {cite}`Stirling2021-sg` is a software designed for biologists by biologists; it creates a bridge between image analysis and scientist with no need of computational expertise. It was designed with the idea of an image analysis pipeline in mind: it allows you to take a series of interoperable modules to design your own custom analysis pipeline that can be applied to one or thousands of images, making it suitable for high throughput image analysis. 


```{dropdown} What are its disadvantages?


* CellProfiler can’t handle large images, like whole tissue sections from histology experiments. The image size is currently limited by the available memory on your computer.
* While CellProfiler can perform analysis on 3D images the visualization is limited to a one z-plane at a time via a slider on the viewing window.
* Also several features of CellProfiler are only available for 2D images.
```

```{dropdown} How to download/install and learn more?

To download CellProfiler



* 🌐 [CellProfiler download](https://cellprofiler.org/releases)

For documentation examples and  tutorials.



* 🌐 [CellProfiler user manual](https://cellprofiler-manual.s3.amazonaws.com/CellProfiler-4.2.4/index.html) 
* 🌐 [Examples](https://cellprofiler.org/examples)
* 🌐 [Tutorials](https://tutorials.cellprofiler.org/)
* 🎥 [Video tutorials and workshops](https://www.youtube.com/playlist?list=PLXSm9cHbSZBBy7JkChB32_e3lURUcT3RL) 
```

(content/qupath)=
## <img src="https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/6/0/6039b2daa4b6b1c32943f63f464cf3c477898bfe_2_750x750.png" alt="logo" width="30px"> QuPath

[QuPath](https://qupath.github.io/) {cite}`Bankhead2017-kz` offers a wide set of image analysis tools that can be applied to whole slide images. For that reason it is widely utilized with pathology images, but it can be used with other images as well. QuPath also contains pixel classification tools and can integrate with ImageJ (e.g., for sending {term}`ROIs` between the programs, or for accessing ImageJ plugins). 


```{dropdown} What are its disadvantages?

* To get the most out of QuPath (especially when analyzing many images), some scripting and knowledge of coding (or adapting other’s code) is necessary
```

```{dropdown} How to download/install and learn more?

To download QuPath



* 🌐 [QuPath download](https://qupath.github.io/)

For documentation examples and  tutorials.



* 🌐 [QuPath user manual](https://qupath.readthedocs.io/en/stable/) 
* 🎥 [Video tutorials and workshops](https://www.youtube.com/c/qupath) 
```

(content/icy)=
## <img src="https://icy.bioimageanalysis.org/wp-content/uploads/2018/07/logo_full_notext600px.png" alt="logo" width="30px"> Icy

[Icy](https://icy.bioimageanalysis.org/) {cite}`De_Chaumont2012-pe` is an out of the box image analysis tools, it utilizes plugins to create visual image analysis protocols that can be shared with other users.


```{dropdown} What are its disadvantages?



* Icy interoperability with other softwares is limited to ImageJ
```

```{dropdown} How to download/install and learn more?

To download Icy



* 🌐 [Icy download](https://icy.bioimageanalysis.org/download/)

For documentation examples and  tutorials.



* 🌐 [Icy course and tutorial](https://icy.bioimageanalysis.org/trainings/) 
* 🎥 [Bioimage analysis with Icy ](https://www.youtube.com/watch?v=myal9BD6J-k) 
```

(content/mib)=
## <img src="https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/7/4/74273a1f9a663b52053d44c9767ed49193f2170f_2_787x750.png" alt="logo" width="30px"> MIB (Microscopy Image Browser) 

[MIB](http://mib.helsinki.fi/index.html) {cite}`Belevich2016-vi` is a user-friendly software for image analysis of multidimensional datasets for both light and electron microscopy. It allows you to use the whole acquired data for its analysis and extraction of morphological features.


```{dropdown} What are its disadvantages?



* It was created using MATLAB, a standalone packaged version exist, but they do not use the most up-to-date MATLAB releases
```

```{dropdown} How to download/install and learn more?

To download MIB



* 🌐 [MIB download](http://mib.helsinki.fi/downloads.html)

For documentation examples and  tutorials.



* 🌐 [MIB user guide](http://mib.helsinki.fi/help/main2/im_browser_user_guide.html) 
* 🌐 [Tutorials](http://mib.helsinki.fi/tutorials.html)
* 🎥 [Video tutorials](https://www.youtube.com/playlist?list=PLGkFvW985wz8cj8CWmXOFkXpvoX_HwXzj) 
```

(content/napari)=
## <img src="https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/7/7/775e83f70639e1cb7cb299d8681d272e18718089_2_750x750.png" alt="logo" width="30px"> napari

[napari](https://napari.org/) {cite}`Sofroniew2022-nd` is being developed as a multi-dimensional image viewer that can be expanded via a variety of plugins to perform basic and complex image analysis tasks.


```{dropdown} What are its disadvantages?



* napari is still in the development stages, but it is a very popular platform and already has a variety of plugins and use cases with tutorials available.
```

```{dropdown} How to download/install and learn more?

To download napari



* 🌐 [napari bundled app download ](https://napari.org/stable/tutorials/fundamentals/installation.html#install-as-a-bundled-app)

For documentation examples and  tutorials.



* 🌐 [New to napari guide ](https://napari.org/stable/tutorials/fundamentals/getting_started.html) 
* 🌐 [Tutorials](https://napari.org/stable/tutorials/index.html)
```

