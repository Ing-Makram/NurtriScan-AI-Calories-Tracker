from celery import shared_task
import time

@shared_task
def process_food_image_ai(image_id):
    # Dummy processing for demonstration
    time.sleep(5)  # Simulate AI processing
    # Here you would load the image, run the AI model, and save results
    return f"Processed image {image_id}"