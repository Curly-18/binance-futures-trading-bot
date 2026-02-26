# 🚀 How to Push Your Trading Bot to GitHub

## Prerequisites

Before starting, make sure Git is installed:
```
bash
git --version
```

If not installed, download from: https://git-scm.com/download/win

---

## Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. **Repository name**: `binance-futures-trading-bot`
3. **Description**: "Python trading bot for Binance Futures Testnet with Market, Limit, and Stop-Limit orders"
4. **Visibility**: Public
5. **Options**: Leave all unchecked
6. Click **"Create repository"**

---

## Step 2: Initialize Git (Run these commands in trading_bot folder)

```
bash
git init
```

---

## Step 3: Configure Git (First time only)

```
bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 4: Add Files to Git

```
bash
git add .
```

---

## Step 5: Create Initial Commit

```
bash
git commit -m "Initial commit - Binance Futures Testnet Trading Bot"
```

---

## Step 6: Connect to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```
bash
git remote add origin https://github.com/YOUR_USERNAME/binance-futures-trading-bot.git
```

---

## Step 7: Rename Branch (if needed)

```
bash
git branch -M main
```

---

## Step 8: Push to GitHub

```
bash
git push -u origin main
```

---

## ✅ After Running Orders

After you test the bot with orders, you'll have a `trading_bot.log` file. 
Make sure to:
- Run one MARKET order
- Run one LIMIT order
- Include the log file when submitting

---

## 📧 Email Submission

Send your resume + GitHub repo link + log files to:
- joydip@anything.ai
- chetan@anything.ai
- hello@anything.ai
- CC: sonika@anything.ai

---

## Quick Reference Commands

| Command | Description |
|---------|-------------|
| `git status` | Check current status |
| `git add .` | Add all files |
| `git commit -m "message"` | Commit changes |
| `git push` | Push to remote |
| `git log` | View commit history |
