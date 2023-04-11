# Experimental design

## Microscope modality

## Mounting

## Dye/antibody/FP

Fluorophores are molecules that are able to emit light upon absorption of a photon, typically of shorter wavelength. The fluorophores relevant to biomedical research can be small molecules organic dyes (FITC, Alexa Fluor 488) that bind specific cell structure (e.g., DAPI, BODIPY, mitotrackers), fluorescent analogues of small molecules (e.g., phalloidin, fluorescent amino acids) or fluorescent proteins. Some of the important properties to consider when choosing fluorophores are listed below:

- Excitation/emission spectra: each fluorophore 
- Brightness
- Photostability
- Propensity to oligomerize (in the case of fluorescent proteins)

Understanding what fluorophores are available, their properties and the specifications of the hardware to image the sample (light source, excitation/emission filter cube, detector) are key in selecting the appropriate fluorophore(s) to address a scientific question. 


### Specificity

### Cross compatibility

## Fixation/perm/blocking
<!-- 
JB GDoc text
Antioxidants
Fluorescent light induces DNA damage and oxidation of cellular components (phototoxicity). In addition, fluorophore photobleaching can further induce phototoxicity by creating reactive oxygen species (ROS). The addition of antioxidants and removal of certain molecules (e.g., riboflavin) from the imaging media can reduce the ROS produced during imaging, improving the health of the sample{cite}`Stockley2017`.  

Oxygen Scavengers
Oxygen tends to induce photobleaching of organic dyes and other fluorophores. Addition of oxygen scavengers to the imaging media such as glucose oxidase or pyranose 2-oxidase can significantly reduce photobleaching of the fluorophores present in the sample. It is important to understand that the use of oxygen scavengers may affect live cell imaging, as these scavengers can affect the ATP and oxygen levels within the sample, compromising its health and therefore biological function.   
Blocking
During the immunostaining procedure, it is important to minimize nonspecific binding of the primary or secondary antibodies. In most cases, this is achieved by blocking this 
Permeabilization 
In order for the antibodies used during immunostaining or other fluorophores to penetrate and bind to their antigen within a cell or tissue, the membrane integrity (holes) needs to be challenged with a mild detergent. The permeabilization step needs to be carefully optimized depending on the antigen of interest, as it can result in a loss of cytoplasm or a degradation of the signal. 

Photobleaching reducing agents
Photobleaching can be defined as the irreversible destruction of a fluorophore in its excited state, meaning, that fluorophore will not be able to emit more light and the fluorescence signal will therefore degrade over time, affecting signal to noise ratio and intensity measurements. In order to minimize photobleaching during acquisition, there are a number of photobleaching reagent agents that can be added to the mounting or imaging media. These agents minimize photobleaching of fluorophores to a different extent, and therefore it is important to contact the manufacturer to ensure they are optimal for the specific fluorophore.  

Coverslip thickness
While there is a wide range of coverslip sizes and shapes, the most important specification to take into account is the coverslip thickness (0.17 mm) or grade (#1.5 grade) and tolerance (how precise the thickness measurement is. For example,  the thickness of a #1.5 coverslip can vary between 0.17-0.19mm, whereas a #1.5H has a standard deviation of 0.005 mm).  The reason the thickness and tolerance is important is because most microscope manufacturers assume a specific coverslip thickness in the design of objective lenses to minimize common occurring aberrations. These aberrations tend to affect the brightness and axial resolution, reducing signal to noise ratio, sharpness and resolution . The tolerance of the coverslip (to minimize the variability in thickness) is essential for super-resolution techniques or intensity measurements in images collected with high numerical aperture objectives.  


Mounting media
 Is the solution in which your specimen is placed in (mounted). Its purpose is to preserve the sample, including the fluorophores in it,  and enhance the imaging quality during acquisition, by buffering the pH, matching the refractive index throughout the sample (ideally matching it to that of glass) and minimizing photobleaching (depending on the medium) . Mounting media prevents the sample from drying out allowing long-term storage.    
Immersion media
 The immersion media is the medium that fills the gap between your objective lens and the glass coverslip or sample. It ultimately determines the numerical aperture of the objective lens (NA=RI * sin(Theta)), thus impacting lateral and axial resolution. It is critical to match the RI of the immersion media with that of the mounting media to minimize aberrations and improve image quality. Immersion media can be air, water, silicone oil, glycerol or oil. 
Air
Water
Oil
Optical polymers (for dish material) 
Most applications in microscopy require imaging through a glass coverslip of a specific thickness and tolerance. However, many cell types do not survive or cannot grow on glass and require additional coatings and manipulations of the coverslip to ensure the health of the sample. As an alternative some companies manufacture imaging chambers (multi well plates, 35 mm dishes…) with proprietary polymers that have similar properties to glass (optical polymers), thus enabling high resolution imaging. It is imperative to understand whether the immersion oil used during imaging affects the integrity of these polymers, as the solvents in some immersion media can crack or dissolve the polymer layer. 


----
Paper text

General
A high quality imaging experiment begins at the bench. The best performing microscope will not produce good quality data unless sample preparation is optimized first. Optimal sample preparation helps control for optical aberrations during the microscopy and enables more accurate measurements. When comparing multiple samples, samples should be processed in parallel whenever possible, using the same reagents to avoid technical variability. Positive and negative controls should always be included to ensure that sample processing went as expected and did not introduce artifacts to the imaging [2].

Some aspects of sample preparation are generalizable; major decisions can be roughly divided by preparations designed to be imaged through a coverslip versus preparations where the objective is in direct contact with the sample itself. Most standard applications require imaging through a coverslip, and for most high-resolution imaging experiments, glass thickness should be 0.17 mm (or #1.5 grade coverslips). Using a different thickness does not mean the experiment will not work, but since most objective lenses are corrected for this specific thickness, the image of the sample is brighter, appears sharper, and has better resolution and contrast. It is also critical to choose an appropriate immersion (e.g., air, oil, or water) for the sample holder, objective, and application. All major microscopy manufacturing companies manufacture one or more varieties of their own immersion oil. Each oil is optimized for the company’s lenses and sometimes further optimized for specific uses like brightfield or fluorescence imaging.  In contrast to approaches utilizing coverslips, microscopy techniques such as tissue and intravital imaging as well as lattice light sheet microscopy use dipping objectives where the objective is partially submerged with the sample. This removes concerns about glass thickness and immersion between glass, but adds considerations about the composition and refractive index of the sample buffer.

A general principle related to fluorescence imaging is that when selecting fluorophores, one must keep in mind compatibility with the specimen, available illumination sources and filters, and the overall sample preparation workflow. In general, bright and photostable fluorophores are critical, especially when doing live cell imaging, as their use minimizes phototoxicity and photobleaching, which can affect reproducibility in live cell imaging. In general, organic dyes are brighter and more photostable than fluorescent proteins but generally cannot be genetically encoded. If performing multi-color imaging, pay attention to whether the spectra of the different fluorophores are overlapping [3].
Live samples
The health of a living sample should always be prioritized, especially as stress is cumulative. As mentioned above, imaging typically requires glass as the sample interface, but many cell types grow poorly when grown directly on glass [4]. To combat specimen incompatibility, the glass can be coated (e.g., with poly-L-lysine, gelatin, fibronectin) or dishes constructed out of optical polymers designed to be compatible with the immersion oil [5]. To help determine what works for a specific cell type, we recommend looking in the literature at what others have used; the substrate used can affect biological processes. Please note standard tissue-culture plastic is autofluorescent, so avoid regular culture dishes if possible. 

The imaging media will affect both sample health and signal. Agents such as antioxidants and reactive oxygen species scavengers can be added to the media to reduce phototoxicity and photobleaching but must be tested for effects on the health of the sample [6,7]. Typical media components such as phenol red, fetal bovine serum, riboflavins and vitamins can produce a high fluorescence background; thus, the components added to media must be balanced such that the sample is healthy, but also signal is detectable [8–10]. 

Choosing dyes and fluorescent proteins with longer excitation wavelengths (e.g., NucRed instead of Hoechst) and using gentler illumination settings (lower irradiation, shorter exposure times, etc) will reduce phototoxicity and facilitate longer periods of imaging. It is always a good idea to simultaneously monitor the sample in brightfield mode during imaging, as certain morphological changes readily visible in brightfield (e.g., blebs, condensed nuclei, rounded cells) can indicate cell stress. 
Fixed samples
The final quality of labeling in fixed samples depends on proper fixation and permeabilization. The type of fixative, its concentration, and the fixation conditions (e.g., temperature, buffer components, and fixation length) have large effects on the preservation of the cellular structures and the general morphology of the sample. When possible, it is useful to assess how fixation affects morphology by comparing to live speciments. As with many other aspects, the fixation type and conditions should be optimized for each sample and staining. One example is immunofluorescence experiments, in which antibodies are used to label proteins of interest, permeabilization is needed so that antibodies can access the intracellular space. It is important to note that permeabilization can remove soluble proteins and lipids that are not cross-linked, so this step must also be optimized for a given target. 



In addition to immunofluorescence labeling, dyes are available that specifically label different cellular components (e.g., MitoTracker and DAPI, see Fig 2). When using such dyes, follow the manufacturer’s recommendations, as some do not withstand fixation. If detecting genetically expressed fluorescent proteins in a fixed sample, note that the fixative can affect the structure of the fluorescent proteins and alter their localization [12,13]. If the signal is no longer detectable after fixation, the fluorescent protein can be immunolabeled. 

The last consideration for fixed samples is the mounting medium. Different mounting media are not alike and have varying compatibility with different fluorophores. Mounting media maintain the appropriate pH for the fluorophore, have photobleaching-reducing agents and have a high refractive index (RI) meant to reduce aberrations due to a mismatch in RI between the sample, the coverslip, and the immersion medium. Many mounting media come with DAPI, but these may produce high background or uneven staining in tissue sections and thus should be validated before use [14,15]. 


 -->