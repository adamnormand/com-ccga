# -*- coding: utf-8 -*-
"""Regional subsites — EN / FR.
Sources (read 2026-11-21): rcmsar.com, cn-cga.ca, ccga-ca.com, gcac-q.ca, ccga-m.ca, ccga-nl.ca,
and the regional profile pages on ccga-gcac.ca."""

def facts(items):
    return '<div class="stats">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in items) + "</div>"

REGIONS = []

# =====================================================================  PACIFIC — RCMSAR
REGIONS.append({
 "key": "pacific",
 "path": {"en": "pacific", "fr": "pacifique"},
 "name": {"en": "Pacific — RCMSAR", "fr": "Pacifique — RCMSAR"},
 "short": {"en": "Pacific RCM-SAR", "fr": "Pacifique RCM-SAR"},
 "org": {"en": "Royal Canadian Marine Search and Rescue", "fr": "Royal Canadian Marine Search and Rescue"},
 "sub": {"en": "Pacific region · British Columbia", "fr": "Région du Pacifique · Colombie-Britannique"},
 "area": {"en": "BC coast and the Shuswap", "fr": "Côte de la C.-B. et Shuswap"},
 "figure": {"en": "950+ volunteers · 29 stations", "fr": "950+ bénévoles · 29 stations"},
 "lead": {"en": "Volunteer marine rescue on 450,000 km² of British Columbia's coastal and inland waters.",
          "fr": "Sauvetage maritime bénévole sur 450 000 km² d'eaux côtières et intérieures de la Colombie-Britannique."},
 "emergency": {"en": "JRCC Victoria: 1-800-567-5111 · VHF 16 · *16, #727 or 911",
               "fr": "CCCS Victoria : 1-800-567-5111 · VHF 16 · *16, #727 ou 911"},
 "president": "Tracy Lakeman, Chair · Bill Riggs, CEO",
 "join": "volunteer", "donate": "donate",
 "contact_block": {
   "en": "<strong>Royal Canadian Marine Search and Rescue</strong><br>6040 East Sooke Road<br>Sooke, BC V9Z 0Z7<br>1-800-665-4757<br><a href=\"mailto:info@rcmsar.com\">info@rcmsar.com</a>",
   "fr": "<strong>Royal Canadian Marine Search and Rescue</strong><br>6040, East Sooke Road<br>Sooke (C.-B.) V9Z 0Z7<br>1-800-665-4757<br><a href=\"mailto:info@rcmsar.com\">info@rcmsar.com</a>"},
 "website": "https://rcmsar.com/",
 "nav": ["stations", "kids-dont-float", "volunteer", "contact"],
 "pages": {
  "index": {"slug": {"en": "", "fr": ""},
   "title": {"en": "Royal Canadian Marine Search and Rescue", "fr": "Royal Canadian Marine Search and Rescue"},
   "hero": {"en": ("We are the charity that saves lives on the water", "More than 950 volunteers operating 29 rescue stations on the coast of British Columbia and the inland waters of the Shuswap — on call 24 hours a day, 365 days a year."),
            "fr": ("L'organisme de bienfaisance qui sauve des vies sur l'eau", "Plus de 950 bénévoles exploitent 29 stations de sauvetage sur la côte de la Colombie-Britannique et les eaux intérieures de la Shuswap — en disponibilité 24 heures sur 24, 365 jours par année.")},
   "body": {
    "en": """
<section class="wrap split">
<div class="prose">
<p class="eyebrow">Who we are</p>
<h2>A key part of the marine search and rescue system</h2>
<p>Royal Canadian Marine Search and Rescue (RCMSAR) is the Canadian Coast Guard Auxiliary for the Pacific region: a not-for-profit, volunteer-based organization operating rescue stations from Vancouver's busy harbour to the remote waters of the North Coast. Its area of operations covers more than 25,000 km of rugged coastline known for challenging weather and sea conditions.</p>
<p>Volunteers have been part of marine rescue on the BC coast for more than 100 years. In 1978, volunteer groups across Canada created the Canadian Coast Guard Auxiliary; in 2012 the Pacific auxiliary took the name Royal Canadian Marine Search and Rescue. The mission remains the same — saving lives on the water.</p>
<h2>How we save lives</h2>
<p>Through an agreement with the Canadian Coast Guard, crews are tasked to marine emergencies by the Joint Rescue Coordination Centre in Victoria. RCMSAR is also available for humanitarian aid on the water when called upon by provincial authorities. Each station is run by station leaders and a local governance board, with oversight and support from headquarters in Sooke. RCMSAR crews handle roughly one quarter of all marine rescues in the region each year.</p>
<h2>Vision and values</h2>
<p>Excellence in community-based marine safety, built on <b>safety</b>, <b>trust</b> and <b>teamwork</b> — and a “one-crew” culture.</p>
</div>
<div>
{facts}
<div class="card accent"><h3>2025 Lieutenant Governor's Marine Achievement Award</h3><p>On behalf of its volunteers, past and present, RCMSAR received the 2025 Lieutenant Governor's Award for Marine Achievement.</p></div>
</div>
</section>""",
    "fr": """
<section class="wrap split">
<div class="prose">
<p class="eyebrow">Qui nous sommes</p>
<h2>Un maillon essentiel du système de recherche et sauvetage maritimes</h2>
<p>Royal Canadian Marine Search and Rescue (RCMSAR) est la Garde côtière auxiliaire de la région du Pacifique : un organisme sans but lucratif, fondé sur le bénévolat, qui exploite des stations de sauvetage du port achalandé de Vancouver jusqu'aux eaux isolées de la côte Nord. Son territoire couvre plus de 25 000 km d'un littoral accidenté, réputé pour ses conditions météo et de mer difficiles.</p>
<p>Des bénévoles participent au sauvetage maritime sur la côte de la C.-B. depuis plus de 100 ans. En 1978, des groupes bénévoles de partout au pays ont créé la Garde côtière auxiliaire canadienne; en 2012, l'auxiliaire du Pacifique a pris le nom de Royal Canadian Marine Search and Rescue. La mission demeure : sauver des vies sur l'eau.</p>
<h2>Comment nous sauvons des vies</h2>
<p>En vertu d'une entente avec la Garde côtière canadienne, les équipages sont dépêchés par le Centre conjoint de coordination de sauvetage de Victoria. RCMSAR peut aussi offrir de l'aide humanitaire sur l'eau à la demande des autorités provinciales. Chaque station est dirigée par ses chefs et un conseil local, avec la supervision et le soutien du siège social de Sooke. Les équipages de RCMSAR effectuent environ le quart des sauvetages maritimes de la région chaque année.</p>
<h2>Vision et valeurs</h2>
<p>L'excellence en sécurité maritime communautaire, fondée sur la <b>sécurité</b>, la <b>confiance</b> et le <b>travail d'équipe</b> — et une culture « un seul équipage ».</p>
</div>
<div>
{facts}
<div class="card accent"><h3>Prix du lieutenant-gouverneur 2025 pour l'excellence maritime</h3><p>Au nom de ses bénévoles d'hier et d'aujourd'hui, RCMSAR a reçu le Prix du lieutenant-gouverneur 2025 pour l'excellence maritime.</p></div>
</div>
</section>"""},
   "facts": {"en": [("950+", "volunteers"), ("29", "marine rescue stations"), ("450,000 km²", "of internal and offshore waters"), ("500+", "calls for assistance in an average year")],
             "fr": [("950+", "bénévoles"), ("29", "stations de sauvetage maritime"), ("450 000 km²", "d'eaux intérieures et extracôtières"), ("500+", "appels d'assistance par année en moyenne")]}},

  "stations": {"slug": {"en": "stations", "fr": "stations"},
   "title": {"en": "Rescue stations", "fr": "Stations de sauvetage"},
   "body": {
    "en": """
<section class="wrap prose"><p class="lead">29 marine rescue stations on the BC coast and in the Interior, plus a boating safety station in Vancouver.</p></section>
<section class="wrap grid3">
<div class="card"><h3>Vancouver Island &amp; Gulf Islands</h3><ul class="plain"><li>Brentwood Bay — Station 31</li><li>Comox — Station 60</li><li>Cowichan — Station 34</li><li>Deep Bay — Station 59</li><li>Gulf Islands (Salt Spring) — Station 25</li><li>Ladysmith — Station 29</li><li>Nanaimo — Station 27</li><li>Oak Bay — Station 33</li><li>Pender Island — Station 20</li><li>Port Alberni — Station 39</li><li>Sidney — Station 36</li><li>Sooke — Station 37</li><li>Ucluelet — Station 38</li><li>Victoria — Station 35</li></ul></div>
<div class="card"><h3>Northern BC</h3><ul class="plain"><li>Hartley Bay — Station 70</li><li>Kitimat — Station 63</li><li>Lax Kw'alaams — Station 65</li><li>Masset — Station 45</li><li>Prince Rupert — Station 64</li></ul></div>
<div class="card"><h3>Southern BC &amp; the Interior</h3><ul class="plain"><li>Crescent Beach — Station 5</li><li>Delta — Station 8</li><li>Gibsons — Station 14</li><li>Halfmoon Bay — Station 12</li><li>North Vancouver — Station 2</li><li>Pender Harbour — Station 61</li><li>Richmond — Station 10</li><li>Shuswap — Station 106</li><li>Squamish — Station 4</li><li>West Vancouver — Station 1</li><li>Vancouver Boating Safety — Station 103</li></ul></div>
</section>""",
    "fr": """
<section class="wrap prose"><p class="lead">29 stations de sauvetage maritime sur la côte de la C.-B. et à l'intérieur des terres, en plus d'une station de sécurité nautique à Vancouver.</p></section>
<section class="wrap grid3">
<div class="card"><h3>Île de Vancouver et îles Gulf</h3><ul class="plain"><li>Brentwood Bay — station 31</li><li>Comox — station 60</li><li>Cowichan — station 34</li><li>Deep Bay — station 59</li><li>Îles Gulf (Salt Spring) — station 25</li><li>Ladysmith — station 29</li><li>Nanaimo — station 27</li><li>Oak Bay — station 33</li><li>Île Pender — station 20</li><li>Port Alberni — station 39</li><li>Sidney — station 36</li><li>Sooke — station 37</li><li>Ucluelet — station 38</li><li>Victoria — station 35</li></ul></div>
<div class="card"><h3>Nord de la C.-B.</h3><ul class="plain"><li>Hartley Bay — station 70</li><li>Kitimat — station 63</li><li>Lax Kw'alaams — station 65</li><li>Masset — station 45</li><li>Prince Rupert — station 64</li></ul></div>
<div class="card"><h3>Sud de la C.-B. et intérieur</h3><ul class="plain"><li>Crescent Beach — station 5</li><li>Delta — station 8</li><li>Gibsons — station 14</li><li>Halfmoon Bay — station 12</li><li>North Vancouver — station 2</li><li>Pender Harbour — station 61</li><li>Richmond — station 10</li><li>Shuswap — station 106</li><li>Squamish — station 4</li><li>West Vancouver — station 1</li><li>Sécurité nautique Vancouver — station 103</li></ul></div>
</section>"""}},

  "kids-dont-float": {"slug": {"en": "kids-dont-float", "fr": "kids-dont-float"},
   "title": {"en": "Kids Don't Float", "fr": "Kids Don't Float"},
   "body": {
    "en": """
<section class="wrap prose">
<p class="lead">Free loaner lifejackets for infants, children and youth at more than 100 docks, marinas and beaches on BC's coast and in the Shuswap.</p>
<p>Inspired by the State of Alaska's program of the same name, Kids Don't Float is supported by police, municipalities, marinas and community groups. Parents or guardians without a properly sized lifejacket simply borrow one from a kiosk and return it at the end of the day so other children can use it. The program protects young people from 6 months to 16 years.</p>
<p>Since 2003 the program has helped reduce child drowning deaths in our communities, and it won the Canadian Safe Boating Award for Best Boating Safety Initiative in 2018. In 2023, RCMSAR and SSA Marine announced a three-year funding partnership to grow it.</p>
<p class="small"><b>Fit matters.</b> Before use, parents and guardians must read the sizing instructions inside the lifejacket and check its condition; they are solely responsible for ensuring children wear an appropriately sized lifejacket.</p>
</section>""",
    "fr": """
<section class="wrap prose">
<p class="lead">Des gilets de sauvetage prêtés gratuitement aux bébés, enfants et adolescents dans plus de 100 quais, marinas et plages de la côte de la C.-B. et de la Shuswap.</p>
<p>Inspiré du programme du même nom de l'État de l'Alaska, Kids Don't Float est appuyé par les corps policiers, les municipalités, les marinas et des groupes communautaires. Les parents ou tuteurs qui n'ont pas de gilet de la bonne taille en empruntent un à un présentoir et le rapportent à la fin de la journée pour d'autres enfants. Le programme protège les jeunes de 6 mois à 16 ans.</p>
<p>Depuis 2003, le programme a contribué à réduire les noyades d'enfants dans nos communautés; il a remporté le Prix canadien de la sécurité nautique pour la meilleure initiative en 2018. En 2023, RCMSAR et SSA Marine ont annoncé un partenariat de financement de trois ans pour l'étendre.</p>
<p class="small"><b>La taille compte.</b> Avant usage, les parents et tuteurs doivent lire les consignes de taille à l'intérieur du gilet et en vérifier l'état; ils sont seuls responsables de s'assurer que l'enfant porte un gilet de la bonne taille.</p>
</section>"""}},

  "volunteer": {"slug": {"en": "volunteer", "fr": "benevolat"},
   "title": {"en": "Volunteer with RCMSAR", "fr": "Devenir bénévole chez RCMSAR"},
   "body": {
    "en": """
<section class="wrap split">
<div class="prose">
<p class="lead">Many crew members come from a marine background, but it is not a requirement. With time, commitment and RCMSAR's training plans, non-mariners become highly skilled crew.</p>
<h2>Your commitment</h2>
<ul><li>Regular training sessions and meetings on evenings and weekends</li><li>Living or working close to your station's boat launch</li><li>Responding to emergencies on short notice</li><li>Occasional community events</li></ul>
<h2>Crew qualifications</h2>
<ul><li>Over 19 years of age; Canadian citizen or permanent resident</li><li>Good physical condition and able to pass the annual RCMSAR Fitness Test</li><li>Three-month probationary period</li><li>Police Information Check, including Vulnerable Sector Check</li><li>Pleasure Craft Operator Certificate and Restricted Operator Certificate – Marine</li><li>Marine Basic First Aid or equivalent, with CPR/AED Level C</li></ul>
<p>Under 19? Ask your local station or headquarters about the junior program. Supporting members are welcome too: boating safety advocacy, vessel maintenance, fundraising and events, media and social media.</p>
</div>
<div>
<div class="card"><h3>Training path</h3>
<table><thead><tr><th>Level</th><th>Average time</th></tr></thead><tbody>
<tr><td>New crew</td><td>3–6 months</td></tr><tr><td>Crew</td><td>12–18 months</td></tr><tr><td>Advanced crew</td><td>12–18 months</td></tr><tr><td>Coxswain</td><td>12–24 months</td></tr></tbody></table>
<p class="small">Station training officers deliver weekly classroom and on-water training. Advanced seamanship training takes place at the RCMSAR Training Centre in East Sooke.</p></div>
<blockquote>“If you're in need of assistance, we will come and help as best we can and to the best of our abilities.”<cite>— James Henry, Station Leader, Lax Kw'alaams (Station 65)</cite></blockquote>
</div>
</section>""",
    "fr": """
<section class="wrap split">
<div class="prose">
<p class="lead">Bien des membres d'équipage viennent du milieu maritime, mais ce n'est pas obligatoire. Avec du temps, de l'engagement et les plans de formation de RCMSAR, des personnes sans expérience deviennent des équipiers aguerris.</p>
<h2>Votre engagement</h2>
<ul><li>Séances de formation et réunions régulières, en soirée et la fin de semaine</li><li>Habiter ou travailler près de la rampe de mise à l'eau de votre station</li><li>Répondre aux urgences à court préavis</li><li>Participer à l'occasion à des événements communautaires</li></ul>
<h2>Qualifications d'équipier</h2>
<ul><li>Plus de 19 ans; citoyenneté canadienne ou résidence permanente</li><li>Bonne condition physique et réussite du test annuel de condition physique de RCMSAR</li><li>Période probatoire de trois mois</li><li>Vérification policière, y compris auprès des personnes vulnérables</li><li>Carte de conducteur d'embarcation de plaisance et certificat restreint d'opérateur radio – maritime</li><li>Secourisme maritime de base ou l'équivalent, avec RCR/DEA niveau C</li></ul>
<p>Moins de 19 ans? Renseignez-vous sur le programme junior auprès de votre station ou du siège social. Les membres de soutien sont aussi les bienvenus : sécurité nautique, entretien des embarcations, collectes de fonds et événements, médias et réseaux sociaux.</p>
</div>
<div>
<div class="card"><h3>Parcours de formation</h3>
<table><thead><tr><th>Niveau</th><th>Durée moyenne</th></tr></thead><tbody>
<tr><td>Nouvel équipier</td><td>3 à 6 mois</td></tr><tr><td>Équipier</td><td>12 à 18 mois</td></tr><tr><td>Équipier avancé</td><td>12 à 18 mois</td></tr><tr><td>Patron d'embarcation</td><td>12 à 24 mois</td></tr></tbody></table>
<p class="small">Les responsables de la formation donnent chaque semaine des cours en classe et sur l'eau. La formation avancée en matelotage se donne au centre de formation de RCMSAR, à East Sooke.</p></div>
<blockquote>« Si vous avez besoin d'aide, nous viendrons vous aider du mieux que nous pouvons. »<cite>— James Henry, chef de station, Lax Kw'alaams (station 65)</cite></blockquote>
</div>
</section>"""}},

  "donate": {"slug": {"en": "donate", "fr": "donner"},
   "title": {"en": "Donate to RCMSAR", "fr": "Donner à RCMSAR"},
   "body": {
    "en": """<section class="wrap prose"><p class="lead">In the past year, more than 600 people were helped by RCMSAR volunteers — 67 of them might not be here today without that help.</p><p>Donations support volunteer training, keep equipment in excellent condition and fund prevention programs. You can also give through a legacy gift or securities.</p><p><a class="btn" href="https://rcmsar.com/donate/" rel="noopener">Donate to RCMSAR</a></p><p class="small">By phone: 1-800-665-4757 ext. 103 · <a href="mailto:funds.media@rcmsar.com">funds.media@rcmsar.com</a></p></section>""",
    "fr": """<section class="wrap prose"><p class="lead">Au cours de la dernière année, plus de 600 personnes ont reçu l'aide des bénévoles de RCMSAR — 67 d'entre elles ne seraient peut-être plus là sans cette aide.</p><p>Les dons financent la formation des bénévoles, l'entretien de l'équipement et les programmes de prévention. Vous pouvez aussi faire un don planifié ou un don de titres.</p><p><a class="btn" href="https://rcmsar.com/donate/" rel="noopener">Donner à RCMSAR</a></p><p class="small">Par téléphone : 1-800-665-4757, poste 103 · <a href="mailto:funds.media@rcmsar.com">funds.media@rcmsar.com</a></p></section>"""}},

  "contact": {"slug": {"en": "contact", "fr": "contact"},
   "title": {"en": "Contact RCMSAR", "fr": "Joindre RCMSAR"},
   "body": {
    "en": """
<section class="wrap split"><div class="prose">
<div class="card emergency-card"><h3>Marine emergency</h3><p>Joint Rescue Coordination Centre (JRCC) Victoria: <a href="tel:+18005675111"><strong>1-800-567-5111</strong></a> · VHF Channel 16 (156.8 MHz) · <strong>*16</strong>, <strong>#727</strong> or <strong>911</strong></p></div>
<h2>Headquarters</h2><p>6040 East Sooke Road, Sooke, BC V9Z 0Z7<br>General: <a href="tel:+18006654757">1-800-665-4757</a> · <a href="mailto:info@rcmsar.com">info@rcmsar.com</a><br>Volunteering: <a href="mailto:volunteer@rcmsar.com">volunteer@rcmsar.com</a><br>Donations: ext. 103 · <a href="mailto:funds.media@rcmsar.com">funds.media@rcmsar.com</a></p>
<h2>Media</h2><p><a href="mailto:media@rcmsar.com">media@rcmsar.com</a> · 1-778-352-2016. RCMSAR cannot comment on an active mission; for an active search, contact Maritime Forces Pacific (MARPAC) Media Relations at 604-666-1746.</p>
</div><div class="card"><h3>Leadership</h3><p>Tracy Lakeman, Chair<br>Bill Riggs, Chief Executive Officer — <a href="mailto:bill.riggs@rcmsar.com">bill.riggs@rcmsar.com</a></p><p class="small">Regional website: <a href="https://rcmsar.com/" rel="noopener">rcmsar.com</a></p></div></section>""",
    "fr": """
<section class="wrap split"><div class="prose">
<div class="card emergency-card"><h3>Urgence maritime</h3><p>Centre conjoint de coordination de sauvetage (CCCS) de Victoria : <a href="tel:+18005675111"><strong>1-800-567-5111</strong></a> · canal VHF 16 (156,8 MHz) · <strong>*16</strong>, <strong>#727</strong> ou <strong>911</strong></p></div>
<h2>Siège social</h2><p>6040, East Sooke Road, Sooke (C.-B.) V9Z 0Z7<br>Renseignements : <a href="tel:+18006654757">1-800-665-4757</a> · <a href="mailto:info@rcmsar.com">info@rcmsar.com</a><br>Bénévolat : <a href="mailto:volunteer@rcmsar.com">volunteer@rcmsar.com</a><br>Dons : poste 103 · <a href="mailto:funds.media@rcmsar.com">funds.media@rcmsar.com</a></p>
<h2>Médias</h2><p><a href="mailto:media@rcmsar.com">media@rcmsar.com</a> · 1-778-352-2016. RCMSAR ne commente pas une mission en cours; pour une recherche active, joignez les relations avec les médias des Forces maritimes du Pacifique (FMAR(P)) au 604-666-1746.</p>
</div><div class="card"><h3>Direction</h3><p>Tracy Lakeman, présidente du conseil<br>Bill Riggs, chef de la direction — <a href="mailto:bill.riggs@rcmsar.com">bill.riggs@rcmsar.com</a></p><p class="small">Site régional : <a href="https://rcmsar.com/" rel="noopener">rcmsar.com</a></p></div></section>"""}},
 }})

# =====================================================================  COASTAL NATIONS
REGIONS.append({
 "key": "coastal-nations",
 "path": {"en": "coastal-nations", "fr": "nations-cotieres"},
 "name": {"en": "Coastal Nations", "fr": "Nations côtières"},
 "short": {"en": "Coastal Nations", "fr": "Nations côtières"},
 "org": {"en": "Coastal Nations Coast Guard Auxiliary", "fr": "Garde côtière auxiliaire des Nations côtières"},
 "sub": {"en": "Pacific · Indigenous-led", "fr": "Pacifique · dirigée par des Autochtones"},
 "area": {"en": "BC coast — Member Nations' waters", "fr": "Côte de la C.-B. — eaux des Nations membres"},
 "figure": {"en": "11 Member Nations · founded 2018", "fr": "11 Nations membres · fondée en 2018"},
 "lead": {"en": "Canada's first Indigenous-led Coast Guard Auxiliary.", "fr": "La première garde côtière auxiliaire dirigée par des Autochtones au Canada."},
 "emergency": {"en": "JRCC Victoria: 1-800-567-5111 · VHF 16 · *16 or 911",
               "fr": "CCCS Victoria : 1-800-567-5111 · VHF 16 · *16 ou 911"},
 "president": "Alec Dick, President · Dawn Wilson, CEO",
 "join": "contact", "donate": "contact",
 "contact_block": {
   "en": "<strong>Coastal Nations Coast Guard Auxiliary (Western) Inc.</strong><br>25 Huron Street<br>Victoria, BC V8V 4Z9<br>778-679-5151<br><a href=\"mailto:dawn@cn-cga.ca\">dawn@cn-cga.ca</a>",
   "fr": "<strong>Coastal Nations Coast Guard Auxiliary (Western) Inc.</strong><br>25, rue Huron<br>Victoria (C.-B.) V8V 4Z9<br>778-679-5151<br><a href=\"mailto:dawn@cn-cga.ca\">dawn@cn-cga.ca</a>"},
 "website": "https://www.cn-cga.ca/",
 "nav": ["member-nations", "contact"],
 "pages": {
  "index": {"slug": {"en": "", "fr": ""},
   "title": {"en": "Coastal Nations Coast Guard Auxiliary", "fr": "Garde côtière auxiliaire des Nations côtières"},
   "hero": {"en": ("We are Coastal Nations saving lives at sea", "An Indigenous-led, volunteer-based organization providing marine search and rescue along the coast of British Columbia."),
            "fr": ("Les Nations côtières sauvent des vies en mer", "Un organisme autochtone fondé sur le bénévolat qui assure la recherche et le sauvetage maritimes le long de la côte de la Colombie-Britannique.")},
   "body": {
    "en": """
<section class="wrap split">
<div class="prose">
<p>The Coastal Nations Coast Guard Auxiliary (Western) Inc. (CN-CGA) was incorporated in 2018 with federal sponsorship to provide organized volunteer maritime search and rescue in coastal areas of British Columbia. In addition to SAR, CN-CGA promotes water safety and conducts coastal safety patrols in an auxiliary support role to the Canadian Coast Guard.</p>
<p>As Canada's first Indigenous-led auxiliary, its purpose is to protect mariners and citizens by forging strong, lasting partnerships between First Nations and the Canadian Coast Guard. Trained crews from its Member Nations respond to emergencies in some of the most remote and challenging coastal areas of BC.</p>
<h2>Mission</h2><p>To provide effective maritime search and rescue services, promote safety, and save lives of people in distress in our traditional waters.</p>
<h2>Vision</h2><p>Coastal Nations working together to save lives on our traditional waters.</p>
<h2>Values</h2>
<p class="tags"><span>Openness and honesty</span><span>Striving towards excellence</span><span>Respect for culture and tradition</span><span>Teamwork and collaboration</span><span>Innovation and continuous learning</span><span>Leadership and inspiration</span><span>Sharing knowledge</span><span>Compassion</span><span>Dependability</span><span>Courage</span></p>
</div>
<div>{facts}
<div class="card accent"><h3>Supporting our crews</h3><p>CN-CGA staff support Nation board members, zone coordinators and crew members, working with local communities, agencies and partners to keep crews safe and uphold the highest standards of care.</p></div>
</div>
</section>""",
    "fr": """
<section class="wrap split">
<div class="prose">
<p>La Coastal Nations Coast Guard Auxiliary (Western) Inc. (GCA-NC) a été constituée en 2018, avec le parrainage du gouvernement fédéral, pour offrir un service bénévole organisé de recherche et sauvetage maritimes dans les zones côtières de la Colombie-Britannique. En plus de la recherche et du sauvetage, elle fait la promotion de la sécurité nautique et effectue des patrouilles côtières en appui à la Garde côtière canadienne.</p>
<p>Première auxiliaire dirigée par des Autochtones au Canada, elle a pour but de protéger les navigateurs et la population en tissant des partenariats solides et durables entre les Premières Nations et la Garde côtière canadienne. Les équipages formés de ses Nations membres interviennent dans certaines des zones côtières les plus isolées et exigeantes de la C.-B.</p>
<h2>Mission</h2><p>Offrir des services efficaces de recherche et sauvetage maritimes, promouvoir la sécurité et sauver la vie des personnes en détresse dans nos eaux traditionnelles.</p>
<h2>Vision</h2><p>Des Nations côtières qui travaillent ensemble pour sauver des vies dans leurs eaux traditionnelles.</p>
<h2>Valeurs</h2>
<p class="tags"><span>Ouverture et honnêteté</span><span>Recherche de l'excellence</span><span>Respect de la culture et des traditions</span><span>Travail d'équipe et collaboration</span><span>Innovation et apprentissage continu</span><span>Leadership et inspiration</span><span>Partage des connaissances</span><span>Compassion</span><span>Fiabilité</span><span>Courage</span></p>
</div>
<div>{facts}
<div class="card accent"><h3>Au service de nos équipages</h3><p>Le personnel de la GCA-NC soutient les administrateurs des Nations, les coordonnateurs de zone et les équipiers, en collaboration avec les communautés, les organismes et les partenaires, pour assurer la sécurité des équipages et les plus hautes normes de diligence.</p></div>
</div>
</section>"""},
   "facts": {"en": [("2018", "incorporated"), ("11", "Member Nations"), ("1st", "Indigenous-led auxiliary in Canada")],
             "fr": [("2018", "constitution"), ("11", "Nations membres"), ("1re", "auxiliaire dirigée par des Autochtones au Canada")]}},

  "member-nations": {"slug": {"en": "member-nations", "fr": "nations-membres"},
   "title": {"en": "Member Nations", "fr": "Nations membres"},
   "body": {
    "en": """
<section class="wrap prose">
<p class="lead">Each Member Nation appoints a director to the board and a zone coordinator who leads its crew.</p>
<p>Founding communities named in CN-CGA's national profile include Ahousaht, Heiltsuk, Gitxaala, Nisga'a, Kitasoo, Quatsino, Kyuquot/Checleseht and 'Namgis. The auxiliary now counts 11 Member Nations.</p>
<p>The documentary series <i>Ocean Warriors: Mission Ready</i> features the crews of Ahousaht, Quatsino, 'Namgis and Heiltsuk First Nations.</p>
</section>
<section class="wrap"><div class="card"><h3>Board directors and zone coordinators</h3>
<table><thead><tr><th>Director</th><th>Zone coordinator</th></tr></thead><tbody>
<tr><td>Alec Dick (President)</td><td>Kurt John</td></tr>
<tr><td>Colin Nelson</td><td>Don Nelson</td></tr>
<tr><td>Alfred Adams</td><td>Noel Bellis</td></tr>
<tr><td>Harry Alfred</td><td>Harry Alfred (acting)</td></tr>
<tr><td>Samantha Christiansen</td><td>Elizabeth Jack (acting)</td></tr>
<tr><td>Harvey Robinson</td><td>Vacant</td></tr>
<tr><td>Vacant</td><td>Ernie Tallio</td></tr>
<tr><td>Lena Collins</td><td>Crystal Matilpi</td></tr>
<tr><td>James Wallas</td><td>Vacant</td></tr>
<tr><td>Alan Lambert</td><td>Errol Nyce</td></tr>
</tbody></table>
<p class="small">The Nation each pair represents is shown as artwork on the current regional site; Nation names to be confirmed with CN-CGA before publication.</p></div></section>""",
    "fr": """
<section class="wrap prose">
<p class="lead">Chaque Nation membre nomme un administrateur au conseil et un coordonnateur de zone qui dirige son équipage.</p>
<p>Parmi les communautés fondatrices nommées dans le profil national de la GCA-NC figurent Ahousaht, Heiltsuk, Gitxaala, Nisga'a, Kitasoo, Quatsino, Kyuquot/Checleseht et 'Namgis. L'auxiliaire compte maintenant 11 Nations membres.</p>
<p>La série documentaire <i>Ocean Warriors: Mission Ready</i> présente les équipages des Premières Nations Ahousaht, Quatsino, 'Namgis et Heiltsuk.</p>
</section>
<section class="wrap"><div class="card"><h3>Administrateurs et coordonnateurs de zone</h3>
<table><thead><tr><th>Administrateur</th><th>Coordonnateur de zone</th></tr></thead><tbody>
<tr><td>Alec Dick (président)</td><td>Kurt John</td></tr>
<tr><td>Colin Nelson</td><td>Don Nelson</td></tr>
<tr><td>Alfred Adams</td><td>Noel Bellis</td></tr>
<tr><td>Harry Alfred</td><td>Harry Alfred (par intérim)</td></tr>
<tr><td>Samantha Christiansen</td><td>Elizabeth Jack (par intérim)</td></tr>
<tr><td>Harvey Robinson</td><td>Poste vacant</td></tr>
<tr><td>Poste vacant</td><td>Ernie Tallio</td></tr>
<tr><td>Lena Collins</td><td>Crystal Matilpi</td></tr>
<tr><td>James Wallas</td><td>Poste vacant</td></tr>
<tr><td>Alan Lambert</td><td>Errol Nyce</td></tr>
</tbody></table>
<p class="small">La Nation représentée par chaque paire figure en image sur le site régional actuel; les noms des Nations sont à confirmer avec la GCA-NC avant la mise en ligne.</p></div></section>"""}},

  "contact": {"slug": {"en": "contact", "fr": "contact"},
   "title": {"en": "Contact Coastal Nations", "fr": "Joindre les Nations côtières"},
   "body": {
    "en": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Marine emergency</h3><p>JRCC Victoria: <a href="tel:+18005675111"><strong>1-800-567-5111</strong></a> · VHF Channel 16 · <strong>*16</strong> or <strong>911</strong></p></div>
<h2>Office</h2><p>Coastal Nations Coast Guard Auxiliary (Western) Inc.<br>25 Huron Street, Victoria, BC V8V 4Z9<br><a href="tel:+17786795151">778-679-5151</a></p>
<p>To join a crew, support CN-CGA or learn about the Indigenous Community Boat Volunteer Program, contact the office.</p></div>
<div class="card"><h3>Leadership</h3><p>Alec Dick, President<br>Dawn Wilson, Chief Executive Officer — <a href="mailto:dawn@cn-cga.ca">dawn@cn-cga.ca</a></p><p class="small">Regional website: <a href="https://www.cn-cga.ca/" rel="noopener">cn-cga.ca</a></p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Urgence maritime</h3><p>CCCS Victoria : <a href="tel:+18005675111"><strong>1-800-567-5111</strong></a> · canal VHF 16 · <strong>*16</strong> ou <strong>911</strong></p></div>
<h2>Bureau</h2><p>Coastal Nations Coast Guard Auxiliary (Western) Inc.<br>25, rue Huron, Victoria (C.-B.) V8V 4Z9<br><a href="tel:+17786795151">778-679-5151</a></p>
<p>Pour vous joindre à un équipage, soutenir la GCA-NC ou en savoir plus sur le Programme de bateaux bénévoles des communautés autochtones, communiquez avec le bureau.</p></div>
<div class="card"><h3>Direction</h3><p>Alec Dick, président<br>Dawn Wilson, chef de la direction — <a href="mailto:dawn@cn-cga.ca">dawn@cn-cga.ca</a></p><p class="small">Site régional : <a href="https://www.cn-cga.ca/" rel="noopener">cn-cga.ca</a></p></div></section>"""}},
 }})

# =====================================================================  CENTRAL & ARCTIC
REGIONS.append({
 "key": "central-arctic",
 "path": {"en": "central-arctic", "fr": "centre-arctique"},
 "name": {"en": "Central & Arctic", "fr": "Centre et Arctique"},
 "short": {"en": "Central & Arctic", "fr": "Centre et Arctique"},
 "org": {"en": "Canadian Coast Guard Auxiliary — Central & Arctic", "fr": "Garde côtière auxiliaire canadienne — Centre et Arctique"},
 "sub": {"en": "Ontario · Prairies · NWT · Nunavut", "fr": "Ontario · Prairies · T.N.-O. · Nunavut"},
 "area": {"en": "Great Lakes to the Arctic", "fr": "Des Grands Lacs à l'Arctique"},
 "figure": {"en": "1,013 volunteers · 83 vessels", "fr": "1 013 bénévoles · 83 embarcations"},
 "lead": {"en": "The largest geographic area in the CCGA: 67% of Canada's fresh water.", "fr": "Le plus vaste territoire de la GCAC : 67 % de l'eau douce du Canada."},
 "emergency": {"en": "1-800-267-7270 · VHF 16 · *16",
               "fr": "1-800-267-7270 · VHF 16 · *16"},
 "join": "get-involved", "donate": "get-involved",
 "contact_block": {
   "en": "<strong>Canadian Coast Guard Auxiliary, C&amp;A Inc.</strong><br>c/o 1700 – 2 St. Clair Ave W<br>Toronto, ON M4V 1L4<br>1-866-429-7283<br><a href=\"mailto:office@ccga-ca.com\">office@ccga-ca.com</a>",
   "fr": "<strong>Canadian Coast Guard Auxiliary, C&amp;A Inc.</strong><br>a/s 1700 – 2, av. St. Clair Ouest<br>Toronto (Ont.) M4V 1L4<br>1-866-429-7283<br><a href=\"mailto:office@ccga-ca.com\">office@ccga-ca.com</a>"},
 "website": "https://ccga-ca.com/",
 "nav": ["about", "get-involved", "contact"],
 "pages": {
  "index": {"slug": {"en": "", "fr": ""},
   "title": {"en": "Central & Arctic", "fr": "Centre et Arctique"},
   "hero": {"en": ("Volunteers saving lives on the water", "From the Great Lakes to Great Slave Lake and the Mackenzie River, Central & Arctic volunteers provide search and rescue and safe boating across four provinces and two territories."),
            "fr": ("Des bénévoles qui sauvent des vies sur l'eau", "Des Grands Lacs au Grand lac des Esclaves et au fleuve Mackenzie, les bénévoles du Centre et de l'Arctique assurent la recherche et le sauvetage et la sécurité nautique dans quatre provinces et deux territoires.")},
   "body": {
    "en": """
<section class="wrap split"><div class="prose">
<p>The Canadian Coast Guard Auxiliary Central &amp; Arctic Region, CCGA (C&amp;A), was incorporated in September 1978 under federal sponsorship to provide organized volunteer maritime search and rescue and to promote safety afloat, in an auxiliary support role to the Canadian Coast Guard.</p>
<p>Its grassroots structure delivers SAR response, boating safety and prevention messages across the largest geographic area in the CCGA — including Great Slave Lake, the Mackenzie River, Lake Athabasca, Lake Winnipeg and the Great Lakes.</p>
<h2>We need your help</h2>
<p>CCGA (C&amp;A) is a not-for-profit charity that relies on volunteers. There are three ways to help save lives on the water:</p>
<ol><li>Become a member of one of our search and rescue crews</li><li>Make a charitable donation</li><li>Become a corporate sponsor</li></ol>
<p><a class="btn" href="{r:get-involved}">Get involved</a></p>
</div><div>{facts}</div></section>""",
    "fr": """
<section class="wrap split"><div class="prose">
<p>La Garde côtière auxiliaire canadienne, région du Centre et de l'Arctique — GCAC (C&amp;A) — a été constituée en septembre 1978 avec le parrainage du gouvernement fédéral pour offrir un service bénévole organisé de recherche et sauvetage maritimes et promouvoir la sécurité sur l'eau, en appui à la Garde côtière canadienne.</p>
<p>Sa structure ancrée dans les communautés assure la recherche et le sauvetage, la sécurité nautique et la prévention sur le plus vaste territoire de la GCAC — notamment le Grand lac des Esclaves, le fleuve Mackenzie, le lac Athabasca, le lac Winnipeg et les Grands Lacs.</p>
<h2>Nous avons besoin de vous</h2>
<p>La GCAC (C&amp;A) est un organisme de bienfaisance sans but lucratif qui compte sur ses bénévoles. Trois façons d'aider à sauver des vies sur l'eau :</p>
<ol><li>Devenir membre d'un équipage de recherche et sauvetage</li><li>Faire un don de bienfaisance</li><li>Devenir commanditaire</li></ol>
<p><a class="btn" href="{r:get-involved}">S'impliquer</a></p>
</div><div>{facts}</div></section>"""},
   "facts": {"en": [("1,013", "volunteer members"), ("83", "vessels"), ("123,671", "hours of service a year"), ("175+", "Boating Safety Specialists")],
             "fr": [("1 013", "membres bénévoles"), ("83", "embarcations"), ("123 671", "heures de service par année"), ("175+", "spécialistes de la sécurité nautique")]}},

  "about": {"slug": {"en": "about", "fr": "a-propos"},
   "title": {"en": "About Central & Arctic", "fr": "À propos du Centre et de l'Arctique"},
   "body": {
    "en": """
<section class="wrap split"><div class="prose">
<h2>Mission</h2>
<p>To provide a permanent day and night search and rescue service to cover marine requirements in Canada and prevent the loss of life and injury. Our objectives:</p>
<ul><li>Save 100% of lives at risk</li><li>Reduce the number and severity of SAR incidents</li><li>Promote marine safety</li><li>Support the Canadian Coast Guard</li><li>Provide a humanitarian service</li><li>Maintain the highest professional standards</li><li>Promote dedication and pride of membership</li></ul>
<h2>Regional structure</h2>
<p>Each regional CCGA corporation is a unique, incorporated entity registered as a charity. Its structure is set out in its Certificate of Continuance, the CCGA C&amp;A By-Laws, the CCGA National Guidelines, the C&amp;A Regional Regulations, Policies and Procedures, and the contribution agreement with the Crown.</p>
<table><tbody>
<tr><td>President, Vice-President, Past President</td><td>3-year terms</td></tr>
<tr><td>Secretary, Treasurer, Board of Directors</td><td>2-year terms</td></tr>
<tr><td>Manager of Operations, Manager of Training</td><td>2-year appointments</td></tr>
</tbody></table>
</div><div class="card"><h3>Our territory</h3><ul class="plain">
<li>4 provinces and 2 territories</li><li>64% of Canada's land mass</li><li>65% of Canada's maritime waters</li><li>67% of Canada's fresh water</li><li>56% of Canada's population</li><li>1.2 million boats in Ontario — 780,000 on the Great Lakes</li><li>Great Slave Lake, Canada's fifth-largest lake; the Mackenzie, its longest river; Lake Winnipeg, its sixth-largest freshwater lake</li></ul></div></section>""",
    "fr": """
<section class="wrap split"><div class="prose">
<h2>Mission</h2>
<p>Offrir un service permanent de recherche et sauvetage, jour et nuit, pour répondre aux besoins maritimes au Canada et prévenir les pertes de vie et les blessures. Nos objectifs :</p>
<ul><li>Sauver 100 % des vies en danger</li><li>Réduire le nombre et la gravité des incidents SAR</li><li>Promouvoir la sécurité maritime</li><li>Appuyer la Garde côtière canadienne</li><li>Offrir un service humanitaire</li><li>Maintenir les plus hautes normes professionnelles</li><li>Promouvoir le dévouement et la fierté des membres</li></ul>
<h2>Structure régionale</h2>
<p>Chaque société régionale de la GCAC est une entité constituée distincte, enregistrée comme organisme de bienfaisance. Sa structure est définie par son certificat de prorogation, les règlements administratifs de la GCAC C&amp;A, les lignes directrices nationales de la GCAC, les règlements, politiques et procédures régionaux et l'accord de contribution avec l'État.</p>
<table><tbody>
<tr><td>Président, vice-président, président sortant</td><td>mandats de 3 ans</td></tr>
<tr><td>Secrétaire, trésorier, conseil d'administration</td><td>mandats de 2 ans</td></tr>
<tr><td>Gestionnaire des opérations, gestionnaire de la formation</td><td>nominations de 2 ans</td></tr>
</tbody></table>
</div><div class="card"><h3>Notre territoire</h3><ul class="plain">
<li>4 provinces et 2 territoires</li><li>64 % de la masse terrestre du Canada</li><li>65 % des eaux maritimes du Canada</li><li>67 % de l'eau douce du Canada</li><li>56 % de la population canadienne</li><li>1,2 million de bateaux en Ontario — 780 000 sur les Grands Lacs</li><li>Le Grand lac des Esclaves, 5<sup>e</sup> plus grand lac du pays; le Mackenzie, plus long fleuve; le lac Winnipeg, 6<sup>e</sup> plus grand lac d'eau douce</li></ul></div></section>"""}},

  "get-involved": {"slug": {"en": "get-involved", "fr": "simpliquer"},
   "title": {"en": "Get involved", "fr": "S'impliquer"},
   "body": {
    "en": """<section class="wrap grid3">
<div class="card"><h3>Join a SAR crew</h3><p>Age of majority, good physical condition, Pleasure Craft Operator Card and Marine Basic First Aid with CPR/AED Level C. Contact the office for an application.</p></div>
<div class="card"><h3>Donate</h3><p>CCGA (C&amp;A) is a registered charity. Contact the office to make a donation and receive a tax receipt.</p></div>
<div class="card"><h3>Corporate sponsorship</h3><p>Partner with volunteer crews protecting boaters on the Great Lakes and northern waters.</p></div>
</section><section class="wrap prose"><p>Call <a href="tel:+18664297283">1-866-429-7283</a> or email <a href="mailto:office@ccga-ca.com">office@ccga-ca.com</a>.</p></section>""",
    "fr": """<section class="wrap grid3">
<div class="card"><h3>Se joindre à un équipage</h3><p>Âge de la majorité, bonne condition physique, carte de conducteur d'embarcation de plaisance et secourisme maritime de base avec RCR/DEA niveau C. Demandez un formulaire au bureau.</p></div>
<div class="card"><h3>Faire un don</h3><p>La GCAC (C&amp;A) est un organisme de bienfaisance enregistré. Communiquez avec le bureau pour faire un don et recevoir un reçu fiscal.</p></div>
<div class="card"><h3>Commandite d'entreprise</h3><p>Associez-vous aux équipages bénévoles qui protègent les plaisanciers sur les Grands Lacs et les eaux du Nord.</p></div>
</section><section class="wrap prose"><p>Composez le <a href="tel:+18664297283">1-866-429-7283</a> ou écrivez à <a href="mailto:office@ccga-ca.com">office@ccga-ca.com</a>.</p></section>"""}},

  "contact": {"slug": {"en": "contact", "fr": "contact"},
   "title": {"en": "Contact Central & Arctic", "fr": "Joindre le Centre et l'Arctique"},
   "body": {
    "en": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Marine emergency</h3><p>Call <a href="tel:+18002677270"><strong>1-800-267-7270</strong></a>, VHF Channel 16, or <strong>*16</strong> on a mobile phone.</p></div>
<h2>Office</h2><p>Canadian Coast Guard Auxiliary, C&amp;A Inc.<br>c/o 1700 – 2 St. Clair Ave W, Toronto, ON M4V 1L4<br>Phone: 416-463-7283 · Toll free: <a href="tel:+18664297283">1-866-429-7283</a> · Fax: 416-463-7285<br><a href="mailto:office@ccga-ca.com">office@ccga-ca.com</a></p></div>
<div class="card"><h3>Leadership</h3><p>Philip Unger, President<br>Shannon Laird, Executive Director — <a href="mailto:shannon@ccga-ca.com">shannon@ccga-ca.com</a></p><p class="small">Regional website and member login: <a href="https://ccga-ca.com/" rel="noopener">ccga-ca.com</a></p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Urgence maritime</h3><p>Composez le <a href="tel:+18002677270"><strong>1-800-267-7270</strong></a>, le canal VHF 16 ou <strong>*16</strong> sur un cellulaire.</p></div>
<h2>Bureau</h2><p>Canadian Coast Guard Auxiliary, C&amp;A Inc.<br>a/s 1700 – 2, av. St. Clair Ouest, Toronto (Ont.) M4V 1L4<br>Tél. : 416-463-7283 · Sans frais : <a href="tel:+18664297283">1-866-429-7283</a> · Téléc. : 416-463-7285<br><a href="mailto:office@ccga-ca.com">office@ccga-ca.com</a></p></div>
<div class="card"><h3>Direction</h3><p>Philip Unger, président<br>Shannon Laird, direction générale — <a href="mailto:shannon@ccga-ca.com">shannon@ccga-ca.com</a></p><p class="small">Site régional et accès membres : <a href="https://ccga-ca.com/" rel="noopener">ccga-ca.com</a></p></div></section>"""}},
 }})

# =====================================================================  QUÉBEC
REGIONS.append({
 "key": "quebec",
 "path": {"en": "quebec", "fr": "quebec"},
 "name": {"en": "Québec", "fr": "Québec"},
 "short": {"en": "Québec", "fr": "Québec"},
 "org": {"en": "Canadian Coast Guard Auxiliary (Québec)", "fr": "Garde côtière auxiliaire canadienne (Québec)"},
 "sub": {"en": "GCAC(Q) · 7 zones", "fr": "GCAC(Q) · 7 zones"},
 "area": {"en": "St. Lawrence, Nunavik, James Bay", "fr": "Saint-Laurent, Nunavik, Baie-James"},
 "figure": {"en": "917 members · 65 units", "fr": "917 membres · 65 unités"},
 "lead": {"en": "Volunteer search and rescue from the Ontario border to Blanc-Sablon, Nunavik and James Bay.", "fr": "Recherche et sauvetage bénévoles de la frontière ontarienne à Blanc-Sablon, au Nunavik et à la Baie-James."},
 "emergency": {"en": "1-800-463-4393 · Mobile *16 · VHF 16",
               "fr": "1-800-463-4393 · Cellulaire *16 · VHF 16"},
 "president": "Daniel Michaud",
 "join": "become-a-member", "donate": "support-us",
 "contact_block": {
   "en": "<strong>Canadian Coast Guard Auxiliary (Québec) Inc.</strong><br>17 du Prince Street<br>Sorel-Tracy, QC J3P 4J4<br>Non-emergency: 1-877-746-4385<br><a href=\"mailto:louis.melancon@gcac-q.ca\">louis.melancon@gcac-q.ca</a>",
   "fr": "<strong>Garde côtière auxiliaire canadienne (Québec) inc.</strong><br>17, rue du Prince<br>Sorel-Tracy (Québec) J3P 4J4<br>Non urgent : 1-877-746-4385<br><a href=\"mailto:louis.melancon@gcac-q.ca\">louis.melancon@gcac-q.ca</a>"},
 "website": "https://www.gcac-q.ca/",
 "nav": ["about", "zones", "prevention", "fleet", "become-a-member", "contact"],
 "pages": {
  "index": {"slug": {"en": "", "fr": ""},
   "title": {"en": "Canadian Coast Guard Auxiliary (Québec)", "fr": "Garde côtière auxiliaire canadienne (Québec)"},
   "hero": {"en": ("Search and rescue on the water — in your community", "Experienced mariners, specially trained to keep you safe, prevent accidents and save lives on Québec's waterways, 24 hours a day, 7 days a week."),
            "fr": ("Recherche et sauvetage sur l'eau — dans votre communauté", "Des navigateurs d'expérience, spécialement formés pour assurer votre sécurité, prévenir les accidents et sauver des vies sur les voies navigables du Québec, 24 heures sur 24, 7 jours sur 7.")},
   "body": {
    "en": """
<section class="band emergency-band"><div class="wrap"><h2>Marine emergency</h2>
<p>Toll free <a href="tel:+18004634393"><strong>1-800-463-4393</strong></a> · Mobile <strong>*16</strong> · <strong>VHF Channel 16</strong> — the Canadian Coast Guard Maritime Rescue Sub-Centre in Québec City dispatches the nearest available resource.</p>
<p class="small">Non-emergency: 1-877-746-4385 or 450-746-4385</p></div></section>
<section class="wrap split"><div class="prose">
<p class="lead">The Canadian Coast Guard Auxiliary (Québec) is a not-for-profit organization dedicated to search and rescue on the water. Its volunteer marine rescuers live in your community.</p>
<p>Our volunteer crews are ready to respond to marine emergencies 24/7 from 65 units along Québec's waterways — the St. Lawrence from the Ontario border to Blanc-Sablon on the Lower North Shore and to the Baie des Chaleurs on the south shore, the Richelieu and Saguenay rivers, and, since 2016 and 2021, Nunavik and James Bay.</p>
<p><a class="btn" href="{r:become-a-member}">Become a member</a> <a class="btn btn-ghost" href="{r:support-us}">Support us</a></p>
</div><div><h3 class="stat-title">2025 in numbers</h3>{facts}</div></section>""",
    "fr": """
<section class="band emergency-band"><div class="wrap"><h2>Urgence maritime</h2>
<p>Sans frais <a href="tel:+18004634393"><strong>1-800-463-4393</strong></a> · Cellulaire <strong>*16</strong> · <strong>canal VHF 16</strong> — le Centre secondaire de sauvetage maritime de la Garde côtière canadienne, à Québec, dépêche la ressource disponible la plus proche.</p>
<p class="small">Non urgent : 1-877-746-4385 ou 450-746-4385</p></div></section>
<section class="wrap split"><div class="prose">
<p class="lead">La Garde côtière auxiliaire canadienne (Québec) est un organisme sans but lucratif voué à la recherche et au sauvetage sur l'eau. Ses sauveteurs maritimes bénévoles vivent dans votre communauté.</p>
<p>Nos équipages bénévoles sont prêts à répondre aux urgences maritimes 24 heures sur 24, 7 jours sur 7, à partir de 65 unités le long des voies navigables du Québec — le Saint-Laurent, de la frontière ontarienne jusqu'à Blanc-Sablon sur la Basse-Côte-Nord et jusqu'à la Baie des Chaleurs sur la rive sud, les rivières Richelieu et Saguenay et, depuis 2016 et 2021, le Nunavik et la Baie-James.</p>
<p><a class="btn" href="{r:become-a-member}">Devenir membre</a> <a class="btn btn-ghost" href="{r:support-us}">Nous aider</a></p>
</div><div><h3 class="stat-title">2025 en chiffres</h3>{facts}</div></section>"""},
   "facts": {"en": [("419", "missions"), ("48,449", "volunteer hours"), ("917", "members"), ("725", "people assisted")],
             "fr": [("419", "missions"), ("48 449", "heures de bénévolat"), ("917", "membres"), ("725", "personnes assistées")]}},

  "about": {"slug": {"en": "about", "fr": "a-propos"},
   "title": {"en": "About GCAC(Q)", "fr": "À propos de la GCAC(Q)"},
   "body": {
    "en": """
<section class="wrap split"><div class="prose">
<p>Founded more than 30 years ago, the Canadian Coast Guard Auxiliary (Québec) brings together volunteers specialized in marine search and rescue. Its members are spread across 65 units; the fleet has about 80 vessels, roughly 20 owned by the organization and the rest supplied by members.</p>
<p>Rescuers are volunteers: their only material compensation is reimbursement of costs tied to their missions. Distress calls are received by the Canadian Coast Guard rescue centre in Québec City and passed to the nearest available rescuer.</p>
<h2>Our mission</h2>
<p>To provide a volunteer search and rescue service day and night, meeting Canada's marine service needs and preventing loss of life and injury at sea:</p>
<ul><li>Save 100% of lives at risk</li><li>Reduce the number and severity of SAR incidents</li><li>Promote marine safety</li><li>Support the Canadian Coast Guard</li><li>Provide humanitarian assistance</li><li>Maintain the highest professional standards</li><li>Promote members' dedication and pride</li></ul>
<h2>Our vision</h2>
<p>To be the volunteer organization of excellence in marine rescue and boating safety: dynamic, innovative and recognized; always staffed by competent, well-trained and well-equipped rescuers; with members' lives and safety at the centre of its concerns; and a source of great pride for its members.</p>
<h2>Code of ethics</h2>
<p><b>Mutual aid</b>, <b>excellence</b>, <b>accountability</b>, <b>transparency</b>, <b>respect</b>, <b>teamwork</b> and the <b>safety</b> of our members — as much a priority as the safety of the people we rescue.</p>
</div><div class="card"><h3>Milestones</h3><ul class="timeline">
<li><b>1978</b> Creation of the Canadian Marine Rescue Auxiliary — renamed the Canadian Coast Guard Auxiliary in 1997 — including the Québec region.</li>
<li><b>2003</b> 25th anniversary: some 700 members and nearly 140 boats in Québec; 400+ missions a year.</li>
<li><b>2009</b> Agreements with riverside RCMs and municipalities to cover boating safety on their territory.</li>
<li><b>2010</b> Mérite québécois de la sécurité civile from Québec's Ministère de la Sécurité publique.</li>
<li><b>2012</b> Major update of governance rules: internal democracy and accountability.</li>
<li><b>2016</b> Territory expanded to Nunavik — some 14 new units.</li>
<li><b>2021</b> Territory expanded to James Bay — some 4 new units.</li>
<li><b>2023</b> 45th anniversary.</li></ul></div></section>""",
    "fr": """
<section class="wrap split"><div class="prose">
<p>Fondée il y a plus de 30 ans, la Garde côtière auxiliaire canadienne (Québec) regroupe des bénévoles spécialisés en recherche et sauvetage maritimes. Ses membres sont répartis dans 65 unités; la flotte compte près de 80 embarcations, dont une vingtaine appartiennent à l'organisation, les autres étant fournies par les membres.</p>
<p>Les sauveteurs sont des bénévoles : leur seule compensation matérielle est le remboursement des coûts liés à leurs interventions. C'est le centre de sauvetage de la Garde côtière canadienne, à Québec, qui reçoit les appels de détresse et les achemine au sauveteur disponible le plus proche.</p>
<h2>Notre mission</h2>
<p>Offrir, jour et nuit, un service de recherche et sauvetage assuré par des bénévoles, afin de répondre aux besoins maritimes du Canada et de prévenir les pertes de vie et les blessures en mer :</p>
<ul><li>Sauver 100 % des vies en danger</li><li>Réduire le nombre et la gravité des incidents de recherche et sauvetage</li><li>Promouvoir la sécurité en milieu marin</li><li>Appuyer la Garde côtière canadienne</li><li>Apporter une aide humanitaire</li><li>Maintenir les normes professionnelles les plus élevées</li><li>Promouvoir le dévouement et la fierté des membres</li></ul>
<h2>Notre vision</h2>
<p>Devenir l'organisation bénévole par excellence en sauvetage maritime et en sécurité nautique : dynamique, innovante et reconnue; comptant en tout temps sur des sauveteurs compétents, bien formés et équipés; plaçant la vie et la sécurité de ses membres au centre de ses préoccupations; et source de grande fierté pour ses membres.</p>
<h2>Code d'éthique</h2>
<p><b>L'entraide</b>, <b>l'excellence</b>, <b>la responsabilisation</b>, <b>la transparence</b>, <b>le respect</b>, <b>le travail d'équipe</b> et <b>la sécurité</b> de nos membres — une priorité tout autant que celle des personnes que nous sauvons.</p>
</div><div class="card"><h3>Jalons</h3><ul class="timeline">
<li><b>1978</b> Création du Service auxiliaire canadien de sauvetage maritime — devenu la Garde côtière auxiliaire canadienne en 1997 —, dont la région du Québec.</li>
<li><b>2003</b> 25<sup>e</sup> anniversaire : quelque 700 membres et près de 140 bateaux au Québec; plus de 400 interventions par année.</li>
<li><b>2009</b> Ententes avec les MRC et municipalités riveraines pour couvrir la sécurité nautique sur leur territoire.</li>
<li><b>2010</b> Mérite québécois de la sécurité civile, ministère de la Sécurité publique du Québec.</li>
<li><b>2012</b> Mise à jour importante des règles de gouvernance : démocratie interne et reddition de comptes.</li>
<li><b>2016</b> Élargissement au Nunavik — quelque 14 nouvelles unités.</li>
<li><b>2021</b> Élargissement à la Baie-James — quelque 4 nouvelles unités.</li>
<li><b>2023</b> 45<sup>e</sup> anniversaire.</li></ul></div></section>"""}},

  "zones": {"slug": {"en": "in-your-community", "fr": "dans-votre-communaute"},
   "title": {"en": "In your community", "fr": "Dans votre communauté"},
   "body": {
    "en": """
<section class="wrap prose"><p class="lead">Members are spread across 65 units along Québec's waterways, grouped into seven zones.</p></section>
<section class="wrap grid3">
<div class="card"><h3>Zone 1</h3><p>Côte-Nord / Saguenay</p></div>
<div class="card"><h3>Zone 2</h3><p>Bas-Saint-Laurent / Gaspésie</p></div>
<div class="card"><h3>Zone 3</h3><p>Québec</p></div>
<div class="card"><h3>Zone 4</h3><p>Saint-Laurent / Richelieu</p></div>
<div class="card"><h3>Zone 5</h3><p>Soulanges / Basses-Laurentides</p></div>
<div class="card"><h3>Zone 6</h3><p>Nunavik — 14 communities take part in SAR with support from the Indigenous Community Boat Volunteer Program</p></div>
<div class="card"><h3>Zone 7</h3><p>James Bay</p></div>
</section>
<section class="wrap prose"><h2>Search and rescue</h2><p>Marine search and rescue is at the heart of GCAC(Q)'s mission. Units along the main waterways respond quickly to distress calls, which should always go to the Canadian Coast Guard rescue centre in Québec City — 1-800-463-4393, VHF 16 or *16. Depending on the situation, the centre tasks the Coast Guard, GCAC(Q), the Sûreté du Québec or another authorized agency. Every minute counts: our volunteers offer a professional service.</p></section>""",
    "fr": """
<section class="wrap prose"><p class="lead">Les membres sont répartis dans 65 unités le long des voies navigables du Québec, regroupées en sept zones.</p></section>
<section class="wrap grid3">
<div class="card"><h3>Zone 1</h3><p>Côte-Nord / Saguenay</p></div>
<div class="card"><h3>Zone 2</h3><p>Bas-Saint-Laurent / Gaspésie</p></div>
<div class="card"><h3>Zone 3</h3><p>Québec</p></div>
<div class="card"><h3>Zone 4</h3><p>Saint-Laurent / Richelieu</p></div>
<div class="card"><h3>Zone 5</h3><p>Soulanges / Basses-Laurentides</p></div>
<div class="card"><h3>Zone 6</h3><p>Nunavik — 14 communautés participent à la recherche et au sauvetage avec l'appui du Programme de bateaux bénévoles des communautés autochtones</p></div>
<div class="card"><h3>Zone 7</h3><p>Baie-James</p></div>
</section>
<section class="wrap prose"><h2>Recherche et sauvetage</h2><p>La recherche et le sauvetage maritimes sont au cœur de la mission de la GCAC(Q). Les unités situées le long des principales voies navigables répondent rapidement aux appels de détresse, qui doivent toujours être dirigés vers le centre de sauvetage de la Garde côtière canadienne à Québec — 1-800-463-4393, VHF 16 ou *16. Selon la situation, le centre dépêche la Garde côtière, la GCAC(Q), la Sûreté du Québec ou un autre organisme habilité. Chaque minute compte : nos bénévoles offrent un service professionnel.</p></section>"""}},

  "prevention": {"slug": {"en": "prevention", "fr": "prevention"},
   "title": {"en": "Prevention", "fr": "Prévention"},
   "body": {
    "en": """
<section class="wrap prose"><p class="lead">Our first concern is to prevent accidents — or at least reduce their severity.</p>
<p>Most members are trained in prevention and boating safety; some make it their specialty. Our prevention advisers are active on water patrols, at shows and exhibitions, and in marinas.</p>
<h2>Wear your lifejacket — always</h2><p>Wearing a lifejacket or PFD is one of the most important safety measures, and one of the most neglected. Having enough on board is not enough: <b>everyone must wear one</b>. Québec waters are cold most of the year; Dr. Gordon Giesbrecht's “1-10-1” rule describes the three critical phases of cold-water immersion.</p></section>
<section class="wrap grid2">
<div class="card"><h3>Courtesy checks</h3><p>Simple, useful and free. A trained volunteer comes aboard and, with you, checks the presence and condition of the safety equipment required by law. No penalty is attached — it is a courtesy aimed at education and prevention. Responsibility for compliance with Transport Canada requirements remains with the owner and operator.</p></div>
<div class="card"><h3>Bobbie the Boat</h3><p>A go-cart-sized boat that moves, blinks and talks — and teaches children and parents the basic rules of safety on the water. Bobbie visits shows, nautical events, marinas, yacht clubs and schools, at a very affordable cost. Contact us to book Bobbie.</p></div>
</section>""",
    "fr": """
<section class="wrap prose"><p class="lead">Notre préoccupation première : éviter les accidents — ou à tout le moins en réduire la gravité.</p>
<p>La plupart des membres ont reçu une formation en prévention et en sécurité nautique; certains en ont fait leur spécialité. Nos conseillers en prévention sont actifs lors des patrouilles nautiques, dans les salons et expositions et dans les marinas.</p>
<h2>Portez votre VFI — en tout temps</h2><p>Porter un gilet de sauvetage ou un VFI est l'une des plus importantes mesures de sécurité, et l'une des plus négligées. Il ne suffit pas d'en avoir assez à bord : <b>tous les passagers doivent le porter</b>. Les eaux du Québec sont froides une grande partie de l'année; la règle « 1-10-1 » du Dr Gordon Giesbrecht décrit les trois phases critiques de l'immersion en eau froide.</p></section>
<section class="wrap grid2">
<div class="card"><h3>Vérification de courtoisie</h3><p>Simple, utile et gratuite. Un bénévole formé monte à bord et vérifie avec vous la présence et l'état des équipements de sécurité exigés par la loi. Aucune sanction n'y est rattachée : c'est un geste de courtoisie axé sur la formation et la prévention. La conformité aux exigences de Transports Canada demeure la responsabilité du propriétaire et de l'opérateur.</p></div>
<div class="card"><h3>Programme Bobbie</h3><p>Un bateau de la taille d'une voiturette qui avance, cligne des yeux et parle — et enseigne aux enfants et aux parents les règles élémentaires de la sécurité sur l'eau. Bobbie visite salons, activités nautiques, marinas, clubs nautiques et écoles, à coût très abordable. Communiquez avec nous pour réserver Bobbie.</p></div>
</section>"""}},

  "fleet": {"slug": {"en": "fleet", "fr": "flotte"},
   "title": {"en": "Fleet", "fr": "Flotte"},
   "body": {
    "en": """<section class="wrap prose"><p class="lead">GCAC(Q) can count on about 76 vessels.</p><p>About 30 belong to GCAC(Q) and are loaned to units; the others belong to members — recreational boaters or commercial fishers. All vessels must meet very strict standards. Members equip their boats with specialized SAR equipment, at a cost that can reach several thousand dollars, and maintain their own or loaned vessels.</p><p>Each year, with the Coast Guard's Maritime Rescue Sub-Centre, GCAC(Q) decides where available boats are stationed to provide the best possible coverage. In Nunavik and James Bay, 18 vessels adapted to northern conditions belong to the local communities.</p></section>""",
    "fr": """<section class="wrap prose"><p class="lead">La GCAC(Q) peut compter sur près de 76 embarcations.</p><p>Une trentaine appartiennent à la GCAC(Q) et sont prêtées aux unités; les autres appartiennent aux membres — plaisanciers ou pêcheurs commerciaux. Tous les bateaux doivent répondre à des normes très strictes. Les membres munissent leurs bateaux d'équipements spécialisés de recherche et sauvetage, ce qui peut coûter plusieurs milliers de dollars, et en assurent l'entretien.</p><p>Chaque année, avec le Centre secondaire de sauvetage maritime de la Garde côtière, la GCAC(Q) décide de la localisation des bateaux afin d'assurer la meilleure couverture possible. Au Nunavik et à la Baie-James, 18 embarcations adaptées aux conditions nordiques appartiennent aux communautés locales.</p></section>"""}},

  "become-a-member": {"slug": {"en": "become-a-member", "fr": "devenir-membre"},
   "title": {"en": "Become a member", "fr": "Devenir membre"},
   "body": {
    "en": """<section class="wrap split"><div class="prose"><p class="lead">Why not join the GCAC(Q) team?</p>
<p>Our volunteer rescuers are men and women you can count on:</p>
<ul><li>Volunteers who put their skills, equipment and time at their community's service</li><li>Experienced mariners trained in marine SAR to strict national standards</li><li>Key collaborators of the Canadian Coast Guard</li><li>Members of your community, already on site and ready to respond quickly</li><li>Committed citizens working with your municipality for optimal boating safety</li></ul>
<p>Applicants must be in good physical condition, with a strong sense of responsibility, availability and an ability to work in a team. Those selected receive training maintained through regular theory courses and practical exercises.</p></div>
<div class="card accent"><h3>Interested?</h3><p>Call <a href="tel:+18777464385">1-877-746-4385</a> or write to the head office to be referred to the unit nearest you.</p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose"><p class="lead">Pourquoi ne pas vous joindre à la grande équipe de la GCAC(Q)?</p>
<p>Nos sauveteurs bénévoles sont des hommes et des femmes sur lesquels vous pouvez compter :</p>
<ul><li>Des bénévoles qui mettent leurs compétences, leurs équipements et leur temps au service de leur communauté</li><li>Des navigateurs d'expérience formés en recherche et sauvetage maritimes selon des normes nationales très strictes</li><li>Des collaborateurs de premier plan de la Garde côtière canadienne</li><li>Des membres de votre communauté, déjà sur place et prêts à répondre rapidement</li><li>Des citoyens engagés qui collaborent avec votre municipalité pour une sécurité nautique optimale</li></ul>
<p>Il faut une bonne condition physique, un grand sens des responsabilités, de la disponibilité et une facilité à travailler en équipe. Les personnes retenues reçoivent une formation maintenue par des cours théoriques et des exercices pratiques réguliers.</p></div>
<div class="card accent"><h3>Intéressé?</h3><p>Composez le <a href="tel:+18777464385">1-877-746-4385</a> ou écrivez au siège social pour être dirigé vers l'unité la plus proche.</p></div></section>"""}},

  "support-us": {"slug": {"en": "support-us", "fr": "nous-aider"},
   "title": {"en": "Support us", "fr": "Nous aider"},
   "body": {
    "en": """<section class="wrap split"><div class="prose">
<p class="lead">GCAC(Q) is a registered charity (BN 119145910RR0001). All donations are tax deductible.</p>
<p>It is mainly funded by a federal contribution program administered by Fisheries and Oceans Canada through the Canadian Coast Guard, which reimburses mission costs and covers members' insurance. Additional funds are needed to maintain rescue services, provide proper SAR equipment and ensure continuing training — repairing or renewing gear and, in some cases, buying specialized equipment such as defibrillators.</p>
<h2>Ways to give</h2>
<ul><li><b>By mail:</b> cheque or money order to <i>Garde côtière auxiliaire canadienne (Québec) Inc.</i>, 17 du Prince Street, Sorel-Tracy, QC J3P 4J4. Do not send cash.</li><li><b>By phone:</b> 1-877-746-4385 to receive a form.</li><li><b>Boat or equipment:</b> donate your vessel; GCAC(Q) covers transport and docking and issues a receipt for its fair market value.</li><li><b>Planned gift</b> in your will, or a <b>memorial gift</b>.</li></ul>
<p class="small">GCAC(Q) does not disclose supporters' names or addresses to other organizations.</p></div>
<div class="card"><h3>Become a partner</h3><p>Boat builders and distributors, marine equipment makers, boating and safety associations, and local businesses near our units can sponsor events and gain visibility with their target audience. Contact us to discuss sponsorship.</p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose">
<p class="lead">La GCAC(Q) est un organisme de bienfaisance enregistré (NE 119145910RR0001). Tous les dons sont déductibles d'impôt.</p>
<p>Elle est principalement financée par un programme de contribution fédéral administré par Pêches et Océans Canada via la Garde côtière canadienne, qui rembourse les frais de mission et couvre l'assurance des membres. Des fonds supplémentaires sont nécessaires pour maintenir les services de sauvetage, fournir l'équipement adéquat et assurer la formation continue — réparer ou renouveler l'équipement et, parfois, acheter du matériel spécialisé comme un défibrillateur.</p>
<h2>Façons de donner</h2>
<ul><li><b>Par la poste :</b> chèque ou mandat à l'ordre de la <i>Garde côtière auxiliaire canadienne (Québec) Inc.</i>, 17, rue du Prince, Sorel-Tracy (Québec) J3P 4J4. Ne pas envoyer d'argent comptant.</li><li><b>Par téléphone :</b> 1-877-746-4385 pour obtenir un formulaire.</li><li><b>Embarcation ou équipement :</b> faites don de votre bateau; la GCAC(Q) prend en charge le transport et l'accostage et remet un reçu correspondant à sa valeur marchande.</li><li><b>Don planifié</b> par testament ou <b>don commémoratif</b>.</li></ul>
<p class="small">La GCAC(Q) ne divulgue pas les noms ni les adresses de ses donateurs à d'autres organisations.</p></div>
<div class="card"><h3>Devenir partenaire</h3><p>Fabricants et distributeurs d'embarcations, d'équipement nautique, associations de navigation et de sécurité, commerces situés près de nos unités : commanditez nos événements et gagnez en visibilité auprès de votre public cible. Communiquez avec nous.</p></div></section>"""}},

  "contact": {"slug": {"en": "contact", "fr": "contact"},
   "title": {"en": "Contact GCAC(Q)", "fr": "Joindre la GCAC(Q)"},
   "body": {
    "en": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Emergency</h3><p>Toll free <a href="tel:+18004634393"><strong>1-800-463-4393</strong></a> · Mobile <strong>*16</strong> · VHF Channel 16</p></div>
<h2>Head office</h2><p>17 du Prince Street, Sorel-Tracy, QC J3P 4J4<br>Non-emergency: <a href="tel:+18777464385">1-877-746-4385</a> or 450-746-4385<br>Fax: 450-746-4386</p>
<p>Le Dauphin, GCAC(Q)'s magazine, is published twice a year.</p></div>
<div class="card"><h3>Leadership</h3><p>Daniel Michaud, President<br>Louis Melançon, Executive Director — <a href="mailto:louis.melancon@gcac-q.ca">louis.melancon@gcac-q.ca</a> · 514-953-8234</p><p class="small">Member access (GISAR): <a href="https://www.gcac-q.ca/" rel="noopener">gcac-q.ca</a></p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Urgence</h3><p>Sans frais <a href="tel:+18004634393"><strong>1-800-463-4393</strong></a> · Cellulaire <strong>*16</strong> · canal VHF 16</p></div>
<h2>Siège social</h2><p>17, rue du Prince, Sorel-Tracy (Québec) J3P 4J4<br>Non urgent : <a href="tel:+18777464385">1-877-746-4385</a> ou 450-746-4385<br>Téléc. : 450-746-4386</p>
<p>Le Dauphin, le magazine de la GCAC(Q), paraît deux fois par année.</p></div>
<div class="card"><h3>Direction</h3><p>Daniel Michaud, président<br>Louis Melançon, directeur général — <a href="mailto:louis.melancon@gcac-q.ca">louis.melancon@gcac-q.ca</a> · 514-953-8234</p><p class="small">Accès membres (GISAR) : <a href="https://www.gcac-q.ca/" rel="noopener">gcac-q.ca</a></p></div></section>"""}},
 }})

# =====================================================================  MARITIMES
REGIONS.append({
 "key": "maritimes",
 "path": {"en": "maritimes", "fr": "maritimes"},
 "name": {"en": "Maritimes", "fr": "Maritimes"},
 "short": {"en": "Maritimes", "fr": "Maritimes"},
 "org": {"en": "Canadian Coast Guard Auxiliary — Maritimes", "fr": "Garde côtière auxiliaire canadienne — Maritimes"},
 "sub": {"en": "NB · NS · PEI · Îles-de-la-Madeleine", "fr": "N.-B. · N.-É. · Î.-P.-É. · Îles-de-la-Madeleine"},
 "area": {"en": "NB, NS, PEI, Îles-de-la-Madeleine", "fr": "N.-B., N.-É., Î.-P.-É., Îles-de-la-Madeleine"},
 "figure": {"en": "800 volunteers · 400 vessels", "fr": "800 bénévoles · 400 embarcations"},
 "lead": {"en": "Volunteer crews — 90% of them commercial fishers — on the waters of the Maritimes.", "fr": "Des équipages bénévoles — à 90 % des pêcheurs commerciaux — sur les eaux des Maritimes."},
 "emergency": {"en": "VHF Radio: Channel 16 · Mobile: *16 or 911", "fr": "Radio VHF : canal 16 · Cellulaire : *16 ou 911"},
 "join": "volunteer", "donate": "contact",
 "contact_block": {
   "en": "<strong>Canadian Coast Guard Auxiliary (Maritimes)</strong><br>103-900 Windmill Road<br>Dartmouth, NS B3B 1P7<br>902-220-1058<br><a href=\"mailto:darcy.henn@ccga-m.ca\">darcy.henn@ccga-m.ca</a>",
   "fr": "<strong>Garde côtière auxiliaire canadienne (Maritimes)</strong><br>103-900, chemin Windmill<br>Dartmouth (N.-É.) B3B 1P7<br>902-220-1058<br><a href=\"mailto:darcy.henn@ccga-m.ca\">darcy.henn@ccga-m.ca</a>"},
 "website": "https://www.ccga-m.ca/",
 "nav": ["programs", "volunteer", "contact"],
 "pages": {
  "index": {"slug": {"en": "", "fr": ""},
   "title": {"en": "Canadian Coast Guard Auxiliary — Maritimes", "fr": "Garde côtière auxiliaire canadienne — Maritimes"},
   "hero": {"en": ("Volunteers saving lives on the water", "800 volunteers and nearly 400 privately owned vessels across New Brunswick, Nova Scotia, Prince Edward Island and Îles-de-la-Madeleine."),
            "fr": ("Des bénévoles qui sauvent des vies sur l'eau", "800 bénévoles et près de 400 embarcations privées au Nouveau-Brunswick, en Nouvelle-Écosse, à l'Île-du-Prince-Édouard et aux Îles-de-la-Madeleine.")},
   "body": {
    "en": """
<section class="wrap split"><div class="prose">
<h2>Who we are</h2><p>The Canadian Coast Guard Auxiliary Maritimes (CCGA-M) is a non-profit organization and registered charity. In existence since 1978, it assists the Canadian Coast Guard and National Defence with search and rescue and safe boating programs.</p>
<h2>What we do</h2><p>CCGA-M is dedicated to search and rescue and safe boating. Our mission is to provide a permanent day and night SAR service covering marine requirements in the Maritime region and to prevent loss of life and injury. Members also provide on-water support in each province during fishing season openings, including the lobster openings in Lobster Fishing Areas 33 and 34.</p>
<h2>Where we are</h2><p>New Brunswick, Nova Scotia, Prince Edward Island and Îles-de-la-Madeleine.</p>
<h2>Our mission, vision and values</h2><p>CCGA-M shares the Auxiliary's national <a href="{n:about}">mission, vision and values</a>: saving lives on the water and promoting safe boating.</p>
</div><div>{facts}<div class="card accent"><h3>Vessel owner or crew?</h3><p>We are seeking experienced vessel owners, captains and crew ready to support marine SAR in their communities.</p><p><a href="{r:volunteer}">How to join →</a></p></div></div></section>""",
    "fr": """
<section class="wrap split"><div class="prose">
<h2>Qui nous sommes</h2><p>La Garde côtière auxiliaire canadienne — Maritimes (GCAC-M) est un organisme sans but lucratif et un organisme de bienfaisance enregistré. Active depuis 1978, elle appuie la Garde côtière canadienne et la Défense nationale en recherche et sauvetage et dans les programmes de sécurité nautique.</p>
<h2>Ce que nous faisons</h2><p>La GCAC-M se consacre à la recherche et au sauvetage et à la sécurité nautique. Sa mission : offrir un service SAR permanent, jour et nuit, pour répondre aux besoins maritimes de la région et prévenir les pertes de vie et les blessures. Les membres assurent aussi un soutien sur l'eau dans chaque province lors de l'ouverture des saisons de pêche, notamment l'ouverture du homard dans les zones de pêche 33 et 34.</p>
<h2>Où nous sommes</h2><p>Nouveau-Brunswick, Nouvelle-Écosse, Île-du-Prince-Édouard et Îles-de-la-Madeleine.</p>
<h2>Mission, vision et valeurs</h2><p>La GCAC-M partage la <a href="{n:about}">mission, la vision et les valeurs</a> nationales de l'Auxiliaire : sauver des vies sur l'eau et promouvoir la sécurité nautique.</p>
</div><div>{facts}<div class="card accent"><h3>Propriétaire ou équipier?</h3><p>Nous recherchons des propriétaires d'embarcation, capitaines et équipiers d'expérience prêts à appuyer la recherche et le sauvetage dans leur communauté.</p><p><a href="{r:volunteer}">Comment se joindre →</a></p></div></div></section>"""},
   "facts": {"en": [("800", "volunteers"), ("~400", "participating vessels"), ("90%", "of volunteers are commercial fishers"), ("1978", "in service since")],
             "fr": [("800", "bénévoles"), ("~400", "embarcations participantes"), ("90 %", "des bénévoles sont pêcheurs commerciaux"), ("1978", "en service depuis")]}},

  "programs": {"slug": {"en": "boating-safety", "fr": "securite-nautique"},
   "title": {"en": "Boating safety programs", "fr": "Programmes de sécurité nautique"},
   "body": {
    "en": """<section class="wrap grid3">
<div class="card"><h3>Pleasure craft safety checks</h3><p>A free, no-penalty check of the safety equipment required on board, done with you by a trained volunteer.</p></div>
<div class="card"><h3>Kids Don't Float</h3><p>Loaner lifejacket stations so children near the water always have a properly sized lifejacket.</p></div>
<div class="card"><h3>Bobbie the Boat</h3><p>Our talking robot boat brings safe boating messages to children at events, schools and marinas.</p></div>
</section><section class="wrap prose"><p class="small">Program details to be completed with CCGA-M before publication.</p></section>""",
    "fr": """<section class="wrap grid3">
<div class="card"><h3>Vérification de sécurité des embarcations</h3><p>Une vérification gratuite et sans pénalité de l'équipement de sécurité requis à bord, faite avec vous par un bénévole formé.</p></div>
<div class="card"><h3>Kids Don't Float</h3><p>Des stations de prêt de gilets de sauvetage pour que les enfants près de l'eau aient toujours un gilet de la bonne taille.</p></div>
<div class="card"><h3>Bobbie le bateau</h3><p>Notre bateau robot parlant transmet les messages de sécurité nautique aux enfants lors d'événements, dans les écoles et les marinas.</p></div>
</section><section class="wrap prose"><p class="small">Détails des programmes à compléter avec la GCAC-M avant la mise en ligne.</p></section>"""}},

  "volunteer": {"slug": {"en": "volunteer", "fr": "benevolat"},
   "title": {"en": "Volunteer with CCGA-M", "fr": "Devenir bénévole à la GCAC-M"},
   "body": {
    "en": """<section class="wrap split"><div class="prose"><p class="lead">If you are safety-minded, dependable and willing to train to our standards, put your vessel and skills in service to saving lives on the water.</p>
<h2>To become a member</h2><ul><li>Be the age of majority under provincial legislation</li><li>Be in good physical condition</li><li>Complete the Pleasure Craft Operator Certificate course</li><li>Hold Marine Basic First Aid or equivalent, with CPR/AED Level C</li></ul>
<p>For an application form, contact the regional office.</p>
<h2>More ways to volunteer</h2><ul><li>Advocate for boating safety</li><li>Vessel maintenance and equipment management</li><li>Fundraising and special events</li><li>Media and marketing</li></ul></div>
<div class="card"><h3>Mission ready</h3><p>Instructor-led operational readiness training and joint exercises with other SAR agencies prepare crews for every level of response. Average time to deploy to a marine emergency: about 25 minutes.</p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose"><p class="lead">Si vous avez le souci de la sécurité, êtes fiable et prêt à vous former selon nos normes, mettez votre embarcation et vos compétences au service du sauvetage sur l'eau.</p>
<h2>Pour devenir membre</h2><ul><li>Avoir l'âge de la majorité selon la loi provinciale</li><li>Être en bonne condition physique</li><li>Réussir le cours de la Carte de conducteur d'embarcation de plaisance</li><li>Détenir un secourisme maritime de base ou l'équivalent, avec RCR/DEA niveau C</li></ul>
<p>Pour un formulaire d'adhésion, communiquez avec le bureau régional.</p>
<h2>D'autres façons d'aider</h2><ul><li>Promouvoir la sécurité nautique</li><li>Entretien des embarcations et de l'équipement</li><li>Collectes de fonds et événements spéciaux</li><li>Médias et marketing</li></ul></div>
<div class="card"><h3>Prêts pour la mission</h3><p>Une formation opérationnelle donnée par des instructeurs et des exercices conjoints avec d'autres organismes SAR préparent les équipages à tous les niveaux d'intervention. Délai moyen de déploiement : environ 25 minutes.</p></div></section>"""}},

  "contact": {"slug": {"en": "contact", "fr": "contact"},
   "title": {"en": "Contact CCGA-M", "fr": "Joindre la GCAC-M"},
   "body": {
    "en": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Marine emergency</h3><p>VHF Channel 16 · <strong>*16</strong> on a mobile phone · <strong>911</strong></p></div>
<h2>Regional office</h2><p>103-900 Windmill Road, Dartmouth, NS B3B 1P7<br>Office: <a href="tel:+19022201058">902-220-1058</a> · Fax: 902-481-2749</p></div>
<div class="card"><h3>Leadership</h3><p>Richard Herring, President<br>Darcy Henn, Executive Director — <a href="mailto:darcy.henn@ccga-m.ca">darcy.henn@ccga-m.ca</a></p><p class="small">Regional website (forms, executive committee, zone directors): <a href="https://www.ccga-m.ca/" rel="noopener">ccga-m.ca</a></p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Urgence maritime</h3><p>Canal VHF 16 · <strong>*16</strong> sur un cellulaire · <strong>911</strong></p></div>
<h2>Bureau régional</h2><p>103-900, chemin Windmill, Dartmouth (N.-É.) B3B 1P7<br>Bureau : <a href="tel:+19022201058">902-220-1058</a> · Téléc. : 902-481-2749</p></div>
<div class="card"><h3>Direction</h3><p>Richard Herring, président<br>Darcy Henn, direction générale — <a href="mailto:darcy.henn@ccga-m.ca">darcy.henn@ccga-m.ca</a></p><p class="small">Site régional (formulaires, comité exécutif, directeurs de zone) : <a href="https://www.ccga-m.ca/" rel="noopener">ccga-m.ca</a></p></div></section>"""}},
 }})

# =====================================================================  NEWFOUNDLAND & LABRADOR
REGIONS.append({
 "key": "newfoundland-labrador",
 "path": {"en": "newfoundland-labrador", "fr": "terre-neuve-labrador"},
 "name": {"en": "Newfoundland & Labrador", "fr": "Terre-Neuve-et-Labrador"},
 "short": {"en": "Newfoundland & Labrador", "fr": "Terre-Neuve-et-Labrador"},
 "org": {"en": "Canadian Coast Guard Auxiliary — Newfoundland & Labrador", "fr": "Garde côtière auxiliaire canadienne — Terre-Neuve-et-Labrador"},
 "sub": {"en": "10 districts · 63 sectors", "fr": "10 districts · 63 secteurs"},
 "area": {"en": "Newfoundland and Labrador waters", "fr": "Eaux de Terre-Neuve-et-Labrador"},
 "figure": {"en": "797 volunteers · 343 vessels", "fr": "797 bénévoles · 343 embarcations"},
 "lead": {"en": "On average, CCGA-NL volunteers have the longest sail to a SAR call.", "fr": "En moyenne, ce sont les bénévoles de la GCAC-TNL qui naviguent le plus longtemps pour se rendre à un appel SAR."},
 "emergency": {"en": "VHF Radio: Channel 16 · Mobile: *16 or 911", "fr": "Radio VHF : canal 16 · Cellulaire : *16 ou 911"},
 "join": "join", "donate": "contact",
 "contact_block": {
   "en": "<strong>Canadian Coast Guard Auxiliary (NL) Inc.</strong><br>878-C Topsail Road, Mount Pearl<br>PO Box 938, St. John's, NL A1C 5M3<br>1-800-563-6158<br><a href=\"mailto:Kelly.Doody@ccga-nl.ca\">Kelly.Doody@ccga-nl.ca</a>",
   "fr": "<strong>Canadian Coast Guard Auxiliary (NL) Inc.</strong><br>878-C, chemin Topsail, Mount Pearl<br>C.P. 938, St. John's (T.-N.-L.) A1C 5M3<br>1-800-563-6158<br><a href=\"mailto:Kelly.Doody@ccga-nl.ca\">Kelly.Doody@ccga-nl.ca</a>"},
 "website": "https://ccga-nl.ca/",
 "nav": ["about", "districts", "join", "faq", "contact"],
 "pages": {
  "index": {"slug": {"en": "", "fr": ""},
   "title": {"en": "Canadian Coast Guard Auxiliary — Newfoundland & Labrador", "fr": "Garde côtière auxiliaire canadienne — Terre-Neuve-et-Labrador"},
   "hero": {"en": ("Dedicated volunteers for marine search and rescue and safe boating", "CCGA (NL) members and their vessels respond to search and rescue incidents in the waters around Newfoundland and Labrador, alongside the Canadian Coast Guard."),
            "fr": ("Des bénévoles dévoués à la recherche et au sauvetage maritimes et à la sécurité nautique", "Les membres de la GCAC (TNL) et leurs embarcations interviennent lors d'incidents de recherche et sauvetage dans les eaux de Terre-Neuve-et-Labrador, aux côtés de la Garde côtière canadienne.")},
   "body": {
    "en": """<section class="wrap split"><div class="prose">
<p>CCGA (NL) is a non-profit volunteer organization that augments search and rescue resources in the Newfoundland and Labrador region, working in conjunction with the Canadian Coast Guard.</p>
<blockquote>“The prevention of loss of life and/or injury at sea, including, where possible and directly related thereto, reasonable efforts to minimize damage to or loss of property.”</blockquote>
<h2>Our mission</h2><p>To provide a permanent day and night search and rescue service covering marine requirements in the Newfoundland and Labrador region and to prevent loss of life and injury.</p>
<ul><li>Save 100% of lives at risk</li><li>Reduce the number and severity of SAR incidents</li><li>Promote marine safety</li><li>Support the Canadian Coast Guard</li><li>Provide a humanitarian service</li><li>Maintain the highest professional standards</li><li>Promote dedication and pride of membership</li></ul>
</div><div>{facts}</div></section>""",
    "fr": """<section class="wrap split"><div class="prose">
<p>La GCAC (TNL) est un organisme bénévole sans but lucratif qui renforce les ressources de recherche et sauvetage de la région de Terre-Neuve-et-Labrador, en collaboration avec la Garde côtière canadienne.</p>
<blockquote>« Prévenir les pertes de vie ou les blessures en mer, y compris, lorsque c'est possible et directement lié, déployer des efforts raisonnables pour réduire au minimum les dommages ou les pertes matérielles. »</blockquote>
<h2>Notre mission</h2><p>Offrir un service permanent de recherche et sauvetage, jour et nuit, pour répondre aux besoins maritimes de la région de Terre-Neuve-et-Labrador et prévenir les pertes de vie et les blessures.</p>
<ul><li>Sauver 100 % des vies en danger</li><li>Réduire le nombre et la gravité des incidents SAR</li><li>Promouvoir la sécurité maritime</li><li>Appuyer la Garde côtière canadienne</li><li>Offrir un service humanitaire</li><li>Maintenir les plus hautes normes professionnelles</li><li>Promouvoir le dévouement et la fierté des membres</li></ul>
</div><div>{facts}</div></section>"""},
   "facts": {"en": [("797", "volunteers, most of them commercial fishers"), ("343", "participating vessels"), ("10", "districts"), ("63", "sectors")],
             "fr": [("797", "bénévoles, surtout des pêcheurs commerciaux"), ("343", "embarcations participantes"), ("10", "districts"), ("63", "secteurs")]}},

  "about": {"slug": {"en": "organization", "fr": "organisation"},
   "title": {"en": "Organization", "fr": "Organisation"},
   "body": {
    "en": """<section class="wrap split"><div class="prose">
<h2>Structure</h2><p>CCGA (NL) Inc. is controlled by its Board of Directors and jointly administered by its Executive, employees and the CCGA Regional Coordinator. The regional presidents form the CCGA National Council, which negotiates the contribution agreement with the Minister of Fisheries and Oceans — usually for five years, and valid only once signed by every president.</p>
<h2>Operations</h2><p>Operationally, CCGA (NL) is divided into ten districts and sixty-three sectors, so the SAR controller can quickly pinpoint available resources. An annual membership renewal keeps information at the Maritime Rescue Sub-Centre (MRSC) accurate, and members call in changes affecting their vessels so updates reach the MRSC daily.</p>
<p>Members have responded to major incidents such as the <i>Marie Teixeira Vilarinho</i> (September 1980), <i>Norma &amp; Gladys</i> and <i>Taskall</i> (October 1984) and <i>Zidani</i> (November 1986), and have received awards including the Commissioner's Commendation, Medals of Bravery and awards from the Canadian Power and Sail Squadrons.</p></div>
<div class="card"><h3>Membership responsibilities</h3><p><b>Members:</b></p><ul><li>Make available seaworthy, crewed vessels meeting CCGA and CCG standards, with inspections at enrolment and after — or contribute a skilled volunteer effort instead</li><li>Take the training the CCG and CCGA require</li><li>Follow CCGA bylaws and guidelines and conduct authorized activities prudently and safely</li></ul><p><b>Coast Guard, through the Auxiliary:</b></p><ul><li>Reimburses out-of-pocket expenses for authorized activities</li><li>Provides insurance for members and vessels during authorized activities</li><li>Keeps members informed and helps them build skills</li></ul></div></section>""",
    "fr": """<section class="wrap split"><div class="prose">
<h2>Structure</h2><p>La GCAC (TNL) inc. est dirigée par son conseil d'administration et administrée conjointement par son exécutif, ses employés et le coordonnateur régional de la GCAC. Les présidents régionaux forment le Conseil national de la GCAC, qui négocie l'accord de contribution avec le ministre des Pêches et des Océans — habituellement pour cinq ans, et valide seulement une fois signé par chaque président.</p>
<h2>Opérations</h2><p>Sur le plan opérationnel, la GCAC (TNL) est divisée en dix districts et soixante-trois secteurs, pour que le contrôleur SAR repère rapidement les ressources disponibles. Le renouvellement annuel des adhésions tient à jour l'information au Centre secondaire de sauvetage maritime (CSSM), et les membres signalent tout changement touchant leur embarcation pour une mise à jour quotidienne.</p>
<p>Les membres sont intervenus lors d'incidents majeurs comme ceux du <i>Marie Teixeira Vilarinho</i> (septembre 1980), du <i>Norma &amp; Gladys</i> et du <i>Taskall</i> (octobre 1984) et du <i>Zidani</i> (novembre 1986), et ont reçu des distinctions dont la Mention élogieuse du commissaire, des Médailles de la bravoure et des prix des Escadrilles canadiennes de plaisance.</p></div>
<div class="card"><h3>Responsabilités des membres</h3><p><b>Les membres :</b></p><ul><li>Mettent à disposition des embarcations en état de navigabilité, avec équipage, conformes aux normes de la GCAC et de la GCC, inspectées à l'adhésion et par la suite — ou apportent plutôt une contribution bénévole qualifiée</li><li>Suivent la formation exigée par la GCC et la GCAC</li><li>Respectent les règlements et lignes directrices de la GCAC et mènent les activités autorisées avec prudence</li></ul><p><b>La Garde côtière, par l'entremise de l'Auxiliaire :</b></p><ul><li>Rembourse les dépenses engagées lors des activités autorisées</li><li>Assure les membres et leurs embarcations pendant les activités autorisées</li><li>Tient les membres informés et les aide à développer leurs compétences</li></ul></div></section>"""}},

  "districts": {"slug": {"en": "districts", "fr": "districts"},
   "title": {"en": "Districts and board", "fr": "Districts et conseil"},
   "body": {
    "en": """<section class="wrap"><div class="card"><table><thead><tr><th>District</th><th>Director</th><th>Role</th><th>Contact</th></tr></thead><tbody>
<tr><td>1</td><td>Marcel O'Brien</td><td>1st Vice-President</td><td><a href="mailto:Marcel.OBrien@ccga-nl.ca">Marcel.OBrien@ccga-nl.ca</a> · 709-927-5540</td></tr>
<tr><td>2</td><td>Ron Pittman</td><td>Director</td><td><a href="mailto:Ron.Pittman@ccga-nl.ca">Ron.Pittman@ccga-nl.ca</a> · 709-866-2505</td></tr>
<tr><td>3</td><td>Julia Crocker</td><td>Director</td><td><a href="mailto:Julia.Crocker@ccga-nl.ca">Julia.Crocker@ccga-nl.ca</a> · 709-660-7385</td></tr>
<tr><td>4</td><td>Wesley Snook</td><td>Director</td><td><a href="mailto:Wesley.Snook@ccga-nl.ca">Wesley.Snook@ccga-nl.ca</a> · 709-885-2422</td></tr>
<tr><td>5</td><td>Winston Pitcher</td><td>Director</td><td><a href="mailto:Winston.Pitcher@ccga-nl.ca">Winston.Pitcher@ccga-nl.ca</a> · 709-728-6115</td></tr>
<tr><td>6</td><td>Rom Dalton</td><td>Secretary / Treasurer</td><td><a href="mailto:Rom.Dalton@ccga-nl.ca">Rom.Dalton@ccga-nl.ca</a> · 709-521-2555</td></tr>
<tr><td>7</td><td>James Chidley</td><td>President</td><td><a href="mailto:James.Chidley@ccga-nl.ca">James.Chidley@ccga-nl.ca</a> · 709-363-2931</td></tr>
<tr><td>8</td><td>Ross Petten</td><td>2nd Vice-President</td><td><a href="mailto:Ross.Petten@ccga-nl.ca">Ross.Petten@ccga-nl.ca</a> · 709-683-3218</td></tr>
<tr><td>9</td><td>Aidan Penton</td><td>Immediate Past President</td><td><a href="mailto:Aidan.Penton@ccga-nl.ca">Aidan.Penton@ccga-nl.ca</a> · 709-682-2162</td></tr>
<tr><td>10</td><td>Jeremy Ryan</td><td>Director</td><td><a href="mailto:Jeremy.Ryan@ccga-nl.ca">Jeremy.Ryan@ccga-nl.ca</a> · 709-293-4083</td></tr>
</tbody></table></div></section>""",
    "fr": """<section class="wrap"><div class="card"><table><thead><tr><th>District</th><th>Administrateur</th><th>Rôle</th><th>Coordonnées</th></tr></thead><tbody>
<tr><td>1</td><td>Marcel O'Brien</td><td>1<sup>er</sup> vice-président</td><td><a href="mailto:Marcel.OBrien@ccga-nl.ca">Marcel.OBrien@ccga-nl.ca</a> · 709-927-5540</td></tr>
<tr><td>2</td><td>Ron Pittman</td><td>Administrateur</td><td><a href="mailto:Ron.Pittman@ccga-nl.ca">Ron.Pittman@ccga-nl.ca</a> · 709-866-2505</td></tr>
<tr><td>3</td><td>Julia Crocker</td><td>Administratrice</td><td><a href="mailto:Julia.Crocker@ccga-nl.ca">Julia.Crocker@ccga-nl.ca</a> · 709-660-7385</td></tr>
<tr><td>4</td><td>Wesley Snook</td><td>Administrateur</td><td><a href="mailto:Wesley.Snook@ccga-nl.ca">Wesley.Snook@ccga-nl.ca</a> · 709-885-2422</td></tr>
<tr><td>5</td><td>Winston Pitcher</td><td>Administrateur</td><td><a href="mailto:Winston.Pitcher@ccga-nl.ca">Winston.Pitcher@ccga-nl.ca</a> · 709-728-6115</td></tr>
<tr><td>6</td><td>Rom Dalton</td><td>Secrétaire-trésorier</td><td><a href="mailto:Rom.Dalton@ccga-nl.ca">Rom.Dalton@ccga-nl.ca</a> · 709-521-2555</td></tr>
<tr><td>7</td><td>James Chidley</td><td>Président</td><td><a href="mailto:James.Chidley@ccga-nl.ca">James.Chidley@ccga-nl.ca</a> · 709-363-2931</td></tr>
<tr><td>8</td><td>Ross Petten</td><td>2<sup>e</sup> vice-président</td><td><a href="mailto:Ross.Petten@ccga-nl.ca">Ross.Petten@ccga-nl.ca</a> · 709-683-3218</td></tr>
<tr><td>9</td><td>Aidan Penton</td><td>Président sortant</td><td><a href="mailto:Aidan.Penton@ccga-nl.ca">Aidan.Penton@ccga-nl.ca</a> · 709-682-2162</td></tr>
<tr><td>10</td><td>Jeremy Ryan</td><td>Administrateur</td><td><a href="mailto:Jeremy.Ryan@ccga-nl.ca">Jeremy.Ryan@ccga-nl.ca</a> · 709-293-4083</td></tr>
</tbody></table></div></section>"""}},

  "join": {"slug": {"en": "join", "fr": "adherer"},
   "title": {"en": "Join our team", "fr": "Se joindre à l'équipe"},
   "body": {
    "en": """<section class="wrap split"><div class="prose"><h2>Joining a SAR team</h2><ul>
<li>You must own a vessel or be listed as alternate skipper on a vessel.</li><li>Each request for an application is considered individually and must be approved by the appropriate District Director.</li><li>There are two applications: one for vessel owners, one for other members (co-owners and alternate skippers).</li><li>Each package includes the application form, a Waiver of Salvage Rights and an Acknowledgment and Waiver.</li><li>Vessels of 15 GRT and over need a valid CSI certificate.</li><li>Proof of vessel ownership is required (certificate of registry or equivalent).</li></ul>
<h2>More ways to volunteer</h2><ul><li>Advocate for boating safety</li><li>Vessel maintenance and equipment management</li><li>Fundraising and special events</li><li>Media and marketing</li></ul></div>
<div class="card accent"><h3>Request an application</h3><p>Call <a href="tel:+18005636158">1-800-563-6158</a> or contact your <a href="{r:districts}">District Director</a>.</p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose"><h2>Se joindre à une équipe SAR</h2><ul>
<li>Il faut être propriétaire d'une embarcation ou inscrit comme patron suppléant sur une embarcation.</li><li>Chaque demande est étudiée individuellement et doit être approuvée par le directeur de district concerné.</li><li>Il existe deux formulaires : un pour les propriétaires, un pour les autres membres (copropriétaires et patrons suppléants).</li><li>Chaque trousse comprend le formulaire, une renonciation aux droits de sauvetage et une reconnaissance et renonciation.</li><li>Les embarcations de 15 tjb et plus doivent avoir un certificat d'inspection valide.</li><li>Une preuve de propriété est exigée (certificat d'immatriculation ou l'équivalent).</li></ul>
<h2>D'autres façons d'aider</h2><ul><li>Promouvoir la sécurité nautique</li><li>Entretien des embarcations et de l'équipement</li><li>Collectes de fonds et événements spéciaux</li><li>Médias et marketing</li></ul></div>
<div class="card accent"><h3>Demander un formulaire</h3><p>Composez le <a href="tel:+18005636158">1-800-563-6158</a> ou communiquez avec votre <a href="{r:districts}">directeur de district</a>.</p></div></section>"""}},

  "faq": {"slug": {"en": "faq", "fr": "faq"},
   "title": {"en": "Insurance FAQ", "fr": "FAQ — assurances"},
   "body": {
    "en": """<section class="wrap prose faq">
<details><summary>When does a member's insurance begin?</summary><p>Once the member has been enrolled and accepted by an Auxiliary association and has signed the Memorandum of Understanding (MOU) between the CCGA and the member.</p></details>
<details><summary>When does an owner/operator's vessel coverage begin?</summary><p>Once the vessel has been enrolled and accepted by the Canadian Coast Guard as an Auxiliary vessel, and the owner/operator has been enrolled, accepted and has signed the MOU. Coverage applies during an Authorized Activity.</p></details>
<details><summary>Do I use Medicare and my own health plan first?</summary><p>Yes. Medicare pays first, then any private group plan; the CCGA plan sits on top as third payer — or second payer if you have no group plan.</p></details>
<details><summary>Am I covered if I haven't returned my signed MOU?</summary><p>Yes — an administrative technicality should never interfere with saving lives. But every effort must be made to return it; a member who refuses may eventually be struck from the list.</p></details>
<details><summary>Am I covered while co-crewing on a Coast Guard vessel?</summary><p>Yes. Co-crewing on a CCG vessel is an Authorized Activity.</p></details>
<details><summary>Is my spouse covered when travelling with me to a CCGA function?</summary><p>No — unless your spouse is an enrolled Auxiliary member authorized to attend.</p></details>
</section>""",
    "fr": """<section class="wrap prose faq">
<details><summary>Quand débute l'assurance d'un membre?</summary><p>Dès que le membre a été inscrit et accepté par une association de l'Auxiliaire et qu'il a signé le protocole d'entente entre la GCAC et le membre.</p></details>
<details><summary>Quand débute la couverture de l'embarcation d'un propriétaire-exploitant?</summary><p>Dès que l'embarcation a été inscrite et acceptée par la Garde côtière canadienne comme embarcation de l'Auxiliaire, et que le propriétaire-exploitant a été inscrit, accepté et a signé le protocole d'entente. La couverture s'applique pendant une activité autorisée.</p></details>
<details><summary>Dois-je d'abord utiliser l'assurance maladie publique et mon régime privé?</summary><p>Oui. Le régime public paie d'abord, puis tout régime collectif privé; le régime de la GCAC intervient en troisième — ou en deuxième si vous n'avez pas de régime collectif.</p></details>
<details><summary>Suis-je couvert si je n'ai pas retourné mon protocole d'entente signé?</summary><p>Oui — un détail administratif ne doit jamais nuire au sauvetage de vies. Mais tout doit être fait pour le retourner; un membre qui refuse pourrait être radié.</p></details>
<details><summary>Suis-je couvert lorsque je fais partie de l'équipage d'un navire de la Garde côtière?</summary><p>Oui. Servir à bord d'un navire de la GCC est une activité autorisée.</p></details>
<details><summary>Mon conjoint est-il couvert lorsqu'il m'accompagne à une activité de la GCAC?</summary><p>Non — sauf s'il est lui-même membre inscrit de l'Auxiliaire et autorisé à y participer.</p></details>
</section>"""}},

  "contact": {"slug": {"en": "contact", "fr": "contact"},
   "title": {"en": "Contact CCGA-NL", "fr": "Joindre la GCAC-TNL"},
   "body": {
    "en": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Marine emergency</h3><p>VHF Channel 16 · <strong>*16</strong> on a mobile phone · <strong>911</strong></p></div>
<h2>Office</h2><p>878-C Topsail Road, Mount Pearl<br>Mailing: PO Box 938, St. John's, NL A1C 5M3<br>Toll free: <a href="tel:+18005636158">1-800-563-6158</a> · Office: 709-772-4428 · Fax: 709-772-4109</p></div>
<div class="card"><h3>Leadership</h3><p>James Chidley, President<br>Kelly Doody, Executive Director — <a href="mailto:Kelly.Doody@ccga-nl.ca">Kelly.Doody@ccga-nl.ca</a></p><p class="small">Regional website (documents, gallery, In Memoriam): <a href="https://ccga-nl.ca/" rel="noopener">ccga-nl.ca</a></p></div></section>""",
    "fr": """<section class="wrap split"><div class="prose"><div class="card emergency-card"><h3>Urgence maritime</h3><p>Canal VHF 16 · <strong>*16</strong> sur un cellulaire · <strong>911</strong></p></div>
<h2>Bureau</h2><p>878-C, chemin Topsail, Mount Pearl<br>Adresse postale : C.P. 938, St. John's (T.-N.-L.) A1C 5M3<br>Sans frais : <a href="tel:+18005636158">1-800-563-6158</a> · Bureau : 709-772-4428 · Téléc. : 709-772-4109</p></div>
<div class="card"><h3>Direction</h3><p>James Chidley, président<br>Kelly Doody, direction générale — <a href="mailto:Kelly.Doody@ccga-nl.ca">Kelly.Doody@ccga-nl.ca</a></p><p class="small">Site régional (documents, galerie, In Memoriam) : <a href="https://ccga-nl.ca/" rel="noopener">ccga-nl.ca</a></p></div></section>"""}},
 }})
