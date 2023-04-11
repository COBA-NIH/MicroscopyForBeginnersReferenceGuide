# Statistics

## Introduction

Quantitative data is often summarized and analysed with statistical methods and visualized with plots/graphs/diagrams. Statistical methods reveal quantitative trends, patterns, and outliers in data, while plots and graphs help to convey them to audiences. Carrying out a suitable statistical analysis and choosing a suitable chart type for your data, identifying their potential pitfalls, and faithfully realising the analysis or generating the chart with suitable softwares are essential to back up experimental conclusions with data and reach communication goals. 

## Dimensionality reduction

### What is it?
Dimensionality reduction (also called dimension reduction) aims at mapping high-dimensional data onto a lower dimensional space in order to better reveal trends and patterns. Algorithms performing this task attempt to retain as much information as possible when reducing the dimensionality of the data: this is achieved by assigning importance scores to individual features, removing redundancies, and identifying uninformative (for instance constant) features. Dimensionality reduction is an important step in quantitative analysis as it makes data more manageable and easier to visualize. It is also an important preprocessing step in many downstream analysis algorithms, such as machine learning classifiers. 

```{dropdown} 📏 How do I do it?
The most traditional dimensionality reduction techniques is principal component analysis (PCA). In a nutshell, PCA recovers a linear transformation of the input data into a new coordinate system (the principal components) that concentrates variation into its first axes. This is achieved relying on classical linear algebra, by computing an eigendecomposition of the covariance matrix of the data. As a result, the first 2 or 3 principal components provide a low-dimensional version of the data distribution that is faithful to the variance that was originally present.
More advanced dimensionality reduction methods that are popular in biology include t-distributed stochastic neighbor embedding (t-SNE) and Uniform Manifold Approximation and Projection (UMAP). In contrast to PCA, these methods are non-linear and can therefore exploit more complex relationships between features when building the lower-dimensional representation. This however comes at a cost: both t-SNE and UMAP are stochastic, meaning that the results they produce are highly dependent on the choice of hyperparameters and can differ across different runs. 
<!-- 
Commented out text not shown on the page
A figure or a link would be nice here - the wikipedia article actually looks decent for PCA, and/or something like https://www.nature.com/articles/nmeth.4346
 -->

```

```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
Although reducing dimensionality can be very useful for data exploration and analysis, it may also wipe information or structure that is relevant to the problem being studied. The best way to minimize this risk is to carefully check any underlying assumptions of the method being used, and ensure that they hold for the considered data. Dimensionality reduction may also enhance and reveal patterns that are not biologically relevant, due to noise or systematic artifacts in the original data (see Batch effect correction section below). In addition to applying normalization and batch correction to the data prior to reducing dimensionality, some dimensionality reduction methods also offer so-called regularization strategies to mitigate this. In the end, any pattern identified in dimension-reduced data should be considered while keeping in mind the biological context of the data in order to interpret the results appropriately.
<!-- 
Think about linking out to the Datasaurus Dozen https://www.google.com/url?q=https://www.autodesk.com/research/publications/same-stats-different-graphs%23:~:text%3Dtwo%2520decimal%2520places.-,The%2520Datasaurus%2520Dozen,a%2520picture%2520of%2520a%2520dinosaur&sa=D&source=docs&ust=1680784194149724&usg=AOvVaw2FG9hwMQj-nqenfsISv1Q8
 -->
```

```{dropdown} 📚🤷‍♀️ Where can I learn more?
* 📖 [Dimension Reduction: A Guided Tour](https://www.researchgate.net/publication/220416606_Dimension_Reduction_A_Guided_Tour) {cite}`Burges2010-fi`
* 💻 [UMAP introduction and Python implementation](https://umap-learn.readthedocs.io/en/latest/index.html) 
* 💻 [t-SNE Python implementation](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

```

## Batch correction

### What is it?
Batch effects are systematic variations across samples correlated with experimental conditions (such as different time of the day, different days of the week, or different experimental tools) and that are not related to the biological process of interest. Batch effects must be mitigated prior to making comparisons across several datasets as they impact the reproducibility and reliability of computational analysis and can dramatically bias conclusions. Algorithms for batch effect correction address this by identifying and quantifying sources of technical variation, and adjusting the data so that these are minimized while biological signal is preserved. Most batch effect correction methods were originally developed for microarray data and sequencing data, but can be adapted to feature vectors extracted from images.

```{dropdown} 📏 How do I do it?
Two of the most used methods for batch effect correction are ComBat and Surrogate Variable Analysis (SVA), depending on whether the sources of batch effects is known a priori or not. In a nutshell, ComBat involves three steps: 1) dividing the data into known batches, 2) estimating batch effect by fitting a linear model that includes the batch as a covariatem and 3) adjusting the data by removing the estimated effect of the batch from each data point. In contrast, SVA aims at identifying "surrogate variables" that capture unknown sources of variability in the data. The surrogate variables can be estimated relying on linear algebra methods (such as singular value decomposition) or through a Bayesian factor analysis model. SVA has been demonstrated to reduce unobserved sources of variability and is therefore of particular help when identifying possible causes of batch effects is challenging, but comes at a higher computational cost than ComBat.
```
```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
As important as it is for analysis, batch effect correction can go wrong when too much or too little of it is done. Both over- and under-correction can happen when methods are not used properly or when their underlying assumptions are not met. As a result, either biological signal can be removed (in the case of over-correction) or irrelevant sources of variation can remain (in the case of under-correction) - both potentially leading to inaccurate conclusions. Batch effect correction can be particularly tricky when the biological variation of interest is suspected to confound with the batch. In this cases in particular (although always a good approach), the first line of fight against batch effects should be thought-through experimental design and careful quality control.
<!--
Worth adding here that, as with above, plotting the data batch-by-batch to look for trends to make sure they're similar across batches (ideally, before correction)? This is what the "Superplots" reference that I added to the main paper does - we need not use that reference, but just saying "look at your data" is never a bad thing to emphasize to non-computational folk. 
One major thing that would be nice to clarify in this particular case - how do you know when it is appropriate to use batch correction, and/or how can you tell when you've "over" or "under" corrected? That seems critical to using batch correction appropriately.
-->
```
```{dropdown} 📚🤷‍♀️ Where can I learn more?
* 📄 [Why Batch Effects Matter in Omics Data, and How to Avoid Them](https://doi.org/10.1016/j.tibtech.2017.02.012) {cite}`Goh2017-kd`
* 💻 [pyComBat (ComBat Python implementation)](https://epigenelabs.github.io/pyComBat/)
* 📄 [The sva package for removing batch effects and other unwanted variation in high-throughput experiments](https://doi.org/10.1093/bioinformatics/bts034) {cite}`Leek2012-rv`

```

## Normality testing

### What is it?
Normality testing is about assessing whether data follow a Gaussian (or nomal) distribution. Because the Gaussian distribution is frequently found in nature and has important mathematical properties, normality is a core assumption in many widely-used statistical tests. When this assumption is violated, their conclusions may not hold or be flawed. Normality testing is therefore an important step of the data analysis pipeline prior to any sort of statistical testing. 

```{dropdown} 📏 How do I do it?
Normality of a data distribution can be qualitatively assessed through plotting, for instance relying on a histogram. For a more quantitative readout, statistical methods such as the Kolmogorov-Smirnov (KS) and Shapiro-Wilk tests (among many others) report how much the observed data distribution deviates from a Gaussian. These tests usually return and a p-value linked to the hypothesis that the data are sampled from a Gaussian distribution. A high p-value indicates that the data are not inconsistent with a normal distribution, but is not sufficient to prove that they indeed follow a Gaussian.
A p-values smaller than a pre-defined significance threshold (usually 0.05) indicates that the data are not sampled from a normal distribution.
```
```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
Although lots of the “standard” statistical methods have been designed with a normnality assumption, alternative approaches exist for non-normally-ditributed data. Many biological processes result in multimodal “states” (for instance differentiation) that are inherently not Gaussian. Normality testing should therefore not be mistaken for a quality assessment of the data: it merely informs on the types of tools that are appropriate to use when analyzing them.
```
```{dropdown} 📚🤷‍♀️ Where can I learn more?
* 📖 [Modern statistics for modern biology](https://www.huber.embl.de/msmb/) {cite}`Holmes2019-no`
* 💻 [To get started with statistical analysis: R](https://www.r-project.org/)
* 💻 [To do statistics in Python: scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)

```
<!-- 
Commented out text not shown on the page

 -->