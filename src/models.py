import pickle

import matplotlib.pyplot as plt
import numpy as np

from python_speech_features import mfcc
import scipy.io.wavfile as wav

from sklearn.mixture import GaussianMixture
from sklearn import preprocessing

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

# take list of features and return mean of each in a list
def average_of_features(features):
	mean_features = list()
	for i in range(features.shape[0]):
		mean_features.append(np.mean(features[i]))

	return mean_features

# take 2 lists of mean_features, return error as float
def count_error_square(nonorig, orig):
	error = 0
	for i in zip(nonorig, orig):
		error += abs(i[1]**2 - i[0]**2)
	return error

# taking mfcc from wav
def take_mfcc(path):
	(rate,sig) = wav.read(path)
	return mfcc(sig,rate)

class GMM_Voice_Profile:
	__gmm = None
	__default_error = 0
	__nickname = ""

	def __init__(self, nickname):
		self.__nickname = nickname

	def fit(self, mfcc_of_voice):
		mfcc_of_voice = preprocessing.scale(mfcc_of_voice)

		self.__gmm = GaussianMixture(n_components = 5)
		self.__gmm.fit(mfcc_of_voice)
		self.__default_error = self.__gmm.score(mfcc_of_voice)

	def _score(self, mfcc_of_voice):
		return self.__gmm.score(mfcc_of_voice)

	def predict(self, mfcc_of_voice):
		mfcc_of_voice = preprocessing.scale(mfcc_of_voice)
		current_proba = self.__default_error/self.__gmm.score(mfcc_of_voice)

		with open("Voice_Profiles.pickle", 'rb') as f:
			voice_profiles = pickle.load(f)
			for user in voice_profiles["GMM"]:
				user_GMM = voice_profiles["GMM"].get(user)

				if user == self.__nickname:
					continue

				proba = self.__default_error/user_GMM._score(mfcc_of_voice)
				if proba > current_proba:
					print("No")
					return

		print("Yes")

class Voice_Profile:
	__mean_features = list()
	__nickname = ""

	def __init__(self, nickname):
		self.__nickname = nickname

	def fit(self, mfcc_of_voice):
		mfcc_feat = mfcc2features(mfcc_of_voice)

		features = np.array(mfcc_feat)
		features = features.transpose()

		self.__mean_features = average_of_features(features)

	def _score(self, mfcc_of_voice):
		mfcc_feat = mfcc2features(mfcc_of_voice)
		return count_error_square(mfcc_feat, self.__mean_features)
		
	def predict(self, mfcc_of_voice):
		current_error = self._score(mfcc_of_voice)

		with open("Voice_Profiles.pickle", 'rb') as f:
			voice_profiles = pickle.load(f)
			for user in voice_profiles["Simple"]:
				user_Simple = voice_profiles["Simple"].get(user)

				if user == self.__nickname:
					continue

				error = user_Simple._score(mfcc_of_voice)
				if error < current_error:
					print("No")
					return

		print("Yes")
		
class CNN_Voice_Profile:
	def fit(self, voices):
		pass
	def predict(self, voice):
		pass


def create_empty_pickle():
	data = {"Simple": {}, "GMM": {}, "CNN": {}}
	with open('Voice_Profiles.pickle', 'wb') as f:
		pickle.dump(data, f)

# take nickname and mfcc of voice, create profiles in pickle
def add_user(nickname, mfcc_of_voice):
	with open('Voice_Profiles.pickle', 'rb') as f:
		profiles = pickle.load(f)

		profiles.get("Simple")[nickname] = Voice_Profile(nickname)
		profiles.get("Simple")[nickname].fit(mfcc_of_voice)

		profiles.get("GMM")[nickname] = GMM_Voice_Profile(nickname)
		profiles.get("GMM")[nickname].fit(mfcc_of_voice)
		
		# profiles.get("CNN")[nickname] = GMM_Voice_Profile(nickname)
		# profiles.get("CNN")[nickname].fit(mfcc_of_voice)

	with open('Voice_Profiles.pickle', 'wb') as f:
		pickle.dump(profiles, f)

# return true if user exist in pickle
def user_exist(nickname):
	with open('Voice_Profiles.pickle', 'rb') as f:
		profiles = pickle.load(f)
		if nickname not in profiles.get("Simple") and nickname not in profiles.get("GMM") and nickname not in profiles.get("CNN"):
			return False
		else:
			return True

def print_user_list():
	with open('Voice_Profiles.pickle', 'rb') as f:
		profiles = pickle.load(f)
		print(profiles.get("GMM").keys())

# take nickname and voice, return predictions
def authorization(nickname, mfcc_of_voice):
	with open('Voice_Profiles.pickle', 'rb') as f:
		profiles = pickle.load(f)

		profiles.get("Simple")[nickname].predict(mfcc_of_voice)

		profiles.get("GMM")[nickname].predict(mfcc_of_voice)
		
		# profiles.get("CNN")[nickname].predict(mfcc_of_voice)
