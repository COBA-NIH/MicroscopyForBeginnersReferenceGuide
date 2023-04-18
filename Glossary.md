# Glossary

```{glossary}

Blocking
  During the immunostaining procedure, it is important to minimize nonspecific binding of the primary or secondary antibodies. In most cases, this is achieved by blocking, which typically involves adding substances such as normal sera, gelatin, or albumin before immunostaining in order to "occupy" all the non-specific binding sites in the sample.

Deconvolution
  The process of computationally removing blur from microscopy images by using the known optical properties of the light path to "reassign" pixel intensity away from where it hit the camera and back onto the structure that emitted the light. 

Ex-Vivo imaging
  Refers to imaging performed on live animal tissue in an external controllable environment (e.g., tissue explant on a petri dish). It enables high-resolution imaging of live tissue that may be otherwise inaccessible within the animal. The tissue is maintained alive on the imaging system through perfusion of oxygenated (95% oxygen and 5% CO2), temperature-controlled media using peristaltic pumps and microfluidics.    

Fiji
  [Fiji](https://imagej.net/software/fiji/) Is Just ImageJ. ImageJ2 plus a lot of common plugins.

Fixation
  Fixation of a specimen refers to the stabilization of the cellular/molecular components within the sample while at the same time stopping any biological function in that sample. The fixative used (e.g., paraformaldehyde, glutaraldehyde, methanol), concentration and conditions (e.g., buffer, temperature) determine the extent of preservation of the cellular and/or molecular structures within a sample, and needs to be optimized depending on the sample or structure that is being imaged.

Image processing
  Is an operation that can be performed on an image, the result benign another image. There are simple image processing operations, like resizing or rotating an image. And other more advanced like enhancing particular features of an image like circles or lines.

Immersion media
 The immersion media is the medium that fills the gap between your objective lens and the glass coverslip or sample. It impacts the numerical aperture of the objective lens {math}`NA=RI * sin(θ)`, thus impacting lateral and axial resolution. It is critical to match the RI of the immersion media with that of the mounting media to minimize aberrations and improve image quality. Immersion media can be air, water, silicone oil, glycerol or oil. 

Immunolabeling
  Immunolabeling is one of the most common labeling techniques for fixed samples. You can use fluorescently conjugated primary antibodies to detect the protein of interest or a two-step labeling with a primary antibody and a fluorescently conjugated secondary antibody. Primary-secondary labeling tends to result in signal amplification. The main issue with immunolabeling is the size of the antibodies, which require extensive permeabilization. Another good option is to use nano-bodies, which only have the heavy-chain and are significantly smaller than regular antibodies. 

Intravital imaging
  It refers to the imaging of cellular structures or biological processes inside a live animal in real time, without extracting the organs or fixing the sample. In general, it requires specific instrumentation or modalities with improved light penetration, such as multiphoton microscopy and is limited to the ability to access the specific organ, often through optical windows. Intravital imaging is overseen by bioethical committees and needs to be approved by IACUC and/or other institutional committees. 

Mounting media
 Is the solution in which your specimen is placed in (mounted). Its purpose is to preserve the sample, including the fluorophores in it,  and enhance the imaging quality during acquisition, by buffering the pH, matching the refractive index throughout the sample (ideally matching it to that of glass) and minimizing photobleaching (depending on the medium) . Mounting media prevents the sample from drying out allowing long-term storage.

Object detection
  Is the image processing technique to detect objects within an image. It would not give you a mask of the objects but it could give you a bounding box, or and x,y position.

Oxygen scavengers
  Oxygen tends to induce photobleaching of organic dyes and other fluorophores. Addition of oxygen scavengers to the imaging media such as glucose oxidase or pyranose 2-oxidase can significantly reduce photobleaching of the fluorophores present in the sample. It is important to understand that the use of oxygen scavengers may affect live cell imaging, as these scavengers can affect the ATP and oxygen levels within the sample, compromising its health and therefore biological function.    

Permeabilization
  In order for the antibodies used during immunostaining or other fluorophores to penetrate and bind to their antigen within a cell or tissue, the membrane integrity (holes) needs to be challenged with a mild detergent. The permeabilization step needs to be carefully optimized depending on the antigen of interest, as it can result in a loss of cytoplasm or a degradation of the signal. 

Refractive index
  It's a measure of how light travels through a specific medium. It is an important value when calculating the numerical aperture of an objective, Ideally, a mismatch in refractive index between the sample (mounting medium), the coverslip and immersion media should be minimized in order to enhance the image quality. [See an interactive demo of refactive index at MicroscopyU](https://www.microscopyu.com/microscopy-basics/refractive-index-index-of-refraction)

ROIs
  Regions Of Interest. Pixels in your image that you care about (e.g., a region in tissue, a cell, a tumor, etc.) 

Segmentation
  Method of dividing an image into multiple parts or regions. There are three different types of segmentation. 
    - Semantic segmentation, were all parts of an image are part of a class, common in cell biology will be detecting cells and background on an image.
    - Instance segmentation, the segmentation is object based, not just detecting were the cells are but diving each cell as a separate object.
    - Panoptic Segmentation,  it can be defined as a combination of the prior two, because it identifies the object but also cassifies them. An example in biology might be detecting all the cells on an image and classifying them as dividing vs not.

Thresholding
  The easiest form of image segmentation, it divides the image into two part the background and the foreground (or signal). It creates a binary image were usually the background pixels would be change to a 0 value and the foreground pixels values would be 1.

Tissue clearing
  Fluorescence imaging of the whole thickness of a piece of tissue is very challenging due to light absorption and scattering induced by the inhomogeneities in refractive indexes within the tissue itself, resulting in poor light penetration. Additionally, light coming from different parts of the sample contribute to fluorescence blur, drastically reducing contrast and resolution in any given plane. As a result, researchers tend to use tissue sectioning techniques to extract information about cellular components and their spatial distribution or relationships from a thin two-dimensional volume. However, most components in any complex biological system such as an organ are not contained within this two-dimensional volume, and therefore, this approach compromises the understanding of the spatial relationships among cellular components. Tissue clearing focused on reducing the inhomogeneities in the tissue by equilibrating the refractive index throughout the sample. This allows light to pass through the tissue and therefore enables high resolution, volumetric imaging of whole organs and tissues using conventional microscopy techniques such as confocal microscopy without the need to physically section the sample.

Tissue sectioning
  Light penetration and fluorescence imaging is negatively impacted by light scattering within a thick specimen. This scattering is due to the different refractive indexes present within a tissue. To facilitate imaging of tissues, researchers often cut thick tissues into slices of different thicknesses. This process is called tissue sectioning. In most cases the samples are fixed and embedded in paraffin or frozen in tissue freezing medium and later cut into thin slices by a machine like a cryostat, microtome, or vibratome and sections collected into a tube or onto a slide.


```

<!-- 
Terms that aren't in the book yet but we know we want to add


Widefield
Super-resolution
Deconvolution
Confocal microscopy
Spectral imaging
Light sheet
Multiphoton
Optical clearing
Köhler illumination
Wavelength
Intensity
Objectives
Light source
Laser
Absorption
Numerical aperture (NA)
Color correction
Working distance (WD)
Emission spectra
Photobleaching
Detector
Phototoxicity
Saturation
Photo-multiplier tube
Averaging
Signal to noise ratio


  -->