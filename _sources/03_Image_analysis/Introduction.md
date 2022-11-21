# Image Analysis

## Introduction

Microscopy images are inherently quantitative, which makes them a very powerful data source. As a biologist, image analysis allows you to translate these numbers into insights that answer biological questions. For our purposes, **image analysis** is the process of measuring aspects of biological phenomena captured in microscopy images. Microscopy images are already _inherently quantitative_ in that they are matrices (i.e., grids) of numbers. However, image analysis is the process of turning these raw numbers into biologically interpretable measurements. Image analysis typically involves a series of steps that can be collected into a pipeline or analysis workflow. A simple example workflow is shown below: 

```{mermaid}
flowchart LR
   A[Raw image] -->|Illumination correction| B[Corrected image]
   B -->|Segmentation| C((Identified objects \n e.g., cells, nuclei))
   C -->|Measure morphology| D(Shape measurements \n e.g., Average cell area)

   B & C-->|Measure intensity|G(Intensity measurements \n e.g., Average eGFP intensity)
  classDef empty width:0px,height:0px;

 style G fill:#DCC7FA, stroke:#8338EC

 style C fill:#FFF4d6,stroke:#FFBE0B

 style A fill:#FFD6E8,stroke:#F5006A
 style B fill:#FFD6E8,stroke:#F5006A

 style D fill:#D6E6FF,stroke:#3A86FF
 style G fill:#D6E6FF,stroke:#3A86FF
```
