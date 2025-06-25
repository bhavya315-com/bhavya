from flask import Blueprint, render_template, request, flash, redirect, url_for
import smtplib
from email.message import EmailMessage

base_bp = Blueprint('base_bp', __name__)

@base_bp.route('/culture')
def culture():
    return render_template('culture.html')

@base_bp.route('/timeline')
def timeline():
    return render_template('timeline.html')

@base_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        sender_email = request.form['email']
        message = request.form['message']

        # Email config
        receiver_email = 'shahbhavya13999@gmail.com'
        subject = f"New message from {name}"
        body = f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}"

        try:
            email = EmailMessage()
            email['From'] = sender_email
            email['To'] = receiver_email
            email['Subject'] = subject
            email.set_content(body)

            # Gmail SMTP
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login('shahbhavya13999@gmail.com', 'hdiq jwso yqvv vhjy')  # Replace this!
            smtp.send_message(email)
            smtp.quit()

            flash('Message sent successfully!', 'success')
        except Exception as e:
            print(f"Error: {e}")
            flash('Failed to send message.', 'danger')

        return redirect(url_for('base_bp.contact'))

    return render_template('contact.html')
