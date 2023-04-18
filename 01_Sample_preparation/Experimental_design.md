# Experimental design decisions

A number of critical decisions must be made when designing a quantitative bioimaging experiment. Many of these decisions will be deeply dependent on what is possible given the biology you wish to study, for example:
- You will always prefer live imaging to fixed imaging if it is important to assess the dynamics of a given process
- You may need to perform special processes such as tissue clearing if it is important to image deep into a relatively opaque specimen
- You cannot rely on genetic tagging with fluorescent proteins if your model system is not genetically tractable to such manipulations
- You have to image at a particularly high resolution to confidently assess interactions between two molecules imaged in the same system

 It is therefore _**extremely**_ important to think through all of the aspects of your biological question before ever picking up a pipette or a slide. Many sample preparation decisions are deeply entwined with the availability and suitability of particular microscopes; see [that section](content/microscope_selection) for more information. 

## Mounting

Many imaging applications involve mounting on glass coverslips, either directly or using a coverslip mounted into a dish. While there are a wide range of coverslip sizes and shapes, the most important specification to take into account is the coverslip thickness (0.17 mm) or grade (#1.5 grade) and tolerance (how precise the thickness measurement is. For example, the thickness of a #1.5 coverslip can vary between 0.17-0.19mm, whereas a #1.5H has a standard deviation of 0.005 mm). These factors are important because most microscope manufacturers assume a specific coverslip thickness in the design of objective lenses to minimize common occurring aberrations. These aberrations tend to affect the brightness and axial resolution, reducing signal to noise ratio, sharpness and resolution . The tolerance of the coverslip (to minimize the variability in thickness) is essential for super-resolution techniques or intensity measurements in images collected with high numerical aperture objectives. Other applications do not require the mounting of samples onto glass or plastic, but instead have the sample and the objective lens immersed in the same medium.

The {term}`refractive index` the sample is placed in, as well as the refractive index of the glass and the medium between the objective and the sample are all critical to determining the overall resolution that can be achieved. The {term}`mounting media` can have other important optical and/or experimental properties; it is important to use the correct mounting media for experiment planned. 

```{figure} ../images/mounting_media.png
---
alt: effects of mounting media 
width: 75%
align: center
name: mounting-media-dependence
---
**Effects of mounting media on staining with various fluorophores**. Adapted from Jonkman J., Brown C.M., Wright G.D _et al_. Tutorial: guidance for quantitative confocal microscopy. _Nat Prot_ **15**, (2020) {cite}`Jonkman2020-bo`
```

## Fluorophore selection

Fluorophores are molecules that are able to emit light upon absorption of a photon, typically of shorter wavelength. The fluorophores relevant to biomedical research can be small molecules organic dyes (FITC, Alexa Fluor 488) that bind specific cell structure (e.g., DAPI, BODIPY, mitotrackers), fluorescent analogues of small molecules (e.g., phalloidin, fluorescent amino acids) or fluorescent proteins. Some of the important properties to consider when choosing fluorophores are listed below:

- Excitation/emission spectra of each fluorophore 
- Brightness (dyes tend to be brighter than proteins)
- Photostability
- Propensity to oligomerize (in the case of fluorescent proteins)
- Phototoxicity (when imaging in live samples)

Understanding what fluorophores are available, their properties and the specifications of the hardware to image the sample (light source, excitation/emission filter cube, detector) are key in selecting the appropriate fluorophore(s) to address a scientific question. See the section on [reproducibility](content/reproducibility) for more information.

<!-- 
Commented out text not shown on the page

 -->