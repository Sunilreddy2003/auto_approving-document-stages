from flask import Flask, request, render_template
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")  # Your admin email to receive notifications

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def send_notification_email(username, user_email, file_name):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = f"✅ New Document Uploaded: {file_name}"

    html = f"""
    <h2>📄 New Document Auto-Approved</h2>
    <p><strong>User Name:</strong> {username}</p>
    <p><strong>User Email:</strong> {user_email}</p>
    <p><strong>Document:</strong> {file_name}</p>
    <p><strong>Uploaded At:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    """

    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ Email sent to admin.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        username = request.form['username']
        user_email = request.form['email']
        uploaded_file = request.files['document']

        if uploaded_file.filename == '':
            return "⚠️ No file selected. Please upload a document."

        # Save uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

        
        send_notification_email(username, user_email, uploaded_file.filename)

        return f"✅ Document '{uploaded_file.filename}' uploaded and auto-approved!"

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
