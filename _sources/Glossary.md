# Glossary

````{div} full-width
```{glossary}

Fiji
  [Fiji](https://imagej.net/software/fiji/) Is Just ImageJ. ImageJ2 plus a lot of common plugins.

Image processing
  Is an operation that can be performed on an image, the result benign another image. There are simple image processing operations, like resizing or rotating an image. And other more advanced like enhancing particular features of an image like circles or lines.

ROIs
  Regions Of Interest. Pixels in your image that you care about (e.g., a region in tissue, a cell, a tumor, etc.) 

Segmentation
  Method of dividing an image into multiple parts or regions. There are three different types of segmentation. 
    - Semantic segmentation, were all parts of an image are part of a class, common in cell biology will be detecting cells and background on an image.
    - Instance segmentation, the segmentation is object based, not just detecting were the cells are but diving each cell as a separate object.
    - Panoptic Segmentation,  it can be defined as a combination of the prior two, because it identifies the object but also cassifies them. An example in biology might be detecting all the cells on an image and classifying them as dividing vs not.

```
````

<!-- 
Terms that aren't in the book yet but we know we want to add:
Detection
  Is the image processing technique to detect objects within an image. It would not give you a mask of the objects but it could give you a bounding box, or and x,y position.

Thresholding
  The easiest form of image segmentation, it divides the image into two part the background and the foreground (or signal). It creates a binary image were usually the background pixels would be change to a 0 value and the foreground pixels values would be 1.

  -->