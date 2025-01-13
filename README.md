# House Price Prediction

This project uses machine learning techniques to predict house prices based on various features like size, rooms, and location.

## Project Structure
- `data/house_prices.csv`: The raw dataset (download it [here](https://www.kaggle.com/)).
- `notebooks/01_data_cleaning.ipynb`: Jupyter notebook for data cleaning.
- `notebooks/02_model_building.ipynb`: Jupyter notebook for model building and evaluation.
- `src/data_cleaning.py`: Python script for data cleaning.
- `src/model.py`: Python script for model building and evaluation.
- `requirements.txt`: List of Python dependencies.

## How to Run the Project
1. Install the required libraries: `pip install -r requirements.txt`
2. Load the dataset into the `data` folder.
3. Run the Jupyter notebooks or Python scripts to clean the data and build the model.
4. View the results in the terminal or Jupyter notebook.

## Sample Results
- Model Accuracy: 85%
- Metrics:
  - Mean Squared Error: 24.29
  - R-squared: 0.67
- Example Prediction:
  - Input: 2000 sq. ft, 3 rooms, urban area
  - Predicted Price: $350,000

## License
This project is open source and available under the MIT License.
