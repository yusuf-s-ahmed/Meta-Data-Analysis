#  Marketing Campaign Optimisation Data Science Analysis on Meta’s Advert Dataset

As part of Meta and Digdata's ‘Step Up Career Challenge’, I analysed 78,085 UK-targeted ads from 859 digital campaigns to uncover high-performing marketing strategies for a global sportswear brand. The goal was to evaluate ad effectiveness across customer segments, media formats, and platform placements.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Implementation Details](#implementation-details)
- [Key Insights](#key-insights)
- [Challenges and Solutions](#challenges-and-solutions)
- [Impact](#impact)

## Overview

This project was completed as part of a national data challenge hosted by Meta and Digdata. The brief was to analyse large-scale advertising campaign data to identify trends, evaluate performance, and deliver data-backed marketing recommendations.

After cleaning and validating the dataset, I reduced the sample to 364 high-confidence campaigns. I applied A/B testing techniques in Python and R to analyse how different variables, like interactivity, ad format, and customer targeting—impacted campaign success.

## Features

- Cleaned and processed a dataset of 78,085 ads across 859 UK-based campaigns.
- Applied A/B testing to compare ad performance across variables like interactivity, format, and placement.
- Defined campaign “success” as achieving at least five high-performing ads.
- Conducted audience segment analysis to identify high-engagement customer profiles.
- Visualised insights using Python and R libraries and designed the presentation deck in Figma and PowerPoint.

## Technology Stack

| Component            | Tools and Libraries                       |
|---------------------|--------------------------------------------|
| Data Cleaning        | Python (pandas, NumPy), Excel              |
| Statistical Testing  | Python, R (A/B testing, t-tests)           |
| Visualisation        | matplotlib, seaborn, ggplot2, Figma        |
| Presentation         | PowerPoint                                |
| Version Control      | GitHub                                     |

## Implementation Details

- Data Cleaning: Removed duplicates and incomplete entries, reducing the dataset from 859 campaigns to 364 usable ones.
- Segmentation & Testing: Segmented ads by format, customer segment, and platform placement, applying statistical comparison methods to assess performance.
- A/B Testing Logic: Used Python and R to evaluate how ad interactivity and placement strategies affected outcome metrics.
- Visualisation: Built comparison plots in matplotlib, seaborn, and ggplot2, and embedded them into a Figma-designed PowerPoint deck.
- Presentation: Highlighted key findings and recommendations in a deliverable designed to support executive marketing decisions.

## Key Insights

| Metric/Variable                  | Insight                                                       |
|----------------------------------|----------------------------------------------------------------|
| Interactive Video Ads            | 100% success rate across 42 ads                               |
| Interactivity vs. Static         | Performed nearly 50% better                                   |
| Auto vs. Manual Placement        | Manual placements outperformed auto by 8.43%                  |
| Customer Segment Optimisation    | Improved performance by 19.47%                                |

## Challenges and Solutions

| Challenge                         | Solution                                                       |
|----------------------------------|----------------------------------------------------------------|
| High data volume and redundancy  | Developed filtering scripts to reduce noise and drop duplicates |
| Varying metric definitions       | Standardised “success” threshold across segments               |
| Cross-tool visualisation         | Aligned Python (matplotlib/seaborn) with R (ggplot2) outputs   |
| Communication clarity            | Summarised insights visually in Figma-based slide deck         |

## Impact

This project taught me how to combine large-scale data analysis with A/B testing and visual storytelling to derive actionable insights for digital strategy. It enhanced my ability to work with mixed toolchains (Python, R, Excel), communicate findings through visual design, and use data to support marketing decisions.

