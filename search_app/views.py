from django.shortcuts import render
from nlp_engine import NLPEngine



# Create your views here.

# 1. Instanciation
engine = NLPEngine()

# 2. Jeu de données de test
corpus = [
        (
            "Prise en charge des dégâts des eaux et fuites de canalisation dans"
            " le logement."
        ),
        (
            "Remboursement des soins dentaires et frais d'hospitalisation sur"
            " ordonnance."
        ),
        (
            "Indemnisation des dommages corporels et matériels suite à un"
            " accident de la route."
        ),
        (
            "Couverture des fuites d'eau et dégâts des eaux dans l'habitation."
        ),  # Doublon sémantique avec la clause 0
    ]

# 3. Injection du corpus dans l'instance
engine.ajouter_clauses(corpus)

def index(request):
    resultat = None
    score = None
    requete = ""

    # Si l'utilisateur soumet le formulaire de recherche
    if request.method == "POST":
        requete = request.POST.get("requete_texte", "")
        if requete:
            resultat, score = engine.recherche(requete)

    # Données transmises au template HTML
    context = {
        "requete": requete,
        "resultat": resultat,
        "score": score,
    }

    return render(request, "search_app/index.html", context)
