# Save The Earth

Author: Tony Shum, Jing Wen, Aishwarya Nadimpally, Weilin Han

A data analysis group project for DSCI 522 (Data Science workflows); a
course in the Master of Data Science program at the University of
British Columbia.

## About

Here we attempt to build a prediction model using the k-nearest neighbours algorithm
which can use energy consumption and energy generation measurements to predict CO2
emission of certain country of next year. Our final prediction model perform pretty well
on unseen test dataset, with $R^2$ of 0.975 and an overall accuracy calculated to be 0.976.
However, the model predict CO2 emission by finding the existing cases in the training data set
which is most similiar to unseen data, thus, if there is a case in unseen data set of which
measurements are beyond the ranges in training data set (ie. massive increase of energy usage
or energy efficiency increase or new type of clean energy), then the prediciton might not be
accurate, thus we recomment continuing study to improve this prediction model.

The data set that was used in this project is from World Bank via GAPMINDER.ORG, which is
an independent Swedish foundation with no political, religious or economic affiliations and
the link can be found [here](https://www.gapminder.org/)).

## Report

The final report can be found
[here](https://github.com/UBC-MDS/DSCI_522_Group-11_Save-The-Earth/blob/main/src/save_the_earth_model.html).

## Dependencies
Our project uses Docker to manage the software dependencies required. Please find the Docker image used for this project based on `quay.io/jupyter/minimal-notebook:2023-11-19` image. 

The additional dependencies can be found in the [`Dockerfile`](Dockerfile)

## Usage

#### Setup

1. [Install](https://www.docker.com/get-started/)

2. Launch Docker on your local computer

3. Clone this GitHub repository down to your local computer.

#### Running the analysis

1. At the root of this project on your local computer, please use the
   command line tool (such as terminal) and enter the command below:

``` 
docker compose up
```

2. In the terminal, look for the URL that starts with 
`http://127.0.0.1:8888/lab?token=` and copy/paste the URL to your website browser and change the "8888" to "8889" to avoid potential conflict with your other running Jupyter notebook.

3. Open `src/breast_cancer_predict_report.ipynb` in Jupyter Lab launched on the website to run our analysis
and under the "Kernel" menu click "Restart Kernel and Run All Cells...".

## Tests

We have included tests and test data for functions used in our analysis in the tests folder. 
The test suite can be run via the code below: 

```
pytest tests/*
```

## License

The Save The Earth materials here are licensed under the
Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If
re-using/re-mixing please provide attribution and link to this webpage.

## References

<div id="refs" class="references hanging-indent">

<div id="ref-Dua2019">

Morice, C.P., J.J. Kennedy, N.A. Rayner, J.P. Winn, E. Hogan, R.E. Killick, R.J.H. Dunn, T.J. Osborn, P.D. Jones and I.R. Simpson (in press) An updated assessment of near-surface temperature change from 1850: the HadCRUT5 dataset. Journal of Geophysical Research (Atmospheres)

</div>

<div id="ref-Streetetal">

Hannah Ritchie, Max Roser and Pablo Rosado (2020) - "CO₂ and Greenhouse Gas Emissions". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/co2-and-greenhouse-gas-emissions'

</div>

</div>
