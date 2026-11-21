# -*- coding: utf-8 -*-
"""National (CCGA National Inc.) content — EN / FR.
Source: ccga-gcac.ca (live site, read 2026-11-21) and the Kinsta demo shell."""

NATIONAL = {
  "key": "national",
  "path": {"en": "", "fr": ""},
  "name": {"en": "National", "fr": "National"},
  "short": {"en": "National", "fr": "National"},
  "org": {"en": "Canadian Coast Guard Auxiliary", "fr": "Garde côtière auxiliaire canadienne"},
  "sub": {"en": "", "fr": ""},
  "emergency": {"en": "VHF Radio: Channel 16 · Mobile: *16 or 911",
                "fr": "Radio VHF : canal 16 · Cellulaire : *16 ou 911"},
  "join": "volunteer", "donate": "donate",
  "contact_block": {
    "en": "<strong>Canadian Coast Guard Auxiliary (National) Inc.</strong><br>6040 East Sooke Road<br>Sooke, BC V9Z 0Z7<br><a href=\"mailto:manager@ccga-gcac.ca\">manager@ccga-gcac.ca</a>",
    "fr": "<strong>Garde côtière auxiliaire canadienne (nationale) inc.</strong><br>6040, East Sooke Road<br>Sooke (C.-B.) V9Z 0Z7<br><a href=\"mailto:manager@ccga-gcac.ca\">manager@ccga-gcac.ca</a>"},
  "nav": ["about", "regions", "what-we-do", "news", "contact"],
  "pages": {}
}

P = NATIONAL["pages"]

# ---------------------------------------------------------------- HOME
P["index"] = {
 "slug": {"en": "", "fr": ""},
 "title": {"en": "Saving lives on the water", "fr": "Sauver des vies sur l'eau"},
 "hero": {
   "en": ("Volunteers saving lives on the water",
          "More than 4,100 trained volunteers on three coasts and the Great Lakes, supporting the Canadian Coast Guard and National Defence in marine search and rescue since 1978."),
   "fr": ("Des bénévoles qui sauvent des vies sur l'eau",
          "Plus de 4 100 bénévoles formés sur les trois côtes et les Grands Lacs, en appui à la Garde côtière canadienne et à la Défense nationale en recherche et sauvetage maritimes depuis 1978.")},
 "body": {
  "en": """
<section class="band emergency-band"><div class="wrap">
<h2>For marine emergencies</h2>
<p>Contact your nearest Marine Communications and Traffic Services (MCTS) centre on <strong>VHF Channel 16 (156.8 MHz)</strong>, dial <strong>*16</strong> on a mobile phone, or call <strong>911</strong>.</p>
<p><a href="{r:regions}">Regional emergency numbers →</a></p>
</div></section>

<section class="wrap split">
<div>
<p class="eyebrow">Who we are</p>
<h2>Dedicated volunteers for marine search and rescue and safe boating</h2>
<p>The Canadian Coast Guard Auxiliary (CCGA) is a not-for-profit organization and a registered charity made up of volunteer resources throughout Canada. Since 1978 it has supported the Canadian Coast Guard and National Defence with search and rescue and environmental response.</p>
<p>Our volunteers also promote and support Transport Canada's Safe Boating Program through public outreach and education, and help check aids to navigation. Others contribute ashore: vessel and equipment maintenance, fundraising and special events, and media relations.</p>
<p><a class="btn btn-ghost" href="{r:about}">About the CCGA</a></p>
</div>
<div class="stats">
<div><b>4,139</b><span>members (2020-21)</span></div>
<div><b>964</b><span>participating vessels (2020-21)</span></div>
<div><b>8,027</b><span>maritime SAR calls, April 2015 – March 2020</span></div>
<div><b>24%</b><span>of all annual maritime SAR taskings</span></div>
</div>
</section>

<section class="band light"><div class="wrap">
<p class="eyebrow">The federation</p>
<h2>Six regions, one goal: saving lives on the water</h2>
<p>Six regional auxiliaries — each its own incorporated charity — cover all three coasts and the Great Lakes.</p>
{regioncards}
</div></section>

<section class="wrap split">
<div>
<p class="eyebrow">Join the team</p>
<h2>Volunteer</h2>
<p>Many volunteer crew members join with boating experience. But if you are committed and willing to learn from our training instructors, a non-mariner can also acquire the navigation and vessel-operator skills needed to support marine search and rescue. Prefer to help ashore? There are many roles there too.</p>
<p><a class="btn" href="{r:volunteer}">How to volunteer</a></p>
</div>
<div class="card accent">
<h3>Indigenous Community Boat Volunteer Program</h3>
<p>Funded by the Canadian Coast Guard, the ICBVP helps Indigenous communities buy a boat or equipment so they can take part in the marine safety system as active CCGA members.</p>
<p><a href="{r:icbvp}">About the program →</a></p>
</div>
</section>
""",
  "fr": """
<section class="band emergency-band"><div class="wrap">
<h2>Urgences maritimes</h2>
<p>Communiquez avec le centre des Services de communication et de trafic maritimes (SCTM) le plus proche sur le <strong>canal VHF 16 (156,8 MHz)</strong>, composez <strong>*16</strong> sur un cellulaire ou appelez le <strong>911</strong>.</p>
<p><a href="{r:regions}">Numéros d'urgence par région →</a></p>
</div></section>

<section class="wrap split">
<div>
<p class="eyebrow">Qui nous sommes</p>
<h2>Des bénévoles dévoués à la recherche et au sauvetage maritimes et à la sécurité nautique</h2>
<p>La Garde côtière auxiliaire canadienne (GCAC) est un organisme sans but lucratif et un organisme de bienfaisance enregistré composé de bénévoles partout au Canada. Depuis 1978, elle appuie la Garde côtière canadienne et la Défense nationale en recherche et sauvetage et en intervention environnementale.</p>
<p>Nos bénévoles font aussi la promotion du Programme de sécurité nautique de Transports Canada par la sensibilisation et l'éducation du public, et aident à vérifier les aides à la navigation. D'autres contribuent à terre : entretien des embarcations et de l'équipement, collectes de fonds et événements spéciaux, relations avec les médias.</p>
<p><a class="btn btn-ghost" href="{r:about}">À propos de la GCAC</a></p>
</div>
<div class="stats">
<div><b>4 139</b><span>membres (2020-2021)</span></div>
<div><b>964</b><span>embarcations participantes (2020-2021)</span></div>
<div><b>8 027</b><span>appels SAR maritimes, avril 2015 – mars 2020</span></div>
<div><b>24 %</b><span>de l'ensemble des missions SAR maritimes annuelles</span></div>
</div>
</section>

<section class="band light"><div class="wrap">
<p class="eyebrow">La fédération</p>
<h2>Six régions, un même but : sauver des vies sur l'eau</h2>
<p>Six organisations régionales — chacune un organisme de bienfaisance constitué distinct — couvrent les trois côtes et les Grands Lacs.</p>
{regioncards}
</div></section>

<section class="wrap split">
<div>
<p class="eyebrow">Joignez-vous à l'équipe</p>
<h2>Devenir bénévole</h2>
<p>Bien des membres d'équipage arrivent avec une expérience de la navigation. Mais si vous êtes engagé et prêt à apprendre de nos instructeurs, une personne sans expérience maritime peut aussi acquérir les compétences de navigation et de conduite d'embarcation nécessaires à la recherche et au sauvetage. Vous préférez aider à terre? Les rôles ne manquent pas.</p>
<p><a class="btn" href="{r:volunteer}">Comment devenir bénévole</a></p>
</div>
<div class="card accent">
<h3>Programme de bateaux bénévoles des communautés autochtones</h3>
<p>Financé par la Garde côtière canadienne, le PBBCA aide les communautés autochtones à acheter un bateau ou de l'équipement pour participer au système de sécurité maritime à titre de membres actifs de la GCAC.</p>
<p><a href="{r:icbvp}">À propos du programme →</a></p>
</div>
</section>
"""}}

# ---------------------------------------------------------------- ABOUT
P["about"] = {
 "slug": {"en": "about", "fr": "a-propos"},
 "title": {"en": "About the CCGA", "fr": "À propos de la GCAC"},
 "sub": ["president", "icbvp", "awards", "careers"],
 "body": {
  "en": """
<section class="wrap prose">
<h2>Our mission</h2>
<p>The Canadian Coast Guard Auxiliary's mission is to save lives on the water and promote safe boating.</p>
<h2>Our vision</h2>
<p>The Canadian Coast Guard Auxiliary aspires to become the premier volunteer water rescue and safety organization by:</p>
<ul><li>Striving to save all lives at risk</li><li>Educating water-users about safe practices</li><li>Sustaining Canada-wide partnerships with the Canadian Coast Guard and other maritime services agencies</li></ul>
<h2>Our values</h2>
<ul>
<li>Celebrate the courage, dedication and humanity of our volunteer crew members</li>
<li>Seek the highest standards of professionalism</li>
<li>Sustain our voluntary fellowship</li>
<li>Maintain our independence</li>
<li>Gain the awareness and support of the public</li>
<li>Encourage open and honest communications at all levels</li>
<li>Promote teamwork, both amongst ourselves and with our mission partners</li>
</ul>
<h2>How the federation is organized</h2>
<p>Each regional auxiliary is a separate federally incorporated, not-for-profit charity delivering the national CCGA objectives within its region. The regional presidents form the CCGA National Council, which deals with the federal government on matters common to all regions. The Auxiliary is funded through a contribution agreement negotiated with the Minister of Fisheries and Oceans, through the Canadian Coast Guard.</p>
<p>Distress calls are coordinated by Joint Rescue Coordination Centres and Maritime Rescue Sub-Centres, staffed by Canadian Armed Forces and Canadian Coast Guard SAR coordinators around the clock, who task the closest suitable resource — often an Auxiliary crew.</p>
<h2>Milestones</h2>
<ul class="timeline">
<li><b>1793</b> First lifesaving station in what is now Canada, on Sable Island, Nova Scotia.</li>
<li><b>1962</b> The Canadian Coast Guard is founded.</li>
<li><b>1971</b> The Coast Guard recruits its first volunteers for search and rescue.</li>
<li><b>1978</b> The Canadian Marine Rescue Auxiliary is created; it becomes the Canadian Coast Guard Auxiliary in 1997.</li>
<li><b>2017</b> Launch of the Indigenous Community Boat Volunteer Program.</li>
<li><b>2018</b> Coastal Nations Coast Guard Auxiliary, Canada's first Indigenous-led auxiliary, is incorporated.</li>
</ul>
</section>""",
  "fr": """
<section class="wrap prose">
<h2>Notre mission</h2>
<p>La mission de la Garde côtière auxiliaire canadienne est de sauver des vies sur l'eau et de promouvoir la sécurité nautique.</p>
<h2>Notre vision</h2>
<p>La Garde côtière auxiliaire canadienne aspire à devenir le principal organisme bénévole de sauvetage et de sécurité sur l'eau :</p>
<ul><li>en s'efforçant de sauver toutes les vies en danger;</li><li>en sensibilisant les usagers de l'eau aux pratiques sécuritaires;</li><li>en maintenant des partenariats pancanadiens avec la Garde côtière canadienne et les autres organismes de services maritimes.</li></ul>
<h2>Nos valeurs</h2>
<ul>
<li>Saluer le courage, le dévouement et l'humanité de nos membres d'équipage bénévoles</li>
<li>Viser les plus hautes normes de professionnalisme</li>
<li>Entretenir notre esprit de fraternité bénévole</li>
<li>Préserver notre indépendance</li>
<li>Gagner la reconnaissance et l'appui du public</li>
<li>Favoriser des communications ouvertes et honnêtes à tous les niveaux</li>
<li>Promouvoir le travail d'équipe, entre nous et avec nos partenaires de mission</li>
</ul>
<h2>Organisation de la fédération</h2>
<p>Chaque organisation régionale est un organisme de bienfaisance sans but lucratif distinct, constitué sous le régime fédéral, qui réalise les objectifs nationaux de la GCAC dans sa région. Les présidents régionaux forment le Conseil national de la GCAC, qui traite avec le gouvernement fédéral des questions communes à toutes les régions. L'Auxiliaire est financée par un accord de contribution négocié avec le ministre des Pêches et des Océans, par l'entremise de la Garde côtière canadienne.</p>
<p>Les appels de détresse sont coordonnés par les centres conjoints de coordination de sauvetage et les centres secondaires de sauvetage maritime, où des coordonnateurs SAR des Forces armées canadiennes et de la Garde côtière canadienne veillent jour et nuit et dépêchent la ressource appropriée la plus proche — souvent un équipage de l'Auxiliaire.</p>
<h2>Jalons</h2>
<ul class="timeline">
<li><b>1793</b> Première station de sauvetage au Canada actuel, sur l'île de Sable, en Nouvelle-Écosse.</li>
<li><b>1962</b> Création de la Garde côtière canadienne.</li>
<li><b>1971</b> La Garde côtière recrute ses premiers bénévoles en recherche et sauvetage.</li>
<li><b>1978</b> Création du Service auxiliaire canadien de sauvetage maritime, qui devient la Garde côtière auxiliaire canadienne en 1997.</li>
<li><b>2017</b> Lancement du Programme de bateaux bénévoles des communautés autochtones.</li>
<li><b>2018</b> Constitution de la Garde côtière auxiliaire des Nations côtières, première auxiliaire dirigée par des Autochtones au Canada.</li>
</ul>
</section>"""}}

# ---------------------------------------------------------------- PRESIDENT
P["president"] = {
 "slug": {"en": "presidents-message", "fr": "mot-du-president"},
 "title": {"en": "President's message", "fr": "Mot du président"},
 "body": {
  "en": """
<section class="wrap prose">
<blockquote>“With our volunteers, you find each day the very best of what it means to be a great citizen and community member. These people give of their time, their energy, and their passion with no expectations of return, accolade, or thanks. They prepare, train, and respond throughout the year so that others may live. It remains my great privilege to be associated with them.”<cite>— Randy Strandt, National President</cite></blockquote>
<h2>Randy Strandt</h2>
<p>Randy Strandt returns to the role of National President of the Canadian Coast Guard Auxiliary. With more than 25 years of volunteer service, he continues to serve as a Coxswain at the station in North Vancouver, BC. His past service includes Station Leader, Board Member, Treasurer and President of Royal Canadian Marine Search and Rescue, as well as National Treasurer and previous National President.</p>
<p>Randy started out as a volunteer firefighter in a small community on Vancouver Island, following his father and older brother. When school took him away from home, he found the CCGA, where he serves with some of the best people in the country from coast to coast to coast. His family's connection with the sea runs deep: one grandfather served with the Canadian Coast Guard, the other was a Merchant Mariner, and his son serves in the Royal Canadian Navy.</p>
<p>By day, Randy is Financial Controller for Seaspan in North Vancouver. He holds a business degree from Simon Fraser University and is a Chartered Professional Accountant with 25 years of experience.</p>
</section>""",
  "fr": """
<section class="wrap prose">
<blockquote>« Chez nos bénévoles, on trouve chaque jour ce qu'il y a de meilleur dans le fait d'être un bon citoyen et un membre engagé de sa communauté. Ces personnes donnent leur temps, leur énergie et leur passion sans rien attendre en retour, ni honneurs ni remerciements. Elles se préparent, s'entraînent et interviennent toute l'année pour que d'autres puissent vivre. C'est pour moi un grand privilège de les côtoyer. »<cite>— Randy Strandt, président national</cite></blockquote>
<h2>Randy Strandt</h2>
<p>Randy Strandt reprend la présidence nationale de la Garde côtière auxiliaire canadienne. Fort de plus de 25 ans de bénévolat, il demeure patron d'embarcation à la station de North Vancouver (C.-B.). Il a notamment été chef de station, administrateur, trésorier et président de Royal Canadian Marine Search and Rescue, ainsi que trésorier national et président national.</p>
<p>Randy a commencé comme pompier volontaire dans une petite communauté de l'île de Vancouver, sur les traces de son père et de son frère aîné. Quand ses études l'ont éloigné de chez lui, il a trouvé la GCAC, où il sert aux côtés de gens parmi les meilleurs au pays, d'un océan à l'autre. Les liens de sa famille avec la mer sont profonds : un grand-père à la Garde côtière canadienne, l'autre dans la marine marchande, et son fils sert dans la Marine royale canadienne.</p>
<p>Dans la vie professionnelle, Randy est contrôleur financier chez Seaspan, à North Vancouver. Diplômé en administration de l'Université Simon Fraser, il est comptable professionnel agréé et cumule 25 ans d'expérience.</p>
</section>"""}}

# ---------------------------------------------------------------- ICBVP
P["icbvp"] = {
 "slug": {"en": "icbvp", "fr": "pbbca"},
 "title": {"en": "Indigenous Community Boat Volunteer Program", "fr": "Programme de bateaux bénévoles des communautés autochtones"},
 "body": {
  "en": """
<section class="wrap prose">
<p class="lead">Indigenous and coastal communities have a long history of responding to marine incidents, and are often the first — and only — responders able to reach remote locations in time to make a difference.</p>
<p>The Indigenous Community Boat Volunteer Program (ICBVP), funded by the Canadian Coast Guard, supports Indigenous communities to purchase a boat or the equipment they need to take part in the marine safety response system as active CCGA members. Once the program is established in a community, members are supported by their regional auxiliary. Launched in 2017, the program continues with renewed funding under the Oceans Protection Plan.</p>
<h2>Goals</h2>
<ul><li>Increase Indigenous participation in Canada's marine response system</li><li>Provide equipment so communities can join the Auxiliary, where they receive marine emergency response training and ongoing support</li></ul>
<h2>What funding can cover</h2>
<ul><li>Purchase, retrofit or repair of a SAR-capable boat</li><li>Equipment, including Transport Canada required safety equipment</li><li>A boat shelter and other related equipment</li></ul>
<p>The program does not prescribe the type of boat, since each community's needs and environment are unique — but all boats and equipment must meet Transport Canada and CCGA requirements. Funding is provided 100% up front.</p>
<h2>Eligibility</h2>
<p>First Nations, Inuit and Métis bands and settlements; Indigenous governments under self-government or modern treaties; Indigenous communities or groups; district, chiefs' and tribal councils; Indigenous-led organizations or those serving an Indigenous population; and corporations whose major shareholder is Indigenous.</p>
<p>A CCGA letter of support is mandatory. Non-Indigenous organizations serving an Indigenous population also need a letter from a band council, hamlet office or community council.</p>
<h2>Applying</h2>
<p>Applications are accepted once a year, typically due in the fall for funding starting the following April 1. They are assessed by a committee of SAR professionals, and funding flows through a contribution agreement between the Canadian Coast Guard and the community. Your <a href="{r:regions}">regional auxiliary</a> can provide the form and help with the application.</p>
<h2>Before you apply</h2>
<ul><li><b>Community capacity</b> — are there already Auxiliary members in the community?</li><li><b>Storage</b> — is there a safe place for the boat and equipment? If not, a shelter can be included.</li><li><b>Maintenance</b> — can the community maintain the boat and equipment?</li><li><b>Authority</b> — the person applying needs financial and signing authority.</li></ul>
<p>Receiving funding is a commitment to remain an active Auxiliary member and to use the assets for search and rescue for the initial life cycle of the boat or equipment, or 10 years, whichever is less.</p>
</section>""",
  "fr": """
<section class="wrap prose">
<p class="lead">Les communautés autochtones et côtières interviennent depuis toujours lors d'incidents maritimes; elles sont souvent les premières — et les seules — à pouvoir atteindre à temps les lieux éloignés.</p>
<p>Le Programme de bateaux bénévoles des communautés autochtones (PBBCA), financé par la Garde côtière canadienne, aide les communautés autochtones à acheter un bateau ou l'équipement nécessaire pour participer au système d'intervention en sécurité maritime à titre de membres actifs de la GCAC. Une fois le programme établi, les membres sont soutenus par leur organisation régionale. Lancé en 2017, le programme se poursuit grâce au financement renouvelé du Plan de protection des océans.</p>
<h2>Objectifs</h2>
<ul><li>Accroître la participation autochtone au système d'intervention maritime du Canada</li><li>Fournir l'équipement permettant aux communautés de se joindre à l'Auxiliaire, où elles reçoivent une formation en intervention d'urgence maritime et un soutien continu</li></ul>
<h2>Dépenses admissibles</h2>
<ul><li>Achat, modernisation ou réparation d'un bateau apte à la recherche et au sauvetage</li><li>Équipement, y compris l'équipement de sécurité exigé par Transports Canada</li><li>Abri à bateau et autre équipement connexe</li></ul>
<p>Le programme n'impose pas de type de bateau, puisque chaque communauté a ses propres besoins et son propre milieu — mais tout bateau et tout équipement doivent respecter les exigences de Transports Canada et de la GCAC. Le financement est versé entièrement à l'avance.</p>
<h2>Admissibilité</h2>
<p>Bandes et établissements des Premières Nations, des Inuits et des Métis; gouvernements autochtones visés par une entente d'autonomie gouvernementale ou un traité moderne; communautés ou groupes autochtones; conseils de district, de chefs et tribaux; organisations dirigées par des Autochtones ou desservant une population autochtone; sociétés dont l'actionnaire principal est autochtone.</p>
<p>Une lettre d'appui de la GCAC est obligatoire. Les organisations non autochtones qui desservent une population autochtone doivent aussi fournir une lettre d'un conseil de bande, d'un bureau de hameau ou d'un conseil communautaire.</p>
<h2>Présenter une demande</h2>
<p>Les demandes sont acceptées une fois par année, généralement à l'automne pour un financement débutant le 1<sup>er</sup> avril suivant. Elles sont évaluées par un comité de professionnels de la recherche et du sauvetage, et le financement est versé au moyen d'un accord de contribution entre la Garde côtière canadienne et la communauté. Votre <a href="{r:regions}">organisation régionale</a> peut vous fournir le formulaire et vous accompagner.</p>
<h2>Avant de présenter une demande</h2>
<ul><li><b>Capacité communautaire</b> — y a-t-il déjà des membres de l'Auxiliaire dans la communauté?</li><li><b>Entreposage</b> — existe-t-il un endroit sûr pour le bateau et l'équipement? Sinon, un abri peut être inclus.</li><li><b>Entretien</b> — la communauté peut-elle entretenir le bateau et l'équipement?</li><li><b>Autorité</b> — la personne qui présente la demande doit avoir le pouvoir financier et de signature.</li></ul>
<p>Recevoir ce financement, c'est s'engager à demeurer membre actif de l'Auxiliaire et à utiliser les biens pour la recherche et le sauvetage pendant le cycle de vie initial du bateau ou de l'équipement, ou 10 ans, selon la plus courte période.</p>
</section>"""}}

# ---------------------------------------------------------------- AWARDS
P["awards"] = {
 "slug": {"en": "awards", "fr": "distinctions"},
 "title": {"en": "Awards and recognition", "fr": "Prix et distinctions"},
 "body": {
  "en": """
<section class="wrap prose">
<p class="lead">Auxiliary volunteers receive no direct compensation for their part in Canada's search and rescue program. The National Awards Program recognizes their role through distinction awards.</p>
</section>
<section class="wrap grid3">
<div class="card"><h3>Heroism Medal</h3><p>The Auxiliary's highest honour.</p></div>
<div class="card"><h3>Exemplary Service Medal</h3><p>Honours the lifetime achievements of members whose contribution to the organization has been outstanding.</p></div>
<div class="card"><h3>Operational Merit Medal</h3><p>Recognizes superior skill in performing an assist, a rescue or other meritorious operational service.</p></div>
<div class="card"><h3>Leadership Medal</h3><p>Recognizes sustained professional or leadership achievement in operations or administration.</p></div>
<div class="card"><h3>Humanitarian Service Medal</h3><p>For members and non-members who distinguish themselves by direct participation in a significant humanitarian act or operation.</p></div>
<div class="card"><h3>Administrative Excellence Medal</h3><p>For members and non-members in recognition of outstanding administrative achievement or service to the Auxiliary.</p></div>
<div class="card"><h3>Long Service Medal</h3><p>Service pins and medal for members reaching the corresponding years of service.</p></div>
</section>""",
  "fr": """
<section class="wrap prose">
<p class="lead">Les bénévoles de l'Auxiliaire ne reçoivent aucune rémunération directe pour leur rôle au sein du programme canadien de recherche et sauvetage. Le Programme national de distinctions souligne leur contribution.</p>
</section>
<section class="wrap grid3">
<div class="card"><h3>Médaille de l'héroïsme</h3><p>La plus haute distinction de l'Auxiliaire.</p></div>
<div class="card"><h3>Médaille du service exemplaire</h3><p>Honore l'ensemble des réalisations de membres dont la contribution à l'organisation a été exceptionnelle.</p></div>
<div class="card"><h3>Médaille du mérite opérationnel</h3><p>Souligne une habileté supérieure lors d'une assistance, d'un sauvetage ou d'un autre service opérationnel méritoire.</p></div>
<div class="card"><h3>Médaille du leadership</h3><p>Reconnaît des réalisations professionnelles ou de leadership soutenues, en opérations ou en administration.</p></div>
<div class="card"><h3>Médaille du service humanitaire</h3><p>Pour les membres et non-membres qui se distinguent par leur participation directe à un acte ou à une opération humanitaire d'importance.</p></div>
<div class="card"><h3>Médaille de l'excellence administrative</h3><p>Pour les membres et non-membres, en reconnaissance d'une réalisation ou d'un service administratif exceptionnel.</p></div>
<div class="card"><h3>Médaille de long service</h3><p>Épinglettes et médaille remises aux membres selon leurs années de service.</p></div>
</section>"""}}

# ---------------------------------------------------------------- CAREERS
P["careers"] = {
 "slug": {"en": "careers", "fr": "carrieres"},
 "title": {"en": "Careers", "fr": "Carrières"},
 "body": {
  "en": """
<section class="wrap prose">
<p>The Canadian Coast Guard Auxiliary is an equal opportunity employer, supporting diversity, equity and inclusion. In accordance with the <i>Accessible Canada Act, 2019</i> and applicable provincial accessibility standards, accommodation is available on request to applicants with disabilities throughout the recruitment, selection and assessment process.</p>
<div class="card"><p><strong>There are no job openings at the moment.</strong> Regional auxiliaries post their own openings — see the <a href="{r:regions}">regions</a>.</p></div>
</section>""",
  "fr": """
<section class="wrap prose">
<p>La Garde côtière auxiliaire canadienne souscrit à l'égalité d'accès à l'emploi et soutient la diversité, l'équité et l'inclusion. Conformément à la <i>Loi canadienne sur l'accessibilité</i> (2019) et aux normes provinciales applicables, des mesures d'adaptation sont offertes sur demande aux personnes en situation de handicap tout au long du processus de recrutement, de sélection et d'évaluation.</p>
<div class="card"><p><strong>Aucun poste n'est affiché pour le moment.</strong> Les organisations régionales publient leurs propres offres — voir les <a href="{r:regions}">régions</a>.</p></div>
</section>"""}}

# ---------------------------------------------------------------- REGIONS
P["regions"] = {
 "slug": {"en": "regions", "fr": "regions"},
 "title": {"en": "Our regions", "fr": "Nos régions"},
 "body": {
  "en": """
<section class="wrap prose"><p class="lead">The CCGA is a federation of six regional auxiliaries. Each is a separately incorporated charity with its own board, volunteers and contribution agreement, working under common national guidelines.</p></section>
<section class="wrap">{regiontable}</section>
<section class="wrap">{regioncards}</section>""",
  "fr": """
<section class="wrap prose"><p class="lead">La GCAC est une fédération de six organisations régionales. Chacune est un organisme de bienfaisance constitué distinct, avec son propre conseil, ses bénévoles et son accord de contribution, sous des lignes directrices nationales communes.</p></section>
<section class="wrap">{regiontable}</section>
<section class="wrap">{regioncards}</section>"""}}

# ---------------------------------------------------------------- WHAT WE DO
P["what-we-do"] = {
 "slug": {"en": "what-we-do", "fr": "nos-services"},
 "title": {"en": "What we do", "fr": "Nos services"},
 "sub": ["volunteer", "icbvp"],
 "body": {
  "en": """
<section class="wrap grid3">
<div class="card"><h3>Search and rescue response</h3><p>Volunteer crews are tasked by the Joint Rescue Coordination Centres and Maritime Rescue Sub-Centres to marine emergencies — around the clock, every day of the year. The average time to deploy resources to an emergency is about 25 minutes.</p></div>
<div class="card"><h3>Prevention and safe boating</h3><p>Pleasure craft courtesy checks, public education at shows, marinas and schools, kids' lifejacket loaner stations and mascots like Bobbie the Boat bring Transport Canada's safe boating messages to the public.</p></div>
<div class="card"><h3>Environmental and humanitarian response</h3><p>The Auxiliary supports the Canadian Coast Guard and National Defence in environmental response and, when called upon, humanitarian assistance on the water.</p></div>
<div class="card"><h3>Training</h3><p>Instructor-led operational readiness training prepares volunteers for many levels of maritime response, alongside joint exercises (SAREX) with other SAR agencies.</p></div>
<div class="card"><h3>Aids to navigation</h3><p>Volunteers help check aids to navigation and report on conditions in their home waters.</p></div>
<div class="card"><h3>Fisheries openings</h3><p>In Atlantic Canada, members provide on-water support during lobster and other fishing season openings.</p></div>
</section>""",
  "fr": """
<section class="wrap grid3">
<div class="card"><h3>Intervention en recherche et sauvetage</h3><p>Les équipages bénévoles sont dépêchés par les centres conjoints de coordination de sauvetage et les centres secondaires de sauvetage maritime lors d'urgences maritimes — jour et nuit, toute l'année. Le délai moyen de déploiement est d'environ 25 minutes.</p></div>
<div class="card"><h3>Prévention et sécurité nautique</h3><p>Vérifications de courtoisie des embarcations, sensibilisation dans les salons, marinas et écoles, stations de prêt de gilets pour enfants et mascottes comme Bobbie le bateau portent les messages de sécurité nautique de Transports Canada.</p></div>
<div class="card"><h3>Intervention environnementale et humanitaire</h3><p>L'Auxiliaire appuie la Garde côtière canadienne et la Défense nationale en intervention environnementale et, au besoin, en aide humanitaire sur l'eau.</p></div>
<div class="card"><h3>Formation</h3><p>Une formation de préparation opérationnelle donnée par des instructeurs prépare les bénévoles à plusieurs niveaux d'intervention, en plus d'exercices conjoints (SAREX) avec d'autres organismes SAR.</p></div>
<div class="card"><h3>Aides à la navigation</h3><p>Les bénévoles aident à vérifier les aides à la navigation et signalent les conditions dans leurs eaux.</p></div>
<div class="card"><h3>Ouverture des pêches</h3><p>Dans l'Atlantique, les membres assurent un soutien sur l'eau lors de l'ouverture de la pêche au homard et d'autres saisons.</p></div>
</section>"""}}

# ---------------------------------------------------------------- VOLUNTEER
P["volunteer"] = {
 "slug": {"en": "volunteer", "fr": "benevolat"},
 "title": {"en": "Volunteer", "fr": "Devenir bénévole"},
 "body": {
  "en": """
<section class="wrap split">
<div class="prose">
<p class="lead">Teamwork is one of our greatest strengths, and there are many ways to volunteer — on and off the water.</p>
<h2>Joining a SAR crew</h2>
<ul><li>Be the age of majority under provincial legislation</li><li>Be in good physical condition</li><li>Complete the Pleasure Craft Operator Certificate course</li><li>Hold Marine Basic First Aid or equivalent, with CPR/AED Level C</li></ul>
<p>Each region has additional requirements — for example, vessel ownership in Newfoundland and Labrador, or a fitness test and police check in British Columbia. <a href="{r:regions}">Contact the auxiliary nearest you.</a></p>
<h2>More ways to help</h2>
<ul><li>Advocate for boating safety</li><li>Vessel maintenance and equipment management</li><li>Fundraising and special events</li><li>Media and marketing</li></ul>
</div>
<div class="card accent">
<h3>Volunteer spotlight: Brian McShane</h3>
<p>A Central &amp; Arctic volunteer for more than 16 years, Brian is Arctic Operations Manager in Yellowknife, NWT, supporting 20 auxiliary units and more than 239 volunteers. He received the 2024 Mustang Survival Rescue of the Year at the Canadian Safe Boating Awards: on August 17, 2024, after a 16-foot vessel capsized on Great Slave Lake, he rescued seven people — four adults, two children and an eight-week-old infant.</p>
</div>
</section>
<section class="band light"><div class="wrap grid3">
<div><h3>Training</h3><p>Our volunteers are mission ready: instructor-led operational readiness training, plus joint exercises with other SAR agencies.</p></div>
<div><h3>Teamwork</h3><p>Many challenging, rewarding roles within the camaraderie of your crew.</p></div>
<div><h3>Response time</h3><p>Our average response time is 25 minutes to deploy resources to a marine emergency.</p></div>
</div></section>""",
  "fr": """
<section class="wrap split">
<div class="prose">
<p class="lead">Le travail d'équipe est l'une de nos plus grandes forces, et il y a bien des façons de faire du bénévolat — sur l'eau comme à terre.</p>
<h2>Se joindre à un équipage SAR</h2>
<ul><li>Avoir l'âge de la majorité selon la loi provinciale</li><li>Être en bonne condition physique</li><li>Réussir le cours menant à la Carte de conducteur d'embarcation de plaisance</li><li>Détenir un secourisme maritime de base ou l'équivalent, avec RCR/DEA niveau C</li></ul>
<p>Chaque région a des exigences additionnelles — par exemple, être propriétaire d'une embarcation à Terre-Neuve-et-Labrador, ou réussir un test de condition physique et une vérification policière en Colombie-Britannique. <a href="{r:regions}">Communiquez avec l'organisation la plus proche.</a></p>
<h2>D'autres façons d'aider</h2>
<ul><li>Promouvoir la sécurité nautique</li><li>Entretien des embarcations et gestion de l'équipement</li><li>Collectes de fonds et événements spéciaux</li><li>Médias et marketing</li></ul>
</div>
<div class="card accent">
<h3>Bénévole à l'honneur : Brian McShane</h3>
<p>Bénévole de la région du Centre et de l'Arctique depuis plus de 16 ans, Brian est gestionnaire des opérations de l'Arctique à Yellowknife (T.N.-O.); il appuie 20 unités et plus de 239 bénévoles. Il a reçu le prix Mustang Survival du sauvetage de l'année 2024 aux Prix canadiens de la sécurité nautique : le 17 août 2024, après le chavirement d'une embarcation de 16 pieds sur le Grand lac des Esclaves, il a secouru sept personnes — quatre adultes, deux enfants et un nourrisson de huit semaines.</p>
</div>
</section>
<section class="band light"><div class="wrap grid3">
<div><h3>Formation</h3><p>Nos bénévoles sont prêts pour la mission : formation de préparation opérationnelle donnée par des instructeurs et exercices conjoints avec d'autres organismes SAR.</p></div>
<div><h3>Travail d'équipe</h3><p>Des rôles stimulants et gratifiants, dans la camaraderie de votre équipage.</p></div>
<div><h3>Délai d'intervention</h3><p>Notre délai moyen de déploiement lors d'une urgence maritime est de 25 minutes.</p></div>
</div></section>"""}}

# ---------------------------------------------------------------- DONATE
P["donate"] = {
 "slug": {"en": "donate", "fr": "donner"},
 "title": {"en": "Donate", "fr": "Faire un don"},
 "body": {
  "en": """
<section class="wrap split">
<div class="prose">
<p class="lead">We are a volunteer charity with more than 4,100 members on all three coasts and the Great Lakes.</p>
<p>Your donation supports specialized training and personal protective equipment and safety gear, so that our volunteers are mission ready. Donations also support education and stewardship events that promote water and boating safety.</p>
<p>Thank you for helping save lives on the water.</p>
<p><a class="btn" href="https://www.canadahelps.org/en/charities/canadian-coast-guard-auxiliary-national-inc/" rel="noopener">Donate through CanadaHelps</a></p>
<p class="small">Cheques and postal money orders: payable to <i>Canadian Coast Guard Auxiliary (National) Inc.</i>, 6040 East Sooke Road, Sooke, BC V9Z 0Z7. Please do not send cash.<br>Registered charity (BN) 870298494RR0001.</p>
</div>
<div class="card"><h3>Give to a region</h3><p>Prefer to support crews close to home? Each regional auxiliary also accepts donations.</p>{regionlist}</div>
</section>""",
  "fr": """
<section class="wrap split">
<div class="prose">
<p class="lead">Nous sommes un organisme de bienfaisance bénévole de plus de 4 100 membres sur les trois côtes et les Grands Lacs.</p>
<p>Votre don finance une formation spécialisée ainsi que l'équipement de protection individuelle et de sécurité qui permettent à nos bénévoles d'être prêts pour la mission. Les dons soutiennent aussi des activités d'éducation et de sensibilisation à la sécurité nautique.</p>
<p>Merci de nous aider à sauver des vies sur l'eau.</p>
<p><a class="btn" href="https://www.canadahelps.org/fr/organismesdebienfaisance/canadian-coast-guard-auxiliary-national-inc/" rel="noopener">Donner par CanaDon</a></p>
<p class="small">Chèques et mandats postaux : à l'ordre de <i>Canadian Coast Guard Auxiliary (National) Inc.</i>, 6040, East Sooke Road, Sooke (C.-B.) V9Z 0Z7. Veuillez ne pas envoyer d'argent comptant.<br>Organisme de bienfaisance enregistré (NE) 870298494RR0001.</p>
</div>
<div class="card"><h3>Donner à une région</h3><p>Vous préférez soutenir les équipages de chez vous? Chaque organisation régionale accepte aussi les dons.</p>{regionlist}</div>
</section>"""}}

# ---------------------------------------------------------------- NEWS
P["news"] = {
 "slug": {"en": "news", "fr": "nouvelles"},
 "title": {"en": "News", "fr": "Nouvelles"},
 "body": {
  "en": """
<section class="wrap">
<h2>National news</h2>
<div class="grid2">
<article class="card"><h3>CCGA welcomes new CAO</h3><p>After an extensive search, Ed Helm has joined the CCGA as its first Chief Administrative Officer, a newly created position.</p></article>
<article class="card"><h3>Higher tax credits for volunteer firefighters and SAR volunteers</h3><p>The Department of Finance announced an increase to the tax credits available to volunteer firefighters and search and rescue volunteers, recognizing their critical role.</p></article>
<article class="card"><h3>Mustang Survival named first official partner</h3><p>The CCGA announced Mustang Survival as its first official partner.</p></article>
<article class="card"><h3>Oceans Protection Plan investments</h3><p>Transport Canada announced significant investments in marine safety, including support for Indigenous communities through the Oceans Protection Plan.</p></article>
</div>
<h2>Volunteer highlights</h2>
<div class="grid2">
<article class="card"><h3>Brian McShane — Central &amp; Arctic</h3><p>Arctic Operations Manager in Yellowknife and 2024 Rescue of the Year recipient.</p></article>
<article class="card"><h3>Rona Tepper — RCMSAR</h3><p>Seven years at RCMSAR Station 5, Crescent Beach.</p></article>
<article class="card"><h3>James Fraser</h3><p>After 20+ years in the Royal Canadian Navy and a second career in banking, now on his third — saving lives on the water.</p></article>
<article class="card"><h3>Jack Magnus — RCMSAR</h3><p>Five years at Station 10 (Richmond) and a year and a half with its governing body, the Fraser Marine Rescue Society.</p></article>
<article class="card"><h3>Julia Crocker — Newfoundland &amp; Labrador</h3><p>An auxiliary member since 2017 — the same year her parents Bonnie and Morris joined — and now District 3 Director.</p></article>
</div>
<p class="small">Follow day-to-day news on <a href="https://www.instagram.com/ccga_aux_gcac/" rel="noopener">Instagram</a> and on each region's social media.</p>
</section>""",
  "fr": """
<section class="wrap">
<h2>Nouvelles nationales</h2>
<div class="grid2">
<article class="card"><h3>Arrivée d'un nouveau directeur administratif</h3><p>Au terme d'une recherche approfondie, Ed Helm s'est joint à la GCAC à titre de premier directeur administratif, un poste nouvellement créé.</p></article>
<article class="card"><h3>Hausse des crédits d'impôt pour les pompiers volontaires et les bénévoles SAR</h3><p>Le ministère des Finances a annoncé une hausse des crédits d'impôt offerts aux pompiers volontaires et aux bénévoles en recherche et sauvetage, en reconnaissance de leur rôle essentiel.</p></article>
<article class="card"><h3>Mustang Survival, premier partenaire officiel</h3><p>La GCAC a annoncé que Mustang Survival devient son premier partenaire officiel.</p></article>
<article class="card"><h3>Investissements du Plan de protection des océans</h3><p>Transports Canada a annoncé d'importants investissements en sécurité maritime, notamment en soutien aux communautés autochtones, dans le cadre du Plan de protection des océans.</p></article>
</div>
<h2>Bénévoles à l'honneur</h2>
<div class="grid2">
<article class="card"><h3>Brian McShane — Centre et Arctique</h3><p>Gestionnaire des opérations de l'Arctique à Yellowknife et lauréat du sauvetage de l'année 2024.</p></article>
<article class="card"><h3>Rona Tepper — RCMSAR</h3><p>Sept ans à la station 5 de RCMSAR, à Crescent Beach.</p></article>
<article class="card"><h3>James Fraser</h3><p>Après plus de 20 ans dans la Marine royale canadienne et une deuxième carrière en finance, il en mène une troisième : sauver des vies sur l'eau.</p></article>
<article class="card"><h3>Jack Magnus — RCMSAR</h3><p>Cinq ans à la station 10 (Richmond) et un an et demi au sein de son organisme de gouvernance, la Fraser Marine Rescue Society.</p></article>
<article class="card"><h3>Julia Crocker — Terre-Neuve-et-Labrador</h3><p>Membre depuis 2017 — la même année que ses parents Bonnie et Morris — et aujourd'hui directrice du district 3.</p></article>
</div>
<p class="small">Suivez l'actualité sur <a href="https://www.instagram.com/ccga_aux_gcac/" rel="noopener">Instagram</a> et sur les réseaux sociaux de chaque région.</p>
</section>"""}}

# ---------------------------------------------------------------- CONTACT
P["contact"] = {
 "slug": {"en": "contact", "fr": "contact"},
 "title": {"en": "Contact", "fr": "Nous joindre"},
 "body": {
  "en": """
<section class="wrap split">
<div class="prose">
<div class="card emergency-card"><h3>Marine emergency?</h3><p>Do not use email. Call on <strong>VHF Channel 16</strong>, dial <strong>*16</strong> on a mobile phone, or call <strong>911</strong>. Regional rescue centre numbers are listed on each <a href="{r:regions}">region's page</a>.</p></div>
<h2>National office</h2>
<p>Canadian Coast Guard Auxiliary (National) Inc.<br>6040 East Sooke Road<br>Sooke, BC V9Z 0Z7</p>
<p><a href="mailto:manager@ccga-gcac.ca">manager@ccga-gcac.ca</a></p>
<p>Volunteering, local donations and media requests are best handled by the regional auxiliary for your area.</p>
</div>
<div class="card"><h3>Regional offices</h3>{regionlist}</div>
</section>""",
  "fr": """
<section class="wrap split">
<div class="prose">
<div class="card emergency-card"><h3>Urgence maritime?</h3><p>N'utilisez pas le courriel. Appelez sur le <strong>canal VHF 16</strong>, composez <strong>*16</strong> sur un cellulaire ou faites le <strong>911</strong>. Les numéros des centres de sauvetage figurent sur la page de chaque <a href="{r:regions}">région</a>.</p></div>
<h2>Bureau national</h2>
<p>Garde côtière auxiliaire canadienne (nationale) inc.<br>6040, East Sooke Road<br>Sooke (C.-B.) V9Z 0Z7</p>
<p><a href="mailto:manager@ccga-gcac.ca">manager@ccga-gcac.ca</a></p>
<p>Pour le bénévolat, les dons locaux et les demandes des médias, adressez-vous de préférence à l'organisation régionale de votre secteur.</p>
</div>
<div class="card"><h3>Bureaux régionaux</h3>{regionlist}</div>
</section>"""}}

# ---------------------------------------------------------------- PRIVACY / ACCESSIBILITY
P["privacy"] = {
 "slug": {"en": "privacy", "fr": "confidentialite"},
 "title": {"en": "Privacy", "fr": "Confidentialité"},
 "body": {
  "en": """<section class="wrap prose"><p>This website does not use cookies, analytics or tracking scripts and collects no personal information. If you write to us by email, we use your information only to answer you. The Auxiliary does not share supporters' names or addresses with other organizations. Questions: <a href="mailto:manager@ccga-gcac.ca">manager@ccga-gcac.ca</a>.</p></section>""",
  "fr": """<section class="wrap prose"><p>Ce site n'utilise ni témoins, ni outil d'analyse, ni script de suivi, et ne recueille aucun renseignement personnel. Si vous nous écrivez par courriel, vos renseignements servent uniquement à vous répondre. L'Auxiliaire ne communique pas les noms ni les adresses de ses donateurs à d'autres organisations. Questions : <a href="mailto:manager@ccga-gcac.ca">manager@ccga-gcac.ca</a>.</p></section>"""}}
P["accessibility"] = {
 "slug": {"en": "accessibility", "fr": "accessibilite"},
 "title": {"en": "Accessibility", "fr": "Accessibilité"},
 "body": {
  "en": """<section class="wrap prose"><p>This site aims to meet WCAG 2.1 level AA: semantic HTML, keyboard navigation without scripts, sufficient colour contrast and a layout that adapts to any screen size. If you encounter a barrier, write to <a href="mailto:manager@ccga-gcac.ca">manager@ccga-gcac.ca</a> and we will provide the information in another format.</p></section>""",
  "fr": """<section class="wrap prose"><p>Ce site vise la conformité aux WCAG 2.1, niveau AA : HTML sémantique, navigation au clavier sans script, contraste suffisant et mise en page adaptée à tous les écrans. Si vous rencontrez un obstacle, écrivez à <a href="mailto:manager@ccga-gcac.ca">manager@ccga-gcac.ca</a> et nous vous fournirons l'information dans un autre format.</p></section>"""}}
