# Save The Earth

  - author: Tony Shum, Jing Wen, Aishwarya Nadimpally, Weilin Han

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
the link can be found [here](www.gapminder.org)).

## Report

The final report can be found
[here](https://github.com/UBC-MDS/DSCI_522_Group-11_Save-The-Earth/blob/main/src/save_the_earth_model.html).

## Dependencies

  - Python 3.11.* and Python packages:
    - ipykernel
    - nb_conda_kernels
    - altair=5.1.2
    - vl-convert-python  # For saving altair charts as static images
    - vegafusion  # For working with charts > 5,000 graphical objects
    - vegafusion-python-embed  # Same as the previous one
    - vegafusion-jupyter  # For working with charts > 100,000 graphical objects
    - vega_datasets  # Altair example data
    - scipy
    - matplotlib>=3.2.2
    - scikit-learn>=1.3.1
    - requests>=2.24.0
    - graphviz
    - python-graphviz
    - eli5
    - shap
    - jinja2
    - selenium<4.3.0
    - lightgbm
    - pip:
        - joblib==1.1.0
        - mglearn
        - psutil>=5.7.2

## License

The Save The Earth materials here are licensed under the
Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If
re-using/re-mixing please provide attribution and link to this webpage.
