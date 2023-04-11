# Practical considerations

## Objective selection

Microscope objectives have a number of features that must be considered when deciding which objective is right for your experiment

- Magnification and resolution: the higher the numerical aperture (NA) of the lens, the finer the resolution one can obtain in one's sample. 
- Color correction:
- Working distance:

## Z sampling

- Nyquist sampling - the [online calculator](https://svi.nl/NyquistCalculator)

## Acquisition power/speed

## Filter sets

- Fluorophores

<!-- 
Commented out text not shown on the page

Paper text

Optical properties of the sample
As a starting point, it is important to consider the sample in terms of its transparency and thickness. Relatively thin specimens such as tissue culture cells and ultrathin cryosections (<10 µm thick) do not absorb or scatter light significantly, so they can be readily imaged using standard widefield [19] and some types of super-resolution [20,21] microscopy.  
Tissue sections thicker than 10-20 µm absorb and scatter more heavily, and alsointroduce significant out-of-focus fluorescence, leading to haziness and blur in the image. Good choices here are confocal microscopy [22] and/or computational deconvolution [23] techniques. These approaches allow acquisition of “optical sections” that enhance contrast and resolution compared to widefield techniques. If lacking a confocal microscope, a good option for samples with thicknesses up to about 20 µm is to combine widefield with deconvolution, which computationally improves the sharpness and resolution of images by removing out-of-focus light. From 20-150 µm, confocal or multiphoton microscopes are the gold standard for optical sectioning.
Confocal microscopes reach their usable imaging limit at about 100-150 µm due to absorption and scattering, though the maximum depth can vary depending on the optical properties of the sample. Multiphoton microscopy [24] allows imaging of thicker sections by using longer wavelength lasers to excite fluorescence. When working with fixed tissue, optical clearing [16,25] can improve tissue penetration in most fluorescent microscopy varieties. Optical clearing combined with light sheet [26] microscopy is the gold standard for whole tissue imaging. Light sheet microscopy is also useful for inherently clear samples such as fixed whole embryos from various species and for observing development of live specimens in early developmental stages. 
Not every lab will have access to all types of microscopes, and it is important to remember that an experiment done on a nearly-as-good microscope is more informative than an experiment never done because the perfect microscope could not be accessed. Much can be done in a basic widefield microscope (e.g., second scenario in Fig 2); when not sufficient, other labs or intitutions may allow access to the optimal microscopes needed. If needed, there are also several global opportunities to access microscopes through collaborative initiatives that are working to increase accessibility (Table 1).
Microscope settings 
Once a microscope is chosen, it is time to work out the optimal conditions for image acquisition. When acquiring images, no matter how simple or complex the microscope, take the time to understand the microscope light path from the light source to the detector(s) [28]. Knowing which components in the light path impact image quality enables accurate adjustment of their settings for the application as well as troubleshooting any minor issues with the equipment such as incorrect filters, prisms, etc. being in the path when they should not be.

Pay particular attention to the major components that will impact the quality of the images. The following is a summary of key features and their typical adjustments to look out for. Note that while these parameters are necessary, one must also check that the microscope is in good working order (e.g., cleaned per manufacturer instructions, appropriately calibrated, objectives attached securely, brightfield light path is aligned correctly for Köhler illumination if brightfield imaging is being used). The maintainer of the microscope will typically do this on a regular basis but speak with them about any known issues for a given microscope and how to detect and solve them.


Standard microscopes will contain a variety of components; certain components like the light source, objectives, filters, and detector (e.g., camera) are critical to good image quality. On a widefield microscope, the light source used for visual observation is often the same as for data acquisition. Advanced systems may have separate light sources for visual observation versus data acquisition. While the light path is fixed for fluorescence on most microscopes, it is often composed of several independently movable components for brightfield and must be properly aligned and calibrated before use. 


It is important to choose an objective that has both the magnification and resolving power necessary for the experiment. While magnification is important, the resolving power of the objective is the most critical feature and is defined by the numerical aperture (or NA) and the wavelengths used for imaging. The NA is the measure of the light-gathering ability of the objective and determines how well fine features in a specimen will be resolved. Increasing NA will improve both resolution and how efficiently fluorescence emission is collected. 


The color correction of the objective lens (usually labeled as Fluor, Apo, or Super Apo on the lens) is critical for multicolor imaging. It allows focusing on different colors at the same plane allowing multiple different-colored objects to be in focus at the same time. “Fluor” typically focuses two colors at once, while “Apo” and “Super Apo” can handle three to six different colors. The Working distance (WD, in millimeters) determines how far a lens can focus into a sample. This also includes the thickness of the coverslip and any mounting media, so be sure the working distance is far enough to reach the sample. If the microscope has trouble focusing on the sample and seems to “run out” of focus, it is often because the working distance of the lens is too short.


For fluorescence microscopy, one must match the filter sets to the fluorophore absorption and emission spectra. For quick reference on the spectral characteristics of different fluorophore combinations, consult a spectral viewer [3]. Using a mismatched filter can lead to flawed conclusions or even prevent imaging at all.


Most instruments use either a camera (widefield/super resolution/light sheet) or photomultiplier Tube (PMT) (confocal/multiphoton) for the detection of fluorescence emission. The detector converts fluorescence photons emitted from the sample to an electrical current that is then digitized, and encoded as a number in the digital file that captured. Each point imaged on the sample corresponds to a pixel viewed in the final image. In applications where the goal is to detect a fluorescent reporter, the ratio of the encoded pixel value in areas with fluorescence to areas without fluorescence is often referred to as the signal-to-noise ratio; at higher signal-to-noise ratios, finer gradations in the amount of reporter present can be detected. 


For cameras, adjusting the exposure controls the amount of time the camera is collecting emission light to form an image. The optimal exposure time will depend on the brightness of the sample relative to the intensity of the excitation light. Dimmer specimens require either higher intensity excitation light or longer exposure times. Standard practice is to adjust the excitation intensity to expose the specimen to the lowest dose of excitation light possible to minimize photobleaching and phototoxicity. When using fluorescence, fluorophores often photobleach easily so it is better in general to use a lower illumination power and longer camera exposure when using camera-based systems. Exposure time is  particularly important for live cell experiments where many images are acquired over time to capture a dynamic process. Longer exposure times will also increase the overall image acquisition time. If long exposure times are needed, the field of view, or size of the region being imaged, can be reduced to produce a smaller image and minimize acquisition time. For scanning systems that use PMTs, consider line (or frame) averaging to improve the signal-to-noise ratio. Overexposure, also known as saturation, can be caused by excitation light that is too intense or exposure times that are too long and will render images unsuitable for quantification of intensity. 


In conclusion, the microscopy image is more than a picture; it is a data set that must be as high quality and reproducible as possible. It is often necessary to balance competing needs for spatial resolution, number of targets, and, when examining dynamic processes, acquisition speed. Optimization by definition is iterative, and we recommend testing out different settings before finalizing. Review and analyze preliminary data before finalizing an approach for the whole project. Finally, the imaging parameters of the microscope used must be recorded and reproduced within each experiment [10].


 -->