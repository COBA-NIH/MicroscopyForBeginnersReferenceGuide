# Data management and sharing

## What is it?

Both journals and scientific funders have placed more emphasis in recent years on the fact that it is critical to save both the raw data generated during the course of scientific discovery as well as the workflows used to process such data. While mandates to publicly deposit raw image data have recently gone into place in several countries, it can be difficult for researchers to know where to store images, code, and metadata associated with their bioimaging experiments.

````{dropdown} 🤔 What are my options?

There are many options for storing image data in online repositories. These services make it easy to share and reuse data. The best option will depend on the size of the dataset, the budget for storage, whether there is related non-image data, and how much metadata is available for the dataset. Some options are summarized below:

```{figure} ../images/data_management.png
---
alt: Comparison of various data respositories
width: 100%
align: center
name: data-repository-chart
---
**Options for storing bioimaging data** Figure by Beth Cimini (2023) [Source](https://doi.org/10.5281/zenodo.7628604)
```
````

```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?

* **Not storing original versions of images**. It is critical that the raw image data be saved and stored. It is very important that these files are not compressed formats (e.g., '.jpeg') or modified from the original files on which analysis was performed. If files are modified, measurements will change and the analysis pipeline will not be reproducible to anyone else. 

* **Necessary imaging metadata is unavailable**. In order to properly calibrate measurement data, it's critical that information like pixel size (e.g., in microns), the microscope manufacturer and model, and acquisition settings are included alongside the data. If this isn't included, it will be very difficult to reproduce results or use the combine the data with other datasets. 

```

```{dropdown} 📚🤷‍♀️ Where can I learn more?

* 🌐 [Zenodo](https://zenodo.org/) 
* 🌐 [Figshare](https://figshare.com)
* 🌐 [Dryad](https://datadryad.org)
* 🌐 [Bioimage Archive](https://www.ebi.ac.uk/bioimage-archive/) {cite}`Hartley2022-mt`
* 🌐 [Image Data Resource (IDR)](https://idr.openmicroscopy.org/) {cite}`Williams2017-yy`
* 🌐 [BBBC](https://bbbc.broadinstitute.org/) {cite}`Ljosa2012-fr`
* 🌐 [Cell Painting Gallery](https://registry.opendata.aws/cellpainting-gallery/)

```

<!-- Stuff we know we still want to add
Versioning
GitHub
DataLad
 -->