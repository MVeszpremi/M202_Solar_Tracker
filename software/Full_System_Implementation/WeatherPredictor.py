import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import joblib
import os
import csv
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

class BrightnessAnalyzer:

    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def calculate_overall_brightness(self):
        """Calculating Overall Brightness"""
        return np.mean(self.gray_image)

    def analyze_brightness_histogram(self):
        """Analyzing Luminance Histograms"""
        hist = cv2.calcHist([self.gray_image], [0], None, [256], [0, 256])
        plt.figure()
        plt.title("Brightness Histogram")
        plt.xlabel("Brightness value")
        plt.ylabel("Pixel count")
        plt.plot(hist)
        plt.xlim([0, 256])
        plt.show()
        return hist

    def analyze_local_brightness(self):
        """Analyzing local brightness"""
        local_brightness = []
        h, w = self.gray_image.shape
        grid_size = 10
        for y in range(0, h, grid_size):
            for x in range(0, w, grid_size):
                grid = self.gray_image[y:y+grid_size, x:x+grid_size]
                local_brightness.append(np.mean(grid))
        return local_brightness

    def detect_brightness_variation(self):
        """Detecting Brightness Changes"""
        variation = np.std(self.gray_image)
        return variation

    def visualize_brightness_distribution(self):
        """Visualization of brightness distribution"""
        # plt.figure()
        # plt.imshow(self.gray_image, cmap='gray')
        # plt.colorbar()
        # plt.title("Brightness Distribution")
        # plt.show()

class SaturationAnalyzer:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    def calculate_overall_saturation(self):
        """Calculate overall saturation"""
        saturation = np.mean(self.hsv_image[:, :, 1])
        return saturation

    def analyze_saturation_histogram(self):
        """Analyze the saturation histogram"""
        hist = cv2.calcHist([self.hsv_image], [1], None, [256], [0, 256])
        plt.figure()
        plt.title("Saturation Histogram")
        plt.xlabel("Saturation value")
        plt.ylabel("Pixel count")
        plt.plot(hist)
        plt.xlim([0, 256])
        plt.show()
        return hist

    def analyze_local_saturation(self):
        """Analyzing local saturation changes"""
        local_saturation = []
        h, w, _ = self.hsv_image.shape
        grid_size = 10
        for y in range(0, h, grid_size):
            for x in range(0, w, grid_size):
                grid = self.hsv_image[y:y+grid_size, x:x+grid_size]
                local_saturation.append(np.mean(grid[:, :, 1]))
        return local_saturation

    def detect_saturation_variation(self):
        """Detecting saturation changes"""
        variation = np.std(self.hsv_image[:, :, 1])
        return variation

    def visualize_saturation_distribution(self):
        """Visualize the saturation distribution"""
        # plt.figure()
        # plt.imshow(self.hsv_image[:, :, 1], cmap='gray')
        # plt.colorbar()
        # plt.title("Saturation Distribution")
        # plt.show()

class ContrastAnalyzer:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def calculate_overall_contrast(self):
        """Calculating Overall Contrast"""
        contrast = self.gray_image.std()
        return contrast

    def analyze_contrast_histogram(self):
        """Analyzing Contrast Histograms"""
        hist = cv2.calcHist([self.gray_image], [0], None, [256], [0, 256])
        plt.figure()
        plt.title("Contrast Histogram")
        plt.xlabel("Contrast value")
        plt.ylabel("Pixel count")
        plt.plot(hist)
        plt.xlim([0, 256])
        plt.show()
        return hist

    def analyze_local_contrast(self):
        """Analyzing local contrast"""
        local_contrast = []
        h, w = self.gray_image.shape
        grid_size = 10
        for y in range(0, h, grid_size):
            for x in range(0, w, grid_size):
                grid = self.gray_image[y:y+grid_size, x:x+grid_size]
                local_contrast.append(grid.std())
        return local_contrast

    def detect_contrast_variation(self):
        """Detecting Contrast Changes"""
        variation = self.gray_image.std()
        return variation

    def visualize_contrast_distribution(self):
        """Visual Contrast Distribution"""
        # plt.figure()
        # plt.imshow(self.gray_image, cmap='gray')
        # plt.colorbar()
        # plt.title("Contrast Distribution")
        # plt.show()

class ColorHistogramAnalyzer:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.lab_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)

    def analyze_rgb_histogram(self):
        """Analyze RGB color histograms and return histogram data"""
        color_channels = ('b', 'g', 'r')
        histograms = []
        for i, channel in enumerate(color_channels):
            hist = cv2.calcHist([self.image], [i], None, [256], [0, 256])
            histograms.append(hist)

        # If a histogram is required
        #plt.figure()
        #plt.title("RGB Color Histogram")
        #plt.xlabel("Color value")
        #plt.ylabel("Pixel count")
        #for i, channel in enumerate(color_channels):
            #plt.plot(histograms[i], color=channel)
        #plt.xlim([0, 256])
        #plt.legend(color_channels)
        #plt.show()

        # Returns RGB histogram data
        return histograms

    def analyze_hsv_histogram(self):
        """Analysis of HSV color histogram"""
        color_channels = ('h', 's', 'v')
        plt.figure()
        plt.title("HSV Color Histogram")
        plt.xlabel("Color value")
        plt.ylabel("Pixel count")
        for i, channel in enumerate(color_channels):
            hist = cv2.calcHist([self.hsv_image], [i], None, [256], [0, 256])
            plt.plot(hist, color=channel)
        plt.xlim([0, 256])
        plt.legend(color_channels)
        plt.show()

    def analyze_lab_histogram(self):
        """Analyzing LAB Color Histograms"""
        color_channels = ('l', 'a', 'b')
        plt.figure()
        plt.title("LAB Color Histogram")
        plt.xlabel("Color value")
        plt.ylabel("Pixel count")
        for i, channel in enumerate(color_channels):
            hist = cv2.calcHist([self.lab_image], [i], None, [256], [0, 256])
            plt.plot(hist, color=channel)
        plt.xlim([0, 256])
        plt.legend(color_channels)
        plt.show()

    def visualize_color_histograms(self):
        """Visualize color histograms in different color spaces"""
        # self.analyze_rgb_histogram()
        # self.analyze_hsv_histogram()
        # self.analyze_lab_histogram()

def extract_features_from_frame(image_frame):
    """Extracting features from image frames"""
    gray_image = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(image_frame, cv2.COLOR_BGR2HSV)

    # Calculating Overall Brightness
    overall_brightness = np.mean(gray_image)

    # Calculate overall saturation
    overall_saturation = np.mean(hsv_image[:, :, 1])

    # Calculating Overall Contrast
    overall_contrast = gray_image.std()

    # Extract color histogram features (e.g., using only the R channel)
    hist = cv2.calcHist([image_frame], [0], None, [256], [0, 256])  # R通道
    r_hist_feature = hist.flatten()

    # Combine all features into one feature vector
    features = np.hstack([overall_brightness, overall_saturation, overall_contrast, r_hist_feature])
    return features.reshape(1, -1)

def extract_features(image_path):
    """Extract image features"""
    if not os.path.exists(image_path):
        raise Exception(f"Image path does not exist: {image_path}")

    brightness_analyzer = BrightnessAnalyzer(image_path)
    saturation_analyzer = SaturationAnalyzer(image_path)
    contrast_analyzer = ContrastAnalyzer(image_path)
    color_histogram_analyzer = ColorHistogramAnalyzer(image_path)

    overall_brightness = brightness_analyzer.calculate_overall_brightness()
    overall_saturation = saturation_analyzer.calculate_overall_saturation()
    overall_contrast = contrast_analyzer.calculate_overall_contrast()
    color_histogram_analyzer = ColorHistogramAnalyzer(image_path)
    rgb_hists = color_histogram_analyzer.analyze_rgb_histogram()
    r_hist_feature = rgb_hists[0].flatten()

    # Checking for NaN values and handling them
    features = [overall_brightness, overall_saturation, overall_contrast] + list(r_hist_feature)
    features = [0 if np.isnan(x) else x for x in features]

    return np.array(features).reshape(1, -1)

def load_dataset(folder_path):
    """Load dataset and extract features and labels"""
    all_features = []
    labels = []
    for image_name in os.listdir(folder_path):
        if image_name.endswith('.jpg'):
            image_path = os.path.join(folder_path, image_name)
            img_features = extract_features(image_path)
            all_features.append(img_features[0])  # Adding feature vectors
            if 'sunny' in image_name:  # Sunny Pictures
                labels.append(1)
            else:  # Non-Sunny Pictures
                labels.append(0)

    # Converting Feature Lists to NumPy Arrays
    return np.vstack(all_features), np.array(labels)

def train_svm_classifier(features, labels):
    """Training an SVM classifier"""
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    clf = SVC(kernel='linear')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    return clf

# # Sample Use
# folder_path = "../../data/image"
# features, labels = load_dataset(folder_path)
# svm_classifier = train_svm_classifier(features, labels)

# svm_classifier = joblib.load('./svm_classifier.joblib')

def predict_weather(frame, classifier):
    """Weather prediction for a given image frame"""
    features = extract_features_from_frame(frame)
    prediction = classifier.predict(features)
    return 'Sunny' if prediction == 1 else 'Not Sunny'
