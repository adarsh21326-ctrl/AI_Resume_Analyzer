from skills import SKILLS

with open("resume.txt", "r") as file:
    content = file.read()

found_skills = []
print("Skills Found:")

missing_skills = []

for skill in SKILLS:
    if skill.lower() in content.lower():
        found_skills.append(skill)
        print("-", skill)
    else:
        missing_skills.append(skill)

print()
print("Missing Skills:")

for skill in missing_skills:
    print("-", skill)

score = len(found_skills) * 10
if "Education:" in content:
    score += 20

if "Projects:" in content:
    score += 20

if score >= 80:
    rating = "Excellent"
elif score >= 60:
    rating = "Good"
elif score >= 40:
    rating = "Average"
else:
    rating = "Needs Improvement"


print()
print("Resume Score:", score, "/100")
print("Resume Rating:", rating)

print()
print("Suggestions:")

if len(missing_skills) > 0:
    print("- Try learning:", ", ".join(missing_skills[:3]))

if score < 50:
    print("- Add more skills and projects to improve your resume.")

if "projects:" not in content.lower():
    print("- Add at least 1 real project.")

if "education:" not in content.lower():
    print("- Add your education details.")

with open("report.txt", "w") as report:
    report.write("Resume Analysis Report\n")
    report.write("=====================\n\n")

    report.write("Skills Found:\n")
    for skill in found_skills:
        report.write(f"- {skill}\n")

    report.write("\nMissing Skills:\n")
    for skill in missing_skills:
        report.write(f"- {skill}\n")

    report.write(f"\nResume Score: {score}/100\n")
    report.write(f"Resume Rating: {rating}\n")