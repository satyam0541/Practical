medical_dictionary = {
    "Common Cold": ["Runny_nose", "Sneezing", "Cough", "Sore_throat", "Stuffy_nose"],
    "Pneumonia": ["Cough", "Fever", "Breathlessness", "Chest_pain", "Tiredness", "Chills"],
    "Stomach Flu": ["Sick_stomach", "Loose_stools", "Stomach_cramps", "Fever", "Dehydration"],
    "COVID-19": ["Fever", "Cough", "Short_breath", "Tiredness", "No_taste/smell", "Sore_throat"],
    "Malaria": ["Fever", "Shivers", "Sweating", "Headache", "Body_aches", "Sick_feeling", "Throwing_up"],
    "Viral Fever": ["Fever", "Body_aches", "Headache", "Tiredness"]
}

# Create a unique list of all possible symptoms
all_symptoms = []
for symptom_list in medical_dictionary.values():
    all_symptoms.extend(symptom_list)
symptoms = list(dict.fromkeys(all_symptoms))  # remove duplicates


def userinput(symp):
    print("\nEnter the symptoms (comma separated) from the list below:")
    for i in range(len(symptoms)):
        if i % 10 == 0 and i != 0:
            print()
        print(symptoms[i], end=", ")
    print("\n")
    temp = input("Enter your symptoms: ").strip().split(",")
    symp = symp | set(s.strip() for s in temp if s.strip() != "")
    if len(symp) < 3 :
        print("Please enter more symptom.")
        return symp | userinput(symp)
    return symp

def diagnose(symptoms_input):
    scores = {}
    for disease, disease_symptoms in medical_dictionary.items():
        # print(set(symptoms_input) & set(disease_symptoms))
        match_count = len(symptoms_input.intersection(set(disease_symptoms)))
        scores[disease] = match_count / len(disease_symptoms)

    sorted_diagnosis = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("\nPossible diagnosis based on your symptoms:")
    f=0
    for disease, score in sorted_diagnosis:
        if score > 0:
            f=1
            percentage = round(score * 100)
            print(f"- {disease} ({percentage}% match)")
        else:
            break
    if f==0:
      print("Please visit a doctor for a proper diagnosis.")

# Run the expert system
symp=set()
user_symptoms = userinput(symp)
diagnose(user_symptoms)
#  Runny_nose,Short_breath,Tiredness,Headache,Headache
