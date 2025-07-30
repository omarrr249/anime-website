import os
from zipfile import ZipFile

# اسم المشروع
project_name = "anime_website"
os.makedirs(f"{project_name}/assets", exist_ok=True)

# محتوى ملف HTML
html_content = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>موقع أنمي بسيط</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
    <header>
        <h1>مرحباً بك في عالم الأنمي</h1>
    </header>
    <main>
        <section class="anime">
            <h2>أنمي: Attack on Titan</h2>
            <p>قصة مثيرة حول البشر والعمالقة.</p>
            <a href="https://www.youtube.com/watch?v=MGRm4IzK1SQ" target="_blank">مشاهدة الإعلان</a>
        </section>
        <section class="anime">
            <h2>أنمي: Demon Slayer</h2>
            <p>مغامرة ملحمية لصيادي الشياطين.</p>
            <a href="https://www.youtube.com/watch?v=VQGCKyvzIM4" target="_blank">مشاهدة الإعلان</a>
        </section>
    </main>
    <footer>
        <p>© 2025 موقع أنمي بسيط</p>
    </footer>
</body>
</html>
"""

# محتوى CSS
css_content = """
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    color: #333;
    direction: rtl;
    text-align: right;
    margin: 0;
    padding: 0;
}
header, footer {
    background-color: #222;
    color: white;
    padding: 10px 20px;
    text-align: center;
}
main {
    padding: 20px;
}
.anime {
    background-color: #fff;
    border: 1px solid #ccc;
    margin-bottom: 20px;
    padding: 15px;
    border-radius: 8px;
}
.anime a {
    display: inline-block;
    margin-top: 10px;
    color: #007BFF;
    text-decoration: none;
}
.anime a:hover {
    text-decoration: underline;
}
"""

# حفظ الملفات
with open(f"{project_name}/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open(f"{project_name}/assets/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

# إنشاء ملف ZIP
zip_filename = f"{project_name}.zip"
with ZipFile(zip_filename, 'w') as zipf:
    for foldername, subfolders, filenames in os.walk(project_name):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            zipf.write(filepath, os.path.relpath(filepath, project_name))

print(f"✅ تم إنشاء ملف {zip_filename}")
