# Size and Shape measurements

## What are size measurements?
Size measurements describe the dimensions of objects in your image. Common size measurements include:

* **Area**: the 2D space an object takes up in the image or the 3D surface area of an object
* **Volume**: the 3D space an object takes up in a 3D image
* **Perimeter**: the distance around the edge of an object

## What are shape measurements?
Shape measurements describe the 2D or 3D form of objects in our sample. Common shape measurements include:

* **Circularity**: How round vs. elongated an object is. Formally defined as $circularity = 4pi*{area}/{perimeter}^2$ where 1 is a perfect circle and circularity <1 is a more elongated polygon.
* **Solidity**: how dense vs. wispy/holey an object is. Formally defined as $solidity = area/convex area$ where _convex area_ is akin to the area inside a shape formed by stretching a rubber band around the object.

<br>

```{dropdown} 📏 How do I measure it?

After segmenting an image to locate the pixels belonging to different objects, morphology can be measured readily in many image analysis softwares, like FIJI and CellProfiler. For example, in {term}`Fiji`, after identifying your objects as {term}`ROIs`, be sure to **Analyze > Set Measurements…** and select “Shape Descriptors” then simply measure your {term}`ROIs` with **Analyze > Measure**. In CellProfiler, this is accomplished using the module MeasureObjectSizeShape.
```

```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?

* **Not understanding the limitations of your images**. All biological structures are 3D, but we often analyze 2D images. Often this is still very useful! But the larger and more complex your objects (e.g., neurons in a tissue section), the more limited a 2D view becomes.
* **Failing to use calibrated units**. Be sure to properly calibrate your images and present final measurements in microns (or similar units). If measuring 3D images, be sure to take into account the z-step, which is likely larger than the xy pixel size.
```

```{dropdown} 📚🤷‍♀️ Where can I learn more?

* 📄 [Current Methods and Pipelines for Image-Based Quantitation of Nuclear Shape and Nuclear Envelope Abnormalities](https://www.mdpi.com/2073-4409/11/3/347/htm) {cite}`Janssen2022-bm`
* 🌐 [Description of morphological measurements made by CellProfiler](https://cellprofiler-manual.s3.amazonaws.com/CellProfiler-4.2.4/modules/measurement.html#id20)
* 🎓 [Plain language description of various morphological measures by Michael Wirth](http://www.cyto.purdue.edu/cdroms/micro2/content/education/wirth10.pdf)
```
