# Considerations for different sample types
(content/sample_types)=
There are many different options for types of samples to image, and advances in sample preparation techniques and imaging modalities are continually enabling the imaging of more diverse and complex biological specimens. As with many other aspects of experimental design, sample type selection comes with tradeoffs. Samples that are amenable to simple preparation and imaging tend to be small, thin, and relatively clear, like a monolayer of cultured cells. Such samples have obvious advantages and can be imaged in a high-throughput manner, but they're not suitable for every biological question. Sometimes a thicker specimen, like an organoid, or whole or sectioned tissue is needed, especially when the biological question involves interactions between different types of cells. Carefully consider what biological context is appropriate for your question and what measurements you'd ultimately like to be able to make. Below, we summarize some common sample types

````{dropdown} 🤔 What are my options?

Here we present some major categories for sample types. Note that there are not hard boundaries between these different categories (e.g., both cells and organoids can be cultured in 3D, many of these specimens can be imaged live or after {term}`fixation`), but some general advantages and disadvantages are summarized below. 



**Cultured cells**

Many different types of cells can be cultured, or grown in a dish. Cells can be grown in a monoculture, with only one cell type, or in a co-culture with multiple cell types. 

_Advantages_

* Cultured cells tend to be relatively simple to image and for many questions can be imaged with widefield microscopy (see [Acquisition](content/microscope_selection)), which is faster and more accessible than confocal or superresolution methods. Additionally, high-throughput microscopes integrated with robotics can enable automation of experiments and imaging with cultured cells. 

* Cells can be frozen, thawed, and grown much faster than work with more complex specimens like organoids or whole organisms, compressing the timeline to perform an experiment

_Disadvantages_

* Most applications in microscopy require imaging through a glass coverslip of a specific thickness and tolerance. However, many cell types do not survive or cannot grow on glass and require additional coatings and manipulations of the coverslip to ensure the health of the sample. As an alternative some companies manufacture imaging chambers (multi well plates, 35 mm dishes…) with proprietary polymers that have similar properties to glass (optical polymers), thus enabling high resolution imaging. It is imperative to understand whether the immersion oil used during imaging affects the integrity of these polymers, as the solvents in some immersion media can crack or dissolve the polymer layer. 



**Organoids**

Organoids are cultured cells that are grown in 3D to mimic the structure and sometimes functions of organs. Organoids are typically grown from stem cells that self-organize into a more complex structure, including differentiating into different cell types. Organoids are well suited to questions of development, modeling disease, and for understanding tissue and organ regeneration. 

_Advantages_

* Because organoids contain multiple cell types and reflect some structure and cell relationships seen in organs _in vivo_, they are well-suited to more complex questions about disease and cell-cell interactions. They can also be used to model processes and structures that are necessarily 3D and not recapitulated well in a flat layer of cells, like many developmental processes. 

* Organoids can be made from induced pluripotent stem cells (iPSCs) from human or animal samples, and thus can model disease processes specific to a given human donor. 

_Disadvantages_

* Organoids can take more complex resources and protocols to grow and can take more time than just growing cultured cells on glass or plastic. 

* Because organoids are 3D structures, they often are not amenable to widefield imaging and may require spinning disk or point-scanning confocal microscopy. 



**Tissue**

Tissues are formed when cells act together to perform a specific function. Tissues can be cultured by taking a piece of an animal or plant and allowing it to continue to survive and grow in a dish. Tissues can also be harvested from plants or animals and stained for the presence of different molecules. Tissues are typically cut into pieces (aka {term}`tissue sectioning`), and can be fixed, fresh, or frozen, or even alive in {term}`ex-vivo imaging`.

_Advantages_

* Tissues have more intact cell-cell interactions that are generally more representative of what happens _in vivo_ than in cell culture. 

* Repositories of donated human tissues enable biomedical research to study a diverse sample of patients with a particular disease.

_Disadvantages_

* Primary cells and tissues tend to be sensitive to environment than immortalized cell lines and can be more difficult to grow and may require specialized protocols depending on cell type.  

* Tissues harvested from a whole animal or plant require time for the development and growth of that specimen before harvesting.



**Whole organism / embryo**

Some whole organisms are thin and transparent enough to image. Some animals also have near-transparent embryonic stages, like the zebrafish. Additionally, {term}`intravital imaging` is the imaging of cellular structures or biological processes inside a live animal in real time, without extracting the organs or fixing the sample. In general, it requires specific instrumentation or modalities with improved light penetration, such as multiphoton microscopy and is limited to the ability to access the specific organ, often through optical windows. 

_Advantages_

* Imaging whole organisms or embyros provides the most possible intact biological context when studying a particular process or structure. 

_Disadvantages_

* Imaging of thicker specimens may require processing ({term}`tissue clearing`) of the sample to make its {term}`refractive index` match that of the imaging media and reduce absorption and scattering of light. 

* Intravital imaging often requires specific surgical techniques and is overseen by bioethical committees and needs to be approved by IACUC and/or other institutional committees. 
````

```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?

* **Photobleaching and phototoxicity** - Photobleaching can be defined as the irreversible destruction of a fluorophore in its excited state, meaning, that fluorophore will not be able to emit more light and the fluorescence signal will therefore degrade over time, affecting signal to noise ratio and intensity measurements. In order to minimize photobleaching during acquisition, there are a number of photobleaching reagent agents that can be added to the media. These agents minimize photobleaching of fluorophores to a different extent, and therefore it is important to contact the manufacturer to ensure they are optimal for the specific fluorophore. For example addition of oxygen scavengers to the imaging media such as glucose oxidase or pyranose 2-oxidase can significantly reduce photobleaching. It is important to understand that the use of {term}`oxygen scavengers` may affect live cell imaging, as these scavengers can affect the ATP and oxygen levels within the sample, compromising its health and therefore biological function. 

* **Cells are dying** - Fluorescent light induces DNA damage and oxidation of cellular components (phototoxicity). In addition, fluorophore photobleaching can further induce phototoxicity by creating reactive oxygen species (ROS). The addition of antioxidants and removal of certain molecules (e.g., riboflavin) from the imaging media can reduce the ROS produced during imaging, improving the health of the sample.{cite}`Stockley2017`    


* **My fixed cells don't looked as expected** - Fixation can change the localization and fluorescence of different proteins. Where possible, always compare the distribution of a protein or molecule of interest with and without fixation. Also consider whether a different {term}`fixation` method may be more appropriate for your specimen. 

(content/sample_opacity)=
* **My sample is too opaque** - Thicker specimens, like thick tissue sections, pigmented cells, or whole organisms can be challenging to image due to light absorption and scattering induced by the inhomogeneities in {term}`refractive index` within the tissue itself, resulting in poor light penetration. To facilitate imaging of tissues, researchers often cut thick tissues into slices of different thicknesses. This process is called tissue sectioning. In most cases the samples are fixed and embedded in paraffin or frozen in tissue freezing medium and later cut into thin slices by a machine like a cryostat, microtome, or vibratome and sections collected into a tube or onto a slide. Alternatively, most components in any complex biological system such as an organ are not contained within this two-dimensional volume, and therefore, this approach compromises the understanding of the spatial relationships among cellular components. Tissue clearing focused on reducing the inhomogeneities in the tissue by equilibrating the {term}`refractive index` throughout the sample. This allows light to pass through the tissue and therefore enables high resolution, volumetric imaging of whole organs and tissues using conventional microscopy techniques such as confocal microscopy without the need to physically section the sample.

```

```{dropdown} 📚🤷‍♀️ Where can I learn more?

* 📄 [Organoids Primer](https://www.nature.com/articles/s43586-022-00174-y#:~:text=An%20organoid%20is%20a%20self,%2C9%2C10%2C11.) {cite}`Zhao2022-rm` 
* 📄 [Tutorial: guidance for quantitative confocal microscopy](https://doi.org/10.1038/s41596-020-0313-9) {cite}`Jonkman2020-bo`
* 📄 [Hypothesis-driven quantitative fluorescence microscopy - the importance of reverse-thinking in experimental design](https://pubmed.ncbi.nlm.nih.gov/33154172/) {cite}`Wait2020-gq`

```
<!-- 
Commented out text not shown on the page
Images of the specimen types would be cool!

 -->