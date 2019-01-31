import matplotlib.pyplot as plt
import numpy as np

from python_speech_features import mfcc
import scipy.io.wavfile as wav

from sklearn.mixture import GaussianMixture
from sklearn import preprocessing

# all classes take list of audios as argument in fit()
# all classes take path to audios as argument in predict()

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

def count_min_error(features, mean):
	min_er = 10**8
	if features.shape[0] == 1:
		raise Exception("Only one audio")
	for feature in features:
		er = count_error_square(feature, mean)
		if er < min_er:
			min_er = er
	return min_er


class GMM_Voice_Profile:
	__gmm = None
	__default_error = 0

	def fit(self, voices):
		(rate,sig) = wav.read(voices[0])
		mfcc_of_voice = mfcc(sig,rate)
		for voice in voices[1::]:
			(rate,sig) = wav.read(voice)
			mfcc_of_voice = np.concatenate((mfcc_of_voice, mfcc(sig,rate)))

		mfcc_of_voice = preprocessing.scale(mfcc_of_voice)

		self.__gmm = GaussianMixture(n_components = 16)
		self.__gmm.fit(mfcc_of_voice)
		self.__default_error = self.__gmm.score(mfcc_of_voice)

	def predict(self, voice):
		assert self.__default_error != 0
		(rate,sig) = wav.read(voice)
		mfcc_of_voice = mfcc(sig,rate)
		mfcc_of_voice = preprocessing.scale(mfcc_of_voice)

		proba = self.__default_error/self.__gmm.score(mfcc_of_voice)
		if proba > 1:
			proba = 1
		print(proba)


class Voice_Profile:
	__mean_features = list()
	__default_error = 0
	def fit(self, voices):
		features = list()
		for voice in voices:
			(rate,sig) = wav.read(voice)
			mfcc_of_voice = mfcc(sig,rate)

			mfcc_feat = mfcc2features(mfcc_of_voice)
			features.append(mfcc_feat)

		features = np.array(features)
		features = features.transpose()

		self.__mean_features = average_of_features(features)
	
		self.__default_error = count_min_error(features.transpose(), self.__mean_features)

	def predict(self, voice):
		assert self.__default_error != 0
		(rate,sig) = wav.read(voice)
		mfcc_of_voice = mfcc(sig,rate)
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
