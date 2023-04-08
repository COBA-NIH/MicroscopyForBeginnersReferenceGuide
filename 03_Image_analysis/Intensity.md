# Intensity measurements

## What are intensity measurements?
Intensity refers to the brightness of signal for a fluorescent label. Using intensity measurements, we can infer a relative amount of fluorophore or stain. So for instance, if you have a protein tagged with a fluorophore, you can measure the intensity of that fluorophore to get a relative measure of how much protein is present in your sample. Intensity measurements include the following (non-exhaustive) and can be measured within an image, in a object like a cell, in subregions of an object:
* **Mean intensity**: the average intensity across all pixels
* **Integrated intensity**: the sum of pixel intensities, a proxy for the total amount of that marker in an object
* **Texture measurements**: the smoothness of the intensities

<br>

````{dropdown} 📏 How do I measure it?

Intensity is relatively straightforward to measure, but can be quite tricky to do _correctly_ (see below). We strongly suggest you contact an image analysis expert before proceeding with this type of analysis because there are so many places things can go wrong. In general, you want to measure on either raw images, or illumination-corrected images, but in general with minimal {term}`image processing`. Illumination-correction is a form of {term}`image processing` to compensate for the uneven pattern of illumination produced by most light sources where the middle of the field of illumination is brighter than the edges. Then intensity measurements can be made in any standard image analysis software, either across the whole image or in identified objects. See below for an example workflow:

```{mermaid}
flowchart LR
    A[Raw image] -->|"Correct uneven illumination\n (optional, but best practice)" | B[Corrected image]-->|Segmentation|C((Identified objects \n e.g., cells))

    B -->|Measure intensity| E(Image-level intensity \nmeasurements)
    C -->|Measure intensity| F(Object-level intensity \nmeasurements)

   classDef empty width:0px,height:0px;

  style A fill:#D0F1E3,stroke:#57CC99
  style B fill:#D0F1E3,stroke:#57CC99

  style C fill:#FFF4d6,stroke:#FFBE0B

  style C fill:#FFD6E8,stroke:#F5006A
```
````

````{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
```{margin}
To understand saturation another way, imagine you’re trying to measure average male height with a 2 meter tape measure. If our sample contains men that are taller than 2 meters, we can’t tell _how much taller_ than 6 feet they are; they’re like saturated pixels that exceed the intensity we can detect. This saturation of our measurement tool means we can’t accurately report average height.
```

* **Saturation** Saturated pixels are so bright their intensity values max out our detector (camera). If you have saturated pixels in the cells you’re trying to measure, you really can’t do most intensity measurements. This is because for saturated pixels, you don’t know how bright they really are, just that they’re brighter than you can detect. There are some intensity measurements that are robust to some saturation. For example, the median intensity of an image won’t be affected by saturation unless you have >½ the image saturated. But measurements like mean intensity will be affected by saturation.

* **Inadequate controls** In most cases, the exact intensity measures you get don’t mean anything biologically in isolation. It’s only by comparison of conditions that we can generate some biological insight. A control condition is therefore **very** important to compare to your experimental condition.

* **Not matching imaging conditions across experimental conditions** Because intensity measures are affected by exposure time, light source intensity, and other factors, it’s very important to match imaging settings across your samples. Relatedly, you should make sure you don’t separate imaging your experimental and control conditions to different days if this can be in any way avoided. Fluorophores can become dimmer over time in samples, which complicates interpretation if different sample types were imaged on different days.

````

```{dropdown} 📚🤷‍♀️ Where can I learn more?

* 🎓 [Neubias training resource on intensity measures](https://neubias.github.io/training-resources/measure_intensities/index.html)

```
