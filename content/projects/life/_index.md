---
title: Life Metrics
---

# Life Metrics Project

## Overview
Miscellaneous life data analysis.

<!-- TODO: Python processing -->

## Analysis Notebook
[Open Jupyter Notebook](https://github.com/asifimranaziz/personal-site-2026/blob/main/notebooks/life_analysis.ipynb)

## Visualization
<div id="life-chart" aria-label="Life metrics pie chart"></div>

<script src="https://cdn.plotly/plotly-latest.min.js"></script>
<script>
var data = [{
  values: [30, 20, 50],
  labels: ['Work', 'Leisure', 'Sleep'],
  type: 'pie'
}];
var layout = {title: 'Dummy Life Balance'};
Plotly.newPlot('life-chart', data, layout);
</script>

## AI-Assisted Insights
Balance is skewed towards sleep. Action: Increase leisure activities.

<!-- TODO: AI summaries -->