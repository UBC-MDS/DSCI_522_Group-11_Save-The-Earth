# Save The Earth

  - Author: Tony Shum, Jing Wen, Aishwarya Nadimpally, Weilin Han

A data analysis group project for DSCI 522 (Data Science workflows); a
course in the Master of Data Science program at the University of
British Columbia.

## About

Here we attempt to build a prediction model employing the k-nearest neighbours algorithm, designed to leverage energy consumption and energy generation measurements to predict CO2 emissions of a country. Understanding the correlation between consumption of various energy types and CO2 emission is critical for formulating policies aimed at reducing emissions and mitigating climate change impacts [Allen et al., 2018]. Our model’s performance on the unseen test dataset is quite commendable, as reflected by an $R^2$ of 0.97.

However, the model’s effectiveness lies in its ability to identify instances in the training dataset that closely resemble the data it is trying to predict. This means that when it encounters scenarios not represented in its training data, such as substantial shifts in energy usage or the introduction of new types of clean energy, its predictions may not be as accurate. Consequently, to tackle these potential limitations, it is advisable to continue research efforts to further enhance the model’s predictive capabilities.

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
