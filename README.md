
## 📄 Auto Approving Document Stages

This is a Flask-based web application that allows users to upload documents. Once a document is uploaded, it's **auto-approved** and the **admin receives an email notification** with the user’s details and document info.

---

### 🚀 Features

* Upload documents via a simple web interface.
* Auto-approve documents upon upload.
* Email notification sent to admin with:

  * User Name
  * User Email
  * File Name
  * Timestamp of Upload

---

### 🛠️ Technologies Used

* Python 3
* Flask
* HTML (for frontend form)
* SMTP (for sending email)
* `python-dotenv` (for environment variable management)

---

### 📁 Project Structure

```
.
├── app.py               # Main Flask application
├── templates/
│   └── upload.html      # Upload form HTML page
├── uploads/             # Folder to store uploaded documents
├── .env                 # Environment variables (not committed)
└── README.md            # Project documentation
```

---

### 🔧 Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/auto_approving-document-stages.git
   cd auto_approving-document-stages
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install flask python-dotenv
   ```

4. **Set up environment variables**:

   Create a `.env` file in the root directory with the following contents:

   ```env
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_PASSWORD=your_email_password
   EMAIL_RECEIVER=admin_email@gmail.com
   ```

> 💡 Use [App Passwords](https://support.google.com/accounts/answer/185833) if you're using Gmail with 2FA.

5. **Run the app**:

   ```bash
   python app.py
   ```

6. **Access the application**:

   Open your browser and navigate to:
   `http://127.0.0.1:5000/`

---

### 🧪 Test the Flow

1. Open the app in a browser.
2. Fill in the user name and email, and choose a document to upload.
3. Submit the form.
4. Admin should receive an email with the document and user details.

---



