# Reproducibility

(content/reproducibility)=

A number of factors are critical in designing a reproducible microscopy experiment. A few critical factors are laid out here; see other works such as {cite}`Jost2019-nx` 

## Antibody validation

While in a perfect world, antibodies would always be specific to a particular target, unfortunately, this cannot always be relied upon when performing {term}`immunolabeling`. {cite}`Uhlen2016-wy` When possible, one should perform knockout and/or knockdown controls to confirm antibody specificity; where not, look for availability of another antibody to a different part of the target molecule (sometimes called the _epitope_) and confirm you get consistent localization. 

Optimizing your {term}`blocking` and {term}`permeabilization` conditions for the particular antibody and protocol can reduce non-specific background. No-primary-antibody controls should always be performed as well, as they are essential for validating signal specificity.

## Fluorescent protein localization validation

Expression of fluorescently-tagged proteins can make localization of a molecule or structure possible, especially when no good antibody exist for immunolabeling and/or it will be helpful to observe the molecule's behavior in live cells. While a study comparing overlap between the same molecular targets with fluorescent proteins vs antibodies found 80% overlap, they also found that some considerations (such as whether the C- or N- terminus of a protein is tagged) may cause changes in localization. {cite}`Stadler2013`. A recent paper {cite}`Sittewelle2023` surveys considerations for genetic tagging of molecules for live microscopy.

(content/bleedthrough)=
## Bleedthrough

When performing multicolor fluorescence microscopy, it is critical to choose fluorophores with sufficiently distinct excitation and emission spectra; online tools such as FPbase {cite}`Lambert2019-xl` can help with such selections, especially if you know the various optical components of the microscope on which you will be imaging your samples (these configurations can be saved and shared on FPbase; ask the maintainer of the microscope you plan to use if such a configuration file is already online). Even if you believe your fluorophores are sufficiently separated, it is critical to check single-color fluorescent controls using the same imaging conditions (and preferably on the same day) as your multicolor controls to be certain no bleedthrough is occurring; it is _mandatory_ to do this if you are planning to measure [colocalization](content/colocalization).