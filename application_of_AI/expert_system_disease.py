class DiseaseExpertSystem:
    def __init__(self):
        self.disease_knowledge_base = {
            "cold": 
            {"symptoms": ["sneezing", "coughing", "runny nose"], 
            "treatment": "rest and drink plenty of fluids"
            },
            "flu":
            {"symptoms": ["fever", "muscle aches", "fatigue"], 
            "treatment": "rest and drink plenty of fluids"
            },
            "allergies": 
            {"symptoms": ["sneezing", "itchy eyes", "runny nose"],
            "treatment": "avoid allergens and take antihistamines"
            },
            "strep throat": 
            {"symptoms": ["sore throat", "fever", "swollen lymph nodes"],
            "treatment": "antibiotics"
            },
            "pneumonia": 
            {"symptoms": ["cough", "fever", "shortness of breath"],
            "treatment": "antibiotics"
            }
        }

        symptoms = input("Enter your symptoms (comma-separated): ").split(", ")

        self.diagnose_disease(symptoms)

    def diagnose_disease(self, symptoms):
        for disease, disease_info in self.disease_knowledge_base.items():
            if all(symptom in disease_info["symptoms"] for symptom in symptoms):
                print(f"You may have {disease}. Treatment: {disease_info['treatment']}")
                return

        print("No matching disease found")

def main():
    disease_expert = DiseaseExpertSystem()

if __name__ == "__main__":
    main()