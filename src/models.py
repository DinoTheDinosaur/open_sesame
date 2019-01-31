import matplotlib.pyplot as plt
import numpy as np

from python_speech_features import mfcc
import scipy.io.wavfile as wav

from sklearn.mixture import GaussianMixture
from sklearn import preprocessing

import pickle

# all classes take mfcc of audio as argument in fit()
# all classes take mfcc as argument in predict()

# all classes return dump of profile in fit()
# all classes return probability in predict()

# take mfcc, return list of 13 features on time averaging
def mfcc2features(mfcc):
    mfcc = mfcc.transpose()
    features = list()
    for i in range(mfcc.shape[0]):
        feature = np.mean(mfcc[i])
        features.append(feature)
    return features

# take list of features and return mean of each
def average_of_features(features):
	mean_features = list()
	for i in range(features.shape[0]):
		mean_features.append(np.mean(features[i]))

	return mean_features

# take 2 lists of mean_features, return error
def count_error_square(nonorig, orig):
	error = 0
	for i in zip(nonorig, orig):
		error += abs(i[1]**2 - i[0]**2)
	return error

# uses to count probability
def count_min_error(features, mean):
	min_er = 10**8
	if features.shape[0] == 1:
		raise Exception("Only one audio")
	for feature in features:
		er = count_error_square(feature, mean)
		if er < min_er:
			min_er = er
	return min_er

# taking mfcc from wav
def take_mfcc(path):
	(rate,sig) = wav.read(path)
	return mfcc(sig,rate)

class GMM_Voice_Profile:
	__gmm = None
	__default_error = 0

	def fit(self, mfcc_of_voice):
		mfcc_of_voice = preprocessing.scale(mfcc_of_voice)

		self.__gmm = GaussianMixture(n_components = 5)
		self.__gmm.fit(mfcc_of_voice)
		self.__default_error = self.__gmm.score(mfcc_of_voice)

	def predict(self, mfcc_of_voice):
		assert self.__default_error != 0
		mfcc_of_voice = preprocessing.scale(mfcc_of_voice)
		current_proba = self.__default_error/self.__gmm.score(mfcc_of_voice)

		if current_proba > 1:
			current_proba = 1

		with open("Voice_Profiles.pkl", 'rb') as f:
			voice_profiles = pickle.load(f)
			for user in voice_profiles["GMM"]:
				user_GMM = voice_profiles["GMM"].get(user)
				proba = self.__default_error/user_GMM.score(mfcc__of_voice)
				if proba > current_proba:
					print("No")
					break

		print("Yes")
		print(current_proba)

class Voice_Profile:
	__mean_features = list()
	__default_error = 0
	def fit(self, mfcc_of_voice):
		features = list()
		mfcc_feat = mfcc2features(mfcc_of_voice)

		features = np.array(features)
		features = features.transpose()

		self.__mean_features = average_of_features(features)
	
		self.__default_error = count_min_error(features.transpose(), self.__mean_features)

	def predict(self, mfcc_of_voice):
		assert self.__default_error != 0
		
		mfcc_feat = mfcc2features(mfcc_of_voice)
		
		error = count_error_square(mfcc_feat, self.__mean_features)
		proba = self.__default_error/error
		if proba > 1:
			proba = 1
		print(proba)

class CNN_Voice_Profile:
	def fit(self, voices):
		pass
	def predict(self, voice):
		pass
