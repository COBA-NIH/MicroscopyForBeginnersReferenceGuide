# Object tracking

## What is tracking?
Tracking, or _object tracking_, refers to the ability to estimate the location of objects in motion from one frame of video to the next. Practically, object tracking in microscopy involves identifying your objects in each frame of your video, then relating objects from frame to frame to be able to identify the same cell as it moves in space.

<br>

```{dropdown} 📏 How do I measure it?

There are several options for tracking objects, like the [TrackMate](https://imagej.net/plugins/trackmate/) {cite}`Tinevez2017-fb` plugin in Fiji, but tracking is somewhat more complex to setup than the previous analyses. In addition to just identifying objects in the movie/time series, tracking also allows you to identify splitting (e.g. mitosis) and merging events. There are many measurements that come out of tracking, including spatial measures like where the objects move to, speed measurements, distance traveled (length of track), and rate of splitting events (e.g., mitotic events) and merging events.

```

````{dropdown} <span style="color: red">⚠️</span> Where can things go wrong?
* **Poor {term}`segmentation`** If objects are dropping out from frame to frame, this makes it more difficult to track them over time. Accurate {term}`segmentation` is the foundation of good tracking results. This can become more difficult if your objects are also changing in shape or intensity (due to things such as bleaching) over the course of the video. It’s important to find a {term}`segmentation` strategy that can work well across your frames.
* **Inadequate frame rate** If objects are highly dynamic but the images were not taken at a high frequency, tracking can be difficult because objects might have moved too much for the algorithm to relate them from one frame to the next. It is important to match the image acquisition frequency to how dynamic your cells or objects are.

````

```{dropdown} 📚🤷‍♀️ Where can I learn more?

* 📄 [Computerized Cell Tracking](https://www.sciencedirect.com/science/article/pii/S2468502X20300711)
* 🌐 [TrackMate Manual](https://imagej.net/media/plugins/trackmate/trackmate-manual.pdf)
```
