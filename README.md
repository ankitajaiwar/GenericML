End to End Generic ML Project
# Student Performance Evaluation

## Introduction

This project aims to predict the performance of students using regression analysis. The dataset contains information about high school students in the United States with various attributes such as gender, race, type of lunch, parental level of education, preparation for test etc.

The target variable to predict is:

- **match_Score**: Score of the student in mathematics

Dataset Source Link: [Students Performance in Exams]( https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)


### Deployment and Resources

- **AWS Deployment Link**: [AWS Elastic Beanstalk Link](http://gemstonepriceutkarshgaikwad-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/)
- **API Link**: [API Endpoint](http://gemstonepriceutkarshgaikwad-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/predictAPI)

## Approach

### Data Processing

1. **Data Ingestion**: Read data from CSV and split into training and testing sets.
2. **Data Transformation**: Perform preprocessing using a Pipeline. For numerical variables, apply SimpleImputer with median strategy and Standard Scaling. For categorical variables, use SimpleImputer with most frequent strategy, ordinal encoding, and Standard Scaling. Save the preprocessor as a pickle file.
3. **Model Training**: Test base models, tune hyperparameters. Save the final model as a pickle file.

### Prediction Pipeline

Create a pipeline to convert input data into a DataFrame and use the trained model to predict student's performance.

### Flask App

Develop a Flask web application with a user interface to predict diamond prices.

### Additional Resources

- [Exploratory Data Analysis Notebook]((https://github.com/ankitajaiwar/GenericML/blob/main/src/notebook/EDA.ipynb)): Link to notebook for exploratory data analysis.
- [Model Training Approach Notebook]((https://github.com/ankitajaiwar/GenericML/blob/main/src/notebook/MODEL%20TRAINING.ipynb)): Link to notebook detailing model training process.

## Repository Structure
- **src/**: Contains source code for the project.
- **app/**: Contains Flask application files.
- **data/**: Stores dataset files.
- **artifacts/**: Saves pickle files for processing pipeline and trained model.
- **notebooks/**: Contains Jupyter notebooks for EDA, model training, and interpretation.
- **templates/**: Contains HTML templates for the Flask app.

## Usage

To run the Flask application locally:

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Navigate to the `app` directory and run `python app.py`.
4. Access the application via the provided URL.

## Docker Usage

To run the application through docker image:

1. Download the docker image from [Docker Image](https://hub.docker.com/repository/docker/ankitajaiwar/genericmlapp)
2. Run the docker image using `docker run <imagename>`
3. Specify the container port 5000 is required

## Worflows
**aws.yml"**
GitHub Actions Workflow YAML file for pushing Docker images to Amazon Elastic Container Registry (ECR).

## Contributors

- Ankita Singh
- [Add other contributors if applicable]

## License

[Add license information]
