# Introduction

Microscopy images are inherently quantitative, which makes them a very powerful data source. As a biologist, image analysis allows you to translate these numbers into insights that answer biological questions. For our purposes, **image analysis** is the process of measuring aspects of biological phenomena captured in microscopy images. Microscopy images are already _inherently quantitative_ in that they are matrices (i.e., grids) of numbers. However, image analysis is the process of turning these raw numbers into biologically interpretable measurements. Image analysis typically involves a series of steps that can be collected into a pipeline or analysis workflow. A simple example workflow is shown below:

```{mermaid}

flowchart LR
   A[Raw image] -->|Illumination correction| B[Corrected image]
   B -->|Segmentation| C((Identified objects \n e.g., cells, nuclei))
   C -->|Measure size and shape| D(Size and shape measurements \n e.g., Average cell area)

   B & C-->|Measure intensity|G(Intensity measurements \n e.g., Average eGFP intensity)
  classDef empty width:0px,height:0px;

 style G fill:#DCC7FA, stroke:#8338EC

 style C fill:#FFF4d6,stroke:#FFBE0B

 style A fill:#FFD6E8,stroke:#F5006A
 style B fill:#FFD6E8,stroke:#F5006A

 style D fill:#D6E6FF,stroke:#3A86FF
 style G fill:#D6E6FF,stroke:#3A86FF
```

The specifics of your workflow depend on your biological question. Below we present a few common types of analysis for fluorescence microscopy experiments. For each, we’ll explain key ideas to understand before you begin, common pitfalls, and links to a few key resources to learn more. We encourage you to think about your analysis strategy even before beginning sample preparation. While not always possible, speaking with an image analysis expert in your local core facility or asking a question on the [image.sc](https://image.sc) forum _before you begin_ can save you a ton of time and headache when it comes to designing an image analysis strategy.
