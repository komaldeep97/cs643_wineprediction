#creation of model using mllib 
from pyspark.mllib.linalg import Vectors
from pyspark.ml.regression import RandomForestRegressor
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession	
from pyspark.ml.classification import RandomForestClassifier
from pyspark.mllib.tree import RandomForest


spark = SparkSession(sc)
inputDF = spark.read.csv('s3://wineprediction/TrainingDataset.csv',header='true', inferSchema='true', sep=';')
featureColumns = [c for c in inputDF.columns if c != 'quality']


transformed_df= inputDF.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[0:-1])))

model = RandomForest.trainClassifier(transformed_df,numClasses=10,categoricalFeaturesInfo={}, numTrees=50, maxBins=64, maxDepth=20, seed=33)
model.save(sc,"s3:wineprediction/model_created.model")