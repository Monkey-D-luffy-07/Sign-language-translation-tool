# Sign Language Translation Tool

## Purpose

The primary purpose of this project is to enable basic sign language detection using computer vision techniques. It aims to identify and classify simple hand gestures, such as **Fist** and **Open Hand**, and map them to corresponding text phrases. This facilitates a basic form of non-verbal communication for individuals with speech or hearing impairments.

## Technologies Used

- **OpenCV**: For real-time image and video processing, including color space conversion, contour detection, and gesture classification.
- **NumPy**: For efficient array operations and data manipulation.
- **Google Colab Files Module**: To handle video file uploads within Colab for processing.

## Usage

### 1. File Upload:
Users upload a video file containing hand gestures.

### 2. Frame Processing:
The code extracts frames, converts them to the HSV color space, and applies a skin color mask for hand segmentation.

### 3. Gesture Classification:
It identifies hand shapes like **'Fist'** and **'Open Hand'** using contour analysis and convex hull defects.

### 4. Output Mapping:
Recognized gestures are mapped to predefined text phrases like **'Hello'** and **'Thank You.'**

### 5. Result Display:
The final sequence of recognized gestures is displayed as a simple sentence.

## Example

Upload a video file with gestures, and the system will detect and map them to a simple phrase like:

**Gesture: Fist → "Hello"**

**Gesture: Open Hand → "Thank You"**

## Conclusion

This approach demonstrates a straightforward yet effective way to interpret basic hand gestures into text, offering a foundation for more sophisticated sign language recognition systems. While limited to a few gestures, it highlights the potential for integrating machine learning for more nuanced and comprehensive sign language understanding in future iterations.
