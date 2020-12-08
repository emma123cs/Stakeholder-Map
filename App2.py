import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.DataFrame({"Stakeholder": ["Government", "Investors", "Foundations", "NGO", "UN", "Universities & Academia", "Corporates", "Startups & Unterstützungsprogramme", "User Persona"], "Stakeholder2": [["Juliet Nyrianeza – Ministry of Education (MINEDUC)", "James Ngoga –Rwanda Education Board (REB)", "Vedaste Hakizimana, Christophe Nteziryayo – Ministry of Local Government (MINALOC)", "Augustine Rwomushana – City of Kigali", "Rwanda Agriculture Board (RAB)", "Saidi Sibomana – Local Administrative Entities Development Agency"],
                                                                                                                                                                                                           ["Pacific Tuyishime – Rwanda Development Board", "Martha Phiri, Dr. Claudine Uwera – Rwanda Innovation Fund", "Martha Phiri – African Development Bank", "Dr. Claudine Uwera – Rwandan Government", "Jeremy Wakeford – SIFEM / Obviam", "Hannah Fanning – East Africa Investment Ltd.", "Tom Chaplin – Factor e ventures", "Angela Homsi – Angaza Innovation Fund by Ignite Investments", "Maral Browaldh – Swedfund", "Tenke A. Zoltani – Joint SDG Fund, Better Finance", "Auraib Zahid – TLG Capital", "Martina Straub – Oikocredit", "Konstantin Hapkemeyer – Seedstars, CH", "Huseyin R Demirhisar – World Business Angel Forum"],
                                                                                                                                                                                                           ["Jean Claude Muhire, Dr. Beyhan Şentürk – Friedrich Ebert Stiftung", "Guido von Westerholt – Westerwelle Foundation", "Blaise Dusi – Startup Haus Kigali", "Susanne Peitzmann – Evonik Stiftung", "Stefan Henkelmann – Sparkassenstiftung", "Alice Nkulikiyinka – Business Professionals Network (BPN)", "Stade Muhanga – Hilfswerk Magrit Fuchs Ruanda", "Innocent Uwimana, Violaine Gauthier, Sidone Uwimpuhwe – Clinton Foundation", "Paulin Basinga, Caroline Jehu-Appiah – Bill & Melinda Gates Foundation", "Joe Murphy, Sarah O'Carroll – Ellen McArthur Foundation", "Rwanda Children Education Foundation (RCEF)", "Rica Rwigamba, Diana Dusaidi – Mastercard Foundation"],
                                                                                                                                                                                                           ["Alice Kamau – Food for the Hungry", "Imad Madanat – Adventist Development and Relief Agency (ADRA)", "Caritas Internationalis Rwanda", "Alemayehu Gebremariam – Catholic Relieve Service", "Nick Osborne – CARE International Rwanda", "Kevin Sanderson – Word Relief", "Alice Simington – Concern Worldwide Rwanda", "Désiré Assogbavi – Oxfam International", "Raymond Gbekie – Organization for Poverty Alleviation and Development (OPAD)", "Courtney Lathrop-Juhl – End Poverty Now (EPN)", "Bruce Hickling – Innovations for Poverty Action", "Anna-Katharina Dietrich – European Anti-Poverty Network", "Bobby Shriver – ONE", "Allieu Samuel Bangura – World Hope International", "Anaïs Angoulvant – Trickle Up", "Md Nurnabi – BRAC"],
                                                                                                                                                                                                           ["Abebaw Alemayehu – World Bank", "Caritas Kayilisa – Food and Argiculture Organization (FAO)", "Jean Pierre de Margerie – World Food Programme (WFP)", "Paul Newnham – UN", "Julianna Lindsey – UNICEF", "Walter Huber – World Vision"],
                                                                                                                                                                                                           ["Industry Innovation Lab, Carnegie MellonUniversity Kigali", "Pacifiique Hallellua, Malte Koslowski – Klab, University of Rwanda", "University of Rwanda College of Agriculture, Animal Science and Veterinary Medicine", "University of Rwanda School of Agriculture Engineering", "University of Rwanda School of Agriculture and Food Science", "University of Rwanda College of Business and Economics", "Salomon Nshimiyimana – SDSN, University of Rwanda College of Business and Economics", "Rwanda Global Diaspora Network", "Pereez Nimusima, Nathan Karuhanga, Dativ Mukarutesi – University Jönköping - Sweden Program", "Dr. Thom Achterbosch, Prof. Dr. Arjen Wals – Wageningen University, NL", "Prof. Dr. Alfons Balmann – Leibniz Institut für Agrarentwicklung in Transformationsökonomien", "Margitta Minah – Seminar für ländliche Entwicklung", "Prof. Dr. Harald Grethe, Prof. Dr. Peter Feindt, Prof. Dr. Wolfgang Bokelmann – Food Berlin", "Ulrich Binkert – Germany Trade and Invest (GTAI)", "Prof. Dr. Berthold Hornetz – Uni Trier", "Prof. Sheryl Hendriks – University of Pretoria, South Africa", "Stephan Klingebiel – Deutsches Institut für Entwicklung", "Prof. Dr. Bernhard Brümmer – Georg August Universität Göttingen", "John Ingram – University of Oxford", "Lehrstuhl für Nachhaltigkeitsmanagement – HSG", "Center for Energy Innovation, Governance and Investment (EGI-HSG) – HSG", "Oikos – HSG", "Student Impact – HSG", "Pieces – HSG", "Ignite – HSG", "Youth Engagement – HSG", "BenEdu Service Learning – HSG, Migros", "U Change – Akademien der Wissenschaft, Bund", "Institut für Wirtschaftsethik (IWE-HSG) – HSG", "Center for Leadership and Values in Society (CLVS-HSG) – HSG", "Center for Organizational Excellence (CORE) – HSG, UniGe", "Executive School of Management, Technology, and Law – HSG", "Institute for Supply Chain Management (ISCM-HSG)– HSG", "Institut für Systemisches Management und Public Governance (IMP-HSG) – HSG", "Rigor and Relevance in Sustainability Management Research – HSG", "Smart Government Lab – HSG", "RISE Management Innovation Lab – HSG", "Institut für Klein- und Mittelunternehmen (KMU-HSG) – HSG", "Center for Family Business (CFB-HSG) – HSG", "Institut für Technologiemanagement (ITEM-HSG) – HSG", "Food Tech Lab – HSG", "Chair of Entrepreneurship – HSG", "Startup Navigator Lab – HSG", "Startup@HSG – HSG", "Strategic Entrepreneurship Research Lab – HSG", "Chair of Innovation Management – HSG", "Emerging Technologies Lab – HSG", "Center for Global R&D and Innovation (GLORAD) – HSG", "Center for Innovation (CFI-HSG) – HSG", "Chair of Operations Management", "Bosch IoT Lab – HSG, ETH, Bosch Group", "Chair of Production Management – HSG", "Global Center for Entrepreneurship & Innovation (GCEI-HSG) – HSG", "Center for Impact-Driven Entrepreneurship and Public Innovation (IDEPI-HSG) – HSG", "Business Model Innovation Lab", "Competence Center Open Innovation – HSG", "Institut für Betriebswirtschaft (IfB-HSG) – HSG", "Kompetenzzentrum Innovative Geschäftsmodelle & Wettbewerbsstrategien – HSG", "Zentrum für Religion, Wirtschaft und Politik (ZRWP) – UniBas, UZH, UniLu, UNIL", "Forschungsstelle für Nachhaltige Energie- und Wasserversorgung – UniBas", "Center for Research in Economics and Well-Being (CREW) – UniBas", "Center for Innovative Finance – UniBas", "Students for Sustainability at the University of Basel (SDUBS) – UniBas", "Future Cities Laboratory (FCL) – ETH", "World Food System Center – ETH", "Kompetenzzentrum für Klimamodellierung (C2SM) – ETH", "Group for Sustainability and Technology (SusTec) – ETH", "Sustainability in Business Lab (Sus.lab) – ETH", "Student Sustainability Commission – ETH", "Social Innovation Lab – ETH", "Food and Agro – ETH", "Koordinationsstelle für Nachhaltige Entwicklung – UniBe", "Interdisziplinäres Zentrum für Nachhaltige Entwicklung und Umwelt (CDE) – UniBe", "World Trade Institute (WTI) – UniBe", "Kompetenzzentrum für Public Management – UniBe", "Center for Corporate Responsibility and Sustainability (CCRS) – UZH", "Center for Sustainable Finance and Private Wealth – UZH", "Kommission für Entwicklungsfragen (KfE) – UZH, ETH", "Geneva Public-Private Partnership Center – UniGe", "Environmental Governance & Territorial Development Institute – UniGe", "Geneva Water Hub (pôle eau) – UniGe", "Geneva Science Policy Interface (SPI) – UniGe", "Ecoinvent Centre – EPFL, ETH, Agroscope", "Kompetenzzentrum Energie und Umwelt (CCEM) – EPFL, ETH, PSI, WSL, EAWAG, EMPA, FHNW", "Yunus Social Business Center – EPFL", "Tech4Impact – EPFL", "ACT for Change Lab – EPFL", "Sustainability Incubator (SINC) – USI", "Faculté des sciences économiques – UniNE", "Commission du développement durable (UniD) – UniNe", "Institut für Ecopreneurship – FHNW"],
                                                                                                                                                                                                           ["George Kiongo, Britt Broersen – Danone", "Deus Rugigana – Unilever", "Dr. Evelina Parvanova – Handwerkskammer Koblenz", "Walter Roodt – Zambeef Products Plc.", "Harry Bloechlinger – Bühler", "Elizabeth Ohola – Nestle", "Ngarambe Justine – Simba Supermarket Ltd."],
                                                                                                                                                                                                           ["Lauren Nkuranga – Get it", "Trevor Augustine – Minimex", "Sina Gerard – Sina Gerard", "Segond Fidens – Park & Pick", "Pearl Umuhoza – Yummy N Fresh", "Fair Forward GIZ", "Leonie Munk – Make IT Africa", "Africa AI Accelerator Program", "Cathy Sall – International Trade Centre by UN", "Johanna Nicholas – European Business Chamber of Rwanda", "Stella Murungi – Norrsken Foundation", "Johanna Nicholas – Imanzi Business Institute", "Mafer Betancourt – Impact Hub Kigali", "Prof. Dr. Michael Gielnik – STEP in Zusammenarbeeit mit Leuphana", "Prof. Dr. Harald von Korflesch – StAfrica - Startup Germany-Africa"],
                                                                                                                                                                                                           ["x4", "y4"]]})
#print(df)

#Importance_of_Stakeholder = {"Government": 4, "Investors": 3, "Foundations": 2, "NGO": 1}

Role = {"Government": "Scalability", "Investors": "Scalability", "Foundations": "Implementation", "NGO": "User-centricity", "City of Kigali": "Scalability", "Administration": "Scalability", "VC": "Scalability", "Rocket": "Scalability", "DAAD": "Implementation", "EllenMcArthur": "Implementation", "UNICEF": "User-centricity", "UNEP": "User-centricity"}
    
# Create Graph with edges between Main Stakeholders (those written in first column of DF)
# Third element of edge displays weighted Importance of Relationship
G = nx.MultiDiGraph()
count = 0
for item in range(len(df["Stakeholder"])):
    u = df.iloc[8, 0]
    v = df.iloc[0 + count, 0]
    G.add_edge(u,v)
    count += 1
    length = int(len(df["Stakeholder"])) - 1
    if count == length:
        break 
#print(G.edges)
#G.add_edge(df.iloc[0,0], df.iloc[(int(len(df["Stakeholder"])) - 1), 0])        
# Subgraphs
count1 = 0
for item in range(len(df["Stakeholder"])-1):
    u = df.iloc[item, 0]
    counts = 0
    for element in df.iloc[item, 1]:
        #print(element)
        v = element
        G.add_edge(u,v)
        counts += 1
        if counts == int(len(df.iloc[item, 1])):
            break
                           
# Formatting            
#elarge = [(u, v) in G.edges(data=True) if c["weight"] > 3]
#esmall = [(u, v) in G.edges(data=True) if c["weight"] <= 3]

#print(G.edges)    
#print(G.nodes)
           
    
#pos = nx.spring_layout(G)
#pos = nx.planar_layout(G)
pos = {"Government": [10,10], "Investors": [0,10], "Foundations": [25,-5], "NGO": [-5,-10], "UN": [-10,-2], "Universities & Academia": [25,5], "Corporates":[-7.5,5], "Startups & Unterstützungsprogramme":[7,- 9], "User Persona":[7,0]}


import math
pi = math.pi
def PointsInCircum(r,n):
    n=n+1
    x= [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]
    x[-1]=(x[-2][0]+0.3,x[-2][1]+0.3)
    return x


point=PointsInCircum(10.5, 7)
pos["User Persona"]=[0,0]
poslst=list(pos.keys())
poslst.remove("User Persona")
for item in range(len(point)-1):
    n = poslst[item]
    point1 = point[item]
    x = point1[0]
    y = point1[1] 
    pos[n] = [x,y]
 
points = PointsInCircum(3, n = len(list(G.neighbors("Investors")))-1)
neighbors=list(G.neighbors("Investors"))
if "User Persona" in neighbors:
    neighbors.remove("User Persona")
for item in range(len(points)-1):
    n = neighbors[item]
    point1 = points[item]
    x = point1[0] + pos["Investors"][0]
    y = point1[1] + pos["Investors"][1]
    pos[n] = [x,y]

points = PointsInCircum(3, n = len(list(G.neighbors("Government")))-1)
neighbors=list(G.neighbors("Government"))
if "User Persona" in neighbors:
    neighbors.remove("User Persona")
for item in range(len(points)-1):
    n = neighbors[item]
    point1 = points[item]
    x = point1[0] + pos["Government"][0]
    y = point1[1] + pos["Government"][1]
    pos[n] = [x,y]
    
points = PointsInCircum(3, n = len(list(G.neighbors("NGO")))-1)
neighbors=list(G.neighbors("NGO"))
if "User Persona" in neighbors:
    neighbors.remove("User Persona")
for item in range(len(points)-1):
    n = neighbors[item]
    point1 = points[item]
    x = point1[0] + pos["NGO"][0]
    y = point1[1] + pos["NGO"][1]
    pos[n] = [x,y]
    
points = PointsInCircum(3, n = len(list(G.neighbors("Foundations")))-1)
neighbors=list(G.neighbors("Foundations"))
if "User Persona" in neighbors:
    neighbors.remove("User Persona")
for item in range(len(points)-1):
    n = neighbors[item]
    point1 = points[item]
    x = point1[0] + pos["Foundations"][0]
    y = point1[1] + pos["Foundations"][1]
    pos[n] = [x,y]
    
points = PointsInCircum(3, n = len(list(G.neighbors("UN")))-1)
neighbors=list(G.neighbors("UN"))
if "User Persona" in neighbors:
    neighbors.remove("User Persona")
for item in range(len(points)-1):
    n = neighbors[item]
    point1 = points[item]
    x = point1[0] + pos["UN"][0]
    y = point1[1] + pos["UN"][1]
    pos[n] = [x,y]
    
points = PointsInCircum(3, n = len(list(G.neighbors("Universities & Academia")))-1)
neighbors=list(G.neighbors("Universities & Academia"))
if "User Persona" in neighbors:
    neighbors.remove("User Persona")
for item in range(len(points)-1):
    n = neighbors[item]
    point1 = points[item]
    x = point1[0] + pos["Universities & Academia"][0]
    y = point1[1] + pos["Universities & Academia"][1]
    pos[n] = [x,y]      
    
points = PointsInCircum(3, n = len(list(G.neighbors("Corporates")))-1)
neighbors=list(G.neighbors("Corporates"))
if "User Persona" in neighbors:
    neighbors.remove("User Persona")
for item in range(len(points)-1):
    n = neighbors[item]
    point1 = points[item]
    x = point1[0] + pos["Corporates"][0]
    y = point1[1] + pos["Corporates"][1]
    pos[n] = [x,y]
    

points = PointsInCircum(3, n = len(list(G.neighbors("Startups & Unterstützungsprogramme")))-1)
neighbors=list(G.neighbors("Startups & Unterstützungsprogramme"))
if "User Persona" in neighbors:
    neighbors.remove("User Persona")
for item in range(len(points)-1):
    n = neighbors[item]
    point1 = points[item]
    x = point1[0] + pos["Startups & Unterstützungsprogramme"][0]
    y = point1[1] + pos["Startups & Unterstützungsprogramme"][1]
    pos[n] = [x,y]
    
    
##########################

#nx.draw_networkx_nodes(G, pos, node_size=400, node_color = "lightblue")

#nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2, alpha = 1)
#nx.draw_networkx_edges(G, pos, edgelist=esmall, width=1.5, alpha=0.5)

#nx.draw_networkx_labels(G, pos, font_size=15, font_family="Times New Roman", font_weight="bold")

#plt.figure(figsize=(10,1)) 
#plt.axis("off")
#plt.show()


######################Plotly##########################
import dash
import dash_core_components as dcc
import dash_html_components as html
import networkx as nx
import plotly.graph_objs as go
import pandas as pd
from colour import Color
from textwrap import dedent as d
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Stakeholder Map"

traceRecode = []


for node in G.nodes():
    x = pos[node][0]
    y = pos[node][1]
    text = node
    hovertext = "Stakeholder Name: " + str(node) #+ "\n" + "Role at LoT: " + str(Role[node])
    node_trace = go.Scatter(x=[], y=[], text=[], hovertext = [], mode='markers+text', textposition="top center", textfont_size= 16, textfont_color= "black",textfont_family = "Arial", marker={'size': 20, 'color': 'LightBlue', 'line_width': 1})
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    node_trace['hovertext'] += tuple([hovertext])
    if text in ["Government", "Investors", "Foundations", "NGO", "UN", "Universities & Academia", "Corporates", "Startups & Unterstützungsprogramme", "User Persona"]:
        node_trace['text'] += tuple([text])
    traceRecode.append(node_trace)

        

for edge in G.edges:
    source = edge[0]
    target = edge[1]
    x0, y0 = pos[source][0], pos[source][1]
    x1, y1 = pos[target][0], pos[target][1]
    trace = go.Scatter(x=tuple([x0, x1]), y=tuple([y0, y1]),
                       mode='lines',
                       line={'width': 2},
                       marker=dict(color="LightBlue"),
                       line_shape='spline',
                       opacity=1,
                       )
    traceRecode.append(trace)

traceRecode2=[]

nodelst=list(G.neighbors("Startups & Unterstützungsprogramme"))
nodelst+=list(G.neighbors("NGO"))
nodelst+=list(G.neighbors("Universities & Academia"))
nodelst.append("Startups & Unterstützungsprogramme")
nodelst.append("NGO")
nodelst.append("Universities & Academia")
for node in nodelst:
    x = pos[node][0]
    y = pos[node][1]
    text = node
    hovertext = "Stakeholder Name: " + str(node) #+ "\n" + "Role at LoT: " + str(Role[node])
    node_trace = go.Scatter(x=[], y=[], text=[], hovertext = [], mode='markers+text', textposition="top center", textfont_size= 16, textfont_color= "black",textfont_family = "Arial", marker={'size': 20, 'color': 'LightBlue', 'line_width': 1})
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    node_trace['hovertext'] += tuple([hovertext])
    if text in ["Government", "Investors", "Foundations", "NGO", "UN", "Universities & Academia", "Corporates", "Startups & Unterstützungsprogramme", "User Persona"]:
        node_trace['text'] += tuple([text])
    traceRecode2.append(node_trace)


trace_lst=list(G.edges("Startups & Unterstützungsprogramme"))
trace_lst+=list(G.edges("NGO"))
trace_lst+=list(G.edges("Universities & Academia"))
trace_lst+=[("NGO", "Universities & Academia")]
trace_lst+=[("NGO", "Startups & Unterstützungsprogramme")]
trace_lst+=[("Startups & Unterstützungsprogramme", "Universities & Academia")]
for edge in trace_lst:
    source = edge[0]
    target = edge[1]
    x0, y0 = pos[source][0], pos[source][1]
    x1, y1 = pos[target][0], pos[target][1]
    trace = go.Scatter(x=tuple([x0, x1]), y=tuple([y0, y1]),
                       mode='lines',
                       line={'width': 2},
                       marker=dict(color="LightBlue"),
                       line_shape='spline',
                       opacity=1,
                       )
    traceRecode2.append(trace)

traceRecode3=[]

nodelst2=list(G.neighbors("Corporates"))
nodelst2+=list(G.neighbors("Investors"))
nodelst2+=list(G.neighbors("Foundations"))
nodelst2.append("Corporates")
nodelst2.append("Investors")
nodelst2.append("Foundations")
for node in nodelst2:
    x = pos[node][0]
    y = pos[node][1]
    text = node
    hovertext = "Stakeholder Name: " + str(node) #+ "\n" + "Role at LoT: " + str(Role[node])
    node_trace = go.Scatter(x=[], y=[], text=[], hovertext = [], mode='markers+text', textposition="top center", textfont_size= 16, textfont_color= "black",textfont_family = "Arial", marker={'size': 20, 'color': 'LightBlue', 'line_width': 1})
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    node_trace['hovertext'] += tuple([hovertext])
    if text in ["Government", "Investors", "Foundations", "NGO", "UN", "Universities & Academia", "Corporates", "Startups & Unterstützungsprogramme", "User Persona"]:
        node_trace['text'] += tuple([text])
    traceRecode3.append(node_trace)


trace_lst2=list(G.edges("Corporates"))
trace_lst2+=list(G.edges("Investors"))
trace_lst2+=list(G.edges("Foundations"))
trace_lst2+=[("Corporates", "Investors")]
trace_lst2+=[("Corporates", "Foundations")]
trace_lst2+=[("Investors", "Foundations")]
for edge in trace_lst2:
    source = edge[0]
    target = edge[1]
    x0, y0 = pos[source][0], pos[source][1]
    x1, y1 = pos[target][0], pos[target][1]
    trace = go.Scatter(x=tuple([x0, x1]), y=tuple([y0, y1]),
                       mode='lines',
                       line={'width': 2},
                       marker=dict(color="LightBlue"),
                       line_shape='spline',
                       opacity=1,
                       )
    traceRecode3.append(trace)

traceRecode4=[]

nodelst3=list(G.neighbors("Government"))
nodelst3+=list(G.neighbors("UN"))
nodelst3.append("Government")
nodelst3.append("UN")
for node in nodelst3:
    x = pos[node][0]
    y = pos[node][1]
    text = node
    hovertext = "Stakeholder Name: " + str(node) #+ "\n" + "Role at LoT: " + str(Role[node])
    node_trace = go.Scatter(x=[], y=[], text=[], hovertext = [], mode='markers+text', textposition="top center", textfont_size= 16, textfont_color= "black",textfont_family = "Arial", marker={'size': 20, 'color': 'LightBlue', 'line_width': 1})
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    node_trace['hovertext'] += tuple([hovertext])
    if text in ["Government", "Investors", "Foundations", "NGO", "UN", "Universities & Academia", "Corporates", "Startups & Unterstützungsprogramme", "User Persona"]:
        node_trace['text'] += tuple([text])
    traceRecode4.append(node_trace)


trace_lst3=list(G.edges("Government"))
trace_lst3+=list(G.edges("UN"))
trace_lst3+=[("Government", "UN")]
for edge in trace_lst3:
    source = edge[0]
    target = edge[1]
    x0, y0 = pos[source][0], pos[source][1]
    x1, y1 = pos[target][0], pos[target][1]
    trace = go.Scatter(x=tuple([x0, x1]), y=tuple([y0, y1]),
                       mode='lines',
                       line={'width': 2},
                       marker=dict(color="LightBlue"),
                       line_shape='spline',
                       opacity=1,
                       )
    traceRecode4.append(trace)

traceRecode5=[]

nodelst4=list(G.neighbors("User Persona"))
nodelst4.append("User Persona")
for node in nodelst4:
    x = pos[node][0]
    y = pos[node][1]
    text = node
    hovertext = "Stakeholder Name: " + str(node) #+ "\n" + "Role at LoT: " + str(Role[node])
    node_trace = go.Scatter(x=[], y=[], text=[], hovertext = [], mode='markers+text', textposition="top center", textfont_size= 16, textfont_color= "black",textfont_family = "Arial", marker={'size': 20, 'color': 'LightBlue', 'line_width': 1})
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    node_trace['hovertext'] += tuple([hovertext])
    if text in ["Government", "Investors", "Foundations", "NGO", "UN", "Universities & Academia", "Corporates", "Startups & Unterstützungsprogramme", "User Persona"]:
        node_trace['text'] += tuple([text])
    traceRecode5.append(node_trace)


trace_lst4=list(G.edges("User Persona"))
for edge in trace_lst4:
    source = edge[0]
    target = edge[1]
    x0, y0 = pos[source][0], pos[source][1]
    x1, y1 = pos[target][0], pos[target][1]
    trace = go.Scatter(x=tuple([x0, x1]), y=tuple([y0, y1]),
                       mode='lines',
                       line={'width': 2},
                       marker=dict(color="LightBlue"),
                       line_shape='spline',
                       opacity=1,
                       )
    traceRecode5.append(trace)

jointlst=traceRecode+traceRecode2+traceRecode3+traceRecode4+traceRecode5
figure = go.Figure(
    data= jointlst,
    layout= go.Layout(title='Clusters                                                                                                                               by Group E', showlegend=False,
                        margin={'b': 10, 'l': 10, 'r': 10, 't': 30},
                        xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                        yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                        height=1500,
                        clickmode='event+select'))

lst2=[False]*len(traceRecode) + [True]*len(traceRecode2) + [False]*(len(traceRecode3)+len(traceRecode4)+len(traceRecode5)) #Innovative Ideas
lst3=[False]*(len(traceRecode)+len(traceRecode2)) +[True]*len(traceRecode3)+ [False]*(len(traceRecode4)+len(traceRecode5))  #Scalability
lst4=[False]*(len(traceRecode)+len(traceRecode2)+len(traceRecode3))+[True]*len(traceRecode4)+[False]*len(traceRecode5) #Implementation
lst5=[False]*(len(traceRecode)+len(traceRecode2)+len(traceRecode3)+len(traceRecode4))+[True]*len(traceRecode5) #User Persona
figure.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": True},
                           {"title": "Clusters                                                                                                                               by Group E"}]),
                dict(label="User Persona",
                     method="update",
                     args=[{"visible": lst5},
                           {"title": "Clusters                                                                                                                               by Group E",}]),
                dict(label="Innovative Ideas",
                     method="update",
                     args=[{"visible": lst2},
                           {"title": "Clusters                                                                                                                               by Group E",}]),
                dict(label="Scalability",
                     method="update",
                     args=[{"visible": lst3},
                           {"title": "Clusters                                                                                                                               by Group E",}]),
                dict(label="Implementation",
                     method="update",
                     args=[{"visible": lst4},
                           {"title": "Clusters                                                                                                                               by Group E",}])]))])

app.layout = html.Div([
    html.Div([html.H1("Stakeholder Map - Access to Food")],
             className="row",
             style={'textAlign': "center"}),
    html.Div(className="twelve columns",
             children=[dcc.Graph(id="my-graph",
                                figure=figure)])])
  

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=5000)
