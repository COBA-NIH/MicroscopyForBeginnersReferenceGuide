# Common pitfalls

In addition to the mistakes we summarize for common image analysis tasks, here we present a general list of common mistakes for beginners to image analysis. For each, we explain why this is a problem and make suggestions for how to avoid these issues.

1. Changing your image bit depth

   Let's say you've opened your image in {term}`Fiji` and you want to process it in some way (e.g., maximum intensity projection, splitting channels, etc.) before saving it out to measure somewhere else. You go to `Image` > `Type` > `RGB (Color)` since you want a color image to import into your next analysis software and then save the resulting image. What's the problem with this? By making this change, even if the image looks exactly the same to your eyes, you've actually inadvertently changed the intensity values quite a bit! Let's take a look at an example. In Fiji there are several built-in example images. Let's open neuron.tif (you can follow along by going to `File` > `Open Samples...` > `Neuron (5 channels)`. 
   
   Here's how the image opens. There are 5 channels, but let's just look at the first one:
   ![image](https://user-images.githubusercontent.com/28116530/206793825-364998d4-6043-4b1d-8438-0a5b37b97232.png)

   
<!-- 
Commented out text not shown on the page

 -->