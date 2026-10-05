import PyPDF2
file=open("F:\\pandas app\\resume.pdf.pdf","rb")
reader=PyPDF2.PdfReader(file)
all_text=""
for page in reader.pages:
    text=page.extract_text()
    all_text=all_text + "\n" +text
all_text=all_text.lower()
required_skills=["Python","SQL","Excel","Powerbi"]
found_skill=[]
missing_skill=[]
for skill in required_skills:
    if skill.lower() in all_text:
        found_skill.append(skill)
    else:
        missing_skill.append(skill)
score_calculate=(len(found_skill)/len(required_skills)*100)
print("Required Skill : ",required_skills)
print(f"found skill={found_skill} and Missing Skill={missing_skill}")
print(f"Score : {score_calculate:.2f}%")
if score_calculate>=80:
    print("Excellent Resume")
elif score_calculate>=50:
    print("Good Resume")
else:
    print("Needs Improvement")
print("\nRecommendations:")
for reco in missing_skill:
    print(f"learn {reco}")
