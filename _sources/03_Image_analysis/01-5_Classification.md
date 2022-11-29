# Object classification

## What is classification?
Simply put, phenotypic classification is about categorizing objects into different groups based on their features (aka measurements).

<br>

```{dropdown} 📏 How do I measure it?

Phenotypic classification can be performed a few different ways. One way to break this down is by unsupervised vs. supervised classification. In **unsupervised classification**, you group objects based on their measurements, but without any top-down human-defined guidance to what the groups should look like.

* For a simple example, you could classify cells into two groups based on expression levels of a particular protein tagged with a fluorophore. You could observe the distribution of mean intensities in the channel where you can see the tagged fluorophore and decide a cutoff (manually or using an algorithm).

* For a more complicated example, you could measure hundreds or thousands of features of cells from many treatments, as is typical in large-scale cell profiling experiments. Next you could try to cluster the cells into different groups based on having similar measurements. This is a form of unsupervised clustering, where you observe what groups emerge from a computer considering their measurements only, and not class labels we impose as researchers.

In **supervised classification**, in addition to object measurements, a human also provides information on what the different groups of objects should look like by providing representative examples of each group in a training dataset. The computer then learns how to assign objects to groups based on their measurements by testing models against the ground truth training dataset.

* For example, you could classify cells based on a visual phenotype and train a machine learning classifier to derive which measurement ranges are associated with different classes. This is called supervised classification because a person is providing examples of labels for the computer to learn from. An example of this could be annotating cells that are in different stages of mitosis and training a classifier to use your labels on a subset of data to find other cells in those stages.

```

```{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
* **Valid measurements are still important** Classification can be simple or complex, but results always depend on the validity of your measurements. For this reason, all the caveats of earlier measurement sections also apply here.
* **Machines are dumb** Machine learning classifiers aren’t necessarily going to learn the biologically relevant features that distinguish objects from distinct groups. Confounding features, or features that vary with your phenotype but are not biologically related to it, can limit the usefulness of your classifier and lead to incorrect conclusions. For instance, if clinicians often put rulers next to malignant looking moles and not next to benign moles and try to train a machine learning classifier to distinguish malignant vs. benign, the model might learn to classify images with rulers as malignant without tapping into any of the relevant features of the moles. This is a [real example](https://www.sciencedirect.com/science/article/pii/S0022202X18322930). If possible, examining which features your model is relying on to classify objects can be a way to check for this. It’s also important to standardize how you capture images of your different classes of objects and include a large enough training set with images with lots of variation. You wouldn’t want all your positive cells to come from one image and all your negative to come from another image, for example.
* **Violating model assumptions** If using a machine learning classifier, different models come with different baked-in assumptions. If you’re starting out, it can be difficult to know which to pick. There are interactive tools such as [CellProfiler Analyst](https://academic.oup.com/bioinformatics/article/32/20/3210/2196630?login=false) and [Piximi](https://www.piximi.app/) that make training a classifier easier, especially if you don’t know how to code.  


```

```{dropdown} 📚🤷‍♀️ Where can I learn more?

* 📄 [Data-analysis strategies for image-based cell profiling](https://www.nature.com/articles/nmeth.4397)
* 📄 [Scoring diverse cellular morphologies in image-based screens with iterative feedback and machine learning](https://www.pnas.org/doi/10.1073/pnas.0808843106)
* 🎥 [iBiology video series: Measurement and Phenotype Classification](https://www.youtube.com/watch?v=Odi9pIerT7I)
```
