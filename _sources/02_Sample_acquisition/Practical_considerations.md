# Practical considerations

## Objective selection

Microscope objectives have a number of features that must be considered when deciding which objective is right for your experiment

- Magnification and resolution: the higher the numerical aperture (NA) of the lens, the finer the resolution one can obtain in one's sample. The NA is calculated as {math}`NA=RI * sin(θ)`, relating both to the {term}`refractive index` of the sample, glass, and {term}`immersion media` as well as the range of angles of emitted light that can be collected into the lens. Unless special techniques are used, the typical limit of resultion is calculated as {math}`d = λ / 2NA`, meaning the resolution is set both by the NA of the lens but also by the wavelength of light used for imaging. 

```{figure} ../images/wavelength_resolution.png
---
alt: microtubules imaged at 488nm and 647nm 
width: 50%
align: center
name: resolution-wavelength-dependence
---
**Decreased resolution at longer wavelengths of light**. Microtubules imaged at a shorter wavelength of light show higher resolution than those imaged at longer wavelengths. Adapted from Jonkman J., Brown C.M., Wright G.D _et al_. Tutorial: guidance for quantitative confocal microscopy. _Nat Prot_ **15**, (2020) {cite}`Jonkman2020-bo`
```

- Color correction: When performing multicolor microscopy, it is important to choose an objective lens that is labeled as `Apo` or `Super Apo`, as such lenses are corrected to focus 3 to 6 colors in the same plane at the same time. `Fluor` lenses will typically focus two colors at once. 
- Working distance: The working distance (WD) gives the distance in millimeters that the lens can focus into the sample. This distance includes the coverslip and mounting media as well. If imaging a thick sample, and/or if needing to image away from the surface of the sample, it is important to ensure the lens has a sufficient working distance. 

## Filter sets

It is important to make sure that the microscope that you want to image on has the correct filter sets for the fluorphores you wish to use. See the [section on bleedthrough](content/bleedthrough) for more information. 

## Z sampling

- If you wish to capture multiple z sections, the spacing of these setions is important if you wish to be able to perform an accurate 3D reconstruction. SVI has a [fuller mathematical explanation of this](https://svi.nl/NyquistRate),as well as an easy-to-use [online calculator](https://svi.nl/NyquistCalculator) that you can use to calculate the optimal z section spacing for your imaging conditions.

## Acquisition power/speed

The amount of signal captured from any fluorophore will be related not just to the intrinsic brightness of the fluorophore, but also the amount of excitation light it is exposed to (due to duration, power, or both) as well as amount of time and signal multiplication that happens at the detector (typically a camera or a photomultiplier tube (PMT)). An optimal experiment is typically one that minimizes the amount of light hitting the sample (to reduce photobleaching and/or phototoxicity) while acheiving adequate fluorescent signal and in minimal time on the equipment. How exactly to balance these competing factors will depend on the exact biology being studied and the researcher's constraints.

<!-- 
Commented out text not shown on the page

 -->