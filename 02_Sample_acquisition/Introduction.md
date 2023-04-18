# Introduction

Microscopes are optical instruments, and as such, they are composed of different optical components and devices. As a beginner, it is important to recognize the experimental parameters that can affect the quality and rigor of the imaging data, and by extension, its interpretation. 

A foundational concept is the “light path,” which can be used to trace out light’s trajectory from the light source to the detector. When working with microscopes, whether it is a cell culture microscope or a cutting-edge superresolution system, it is important to take the time to trace out the different light paths in the system. By approaching the system as a sum of its parts means that optimizing and troubleshooting become systematic processes compared to when the system is treated as a black box. This [interactive tutorial at MicroscopyU](https://www.microscopyu.com/tutorials/tepaths) shows the light paths in a standard inverted microscope; [this view](https://www.microscopyu.com/microscopy-basics/components) gives more detail about the various parts.

## Types of microscopes

While far from a comprehensive list of what is available, a few of the most common types of microscopes are listed below.
- **Widefield**, sometimes called _epifluorescence_, microscopes that take in all the light available to them in a single light path; this approach requires the least complex hardware, and also is often advantageous when imaging dim samples. {term}`Deconvolution` is sometimes performed after imaging on a widefield microscope to remove blur.
- **Confocal** - microscopes that remove out-of-focus light in the light path, typically using one or many pinholes to physically block this light. Several variants of confocal microscopy exist; spinning-disk confocal microscopes are often preferred for live-cell imaging applications as they tend to minimize toxicity to the sample.
- **Multiphoton** microscopes utilize multiple pulses of longer-wavelength (lower energy) light to penetrate deep into tissue, since tissues are less likely to scatter these wavelengths; once there, multiple low-engergy photons hitting the fluorphore at the same time will use their combined energy to activate a fluorophore that each photon alone would be too weak to do. Because the benefit of these systems is in their deeper penetration, they are often used for performing live-animal imaging. 
- **Superresolution** microscopes that are designed to allows the user to bypass the minimum optical resolution limit (typically 200 nm, depending on sample consideration) to resolve very small structures. Sometimes this is achieved with specialized hardware (such as in STED and STORM) and sometimes with specialized probes (such as in PALM and STORM). 
- **Light sheet** microscopes that illuminate the sample perpendicular to the axis of imaging, often by a second, orthogonal set of objective lenses. This allows for thin optical sectioning across large volumes, but introduces more considerations around sample mounting. Many variations on light sheet microscopes have emerged in recent years. 

```{important} 
No matter which kind of microscope you use, scientific microscopes are complex instruments with many working parts, all of which typically must be in good working order and calibrated/aligned properly for quantitative imaging to take place. The maintainer of your microscope will typically ensure this, but speak with them regularly about questions you may have and about how changes to the microscope configuration may affect your ability to accurately make certain measurements. Your microscope maintainer may be maintaining a large number of microscopes with a large number of independent users, so if something looks "off", make sure to talk with them before proceeding!
```

<!-- 
Commented out text not shown on the page

 -->