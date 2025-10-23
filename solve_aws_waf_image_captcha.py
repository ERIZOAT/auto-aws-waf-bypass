import requests
import base64
import os

API_KEY = os.environ.get("CAPSOLVER_API_KEY", "YOUR_CAPSOLVER_API_KEY") # Replace with your CapSolver API Key or set as environment variable
IMAGE_PATH = "./captcha_image.png" # Path to the CAPTCHA image (ensure it exists)
QUESTION = "aws:grid:chair" # The question provided by AWS WAF (e.g., "aws:toycarcity:carcity" or "aws:grid:bed")
TARGET_URL = "https://your-target-website.com" # Replace with the URL of the page displaying the CAPTCHA

def encode_image_to_base64(image_path):
    """Encodes an image file to a base64 string."""
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return None
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def solve_aws_waf_image_captcha():
    """Solves an AWS WAF image CAPTCHA using CapSolver API."""
    image_base64 = encode_image_to_base64(IMAGE_PATH)
    if not image_base64:
        return None
    
    create_task_payload = {
        "clientKey": API_KEY,
        "task": {
            "type": "AwsWafClassification",
            "websiteURL": TARGET_URL,
            "images": [image_base64],
            "question": QUESTION
        }
    }
    
    print("Sending image CAPTCHA task to CapSolver...")
    response = requests.post("https://api.capsolver.com/createTask", json=create_task_payload)
    task_response = response.json()
    
    if task_response.get("errorId") == 0:
        solution = task_response.get("solution")
        print("AWS WAF Image CAPTCHA Solution:", solution)
        return solution
    else:
        print("Error solving image CAPTCHA:", task_response)
        return None

if __name__ == "__main__":
    print("Attempting to solve AWS WAF Image CAPTCHA...")
    solution = solve_aws_waf_image_captcha()
    if solution:
        print("Image CAPTCHA solved successfully!")
    else:
        print("Failed to solve image CAPTCHA.")

