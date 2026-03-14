import networkx as nx
import matplotlib.pyplot as plt
from donnees_bus import LIAISONS_PARIS


G = nx.MultiGraph()
for s1, s2, ligne, temps in LIAISONS_PARIS:
    G.add_edge(s1, s2, bus=ligne, weight=temps)

def maj_graphe(chemin=None):
    plt.clf() 
    
    
    pos = nx.spring_layout(G, seed=42)
    
   
    couleurs_noeuds = []
    for n in G.nodes():
        if chemin and n in chemin:
            couleurs_noeuds.append('red') 
        else:
            couleurs_noeuds.append('skyblue')

    
    couleurs_aretes = []
    largeurs = []
    
    
    trajet_edges = []
    if chemin:
        for i in range(len(chemin)-1):
            trajet_edges.append((chemin[i], chemin[i+1]))
            trajet_edges.append((chemin[i+1], chemin[i]))

    for u, v in G.edges():
        if (u, v) in trajet_edges:
            couleurs_aretes.append('red')
            largeurs.append(3.5)
        else:
            couleurs_aretes.append('black')
            largeurs.append(1.0)

   
    nx.draw(G, pos, with_labels=True, node_color=couleurs_noeuds, 
            edge_color=couleurs_aretes, width=largeurs, node_size=800, font_size=8)
    
    
    labels_bus = nx.get_edge_attributes(G, 'bus')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_bus, font_size=7)
    
    plt.title("Plan du reseau de bus")
    plt.draw()
    plt.pause(0.1)


plt.ion() 
plt.show()
maj_graphe()

while True:
    print("\n--- CALCUL D'ITINERAIRE ---")
    depart = input("Station de depart (ou 'stop') : ")
    if depart.lower() == 'stop':
        break
    arrivee = input("Station d'arrivee : ")

    try:
        
        trajet = nx.shortest_path(G, source=depart, target=arrivee, weight='weight')
        
        print("\nResultat :", " -> ".join(trajet))
        
        
        bus_en_cours = ""
        for i in range(len(trajet)-1):
            
            info = G.get_edge_data(trajet[i], trajet[i+1])[0]
            if info['bus'] != bus_en_cours:
                print(f"Prendre le Bus {info['bus']} à '{trajet[i]}'")
                bus_en_cours = info['bus']
        
        
        maj_graphe(trajet)
        
    except:
        print("Erreur : Station introuvable ou pas de trajet.")

    encore = input("\nCalculer un autre trajet ? (o/n) : ")
    if encore.lower() != 'o':
        break

print("Fin du programme.")
plt.ioff()
plt.show()