# Password-strength-checker
# 🔒 Password Strength Checker

An advanced **React-based password strength checker** that evaluates password entropy, detects common weaknesses, and provides real-time feedback with actionable suggestions.

---

## 🚀 Features

✅ Real-time password strength analysis  
✅ Entropy-based scoring (bits of security)  
✅ Detection of common patterns — sequences, repeats, and common passwords  
✅ Intelligent suggestions to improve your password  
✅ Built-in secure random password generator  
✅ Copy-to-clipboard and show/hide functionality  
✅ Clean UI built with **Tailwind CSS**  
✅ Fully client-side — no password data leaves your browser

---

## 🧩 Tech Stack

- **React 18+**
- **Tailwind CSS** for styling

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the app:
   ```bash
   npm run dev
   ```

4. Open your browser and visit:
   ```
   http://localhost:5173
   ```

---

## 🧠 How It Works

This app calculates an estimated **entropy score** for any given password. It uses several heuristics to reduce the score for predictable or weak patterns:

- Detects **common passwords** (like `123456`, `password`, etc.)
- Penalizes **repeated characters** and **sequences** (like `abc`, `1234`)
- Checks for **keyboard patterns** (like `qwerty`)
- Evaluates **character diversity** (uppercase, lowercase, numbers, symbols)
- Computes final **entropy bits** and classifies the result as one of:
  - Very Weak (0–20 bits)
  - Weak (20–40 bits)
  - Fair (40–60 bits)
  - Strong (60–80 bits)
  - Very Strong (80+ bits)

---

## 💡 Example Usage

Type or generate a password, and the component instantly:

- Shows your **entropy score** and **strength label**
- Displays a **colored progress bar**
- Gives a list of **suggestions** to strengthen your password
- Lets you **copy** or **clear** easily

---

## 🧮 Entropy Formula

```
entropy = length * log2(character_set_size) - penalties
```

Penalties are applied for predictable patterns, repeated characters, and short passwords.

---

## 🔐 Password Generation

The built-in generator creates secure random passwords using a customizable character pool:

- Lowercase letters (a-z)
- Uppercase letters (A-Z)
- Numbers (0-9)
- Symbols (!@#$%^&*)

Default length: **16 characters**

---

## 📦 Deployment

To build for production:
```bash
npm run build
```

Then deploy the contents of the `dist/` folder to your preferred static host (e.g., Vercel, Netlify, GitHub Pages).

---

## 📸 Preview

![Password Strength Checker Screenshot](preview.png)

*(Add your own screenshot in the repo)*

---

## 🧑‍💻 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-idea`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-idea`)
5. Open a Pull Request

---

## ⚖️ License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

## ❤️ Acknowledgments

- Inspired by entropy-based password strength models
- Developed using React and Tailwind for performance and simplicity

---

**Stay safe — use strong, unique passwords and a password manager! 🔐**
