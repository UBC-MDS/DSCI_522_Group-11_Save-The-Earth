all : report/_build/html/index.html
# extract and clean data
data/processed/save_the_earth_processed_data.csv : scripts/data_fetch_clean.py
	python scripts/data_fetch_clean.py \
    --write-to=data/processed
#split data into train and test
data/processed/train_df.csv : scripts/split.py data/processed/save_the_earth_processed_data.csv
	python scripts/split.py \
    --raw_data=data/processed/save_the_earth_processed_data.csv \
    --data_to=data/processed
data/processed/test_df.csv : scripts/split.py data/processed/save_the_earth_processed_data.csv
	python scripts/split.py \
    --raw_data=data/processed/save_the_earth_processed_data.csv \
    --data_to=data/processed
# EDA on train data
results/figures/histogram_by_country.png : scripts/eda.py data/processed/train_df.csv
	python scripts/eda.py \
    --train_df=data/processed/train_df.csv \
    --plot_to=results/figures
results/figures/histogram_by_numeric_cols.png : scripts/eda.py data/processed/train_df.csv
	python scripts/eda.py \
    --train_df=data/processed/train_df.csv \
    --plot_to=results/figures
# preprocessor and estimator training
results/models/co2_pipeline.pickle : scripts/preprocessor_and_estimator.py data/processed/train_df.csv
	python scripts/preprocessor_and_estimator.py \
    --training_data=data/processed/train_df.csv \
    --pipeline_to=results/models \
    --results_to=results/tables \
    --seed=522
results/tables/hyperparameter_tuning_scores.csv : scripts/preprocessor_and_estimator.py data/processed/train_df.csv
	python scripts/preprocessor_and_estimator.py \
    --training_data=data/processed/train_df.csv \
    --pipeline_to=results/models \
    --results_to=results/tables \
    --seed=522
results/tables/model_selection_scores.csv : scripts/preprocessor_and_estimator.py data/processed/train_df.csv
	python scripts/preprocessor_and_estimator.py \
    --training_data=data/processed/train_df.csv \
    --pipeline_to=results/models \
    --results_to=results/tables \
    --seed=522
# evaluate the model and test results
results/tables/model_predictions.csv : scripts/evaluate-save-on-earth.py data/processed/train_df.csv \
data/processed/test_df.csv results/models/co2_pipeline.pickle
	python scripts/evaluate-save-on-earth.py \
    --train_data=data/processed/train_df.csv \
    --test_data=data/processed/test_df.csv \
    --pipeline_from=results/models/co2_pipeline.pickle \
    --results_to=results \
    --seed=123
results/tables/model_scores.csv : scripts/evaluate-save-on-earth.py data/processed/train_df.csv \
data/processed/test_df.csv results/models/co2_pipeline.pickle
	python scripts/evaluate-save-on-earth.py \
    --train_data=data/processed/train_df.csv \
    --test_data=data/processed/test_df.csv \
    --pipeline_from=results/models/co2_pipeline.pickle \
    --results_to=results \
    --seed=123
results/figures/scatter_plot.png : scripts/evaluate-save-on-earth.py data/processed/train_df.csv \
data/processed/test_df.csv results/models/co2_pipeline.pickle
	python scripts/evaluate-save-on-earth.py \
    --train_data=data/processed/train_df.csv \
    --test_data=data/processed/test_df.csv \
    --pipeline_from=results/models/co2_pipeline.pickle \
    --results_to=results \
    --seed=123

# buidling jupyter book
report/_build/html/index.html : report/save_the_earth_model.ipynb \
report/_toc.yml \
report/_config.yml \
results/figures/histogram_by_country.png \
results/figures/histogram_by_numeric_cols.png \
results/figures/scatter_plot.png
	jupyter-book build report


clean:
	rm -f results/figures/histogram_by_country.png
	rm -f results/figures/histogram_by_numeric_cols.png
	rm -f results/figures/scatter_plot.png
	rm -f results/tables/hyperparameter_tuning_scores.csv
	rm -f results/tables/model_predictions.csv
	rm -f results/tables/model_scores.csv
	rm -f results/tables/model_selection_scores.csv
	rm -f results/models/co2_pipeline.pickle
	rm -f data/processed/save_the_earth_processed_data.csv
	rm -f data/processed/train_df.csv
	rm -f data/processed/test_df.csv
	rm -rf report/_build