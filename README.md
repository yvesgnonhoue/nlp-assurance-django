# 🔍 Moteur de Recherche Sémantique & Classification de Clauses d'Assurance (NLP)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![PyTorch](https://img.shields.io/badge/PyTorch-IA-red)
![SBERT](https://img.shields.io/badge/Sentence--Transformers-SBERT-orange)

## 📌 Présentation du Projet
Ce projet propose une solution intelligente d'analyse et de recherche sémantique appliquée aux contrats et clauses d'assurance. Contrairement à une recherche par mots-clés classique, le moteur utilise des modèles de langage avancés pour comprendre le sens contextuel des requêtes et faire correspondre automatiquement les demandes aux clauses pertinentes.

## ⚙️ Problématique Métier & Solution Technique
- **Problème :** Les demandes de prise en charge et contrats d'assurance contiennent un vocabulaire hétérogène, rendant la recherche exacte inefficace et chronophage.
- **Solution :** Vectorisation sémantique continue via des modèles d'embeddings **SBERT** (Sentence-Transformers), calcul de similarité cosinus sous **PyTorch/Scikit-learn** et interface utilisateur réactive développée sous **Django**.

## 🚀 Fonctionnalités Clés
- **Vectorisation contextuelle :** Transformation des textes en tenseurs d'embeddings de haute dimension.
- **Match Sémantique :** Calcul de similarité cosinus matricielle pour ordonner les résultats par pertinence.
- **Filtrage Dynamique :** Application de seuils de confiance pour écarter les requêtes hors-sujet et détecter les doublons.
- **Interface Web :** Application web Django avec intégration Bootstrap 5 pour effectuer des recherches en temps réel.

## 🛠️ Stack Technique
- **Backend & Web :** Python, Django 5.2, Bootstrap 5
- **NLP & IA :** Sentence-Transformers (`SBERT`), PyTorch, Scikit-learn
- **Data Handling :** Pandas, NumPy

## 💻 Installation et Lancement

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/yvesgnonhoue/nlp-assurance-django.git](https://github.com/yvesgnonhoue/nlp-assurance-django.git)
   cd nlp-assurance-django
