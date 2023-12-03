# Save The Earth

  - Author: Tony Shum, Jing Wen, Aishwarya Nadimpally, Weilin Han

A data analysis group project for DSCI 522 (Data Science workflows); a
course in the Master of Data Science program at the University of
British Columbia.

## About

Here we attempt to build a prediction model using the k-nearest
neighbours algorithm which can use energy consumption and energy
generation measurements to predict CO2 emission of certain country of
next year. Our final prediction model perform pretty well on unseen test
dataset, with $R^2$ of 0.975 and an overall accuracy calculated to be
0.976. However, the model predict CO2 emission by finding the existing
cases in the training data set which is most similiar to unseen data,
thus, if there is a case in unseen data set of which measurements are
beyond the ranges in training data set (ie. massive increase of energy
usage or energy efficiency increase or new type of clean energy), then
the prediciton might not be accurate, thus we recomment continuing study
to improve this prediction model.

The data set that was used in this project is from World Bank via
GAPMINDER.ORG, which is an independent Swedish foundation with no
political, religious or economic affiliations and the link can be found
[here](https://www.gapminder.org/)).

## Report

The final report can be found
[here](https://ubc-mds.github.io/DSCI_522_Group-11_Save-The-Earth/save_the_earth_model.html).

## Dependencies

Our project uses Docker to manage the software dependencies required.
Please find the Docker image used for this project based on
`quay.io/jupyter/minimal-notebook:2023-11-19` image.

The additional dependencies can be found in the
[`Dockerfile`](Dockerfile)

## Usage

#### Setup

1.  [Install](https://www.docker.com/get-started/)

2.  Launch Docker on your local computer

3.  Clone this GitHub repository down to your local computer.

#### Running the analysis

1.  At the root of this project on your local computer, please use the
    command line tool (such as terminal) and enter the command below:

```         
docker compose up jupyter-lab
```

2.  In the terminal, look for the URL that starts with
    `http://127.0.0.1:8888/lab?token=` and copy/paste the URL to your
    website browser and change the "8888" to "8889" to avoid potential
    conflict with your other running Jupyter notebook.

3.  To run the analysis,
enter the following commands in the terminal in the project root:

```
# extract and clean data
python scripts/data_fetch_clean.py \
    --write-to=Data/Processed

# split data into train and test sets
python scripts/split.py \
    --raw_data=Data/Processed/save_the_earth_processed_data.csv \
    --data_to=Data/Processed

# perform eda and save plots
python scripts/eda.py \
    --train_df=Data/Processed/train_df.csv \
    --plot_to=results/figures

# Perform preprocessor and estimator training
python scripts/preprocessor_and_estimator.py \
    --training_data=Data/Processed/train_df.csv \
    --pipeline_to=results/models \
    --results_to=results/tables \
    --seed=522

# Perform Evaluate scripts and results
python scripts/evaluate-save-on-earth.py \
    --train_data=Data/Processed/train_df.csv \
    --test_data=Data/Processed/test_df.csv \
    --pipeline_from=results/models/co2_pipeline.pickle \
    --results_to=results \
    --seed=123

# build HTML report and copy build to docs folder
jupyter-book build report
cp -r report/_build/html/* docs
```

#### Clean up

1.  `Cntrl` + `C` in the terminal to shut down the container, then
    `docker compose rm` to clean up the resources

## Developer notes

#### Adding a new dependency

1.  To modify the `Dockerfile` and add the dependency to the
    `Dockerfile` file, please create a new branch.

2.  After updating the `Dockerfile`, proceed to build the Docker image
    locally.This step ensures that the Docker image is properly
    constructed and operates as expected.

3.  Upon successfully local building and testing of the Docker image,
    push the changes to GitHub. This action triggers an automatic build
    and push of a new Docker image to Docker Hub. The new image will
    carry a tag that corresponds to the SHA of that commit that
    instigated the change in the DOckerfile.

4.  Update the `docker-compose.yml` file on your branch with the new
    container image.

5.  After all the above steps are completed, please send a pull request
    to merge the changes into the `main` branch.

#### Tests

We have included tests and test data for functions used in our analysis
in the tests folder. The test suite can be run at the root of the
project via the code below:

```         
pytest tests/*
```

## License

The Save The Earth materials here are licensed under the Creative
Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If
re-using/re-mixing please provide attribution and link to this webpage.

## References

<div id="refs" class="references hanging-indent">

<div>
M Allen, OP Dube, W Solecki, F Aragón-Durand, W Cramer, S Humphreys, M Kainuma, and others. Special report: global warming of 1.5 c. Intergovernmental Panel on Climate Change (IPCC), 2018.
</div>

<div>
Ekaba Bisong and Ekaba Bisong. Matplotlib and seaborn. Building Machine Learning and Deep Learning Models on Google Cloud Platform: A Comprehensive Guide for Beginners, pages 151–165, 2019.
</div>

<div>
IEA Global Energy. Co2 status report 2017. international energy agency. 2017c. 2018.
</div>

<div>
Wes McKinney. Data structures for statistical computing in python. In Stéfan van der Walt and Jarrod Millman, editors, Proceedings of the 9th Python in Science Conference, =51 – 56. 2010.
</div>

<div>
Rajendra K Pachauri, Myles R Allen, Vicente R Barros, John Broome, Wolfgang Cramer, Renate Christ, John A Church, Leon Clarke, Qin Dahe, Purnamita Dasgupta, and others. Climate change 2014: synthesis report. Contribution of Working Groups I, II and III to the fifth assessment report of the Intergovernmental Panel on Climate Change. Ipcc, 2014.
</div>

<div>
F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12:2825–2830, 2011.
</div>

<div>
Guido Van Rossum and Fred L. Drake. Python 3 Reference Manual. CreateSpace, Scotts Valley, CA, 2009. ISBN 1441412697.
</div>

<div>
Jake VanderPlas. Altair: interactive statistical visualizations for python. Journal of open source software, 3(7825):1057, 2018. URL:
'<https://joss.theoj.org/papers/10.21105/joss.01057>'
</div>

</div>
