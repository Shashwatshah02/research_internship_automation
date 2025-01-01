# Automated Research Internship Mailing Tool 🚀  

This project simplifies the process of applying for research internships by automating cold emails to professors from top universities. With a click of a button, you can send personalized emails to professors using curated datasets for institutions like MIT, CMU, UCLA, IITs, and more.  

## Features  
- **Curated Professor Datasets:** Access datasets of professors in the computer science domain from various universities.  
- **Automated Mailing System:** Send personalized emails to professors with just a single click.  
- **Customizable Datasets:** Switch datasets easily to target professors from different institutions or research domains.  
- **Efficient Workflow:** Saves time by eliminating the tedious manual process of cold-emailing and following up.  

---

## How It Works  

1. **Prepare Your Email Credentials:**  
   - Update the `your_email` and `your_password` fields in the script with your Gmail credentials.  

2. **Customize the Dataset:**  
   - Choose the dataset of professors you want to email.  
   - Update the file path in the script to use the selected dataset.  

3. **Run the Script:**  
   - Execute the script to send personalized emails to the professors listed in the dataset.  

---

## Special Note for Gmail Users  

If you’re using a **Gmail account** for this tool:  

### Case 1: **No 2-Step Verification**  
- Ensure "Allow less secure apps" is enabled in your [Google account settings](https://myaccount.google.com/security).  
- This setting is required to allow third-party apps like this one to access your account.  

### Case 2: **2-Step Verification Enabled**  
- If you have **2-Step Verification** enabled on your Google account, you will need to generate an **App Password** to use this tool.  
- Follow these steps:  
  1. Go to your [Google account security page](https://myaccount.google.com/security).  
  2. Enable **2-Step Verification** if not already done.  
  3. Generate an **App Password** under the "App Passwords" section.  
  4. Use the generated app password in place of your Gmail password in the script.  

For more details, refer to [Google's App Password Guide](https://support.google.com/accounts/answer/185833).  

---

## Requirements  

- Python 3.10+  
- Required libraries: `smtplib`, `pandas`, and any others specified in `requirements.txt`.  

---

