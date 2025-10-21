# Odoo Dev – Modules de test et carte statique

Ce repository contient des modules de test Odoo 16 pour la démonstration de fonctionnalités de base et la gestion avancée des adresses par Google Maps.

## Modules inclus

### 1. App Simple

> Un module de démonstration qui illustre la structure minimale d’un add-on Odoo : manifest, modèle Python, vue XML.

- **But :** Fournir une base pour développer et tester des modules Odoo.
- **Fichiers clés :** 
    - `__init__.py`
    - `__manifest__.py`
    - `models/`

### 2. Address Map Static

> Ce module permet d’**afficher une carte Google Maps statique** (Static Maps API) directement sur la fiche d’un contact (res.partner) à partir de l’adresse ou des coordonnées GPS renseignées.

**Fonctionnalités :**
- Ajout d’un onglet ou d’un champ “Carte” sur le formulaire Contact.
- Génération dynamique d’un visuel Google Maps selon l’adresse.
- Paramétrage du module via Settings Odoo (configuration backend).

#### Paramétrage (Settings)

Une option personnalisée est ajoutée dans le menu "Paramètres" d’Odoo via les `Settings` :
- **Afficher la carte sur le formulaire Contact**
    - Permet d’activer ou non l’affichage de la carte sur chaque fiche partenaire.
    - Peut être modifié via le menu “Paramètres” > “Technical settings” > “Address Map Static”.

Un champ pour renseigner la **clé API Google Maps** peut être ajouté :
- Permet d’utiliser le service Google Maps Static en toute sécurité, selon les quotas/API key du projet.

Fichier concerné :
- `res_config_settings_view.xml` (vue des paramètres)
- `models/res_config_settings.py` (gestion stockage config)

#### Structure du code

- `address_map/__init__.py` : init module
- `address_map/__manifest__.py` : manifest Odoo
- `address_map/models/` : modèles Python (contacts, config)
- `address_map/views/` : vues XML (contact, settings)

## Installation

1. **Cloner le repository**
