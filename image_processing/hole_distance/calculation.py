import os
import cv2
import numpy as np

def save_grayscale_image(image, folder_path, filename):
    """Saves the grayscale version of an image to a folder.
    Args:
        image: A NumPy array representing the image.
        folder_path: The path to the folder where the image should be saved.
        filename: The filename to use for the saved image.
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the grayscale image
    grayscale_path = os.path.join(folder_path, filename)
    cv2.imwrite(grayscale_path, image)

def mark_and_save_image(image, bullet_holes, folder_path, filename):
    """Creates a copy of the image with hole numbers marked and saves it.
    Args:
        image: A NumPy array representing the original image.
        bullet_holes: A list of tuples containing (x, y) coordinates of bullet holes.
        folder_path: The path to the folder where the marked image should be saved.
        filename: The filename to use for the saved image.
    """
    # Create a copy of the original image to avoid modifying it
    marked_image = image.copy()

    # Font for text
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Loop through bullet holes and draw circles and text
    for i, (x, y) in enumerate(bullet_holes, start=1):
        cv2.circle(marked_image, (x, y), 5, (0, 0, 255), -1)  # Draw red circle
        cv2.putText(marked_image, str(i), (x - 5, y + 5), font, 0.5, (255, 255, 255), 1)  # White text

    # Save the marked image
    marked_path = os.path.join(folder_path, filename)
    cv2.imwrite(marked_path, marked_image)

def distance_between_points(point1, point2):
    """Calculates the Euclidean distance between two points.
    Args:
        point1: A list or tuple containing the x and y coordinates of the first point.
        point2: A list or tuple containing the x and y coordinates of the second point.
    Returns:
        The Euclidean distance between the two points.
    """
    return np.sqrt(((point1[0] - point2[0])**2) + ((point1[1] - point2[1])**2))

def find_bullet_holes(image):
    """Finds the bullet holes in an image of a target.

    Args:
        image: A NumPy array representing the image.

    Returns:
        A list of tuples, where each tuple contains the x and y coordinates of a bullet hole.
    """
    # Convert the image to grayscale.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    folder_to_save = "grayscale_images"
    save_grayscale_image(gray_image, folder_to_save, "grayscale_image.jpg")
    
    # Apply thresholding to isolate the bullet holes.
    thresh = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    print('thresh: ', thresh)

    # Find contours in the thresholded image.
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print('contours: ', contours)
    # Find the center of each contour (bullet hole).
    bullet_holes = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        center_x = x + (w // 2)
        center_y = y + (h // 2)
        bullet_holes.append((center_x, center_y))

    return bullet_holes


def main():
    print('MAIN CALLED')
    # Load the image.
    image = cv2.imread('image_9.jpeg')
    # image = cv2.imread('image_4.png')

    # Find the bullet holes.
    bullet_holes = find_bullet_holes(image)
    print('bullet_holes: ', bullet_holes)
    
    folder_to_save = "analysis_images"
    mark_and_save_image(image, bullet_holes, folder_to_save, "marked_image.jpg")
    # Calculate the distances between all pairs of bullet holes.
    print('Holes: ', len(bullet_holes))
    for i in range(len(bullet_holes)):
        for j in range(i + 1, len(bullet_holes)):
            point1 = bullet_holes[i]
            point2 = bullet_holes[j]
            distance = distance_between_points(point1, point2)
            # print(f"Distance between bullet hole {i+1} and bullet hole {j+1}: {distance:.2f} pixels")

if __name__ == "__main__":
    main()