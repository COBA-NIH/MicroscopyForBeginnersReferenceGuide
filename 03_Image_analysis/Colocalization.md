# Colocalization

(content/colocalization)=
## What is colocalization?

Colocalization is when two or more different labels (e.g., eGFP and mCherry) spatially overlap in your image (also called co-occurrence). Another component of colocalization is that the fluorescent labels often correlate in intensity (i.e., pixels with brighter eGFP also have brighter mCherry). It is very important to measure colocalization quantitatively–**do not just trust your eyes!**

It is also important to recognize that co-ocurrence does not _necessarily_ imply interaction. 

```{margin}
As an example, it is possible for two people to work in the same building an never interact. 
```

```{figure} ../images/colocalization.png
---
alt: degrees of colocalization
width: 100%
align: center
name: colocalization-fig
---
**Colocalization is about intensity and spatial overlap of labels**
```

<br>

````{dropdown} 📏 How do I measure it?

There are two main branches for how to look at colocalization: Object-based and correlation-based.

* **Object-based colocalization** is appropriate when you want to be able to say something about a fraction of objects being positive for multiple labels (e.g., 99% of eGFP+ cells were also mCherry+). Here’s a sample workflow:

```{mermaid}
flowchart LR
    A[Raw image Label #1] -->|Segmentation| B((Identified objects \n eGFP+ cells))
    C[Raw image Label #2] --> |Segmentation| D((Identified objects \n mCherry+ cells))

    B & D -->E(Measure overlap per cell \n if overlap > threshold %, say colocalized )--> G(Fraction of eGFP+ cells also mCherry+)
    E --> H(Fraction of mCherry+ cells also eGFP+)

   classDef empty width:0px,height:0px;

  style A fill:#D0F1E3,stroke:#57CC99
  style B fill:#D0F1E3,stroke:#57CC99

  style C fill:#FFF4d6,stroke:#FFBE0B

  style C fill:#FFD6E8,stroke:#F5006A
  style D fill:#FFD6E8,stroke:#F5006A
```

* **Correlation-based colocalization** is more appropriate when the labels you’re measuring are not found in discrete objects or when you predict that the signal in the labels should correlate. Correlation-based colocalization is simpler to measure as it does not require any {term}`segmentation` of objects. Pearson correlation coefficients are readily measurable in most image analysis softwares (e.g., FIJI, CellProfiler, etc.).
````

````{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
* **Not having adequate controls** (e.g., single label controls where only one fluorescent label is present). Noise, uneven illumination, and other technical artifacts can cause correlation between two channels
* **Not correcting for shift between channels** It’s common to have some degree of shift between different imaging channels due to differences in optics (e.g., different filter cubes). Not correcting for this shift (e.g., by measuring it and applying the corresponding correction to the channels) can limit your ability to detect colocalization.
* **Bleedthrough** Sometimes signal from one fluorescent channel bleeds into another, which can falsely increase your detected colocalization. This happens most commonly with fluorophores that are similar in spectra (e.g., GFP and YFP). This is caused by fluorophore in one channel being weakly excited by light used to excite a different fluorophore and the resulting emitted fluorescence makes it through the emission filter (e.g., your green objects show up in the yellow channel as well). Assess this with single label controls.
* **Improper interpretation of your colocalization metric** The details of the metric chosen here are very important - they vary widely in terms of their inclusion of background pixels, their sensitivity to signal-to-noise, etc. Consultation with an expert and the inclusion of proper controls can help you be assured that your measurement is truly what you think it is. 
````

```{dropdown} 📚🤷‍♀️ Where can I learn more?

* 🔢 [Theoretical background on colocalization](https://svi.nl/ColocalizationTheory)
* 📄 [Image co-localization - co-occurrence versus correlation](https://journals.biologists.com/jcs/article/131/3/jcs211847/77151/Image-co-localization-co-occurrence-versus) {cite}`Aaron2018-qi`
```
