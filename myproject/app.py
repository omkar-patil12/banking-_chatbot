from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# simple chatbot logic (you can expand later)
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "upi" in user_input:
        return "UPI (Unified Payments Interface) allows instant money transfers between bank accounts using a mobile app."
    elif "account" in user_input:
        return "You can open a bank account by visiting your nearest branch or applying online with KYC documents."
    elif "loan" in user_input:
        return "Banks offer personal, home, and business loans. You need documents like ID proof, address proof, and income proof."
    elif "atm" in user_input:
        return "You can withdraw cash from any ATM using your debit card and PIN."
    elif "ifsc" in user_input:
        return "IFSC (Indian Financial System Code) is an 11-digit code used to identify bank branches for online transfers."
    elif "neft" in user_input:
        return "NEFT (National Electronic Funds Transfer) allows one-to-one money transfers between banks in India."
    elif "rtgs" in user_input:
        return "RTGS (Real Time Gross Settlement) is used for high-value transfers above ₹2 lakhs, processed instantly."
    elif "imps" in user_input:
        return "IMPS (Immediate Payment Service) allows instant 24x7 interbank transfers using mobile or internet banking."
    elif "cibil" in user_input:
        return "A CIBIL score is a 3-digit number (300-900) that represents your creditworthiness. A score above 750 is considered good."
    elif "fixed deposit" in user_input or "fd" in user_input:
        return "A Fixed Deposit (FD) is a safe investment where you deposit money for a fixed tenure and earn higher interest."
    elif "net banking" in user_input:
        return "Net banking allows you to manage your account, transfer money, and pay bills online through the bank’s portal."
    elif "mobile banking" in user_input:
        return "Mobile banking lets you use banking services via your smartphone using the bank’s official app."
    elif "debit card" in user_input:
        return "A debit card is linked to your bank account. You can withdraw cash, make purchases, and pay bills directly from your balance."
    elif "credit card" in user_input:
        return "A credit card allows you to borrow money up to a limit to pay for purchases. The amount must be repaid monthly."
    elif "minimum balance" in user_input:
        return "Banks require you to maintain a minimum balance in your account. Falling below this may attract penalty charges."
    else:
        return "Sorry, I don’t understand that. Please ask about UPI, loans, accounts, CIBIL score, or other banking services."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
