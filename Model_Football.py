import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('./goalscorers_rename.csv')

# نمایش نمونه‌ای از داده‌ها
print("Sample data:")
print(data.head())

# تبدیل متغیرهای اسمی به عددی
label_encoder_team = LabelEncoder()
label_encoder_winner = LabelEncoder()

data['HomeTeam'] = label_encoder_team.fit_transform(data['HomeTeam'])
data['AwayTeam'] = label_encoder_team.fit_transform(data['AwayTeam'])
data['Winner'] = label_encoder_winner.fit_transform(data['Winner'])

# انتخاب ویژگی‌ها و برچسب‌ها برای پیش‌بینی تیم برنده
X_team = data[['HomeTeam', 'AwayTeam']]
y_team = data['Winner']

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی برای پیش‌بینی تیم برنده
X_train_team, X_test_team, y_train_team, y_test_team = train_test_split(X_team, y_team, test_size=0.2, random_state=42)

# استانداردسازی داده‌ها
scaler_team = StandardScaler()
X_train_team = scaler_team.fit_transform(X_train_team)
X_test_team = scaler_team.transform(X_test_team)

# ایجاد مدل Random Forest برای پیش‌بینی تیم برنده
model_team = RandomForestClassifier(n_estimators=100, random_state=42)


model_team.fit(X_train_team, y_train_team)

# ارزیابی مدل پیش‌بینی تیم برنده
y_pred_team = model_team.predict(X_test_team)
accuracy_team = accuracy_score(y_test_team, y_pred_team)
print(f'Team Prediction Accuracy: {accuracy_team:.2f}')
print(classification_report(y_test_team, y_pred_team))

# رسم ماتریس درهم‌ریختگی برای پیش‌بینی تیم برنده
# conf_matrix_team = confusion_matrix(y_test_team, y_pred_team)
# print("Confusion Matrix for Team Prediction:")
# print(conf_matrix_team)

# sns.heatmap(conf_matrix_team, annot=True, fmt='d', cmap='Blues')
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.title('Confusion Matrix for Team Prediction')
# plt.show()

# دریافت ورودی از کاربر
home_team = input("Enter the name of the home team: ")
away_team = input("Enter the name of the away team: ")

# تبدیل ورودی‌ها به قالب عددی
home_team_encoded = label_encoder_team.transform([home_team])[0]
away_team_encoded = label_encoder_team.transform([away_team])[0]

# ایجاد DataFrame برای ورودی جدید
new_match_team = pd.DataFrame([[home_team_encoded, away_team_encoded]], columns=['HomeTeam', 'AwayTeam'])

# استانداردسازی داده جدید
new_match_team = scaler_team.transform(new_match_team)

# پیش‌بینی نتیجه تیم برنده
prediction_team = model_team.predict(new_match_team)
predicted_winner = label_encoder_winner.inverse_transform(prediction_team)
print(f'Predicted winner: {predicted_winner[0]}')
