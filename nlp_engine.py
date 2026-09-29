from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
class NLPEngine:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.clauses = [
            "Garantie dégât des eaux : couverture des fuites et infiltrations.",
            "Garantie vol et vandalisme : indemnisation des objets volés ou dégradés.",
            "Responsabilité civile : prise en charge des dommages causés à autrui.",
            "Garantie incendie : couverture des dégâts causés par le feu et la fumée.",
        ]
        self.embeddings = None
        pass

    def ajouter_clauses(self, liste_des_clauses):
        # Je charges les clauses
        self.clauses = liste_des_clauses
        # Je crée la vectorialisation pour les clauses
        self.embeddings = self.model.encode(self.clauses, show_progress_bar=False)

    def recherche(self, requete_client, seuil=0.35):
        #Je crée la vectorialisation pour le client
        self.embeddings_client = self.model.encode([requete_client], show_progress_bar=False)
        # Je calcule les similarités
        score = cosine_similarity(self.embeddings_client, self.embeddings)[0]
        score_max_index = int(np.argmax(score))
        # Bornage et arrondi du score
        score_max = float(np.clip(score[score_max_index], 0.0, 1.0))
        print(f"\nRequête{requete_client}\n")
        if score_max > seuil:
            print(f"Clause Trouvée : {self.clauses[score_max_index]} --> Score:  {score_max} ")
            return self.clauses[score_max_index], round(score_max, 4)
        else:
            print("Aucune clause correspond à votre demande ! ")
            return None, score_max
    def detecter_doublons(self,seuil_doublon=0.70):
        matrice_sim = cosine_similarity(self.embeddings, self.embeddings)
        N = len(self.clauses)
        for i in range(N):
            for j in range(i+1, N):
                score = matrice_sim[i,j]
                if score > seuil_doublon:
                    print(f"Doublon détecté ({score:.4f}) :")
                    print(f"  - Clause {i}: {self.clauses[i]}")
                    print(f"  - Clause {j}: {self.clauses[j]}")








