# wave-forecaster

Code for our modeling efforts can be found in the following two notebooks:
- mlp.ipynb
- reg-boost-lstm.ipynb

Code related to data preprocessing is located in the src folder.

We did some data exploration of our features in the data_exploration.ipynb. Unfortunately, we did not have room to include it within the 5 page limit, but it is available in this repository.

Lastly, raw data from the buoys can be found in our data folder. The text files were downloaded from [here](https://www.ndbc.noaa.gov/).

---

## Poster Session Updates

For the final poster, we used the extra time to run inference on the test sets for all four model types we experimented with. Here are the final results (which can also be found in the final poster linked below). For the MLP results, we inverted the normalized outputs so we were able to directly compares MSE values to the other models.

### Linear Regression

<img src="images/LR_test.png" alt="Example Image" width="300"/>

### XGBoost

<img src="images/XGB_test.png" alt="Example Image" width="300"/>

### Multi-layer perceptron

<img src="images/MLP_test.png" alt="Example Image" width="300"/>

### Long Short-Term Memory

<img src="images/LSTM_test.png" alt="Example Image" width="300"/>

In our project, we tackled the challenging task of predicting wave heights from time series data. Initially, Linear Regression seemed to outperform more advanced models, but this was a result of it replicating the test set's distribution, known as lagging in time series analysis. After experimenting with longer forecast leads, this became evident. The LSTM algorithm, despite not achieving the lowest mean squared errors, proved most effective by capturing long-term data patterns without the lagging behavior, a strength not found in simpler models like Linear Regression or XGBoost. This underscored the importance of evaluating prediction results and understanding model behavior in time series forecasting, particularly the limitations of simpler models and the advantages of more complex ones like LSTM.

Lastly, the project poster can be found [here](https://docs.google.com/presentation/d/1V_g--ssdOsm9H-OhZBR87X6y4vZb_E5mlUuJseP6grw/edit?usp=sharing).
