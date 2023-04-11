# Specific Use Software 

Tools on this page tend to be extremely good at certain tasks, but are less intended for a wide range of use cases. For tools with broader areas of focus, see the [General Use Software](./GeneralUseSoftware.md) page.

(content/cellpose)=
## <img src="https://www.cellpose.org/static/images/cellpose_transparent.png" alt="logo" width="30px"> Cellpose

[Cellpose](https://www.cellpose.org/) {cite}`Stringer2021-uq` is a {term}`segmentation` algorithm, it provides a graphical user interface that allows users to use trained models or train their own using their images and annotations.


```{dropdown} What type of image analysis problem is it best at?

Object {term}`segmentation`, most trained models are for cell {term}`segmentation` but could be applied to segment other similar objects 
```

```{dropdown} What are its disadvantages?



* Its use requires some computational knowledge. 
* Training a new model requires manual annotation correction that can be time consuming, but is likely less time consuming than other methods of training models.
```

```{dropdown} How to download/install and learn more?



* 🌐 [Installation instructions](https://cellpose.readthedocs.io/en/latest/installation.html)
* 🎥 [How to use tutorial](https://www.youtube.com/watch?v=5qANHWoubZU)
```

(content/ilastik)=
## <img src="https://global.discourse-cdn.com/business4/uploads/imagej/original/3X/9/f/9f5be5e138c63bc6a50be0bb0027b8eef0194935.png" alt="logo" width="30px"> ilastik

[ilastik](https://www.ilastik.org/) {cite}`Berg2019-no` is a tool for interactive image classification, {term}`segmentation` and analysis. It leverages machine-learning algorithms to perform pixel and object-level classification. Using it requires no experience in {term}`image processing`.


```{dropdown} What type of image analysis problem is it best at?

It can be used for both instance {term}`segmentation` and semantic {term}`segmentation`. It does also perform {term}`segmentation` and tracking, though with somewhat fewer tunable parameters than some other tools offer. 
```

```{dropdown} What are its disadvantages?



* Sometimes loading or exporting images can require a bit of troubleshooting to get the dimensions correct.
* ilastik is limited by your computer’s RAM so training a model with lots of features or working with very large images is likely to slow you down.
```

```{dropdown} How to download/install and learn more?

To download ilastik:



* 🌐 [ilastik download ](https://www.ilastik.org/download.html)

For documentation examples and  tutorials.



* 🌐 [User guide](https://www.ilastik.org/documentation/index.html#user-documentation) 
```

(content/piximi)=
## <img src="https://global.discourse-cdn.com/business4/uploads/imagej/original/3X/3/f/3fe4d974194caabdb61a5574e24402db8484ab9b.png" alt="logo" width="30px"> Piximi


[Piximi](https://www.piximi.app/) is an application for annotation and classification that runs entirely from your browser and requires no installation and minimal setup. 


```{dropdown} What type of image analysis problem is it best at?

Piximi can do image classification using machine learning 
```

```{dropdown} What are its disadvantages?



* It is still in the developing phases and some of its proposed features are not available yet
```

```{dropdown} How to download/install and learn more?



* 🌐 [Piximi website ](https://www.piximi.app/)
* 🌐 [Piximi user guide ](https://documentation.piximi.app/intro.html)
```