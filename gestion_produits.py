import json,os

def read_json(fichier):
    if os.path.exists(fichier):
        with open(fichier,"r",encoding="utf-8") as file:
            return json.load(file)
    else:
        print("Fichier introuvable")

def write_on_json(fichier,data):
    try:
        with open(fichier,"w") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)
            print("Fichier enregistré avec succès ")
    except Exception as e:
        print("on a une ERREUR :",e)

#Afficher les produit trié par vente decroissante
def afficher_produit(fichier):
    produit = read_json(fichier)
    produit_trie = sorted(produit,key= lambda x:x["ventes"],reverse=True)
    for dicte in produit_trie:
        print(f'nom: {dicte["nom"]:15} | prix: {dicte["prix"]:15} | ventes: {dicte["ventes"]:15}')
        print("-"*70)

fichier  ="produits_magasin.json"
afficher_produit(fichier)
