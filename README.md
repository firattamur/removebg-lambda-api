# 🚀 FastAPI Backend for Image Background Removal Service 📸

This repository contains the code for the FastAPI backend of the Image Background Removal Service. The backend is responsible for handling user requests, managing file uploads and downloads, and communicating with the EC2 worker instances that process the images.

## 🎯 Features

- Secure and scalable architecture with FastAPI, Amazon S3, SQS, SNS, and EC2
- Upload images to the service
- Process images to remove their backgrounds
- Download processed images with removed backgrounds

## 📋 Project Flow

1. The backend receives user requests to upload images for background removal.
2. Images are uploaded to an Amazon S3 bucket.
3. After a successful upload, the backend sends a message to an Amazon SQS queue with the S3 object key of the uploaded image.
4. EC2 worker instances listen for messages from the SQS queue.
5. When a worker receives a message, it processes the image by removing the background.
6. The processed image is uploaded back to the S3 bucket.
7. The worker sends a message to an Amazon SNS topic, indicating that the image processing is complete.
8. The FastAPI backend is subscribed to the SNS topic and receives notifications when processed images are ready.
9. The backend updates the status of the corresponding image processing request.
10. Users can check the status of their requests and download the processed images with removed backgrounds.

## 🏗️ Architecture

![Architecture]()

## 🚀 Getting Started

1. Clone this repository.
2. Create a virtual environment and activate it by running

```bash
python -m venv venv && source venv/bin/activate
```

3. Install the required Python dependencies by running

```bash
pip install -r requirements.txt
```

4. Create a file named .env in the root directory of your project.
5. Add the following lines to the .env file:

```bash
AWS_ACCESS_KEY_ID=<your-aws-access-key-id>
AWS_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
AWS_REGION=<your-aws-region>
SNS_TOPIC_ARN=<your-sns-topic-arn>
SQS_QUEUE_URL=<your-sqs-queue-url>
S3_BUCKET_NAME=<your-s3-bucket-name>
```

4. Run the FastAPI backend using a command like

```bash
uvicorn main:app --reload
```

5. Access the API documentation at `http://localhost:8000/docs`.

## 🌐 Deployment

This project uses GitHub Actions for CI/CD. To deploy the FastAPI backend:

1. Push changes to the main branch of this repository.
2. The GitHub Actions workflow defined in `.github/workflows/main.yml` will automatically build and deploy the FastAPI backend to your desired hosting platform (e.g., AWS Lambda).

## 📚 Documentation

For more information on how this backend fits into the overall Image Background Removal Service, please refer to the [EC2 worker repository](https://github.com/firattamur/removebg-worker).

## 🤝 Contributing

Contributions are more than welcome! If you find any issues, have suggestions for improvements, or would like to add new design pattern examples, please open an issue or submit a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
