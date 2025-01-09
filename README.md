This is a program designed to be ran on local host, with modifications that allow me to upload photos & validation codes to an S3 bucket if configured.

McDonalds offers a code on every one of their reciepts that encourages customers to fill out a survey. If a customer chooses to fill out this survey, McDonalds provides them with a code that the customer can then provide at the counter the next time they order from McDonalds which allows them to get a Buy One Get One any sandwich of equal or lesser value.

I got tired of filling out this survey myself so I developed this project where I can just take a photo of the reciept & upload it to my local host. Then, in the back-end, easyOCR extracts the survey code & Selenium & PyAutoGUI automatically fill out the survey and receive a validation code.
I then made a very simply Flask front-end where the user can upload the photo and, after a couple minutes, receive their BOGO code.

Here is a general flow:
![image](https://github.com/user-attachments/assets/158dba00-e260-47a5-bfbb-9b3f288d1921)
