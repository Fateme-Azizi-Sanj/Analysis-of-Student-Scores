import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# تولید داده‌های تصادفی برای ۱۰ دانشجو و ۵ درس
np.random.seed(42)
students = ['Ali', 'Maryam', 'Vahid', 'Sara', 'Hossein', 'Fatemeh', 'Mohammad', 'Aida', 'Amir', 'Neda']
courses = ['Mathematics', 'Physics', 'Programming', 'logic circuit', 'Statistics']
scores = np.random.randint(10, 20, size=(len(students), len(courses)))

# ساخت دیتافریم از داده‌ها
data = {
    'Student': np.tile(students, len(courses)),   # نام دانشجو
    'Course': np.repeat(courses, len(students)),  # نام درس
    'Score': scores.flatten()                     # نمره‌ها
}
df = pd.DataFrame(data)

# ذخیره و بارگذاری داده‌ها از فایل CSV
df.to_csv('student_grades.csv', index=False)
df = pd.read_csv('student_grades.csv')

# تحلیل کلی نمرات
print("=== GENERAL ANALYSIS ===")
print(f"Average score: {df['Score'].mean():.2f}")  # میانگین تمام نمرات
print(f"Highest score: {df['Score'].max()}")       # بیشترین نمره
print(f"Lowest score: {df['Score'].min()}")        # کمترین نمره

# میانگین نمرات هر درس
print("\n=== AVERAGE SCORE PER COURSE ===")
print(df.groupby('Course')['Score'].mean())

# میانگین نمرات هر دانشجو
student_avg = df.groupby('Student')['Score'].mean()
print("\n=== AVERAGE SCORE PER STUDENT ===")
print(student_avg)

# بهترین و ضعیف‌ترین دانشجو
best_students = student_avg[student_avg == student_avg.max()]
worst_students = student_avg[student_avg == student_avg.min()]
print("\n=== TOP STUDENTS ===")
print(best_students)
print("\n=== LOWEST PERFORMING STUDENTS ===")
print(worst_students)

# نمودار نمرات همه دانشجویان
plt.figure(figsize=(10, 6))
plt.bar(df['Student'], df['Score'], color='skyblue')
plt.title('Student Scores', fontsize=14)
plt.xlabel('Student Name', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# نمودار میانگین نمرات هر درس
plt.figure(figsize=(10, 6))
course_avg = df.groupby('Course')['Score'].mean()
course_avg.plot(kind='bar', color='lightgreen')
plt.title('Average Score per Course', fontsize=14)
plt.xlabel('Course', fontsize=12)
plt.ylabel('Average', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# نمودار افقی میانگین نمرات دانشجویان
plt.figure(figsize=(10, 6))
student_avg_sorted = student_avg.sort_values()
student_avg_sorted.plot(kind='barh', color='orange')
plt.title('Average Score per Student', fontsize=14)
plt.xlabel('Average Score', fontsize=12)
plt.ylabel('Student', fontsize=12)
plt.tight_layout()

# هیستوگرام کلی نمرات
plt.figure(figsize=(10, 6))
plt.hist(df['Score'], bins=5, color='purple', alpha=0.7)
plt.title('Score Histogram', fontsize=14)
plt.xlabel('Score', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tight_layout()

# هیستوگرام نمرات جدا برای هر درس
plt.figure(figsize=(10, 6))
for course in df['Course'].unique():
    course_scores = df[df['Course'] == course]['Score']
    plt.hist(course_scores, bins=5, alpha=0.5, label=course)
plt.title('Score Distribution per Course', fontsize=14)
plt.xlabel('Score', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend()
plt.tight_layout()

# نمایش همه نمودارها
plt.show()