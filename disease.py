import cv2
import numpy as np
import datetime
image_path = 'leaf.jpg'  # replace with your leaf image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found! Check your path.")
    exit()

image = cv2.resize(image, (600, 400))

# --------------------------
# STEP 2: Convert to HSV
# --------------------------
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# --------------------------
# STEP 3: Detect Disease (Color Spot Detection)
# --------------------------
lower = np.array([10, 40, 20])   # range for brown/yellow
upper = np.array([30, 255, 255])
mask = cv2.inRange(hsv, lower, upper)

disease_ratio = (cv2.countNonZero(mask) / (image.size / 3)) * 100

# --------------------------
# STEP 4: Plant Database (Example)
# --------------------------
plants_info = {
    "Beech Tree": {
        "Scientific Name": "Fagus grandifolia",
        "Possible Disease": "Beech Leaf Disease (BLD)",
        "Diagnosis": "The images display classic symptoms of Beech Leaf Disease (BLD), an emerging and devastating disease that causes dark banding and thickened leaf tissue.",
        "Confidence": "98%"
    },
    "Mango": {
        "Scientific Name": "Mangifera indica",
        "Possible Disease": "Anthracnose",
        "Diagnosis": "Dark brown or black lesions on leaves, often spreading during humid weather.",
        "Confidence": "95%"
    },
    "Tomato": {
        "Scientific Name": "Solanum lycopersicum",
        "Possible Disease": "Leaf Blight",
        "Diagnosis": "Irregular brown spots with yellow borders; caused by fungal infection.",
        "Confidence": "92%"
    }
}

# --------------------------
# STEP 5: Select Plant
# --------------------------
plant_name = "Beech Tree"
info = plants_info.get(plant_name, {})

# --------------------------
# STEP 6: Set Status and Date
# --------------------------
if disease_ratio > 15:
    status = "⚠ Diseased Leaf Detected"
else:
    status = "✅ Healthy Leaf Detected"

today = datetime.datetime.now().strftime("%m/%d/%Y")

# --------------------------
# STEP 7: Print Report in Console
# --------------------------
print("-----------------------------------------")
print("🌿 PLANT HEALTH REPORT")
print("-----------------------------------------")
print(f"Plant Name: {plant_name}")
print(f"Scientific Name: {info.get('Scientific Name', 'Unknown')}")
print(f"Detected Disease: {info.get('Possible Disease', 'Unknown')}")
print(f"Diagnosis: {info.get('Diagnosis', 'No information available')}")
print(f"Confidence: {info.get('Confidence', 'N/A')}")
print(f"Status: {status}")
print(f"Date: {today}")
print("-----------------------------------------")

# --------------------------
# STEP 8: Display on Image
# --------------------------
cv2.putText(image, f"Plant: {plant_name}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
cv2.putText(image, f"Disease: {info.get('Possible Disease', 'Unknown')}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
cv2.putText(image, status, (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
cv2.putText(image, f"Date: {today}", (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 2)

# --------------------------
# STEP 9: Show Images
# --------------------------
cv2.imshow("Plant Disease Detection", image)
cv2.imshow("Detected Disease Area", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
