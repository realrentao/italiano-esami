# -*- coding: utf-8 -*-
"""Dati strutturati del Vol.5 degli esami CELI (A1-C2).
Tema: Cultura italiana, arte e cucina (意大利文化、艺术与美食).
Questo modulo è consumato dal generatore (generator_template.py): la
struttura di LEVELS, sections, items e campi è identica a quella attesa
dal motore di rendering.
"""

VOL_NO = 5
THEME_EMOJI = "🎨"
THEME_TEXT = "意大利文化、艺术与美食"

LEVELS = []

# ============================== A1 =========================================
LEVELS.append({
    "code": "A1", "name": "CELI Impatto",
    "subtitle": "la mia famiglia / una gita fuori porta",
    "theme": "🎨 意大利文化、艺术与美食", "subj_max": 20,
    "audio": [],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo 1 — Cartolina（明信片）", "body":
"""Ciao Luca! Sono in montagna con la mia famiglia per una gita fuori porta. Oggi è domenica e fa bello. Mio padre cammina, mia madre legge un libro e io mangio un panino. Domani torniamo a casa. A presto! Marco"""},
            {"title": "Testo 2 — Biglietto（便条）", "body":
"""Ciao Paola! Domani andiamo al lago con i nonni per una gita. Porta il tuo costume e una mela. Mamma"""},
            {"title": "Testo 3 — Avviso（通知）", "body":
"""GITA FUORI PORTA — Domenica andiamo in campagna con la famiglia. Partenza alle 8.00. Pranzo al sacco. 5 euro. Vieni con mamma e papà!"""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Il Testo 1 è：", "options": ["A) un avviso", "B) una cartolina", "C) un biglietto"], "answer": 1},
            {"type": "mc", "prompt": "2. Il Testo 2 è：", "options": ["A) un avviso", "B) una cartolina", "C) un biglietto"], "answer": 2},
            {"type": "mc", "prompt": "3. Il Testo 3 è：", "options": ["A) un avviso", "B) una cartolina", "C) un biglietto"], "answer": 0},
            {"type": "mc", "prompt": "4. Marco è in montagna con：", "options": ["A) i nonni", "B) la sua famiglia", "C) un amico"], "answer": 1},
            {"type": "mc", "prompt": "5. La gita in campagna parte：", "options": ["A) sabato", "B) domenica alle 8.00", "C) lunedì"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Scrivi una cartolina a un amico/a（明信片 / 留言）",
             "prompt": "Scrivi una cartolina a un tuo amico/a. Parla di due cose: la tua famiglia e una gita fuori porta (dove vai? cosa fai?). Scrivi 2–3 frasi（30–50 parole）. Usa il presente. Inizia con \"Ciao [nome]!\" e firma in fondo.",
             "limit": "30–50 词",
             "reference":
"""Ciao Sara! Sono in campagna con la mia famiglia per una gita fuori porta. Mio padre cammina, mia madre legge e io mangio un panino. Domani torniamo a casa. La gita è molto bella! Un abbraccio, Marco."""},
         ]},
        {"kind": "oral", "title": "3. Prova orale（口语，含听力评定）",
         "tasks": [
            {"desc":
"""CELI A1 无独立听力卷，听力并入口语评定。考官先朗读 1–2 句简单指示（模拟音频文本），考生听懂并回应，再进入引导问答与简单表达。
听力原文（模拟音频文本，由考官朗读）：
— "Buongiorno. Come ti chiami?"
— "Domenica fai una gita fuori porta con la famiglia?"
① 考官引导问答（姓名 / 年龄 / 住址 / 家庭 / 郊游）：Come ti chiami? Quanti anni hai? Dove abiti? Con chi abiti? Fai gite fuori porta con la famiglia? Cosa fai in una gita?
② 简单表达：用 2–3 句介绍自己与家人一次郊游（"La domenica vado in montagna con la mia famiglia.", "Mangiamo un panino."）。""",
             "points": 20,
             "rubric":
"""① 听懂考官朗读的 1–2 句简单指示并作出回应（听力并入）；② 问答切题，使用 presente semplice 基本正确（famiglia, gita, domenica 等基础词）；③ 发音可懂，词汇为基础级；④ 能说出 2–3 句连贯自我介绍 / 郊游经历。达到 11 分即通过。""",
             "dims": [
                ("Pronuncia 发音", "发音可懂，重音基本正确，能听懂简单指令"),
                ("Fluenza 流利度", "能用基本词汇与单句作答，自我介绍连贯"),
                ("Grammatica 语法", "使用基础句型(essere/avere/presente)，错误不影响理解"),
                ("Contenuto 内容", "覆盖姓名 / 年龄 / 家庭 / 郊游等任务要求"),
                ("Interazione 互动", "能回应考官提问，维持简短交流"),
             ],
             "ref":
"""Buongiorno, mi chiamo Marco e ho dodici anni. Abito a Milano con la mia famiglia: mio padre, mia madre e io. Nel fine settimana faccio una gita fuori porta. La domenica vado in montagna con la mia famiglia: mio padre cammina, mia madre legge un libro e io mangio un panino. Domani torniamo a casa. Mi piace la natura e stare con la famiglia. E tu, fai gite con la tua famiglia?"""},
         ]},
    ],
})

# ============================== A2 =========================================
LEVELS.append({
    "code": "A2", "name": "CELI 1",
    "subtitle": "una ricetta italiana / una città da visitare",
    "theme": "🎨 意大利文化、艺术与美食", "subj_max": 30,
    "audio": [
        {"title": "Messaggio vocale — Firenze（听力原文）", "body":
"""Ciao! Sono a Firenze con i miei amici per un weekend. Oggi visitiamo il Duomo e Ponte Vecchio: il Duomo è molto grande e bello. Poi mangiamo una bistecca fiorentina, un piatto tipico qui. Domani andiamo agli Uffizi, un museo famoso. La sera camminiamo vicino al fiume Arno. Firenze è magnifica! Consiglio questa città a tutti."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo A — Ricetta（Spaghetti al pomodoro）", "body":
"""RICETTA: SPAGHETTI AL POMODORO. Per 4 persone. Ingredienti: 400 g di spaghetti, 800 g di pomodori, 2 spicchi d'aglio, olio, sale, basilico. Prima fai bollire l'acqua e cuoci gli spaghetti per 10 minuti. Intanto soffriggi l'aglio nell'olio, aggiungi i pomodori e cuoci per 15 minuti. Scola la pasta, mettila nel sugo, aggiungi il basilico. Buon appetito!"""},
            {"title": "Testo B — Guida città（Bologna）", "body":
"""BOLOGNA: UNA CITTÀ DA VISITARE. Bologna è una bella città del nord Italia, famosa per le sue torri e i portici. Puoi visitare Piazza Maggiore, mangiare una piadina e andare a piedi sotto i portici. Il centro è piccolo e tutto vicino! Ci sono anche musei e un mercato molto antico. È ideale per un weekend."""},
         ],
         "items": [
            {"type": "match", "prompt": "1. «Si cucinano i pomodori con l'aglio.» →", "options": ["A) Testo A (ricetta)", "B) Testo B (Bologna)"], "answer": 0},
            {"type": "match", "prompt": "2. «La città ha torri e portici.» →", "options": ["A) Testo A (ricetta)", "B) Testo B (Bologna)"], "answer": 1},
            {"type": "match", "prompt": "3. «Gli spaghetti cuociono per 10 minuti.» →", "options": ["A) Testo A (ricetta)", "B) Testo B (Bologna)"], "answer": 0},
            {"type": "mc", "prompt": "4. Gli spaghetti cuociono per：", "options": ["A) 5 minuti", "B) 10 minuti", "C) 20 minuti"], "answer": 1},
            {"type": "mc", "prompt": "5. Bologna si trova nel：", "options": ["A) nord Italia", "B) sud Italia", "C) mare"], "answer": 0},
            {"type": "mc", "prompt": "6. A Bologna puoi mangiare：", "options": ["A) una piadina", "B) un sushi", "C) una paella"], "answer": 0},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito 1 — Completamenti（补全短文）",
             "prompt": "Completa il testo con le parole: è / servono / facciamo / cuociamo / aggiungiamo. \"La ricetta _____ (1) molto facile. Per 4 persone _____ (2) servono 400 g di spaghetti. Noi _____ (3) facciamo bollire l'acqua e _____ (4) cuociamo la pasta per 10 minuti. Poi _____ (5) il sugo di pomodoro e il basilico.\"",
             "limit": "5 空",
             "reference": "La ricetta è molto facile. Per 4 persone servono 400 g di spaghetti. Noi facciamo bollire l'acqua e cuociamo la pasta per 10 minuti. Poi aggiungiamo il sugo di pomodoro e il basilico."},
            {"title": "Compito 2 — Espansione（扩写留言，50–80 词）",
             "prompt": "Da questo messaggio breve scrivi un biglietto più lungo (50–80 parole): \"Ciao Sara! Domenica vengo a Bologna con la mia famiglia. Voglio visitare la città. A presto!\" Perché Bologna? cosa volete vedere e mangiare?",
             "limit": "50–80 词",
             "reference":
"""Ciao Sara! Domenica vengo a Bologna con la mia famiglia per un weekend. Voglio visitare la città perché è famosa per le torri e i portici: possiamo camminare sotto i portici e vedere Piazza Maggiore. Mangeremo una piadina e un gelato in centro. È una città piccola e tutto è vicino, perfetta per una gita! A presto, Marco."""},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力）",
         "items": [
            {"type": "match", "prompt": "1. Il Duomo →", "options": ["a) museo famoso", "b) grande e bello", "c) vicino si cammina la sera"], "answer": 1},
            {"type": "match", "prompt": "2. Gli Uffizi →", "options": ["a) museo famoso", "b) grande e bello", "c) vicino si cammina la sera"], "answer": 0},
            {"type": "match", "prompt": "3. Il fiume Arno →", "options": ["a) museo famoso", "b) grande e bello", "c) vicino si cammina la sera"], "answer": 2},
            {"type": "mc", "prompt": "4. Firenze si visita per：", "options": ["A) un giorno", "B) un weekend", "C) un mese"], "answer": 1},
            {"type": "mc", "prompt": "5. La bistecca fiorentina è：", "options": ["A) un dolce", "B) un piatto tipico", "C) una bevanda"], "answer": 1},
            {"type": "mc", "prompt": "6. Domani visitano：", "options": ["A) il Duomo", "B) gli Uffizi", "C) il fiume"], "answer": 1},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 自我介绍 + 习惯爱好；② 描述图片；③ 角色扮演。
任务：① 介绍自己与一个兴趣（cucina, viaggi 或 sport）；② 描述一张意大利广场图片（piazza）：人们吃 gelato、散步（c'è? che tempo fa? cosa fanno le persone?）；③ 角色扮演：在旅游咨询处（ufficio turistico）向工作人员询问一座可游览的城市（dove andare? cosa vedere?）。""",
             "points": 20,
             "rubric":
"""① 自我介绍流利，用 presente e passato prossimo 谈兴趣；② 图片描述能使用 c'è / ci sono、天气与动作动词；③ 角色扮演能提出恰当问题（Dove consiglia di andare? Cosa si può vedere?）；④ 发音清楚，互动自然。""",
             "dims": [
                ("Pronuncia 发音", "发音清晰，重音基本正确"),
                ("Fluenza 流利度", "自我介绍流畅，含个人兴趣与爱好"),
                ("Grammatica 语法", "现在时 / 近过去时使用基本正确"),
                ("Contenuto 内容", "涵盖自我介绍、图片描述、角色扮演三项任务"),
                ("Interazione 互动", "角色扮演用语得体，完成信息询问"),
             ],
             "ref":
"""Buongiorno, mi presento: mi chiamo Marco, ho vent'anni e abito a Bologna. Nel tempo libero mi piace cucinare e viaggiare. Nella foto vedo una piazza italiana: ci sono persone che mangiano un gelato e camminano sotto il sole; fa bello e l'atmosfera è allegra. In ufficio turistico chiedo: «Mi consiglia una città da visitare? Cosa si può vedere e mangiare?» Consiglierei Bologna, famosa per le torri e i portici, dove si mangia una buona piadina."""},
         ]},
    ],
})

# ============================== B1 =========================================
LEVELS.append({
    "code": "B1", "name": "CELI 2",
    "subtitle": "le tradizioni italiane / un viaggio in Italia",
    "theme": "🎨 意大利文化、艺术与美食", "subj_max": 30,
    "audio": [
        {"title": "Dialogo — Viaggio in Sicilia（听力原文）", "body":
"""— Allora, Chiara, com'è andato il viaggio in Sicilia?
— Bellissimo! Siamo partite da Palermo e abbiamo visitato il Duomo e il mercato di Ballarò, pieno di colori e profumi. Poi siamo andate a Cefalù, un paese sul mare: abbiamo fatto il bagno e mangiato pesce fresco. A pranzo abbiamo assaggiato gli arancini, tipici di lì. Il terzo giorno siamo salite sull'Etna in funivia: fantastico! La sera a Palermo abbiamo ascoltato musica in piazza. Siamo tornate stanche ma felici."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo A — Invito（传统节日邀请）", "body":
"""Caro Marco, ti invito alla nostra cena di Natale, domenica 22 dicembre alle 20.00 a casa mia. Prepareremo i tortellini, una tradizione della mia famiglia bolognese. Ci saranno anche i miei nonni. Porta un dolce! A presto, Giulia"""},
            {"title": "Testo B — Menu（餐厅菜单）", "body":
"""RISTORANTE DA LUCA
Primi: Spaghetti al pomodoro € 9 — Tortellini in brodo € 12
Secondi: Bistecca fiorentina € 18 — Branzino € 16
Contorni: Insalata € 5 — Patate al forno € 5
Dolci: Tiramisù € 6"""},
            {"title": "Testo C — Diario di viaggio（意大利之旅日记）", "body":
"""La scorsa estate ho fatto un viaggio in Italia con i miei amici. Siamo andati a Roma e abbiamo visitato il Colosseo. Poi siamo partiti per Napoli e abbiamo mangiato la pizza più buona del mondo. È stato un viaggio indimenticabile!"""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. La cena di Natale è：", "options": ["A) sabato", "B) domenica 22 dicembre", "C) lunedì"], "answer": 1},
            {"type": "mc", "prompt": "2. I tortellini sono：", "options": ["A) una tradizione bolognese", "B) un dolce", "C) una bevanda"], "answer": 0},
            {"type": "mc", "prompt": "3. Nel viaggio hanno visitato：", "options": ["A) solo Roma", "B) Roma e Napoli", "C) Milano"], "answer": 1},
            {"type": "match", "prompt": "4. Testo A →", "options": ["a) menu", "b) invito", "c) diario"], "answer": 1},
            {"type": "match", "prompt": "5. Testo C →", "options": ["a) menu", "b) invito", "c) diario"], "answer": 2},
            {"type": "cloze", "text": "6. La scorsa estate _____ andato a Roma con i miei amici.", "answers": ["siamo"]},
            {"type": "cloze", "text": "7. _____ mangiato una pizza buonissima.", "answers": ["abbiamo"]},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito 1 — Questionario（问卷，60–80 词）",
             "prompt": "Compila il questionario sul tuo viaggio in Italia: Nome? Città visitate? Con chi? Tradizione italiana che ti è piaciuta? Cosa consigli? (scrivi 5–6 brevi risposte, 60–80 parole)",
             "limit": "60–80 词",
             "reference":
"""Mi chiamo Marco. Ho visitato Roma e Napoli in Italia. Ci sono andato con i miei amici due anni fa. La tradizione che mi è piaciuta di più è la domenica in famiglia a pranzo. A Napoli ho mangiato la pizza più buona del mondo. Consiglio di visitare il Colosseo e di provare la cucina locale. Porterei anche comode scarpe da cammino!"""},
            {"title": "Compito 2 — E-mail（给朋友写邮件，120–150 词）",
             "prompt": "Scrivi un'email a un amico e racconta un viaggio in Italia che hai fatto: dove sei andato, cosa hai visto, con chi eri, cosa ti è piaciuto di più e perché. Usa il passato (passato prossimo / imperfetto).",
             "limit": "120–150 词",
             "reference":
"""Ciao Sara! Ti scrivo per raccontarti il mio viaggio in Italia dello scorso anno. Sono andato a Roma con i miei genitori per una settimana. Abbiamo visitato il Colosseo, il Pantheon e Fontana di Trevi: è stata un'emozione! Poi siamo partiti per Napoli e lì ho mangiato la pizza più buona della mia vita, in una piccola pizzeria vicino al mare. Mi è piaciuto molto anche passeggiare la sera tra la gente e le luci. È stato un viaggio indimenticabile perché ho scoperto quante tradizioni vive ci sono nelle piazze italiane. Spero di tornare presto anche in Sicilia! Un abbraccio, Marco."""},
         ]},
        {"kind": "listening", "title": "3. Comprensione di testi orali（听力）",
         "items": [
            {"type": "match", "prompt": "1. Palermo →", "options": ["a) bagno e pesce fresco", "b) Duomo, mercato, musica in piazza", "c) arancini a pranzo", "d) salita in funivia"], "answer": 1},
            {"type": "match", "prompt": "2. Cefalù →", "options": ["a) bagno e pesce fresco", "b) Duomo, mercato, musica in piazza", "c) arancini a pranzo", "d) salita in funivia"], "answer": 0},
            {"type": "match", "prompt": "3. Etna →", "options": ["a) bagno e pesce fresco", "b) Duomo, mercato, musica in piazza", "c) arancini a pranzo", "d) salita in funivia"], "answer": 3},
            {"type": "match", "prompt": "4. Arancini →", "options": ["a) bagno e pesce fresco", "b) Duomo, mercato, musica in piazza", "c) arancini a pranzo", "d) salita in funivia"], "answer": 2},
            {"type": "mc", "prompt": "5. Il viaggio è in：", "options": ["A) Sardegna", "B) Sicilia", "C) Puglia"], "answer": 1},
            {"type": "mc", "prompt": "6. A Cefalù hanno：", "options": ["A) sciato", "B) fatto il bagno", "C) visitato un museo"], "answer": 1},
            {"type": "mc", "prompt": "7. Gli arancini sono：", "options": ["A) un dolce", "B) un piatto tipico", "C) una bevanda"], "answer": 1},
            {"type": "mc", "prompt": "8. Sull'Etna sono salite in：", "options": ["A) treno", "B) funivia", "C) barca"], "answer": 1},
            {"type": "mc", "prompt": "9. La sera a Palermo hanno：", "options": ["A) dormito", "B) ascoltato musica in piazza", "C) cucinato"], "answer": 1},
         ]},
        {"kind": "oral", "title": "4. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 自我介绍 / 兴趣 / 日常；② 描述图片；③ 角色扮演。
任务：① 介绍自己、兴趣与一项了解的意大利传统（es. il Natale, la domenica in famiglia）；② 描述一张意大利节日图片（festa di paese）：有乐队、食物摊位（descrivi l'atmosfera e le tradizioni）；③ 角色扮演：在酒店前台预订房间并询问当地传统活动（una festa? un piatto tipico?）。""",
             "points": 30,
             "rubric":
"""① 自我介绍连贯，presente + passato prossimo 叙述经历；② 图片描述使用形容词与场景词（festa, musica, cibo, gente）；③ 角色扮演能完成预订与询问（Ha una camera? Ci sono feste tradizionali?）；④ 互动自然，语法错误不影响理解。""",
             "dims": [
                ("Pronuncia 发音", "发音标准，语调节奏自然"),
                ("Fluenza 流利度", "连贯表达观点与经历，少停顿"),
                ("Grammatica 语法", "现在时 / 近过去时较准确，尝试复合句"),
                ("Contenuto 内容", "图片描述准确，角色扮演体现传统认知"),
                ("Interazione 互动", "能完成预订与询问，互动自然"),
             ],
             "ref":
"""Buongiorno, mi chiamo Marco e mi piace viaggiare. Una tradizione italiana che conosco è il pranzo della domenica in famiglia: ci riuniamo, mangiamo la pasta e parliamo. Nella foto vedo una festa di paese: c'è una banda che suona, bancarelle con il cibo e tanta gente allegra; l'atmosfera è calorosa e tradizionale. In albergo chiedo: «Ha una camera libera per due notti? Ci sono feste o piatti tipici da provare qui vicino?» Mi piace scoprire le tradizioni locali quando viaggio."""},
         ]},
    ],
})

# ============================== B2 =========================================
LEVELS.append({
    "code": "B2", "name": "CELI 3",
    "subtitle": "patrimonio UNESCO / enogastronomia",
    "theme": "🎨 意大利文化、艺术与美食", "subj_max": 50,
    "audio": [
        {"title": "Intervista 1 — Guida UNESCO（Ravenna）", "body":
"""Benvenuti a Ravenna, città patrimonio UNESCO per i suoi mosaici bizantini. Il sito comprende otto monumenti; il più famoso è San Vitale, con mosaici del VI secolo. Ogni anno accogliamo 400.000 visitatori. Il problema? I bus turistici intasano il centro e i mosaici soffrono l'umidità. Noi limitiamo i gruppi a 25 persone."""},
        {"title": "Intervista 2 — Produttrice（olio extravergine）", "body":
"""Io faccio olio extravergine in Puglia, terra di ulivi millenari. La mia azienda è piccola: 3.000 piante, raccolta a novembre, frantoio entro 12 ore. Vendo solo qui e a pochi ristoranti. La grande distribuzione paga poco, perciò difendo la filiera corta. Il turismo enogastronomico? Aiuta, ma deve essere lento."""},
        {"title": "Presentazione — Percorso enogastronomico", "body":
"""Il nostro percorso parte alle 9 da ALBA, capitale del tartufo. Alle 11 visitiamo una CANTINA nel Barolo, dove si spiega la DOCG. A mezzogiorno PRANZO con il vino locale. Nel pomeriggio, alle 15, laboratorio di FORMAGGIO a Bra. Alle 18 rientro. Costo 85 euro a PERSONA, bambini GRATIS. Prenotazione entro VENERDÌ."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "A.1 — Testo A1a（Patrimonio UNESCO: Roma）", "body":
"""Roma ospita il Centro storico con il Vaticano, iscritto nella lista UNESCO nel 1980 e ampliato nel 1990. Il riconoscimento tutela non solo monumenti singoli, ma un paesaggio urbano vivo, dove convivono resti antichi, chiese barocche e vita quotidiana. La sfida è conciliare turismo di massa e conservazione: ogni anno milioni di visitatori premono sulle vestigia, mentre i residenti chiedono spazi vivibili. La fruizione sostenibile del patrimonio è ormai una questione di governo della città, non solo di restauro."""},
            {"title": "A.1 — Testo A1b（Patrimonio UNESCO: Costiera Amalfitana）", "body":
"""La Costiera Amalfitana, dal 1997 patrimonio UNESCO, è un capolavoro di terrazzamenti agricoli sospesi sul mare, frutto di secoli di ingegno contadino. Qui l'architettura si piega alla pendenza: limoneti, vigneti e borghi colorati dialogano con la scogliera. Ma il successo turistico è una doppia spada: i flussi estivi intasano la statale 163 e i giovani emigrano, lasciando stagionalità e fragilità idrogeologica. Il paesaggio non si conserva per decreto: si mantiene abitandolo, coltivandolo, abbandonando l'idea che sia solo uno sfondo per fotografie."""},
            {"title": "A.2 — Testo A2a（Enogastronomia: il vino）", "body":
"""Il Chianti Classico nasce nei colli toscani da uve Sangiovese. La sua produzione è legata a una denominazione controllata e garantita (DOCG) che protegge il metodo e il territorio. Le cantine aprono al pubblico per degustazioni; il paesaggio del vigneto è parte integrante dell'esperienza enologica. Il vino racconta il legame tra suolo, clima e mano dell'uomo."""},
            {"title": "A.2 — Testo A2b（Enogastronomia: il formaggio）", "body":
"""Il Parmigiano Reggiano è un formaggio a latte crudo, stagionato minimo 12 mesi, nato nella pianura padana. La sua filiera è locale: vacche rosse, fieno, caseifici storici. Non contiene additivi. Ogni forma porta un numero che ne traccia l'origine. È un simbolo di enogastronomia lenta e di qualità territoriale."""},
            {"title": "A.3 — Testo（Fiera dell'enogastronomia）", "body":
"""Quando ho partecipato a una fiera dell'enogastronomia locale, ho capito che il cibo non è solo nutrimento: è identità. Piccoli produttori raccontavano ricette tramandate da generazioni, difendendo sapori che la grande distribuzione rischia di cancellare. Ho assaggiato un olio extravergine premuto a freddo e ho parlato con un agricoltore che coltiva come suo nonno. Quella fiera mi ha insegnato che valorizzare il patrimonio enogastronomico significa anche proteggere un modo di vivere. La cultura, a volte, si assaggia."""},
         ],
         "items": [
            {"type": "mc", "prompt": "A.1-1. Il Centro storico di Roma è iscritto UNESCO dal：", "options": ["A) 1990", "B) 1980 (ampliato 1990)", "C) 1997", "D) 1979"], "answer": 1},
            {"type": "mc", "prompt": "A.1-2. Il riconoscimento tutela：", "options": ["A) solo il Colosseo", "B) un paesaggio urbano vivo", "C) solo le chiese", "D) i musei"], "answer": 1},
            {"type": "mc", "prompt": "A.1-3. La sfida principale di Roma è：", "options": ["A) costruire hotel", "B) conciliare turismo e conservazione", "C) chiudere il centro", "D) vietare i turisti"], "answer": 1},
            {"type": "mc", "prompt": "A.1-4. La fruizione sostenibile è vista come：", "options": ["A) solo restauro", "B) governo della città", "C) un errore", "D) un lusso"], "answer": 1},
            {"type": "mc", "prompt": "A.1-5. La Costiera è patrimonio UNESCO dal：", "options": ["A) 1980", "B) 1990", "C) 1997", "D) 2000"], "answer": 2},
            {"type": "mc", "prompt": "A.1-6. I terrazzamenti sono frutto di：", "options": ["A) turismo", "B) ingegno contadino secolare", "C) decreti", "D) architetti moderni"], "answer": 1},
            {"type": "mc", "prompt": "A.1-7. «Il successo turistico è una doppia spada» significa：", "options": ["A) è solo positivo", "B) porta benefici e problemi", "C) è inutile", "D) è pericoloso"], "answer": 1},
            {"type": "mc", "prompt": "A.1-8. Sulla Costiera i giovani：", "options": ["A) arrivano", "B) emigrano", "C) costruiscono hotel", "D) studiano all'estero"], "answer": 1},
            {"type": "mc", "prompt": "A.1-9. Il paesaggio si conserva secondo il testo：", "options": ["A) per decreto", "B) abitandolo e coltivandolo", "C) chiudendolo", "D) fotografandolo"], "answer": 1},
            {"type": "match", "prompt": "A.2-1. «Nasce da uve Sangiovese.»", "options": ["A) vino", "B) formaggio"], "answer": 0},
            {"type": "match", "prompt": "A.2-2. «È stagionato minimo 12 mesi.»", "options": ["A) vino", "B) formaggio"], "answer": 1},
            {"type": "match", "prompt": "A.2-3. «Ha una denominazione DOCG.»", "options": ["A) vino", "B) formaggio"], "answer": 0},
            {"type": "match", "prompt": "A.2-4. «Si produce nella pianura padana.»", "options": ["A) vino", "B) formaggio"], "answer": 1},
            {"type": "match", "prompt": "A.2-5. «Le cantine aprono per degustazioni.»", "options": ["A) vino", "B) formaggio"], "answer": 0},
            {"type": "match", "prompt": "A.2-6. «Non contiene additivi.»", "options": ["A) vino", "B) formaggio"], "answer": 1},
            {"type": "match", "prompt": "A.2-7. «È legato a un territorio toscano.»", "options": ["A) vino", "B) formaggio"], "answer": 0},
            {"type": "match", "prompt": "A.2-8. «Ogni forma ha un numero di origine.»", "options": ["A) vino", "B) formaggio"], "answer": 1},
            {"type": "match", "prompt": "A.2-9. «È fatto con latte crudo.»", "options": ["A) vino", "B) formaggio"], "answer": 1},
            {"type": "match", "prompt": "A.2-10. «Il paesaggio del vigneto è parte dell'esperienza.»", "options": ["A) vino", "B) formaggio"], "answer": 0},
            {"type": "open", "prompt": "A.3-1. Perché, secondo il testo, il cibo è anche «identità»?", "ref": "Perché ricette tramandate e sapori raccontano una cultura / un modo di vivere.", "rows": 2},
            {"type": "open", "prompt": "A.3-2. Quale rischio cita per i sapori tradizionali?", "ref": "La grande distribuzione rischia di cancellarli.", "rows": 2},
            {"type": "open", "prompt": "A.3-3. Cosa ha imparato l'autore alla fiera?", "ref": "Che valorizzare l'enogastronomia significa proteggere un modo di vivere.", "rows": 2},
            {"type": "open", "prompt": "A.3-4. Che cosa significa «valorizzare il patrimonio enogastronomico»?", "ref": "Proteggere anche un modo di vivere e la cultura che si assaggia.", "rows": 2},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "B.1 — Testo personale / situazionale（二选一，120–180 词）",
             "prompt": "Scegli UNO: (a) Racconta un'esperienza personale in cui hai visitato un sito patrimonio UNESCO e spiega che effetto ti ha fatto. (b) Descrivi come l'enogastronomia della tua regione (o di una che conosci) racconta la sua cultura.",
             "limit": "120–180 词",
             "reference":
"""Lo scorso anno ho visitato Urbino, piccola città marchigiana patrimonio UNESCO per il suo centro rinascimentale. Attraversando le vie lastricate e salendo verso il Palazzo Ducale, ho avuto la sensazione di camminare dentro un quadro: ogni pietra sembrava raccontare il Rinascimento. Ciò che mi ha colpito di più non è stato solo la bellezza, ma il silenzio abitato — pochi turisti, studenti, artigiani. Ho capito che un sito UNESCO non è un museo chiuso, ma una comunità viva che lo mantiene. La fruizione sostenibile, ho pensato, parte dal rispetto dei ritmi di chi ci vive. Tornerei volentieri d'inverno, quando la città respira senza la pressione dell'alta stagione."""},
            {"title": "B.2 — Lettera / e-mail（三选一，80–100 词）",
             "prompt": "Scegli UNO: (a) Scrivi a un amico per consigliargli una città italiana patrimonio UNESCO da visitare. (b) Scrivi all'ufficio turistico di una località per chiedere informazioni su un percorso enogastronomico. (c) Scrivi a una rivista per segnalare un prodotto tipico da valorizzare.",
             "limit": "80–100 词",
             "reference":
"""Gentile Ufficio Turistico, vorrei informazioni su un percorso enogastronomico nella vostra zona per il prossimo mese. Siamo un gruppo di 6 persone interessate a produttori locali, cantine e degustazioni di formaggi tipici. Ci piacerebbe un itinerario lento, lontano dal turismo di massa. Potreste indicarci date, costi e se serve prenotare? Resto in attesa di un vostro gentile riscontro. Cordiali saluti, Marco Rossi."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""Il patrimonio UNESCO _____ (1) parte dal riconoscimento di un valore universale. Chi _____ (2) di conservazione spesso dimentica che un sito vive _____ (3) le persone che lo abitano. Non _____ (4) basta un decreto, _____ (5) serve una cura quotidiana. Le città _____ (6) tutelate devono rimanere _____ (7) le comunità che le abitano. Un bene _____ (8) tale valore non _____ (9) può ridurre a scenografia, _____ (10) richiede ascolto e partecipazione. Per _____ (11) motivo le amministrazioni collaborano _____ (12) gli abitanti.

L'enogastronomia _____ (13) un patrimonio culturale vivo. Un prodotto tipico _____ (14) legato al suo territorio e _____ (15) racconta una storia. Quando lo assaggi, _____ (16) anche una cultura. Per questo _____ (17) va difesa la filiera locale. La cucina _____ (18) regionale si tramanda _____ (19) generazione in generazione. Noi _____ (20) consumiamo con gusto, ma _____ (21) dobbiamo rispettare chi la produce. _____ (22) tuteliamo i produttori, il paesaggio _____ (23) resta vivo.""",
            "answers": ["fa","si occupa","con","basta","ma","da tutelare","nelle","di","si","perché","questo","con","è","è","ci","assaggi","va","regionale","di","lo","dobbiamo","Se","resta"]},
         "rewrite": [
            {"prompt": "1. Il turismo cresce. I residenti sono stanchi. I prezzi salgono.", "ref": "Sebbene il turismo cresca, i residenti sono stanchi perché i prezzi salgono."},
            {"prompt": "2. La Costiera è bella. È fragile. Servono limiti.", "ref": "La Costiera è bella ma fragile, perciò servono limiti."},
            {"prompt": "3. Il vino è buono. È locale. Racconta il territorio.", "ref": "Il vino è buono perché è locale e racconta il territorio."},
            {"prompt": "4. Abbiamo visitato Roma. Roma ha il Colosseo. È antica.", "ref": "Abbiamo visitato Roma, dove c'è il Colosseo ed è antica."},
            {"prompt": "5. Mangiamo tipico. Tuteliamo i produttori. La cultura resta viva.", "ref": "Se mangiamo tipico e tuteliamo i produttori, la cultura resta viva."},
            {"prompt": "6. Piove. La gita è confermata. Portiamo l'ombrello.", "ref": "Anche se piove, la gita è confermata: portiamo l'ombrello."},
            {"prompt": "7. Il formaggio è stagionato. Costa di più. È migliore.", "ref": "Il formaggio è stagionato: costa di più ma è migliore."},
         ],
         "wordform": [
            {"text": "1. I (paesaggio) _____ della Costiera sono unici.", "answers": ["paesaggi"]},
            {"text": "2. Questa (tradizione) _____ è molto antica.", "answers": ["tradizione"]},
            {"text": "3. Abbiamo assaggiato (olio) _____ extravergine buonissimo.", "answers": ["olio"]},
            {"text": "4. Le (città) _____ italiane attirano turisti.", "answers": ["città"]},
            {"text": "5. Il produttore (lavorare) _____ da mattina a sera.", "answers": ["lavora"]},
            {"text": "6. Noi (visitare) _____ il sito UNESCO due anni fa.", "answers": ["abbiamo visitato"]},
            {"text": "7. Una (ricetta) _____ tramandata ci lega al passato.", "answers": ["ricetta"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "D.1-1. Ravenna è patrimonio UNESCO per：", "options": ["A) il Colosseo", "B) i mosaici bizantini", "C) il vino", "D) il formaggio"], "answer": 1},
            {"type": "mc", "prompt": "D.1-2. I monumenti UNESCO a Ravenna sono：", "options": ["A) 3", "B) 8", "C) 25", "D) 400"], "answer": 1},
            {"type": "mc", "prompt": "D.1-3. Il più famoso è：", "options": ["A) San Vitale", "B) il Duomo", "C) il frantoio", "D) l'ulivo"], "answer": 0},
            {"type": "mc", "prompt": "D.1-4. I visitatori annuali sono circa：", "options": ["A) 25.000", "B) 400.000", "C) 8.000", "D) 1 milione"], "answer": 1},
            {"type": "mc", "prompt": "D.1-5. Il limite per i gruppi è：", "options": ["A) 8", "B) 25", "C) 400", "D) 12"], "answer": 1},
            {"type": "mc", "prompt": "D.1-6. La produttrice è in：", "options": ["A) Toscana", "B) Puglia", "C) Sicilia", "D) Emilia"], "answer": 1},
            {"type": "mc", "prompt": "D.1-7. Le sue piante sono：", "options": ["A) 400", "B) 3.000", "C) 25", "D) 12"], "answer": 1},
            {"type": "mc", "prompt": "D.1-8. La raccolta è a：", "options": ["A) giugno", "B) novembre", "C) marzo", "D) agosto"], "answer": 1},
            {"type": "mc", "prompt": "D.1-9. Vende a：", "options": ["A) tutta Europa", "B) qui e pochi ristoranti", "C) la grande distribuzione", "D) solo online"], "answer": 1},
            {"type": "mc", "prompt": "D.1-10. Secondo lei il turismo enogastronomico deve essere：", "options": ["A) di massa", "B) lento", "C) vietato", "D) gratis"], "answer": 1},
            {"type": "cloze", "text": "D.2-1. Partenza alle 9 da _____ (città).", "answers": ["Alba"]},
            {"type": "cloze", "text": "D.2-2. Alle 11 visita una _____ nel Barolo.", "answers": ["cantina"]},
            {"type": "cloze", "text": "D.2-3. A mezzogiorno si fa _____.", "answers": ["pranzo"]},
            {"type": "cloze", "text": "D.2-4. Alle 15 laboratorio di _____ a Bra.", "answers": ["formaggio"]},
            {"type": "cloze", "text": "D.2-5. Rientro alle _____.", "answers": ["18"]},
            {"type": "cloze", "text": "D.2-6. Costo 85 euro a _____.", "answers": ["persona"]},
            {"type": "cloze", "text": "D.2-7. I bambini sono _____.", "answers": ["gratis"]},
            {"type": "cloze", "text": "D.2-8. Prenotazione entro _____.", "answers": ["venerdì"]},
            {"type": "tf", "prompt": "D.2-9. Il percorso include il tartufo.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "D.2-10. Il costo è 50 euro.", "options": ["Vero", "Falso"], "answer": 1},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""① 描述图片并回答；② 概述短文并回答；③ 情境角色扮演。
任务：① 描述一张联合国遗产地图片（es. terrazzamenti della Costiera），并回答 "Come concili resti e turismo?"；② 用 1 分钟概述 Testo A3（fiera enogastronomica）并回答 "Perché il cibo è identità?"；③ 角色扮演：你是旅游专员（assessore turistico），以可持续旅游推广一座联合国遗产城市（limiti ai bus, filiera corta）。""",
             "points": 50,
             "rubric":
"""① 描述图片准确，能用 terrazzamenti / fragilità / fruizione 等 B2 词汇表达评判；② 能做 1 分钟 riassunto 且回答有个人立场；③ 角色扮演用 condizionale di cortesia 与语域 formal/istituzionale；④ 流利度与语法（cong.、passivo、relativo）达 B2。""",
             "dims": [
                ("Pronuncia 发音", "发音标准，语域与场合匹配"),
                ("Fluenza 流利度", "表达连贯，能展开论述与评论"),
                ("Grammatica 语法", "虚拟 / 条件 / 关系代词较准确"),
                ("Contenuto 内容", "概述完整、立场清晰，论证有逻辑"),
                ("Interazione 互动", "角色扮演语域得体，提出可持续方案"),
             ],
             "ref":
"""Nella foto vedo i terrazzamenti della Costiera Amalfitana, sospesi sul mare tra limoneti e borghi colorati: un paesaggio fragile e bellissimo. Per conciliare resti e turismo serve limitare i bus turistici e privilegiare la fruizione lenta, abitando il paesaggio. Il Testo A3 parla di una fiera enogastronomica: il cibo è identità perché ricette tramandate e sapori raccontano un modo di vivere. Come assessore turistico promuovo una città patrimonio UNESCO con turismo sostenibile: limiti ai bus, filiera corta e percorsi che valorizzano i produttori locali."""},
         ]},
    ],
})

# ============================== C1 =========================================
LEVELS.append({
    "code": "C1", "name": "CELI 4",
    "subtitle": "identità culturale / turismo sostenibile",
    "theme": "🎨 意大利文化、艺术与美食", "subj_max": 50,
    "audio": [
        {"title": "Intervista — Studiosa di turismo sostenibile", "body":
"""Il turismo sostenibile non è meno turismo, è turismo diverso. Oggi il 70% dei visitatori si concentra sul 5% del territorio italiano: Roma, Firenze, Venezia. Serve spalmare gli arrivi sull'entroterra e sulle stagioni. Tre misure: tassa di sbarco a Venezia (5 euro), prenotazione obbligatoria a siti fragili, e treni verso i borghi. Così l'identità culturale resta viva perché la abitano i residenti, non solo i selfie. La mia proposta: un bonus viaggio per chi sceglie le aree interne. Non è protezionismo, è buon senso."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo 1 — Identità culturale（saggio breve）", "body":
"""L'identità culturale non è un'essenza immobile, ma una costruzione dialogica: esiste solo nel confronto con l'altro. Quando l'Italia si racconta come "paese dell'arte e della buona tavola", cristallizza un'immagine che rassicura ma semplifica. Tale narrazione, utile per il turismo, rischia di oscurare le fratture reali: le diseguaglianze regionali, le migrazioni che da secoli ridisegnano il volto delle città, le tensioni tra memoria ufficiale e memorie sommerse. Un'identità sana non si difende chiudendosi, ma si nutre del conflitto e dell'ibridazione."""},
            {"title": "Testo 2 — Turismo sostenibile（articolo di opinione）", "body":
"""Il turismo di massa sta sfiancando le città d'arte. Venezia e Firenze non sono più abitate, sono contemplate. La cosiddetta "overtourism" trasforma gli abitanti in comparse e i quartieri in scenografie. La risposta non è vietare i visitatori, ma ridistribuirli: tasse di sbarco, prenotazione obbligatoria ai siti fragili, promozione dell'entroterra. Un turismo sostenibile misura il successo non in arrivi, ma in qualità della vita di chi resta. Altrimenti venderemo bellezza e perderemo città."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. Per il Testo 1, l'identità culturale è：", "options": ["A) un'essenza immobile", "B) una costruzione dialogica", "C) solo arte e cucina", "D) un dato biologico"], "answer": 1},
            {"type": "mc", "prompt": "2. La narrazione «paese dell'arte e della tavola» serve soprattutto：", "options": ["A) alla scuola", "B) al turismo", "C) alla politica estera", "D) agli archivi"], "answer": 1},
            {"type": "mc", "prompt": "3. Secondo il Testo 1, un'identità sana：", "options": ["A) si chiude", "B) si nutre del conflitto", "C) esclude l'altro", "D) cancella la storia"], "answer": 1},
            {"type": "mc", "prompt": "4. Il Testo 2 definisce Venezia e Firenze：", "options": ["A) abitate", "B) contemplate, non abitate", "C) in crescita", "D) vuote di turisti"], "answer": 1},
            {"type": "mc", "prompt": "5. La risposta all'overtourism per il Testo 2 è：", "options": ["A) vietare i visitatori", "B) ridistribuirli", "C) chiudere le città", "D) abbassare i prezzi"], "answer": 1},
            {"type": "mc", "prompt": "6. Il successo del turismo sostenibile si misura in：", "options": ["A) numero di arrivi", "B) qualità della vita di chi resta", "C) incassi", "D) pubblicità"], "answer": 1},
            {"type": "tf", "prompt": "7. Il Testo 1 dice che l'identità è un'essenza immobile.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "8. Il Testo 1 cita migrazioni e diseguaglianze come fratture reali.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "9. Il Testo 1 invita a chiudersi per difendere l'identità.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "10. Il Testo 2 dice che Venezia è ancora pienamente abitata.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "11. Il Testo 2 propone tasse di sbarco e prenotazione obbligatoria.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "12. Entrambi i testi criticano una visione semplificata / insostenibile.", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Compito (a) — Riassunto（摘要，80–100 词）",
             "prompt": "Sintetizza le due posizioni dei testi letti in italiano corretto (identità culturale come costruzione dialogica vs overtourism che svuota le città; turismo sostenibile come ridistribuzione dei flussi).",
             "limit": "80–100 词",
             "reference":
"""Il Testo 1 sostiene che l'identità culturale non è un'essenza fissa, ma una costruzione dialogica che rischia di essere appiattita dalla narrazione turistica "arte e tavola". Il Testo 2 denuncia l'overtourism che svuota le città d'arte, riducendo abitanti a comparse. Entrambi convengono che né l'identità né il turismo si difendono chiudendosi: serve un turismo sostenibile che ridistribuisca i flussi e tuteli chi resta. La sintesi è chiara: proteggere l'identità significa mantenere le città vive e abitate, non solo contemplate."""},
            {"title": "Compito (b) — Saggio / articolo（议论文，120–150 词）",
             "prompt": "\"Il turismo di massa distrugge l'identità culturale o la rende visibile?\" Esponi una tesi, argomenti ed esempio (tasse di sbarco, prenotazione ai siti fragili, valorizzazione dei borghi).",
             "limit": "120–150 词",
             "reference":
"""Il turismo di massa non distrugge l'identità culturale in sé, ma la rende invisibile quando la congela in una scenografia. Come nota il Testo 1, l'identità si nutre del confronto e dell'ibridazione, non della chiusura; il Testo 2 aggiunge che l'overtourism trasforma le città in musei a cielo aperto, abitati solo dai selfie. Una gestione sostenibile — tasse di sbarco, prenotazione ai siti fragili, valorizzazione dei borghi — fa respirare i centri e restituisce spazio ai residenti, che sono i veri custodi della cultura. Un esempio concreto è Venezia: ridistribuire gli arrivi sull'entroterra significa vendere bellezza senza perdere città. In conclusione, il turismo non distrugge l'identità se la fa vivere; la distrugge quando la congela."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""L'identità culturale _____ (1) un confronto costante con l'altro. Chi _____ (2) l'altro si chiude e _____ (3) la propria crescita. È _____ (4) una narrazione aperta, in cui ciascuno _____ (5) il diritto di essere ascoltato. Le città _____ (6) tutelate dai flussi turistici, _____ (7) rischiano lo spopolamento. Tuttavia, _____ (8) utili, le tasse di sbarco non _____ (9) bastare se lo Stato non _____ (10). Sarebbe necessario che il centro _____ (11) vissuto dai residenti, non solo dai visitatori. Se il patrimonio _____ (12) abbandonato, la memoria _____ (13) perduta. Per questo _____ (14) propone un patto civico: chi _____ (15) a Venezia deve _____ (16) che la città _____ (17) abitata. _____ (18) le misure fossero applicate, il turismo _____ (19) più sostenibile. Noi _____ (20) rispettare i luoghi, _____ (21) la bellezza _____ (22) un bene di tutti. Insomma, _____ (23) tuteliamo chi resta, l'identità sopravvive.""",
            "answers": ["richiede","esclude","nega","necessaria","abbia","sono","ma","benché","bastano","interviene","fosse","venisse","sarebbe","si","vive","sapere","è","Se","sarebbe","dobbiamo","perché","è","se"]},
         "rewrite": [
            {"prompt": "1. Il turismo cresce. I residenti sono stanchi. I prezzi salgono.", "ref": "Sebbene il turismo cresca, i residenti sono stanchi perché i prezzi salgono."},
            {"prompt": "2. L'overtourism svuota il centro. Gli abitanti se ne vanno. Serve un limite.", "ref": "Poiché l'overtourism svuota il centro e gli abitanti se ne vanno, serve un limite."},
            {"prompt": "3. Il vino è buono. È locale. Racconta il territorio.", "ref": "Il vino è buono perché è locale e racconta il territorio."},
            {"prompt": "4. Abbiamo visitato Roma. Roma ha il Colosseo. È antica.", "ref": "Abbiamo visitato Roma, dove c'è il Colosseo ed è antica."},
            {"prompt": "5. Mangiamo tipico. Tuteliamo i produttori. La cultura resta viva.", "ref": "Se mangiamo tipico e tuteliamo i produttori, la cultura resta viva."},
            {"prompt": "6. Piove. La gita è confermata. Portiamo l'ombrello.", "ref": "Anche se piove, la gita è confermata: portiamo l'ombrello."},
            {"prompt": "7. Il formaggio è stagionato. Costa di più. È migliore.", "ref": "Il formaggio è stagionato: costa di più ma è migliore."},
         ],
         "wordform": [
            {"text": "1. Sarebbe giusto che tutti _____ (potere) godere del patrimonio.", "answers": ["potesse"]},
            {"text": "2. Senza regole, il centro storico _____ (svuotarsi, condizionale).", "answers": ["si svuoterebbe"]},
            {"text": "3. Le città _____ (tutelare, passivo) dalla legge sul paesaggio.", "answers": ["sono tutelate"]},
            {"text": "4. È lo Stato _____ (che / cui / a cui) promuove la cultura.", "answers": ["che"]},
            {"text": "5. _____ (Malgrado / Malgrado che) i costi, investiamo nei borghi.", "answers": ["Malgrado"]},
            {"text": "6. Preferisco che tu _____ (venire) a vivere qui.", "answers": ["venga"]},
            {"text": "7. Se il comune _____ (approvare) il piano, i siti fragili _____ (essere, condizionale) protetti.", "answers": ["approvasse","sarebbero protetti"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "cloze", "text": "Tabella 1. Il _____ % dei visitatori si concentra sul 5% del territorio.", "answers": ["70%"]},
            {"type": "cloze", "text": "Tabella 2. Città con tassa di sbarco: _____.", "answers": ["Venezia"]},
            {"type": "cloze", "text": "Tabella 3. Importo della tassa: _____.", "answers": ["5 euro"]},
            {"type": "cloze", "text": "Tabella 4. Proposta finale: bonus viaggio per le _____.", "answers": ["aree interne"]},
            {"type": "tf", "prompt": "5. La studiosa dice che il turismo sostenibile è meno turismo.", "options": ["Vero", "Falso"], "answer": 1},
            {"type": "tf", "prompt": "6. Roma, Firenze e Venezia attirano la maggior parte dei visitatori.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "7. La prenotazione obbligatoria riguarda i siti fragili.", "options": ["Vero", "Falso"], "answer": 0},
            {"type": "tf", "prompt": "8. Il bonus viaggio è per chi sceglie le aree interne.", "options": ["Vero", "Falso"], "answer": 0},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""带材料面试（长篇论述 + 深度讨论）。
Materiale: i due testi letti (identità culturale / overtourism).
Task：① Esponi la tua posizione in 2–3 minuti: "Il turismo di massa distrugge l'identità culturale o la rende visibile?"；② Discussione con l'esaminatore: rispondi a obiezioni (es. "ma il turismo dà lavoro") e proponi una misura concreta。""",
             "points": 50,
             "rubric":
"""① 论述结构清晰（tesi → argomenti → esempio），语域 formal / argomentativo；② 熟练使用 congiuntivo, condizionale, passivo, relativo；词汇精准（ibridazione, overtourism, fruizione）；③ 讨论中回应质疑并给具体措施（tassa, prenotazione）；④ 发音流利。""",
             "dims": [
                ("Pronuncia 发音", "发音精准，语调节奏自如"),
                ("Fluenza 流利度", "长篇论述流畅，衔接自然"),
                ("Grammatica 语法", "虚拟 / 条件 / 被动准确，句式丰富"),
                ("Contenuto 内容", "立场明确，词汇丰富（ibridazione, overtourism, fruizione）"),
                ("Interazione 互动", "深度讨论中回应质疑，逻辑自洽"),
             ],
             "ref":
"""La mia posizione è che il turismo di massa non distrugge l'identità culturale in sé, ma la rende invisibile quando la congela in una scenografia. Come dice il Testo 1, l'identità si nutre del confronto e dell'ibridazione, non della chiusura; il Testo 2 aggiunge che l'overtourism riduce gli abitanti a comparse. Una misura concreta? Tasse di sbarco, prenotazione ai siti fragili e valorizzazione dei borghi: così la città resta viva perché la abitano i residenti. A chi obietta che il turismo dà lavoro, rispondo: sì, ma un lavoro che non svuoti la città, bensì la faccia respirare."""},
         ]},
    ],
})

# ============================== C2 =========================================
LEVELS.append({
    "code": "C2", "name": "CELI 5",
    "subtitle": "cultura e potere / memoria collettiva",
    "theme": "🎨 意大利文化、艺术与美食", "subj_max": 50,
    "audio": [
        {"title": "Dibattito — Cultura, potere e memoria", "body":
"""Cara collega, lei sostiene che rimuovere una statua sia cancel culture; io replico: ogni intitolazione è già una cancellazione, quella dei vinti. Il potere non sta nel marmo, sta nel diritto di decidere cosa commemorare. Se una piazza onora un gerarca, non è "tradizione", è amnesia comoda. La soluzione non è abbattere alla cieca, ma contestualizzare: targhe, percorsi critici, musealizzazione. Altrimenti sostituiamo un silenzio con un altro. La memoria onesta è faticosa; la nostra, purtroppo, preferisce i monumenti comodi."""},
    ],
    "sections": [
        {"kind": "reading", "title": "1. Comprensione di testi scritti（阅读）",
         "texts": [
            {"title": "Testo — Saggio letterario（cultura e potere / memoria collettiva）", "body":
"""Ogni monumento è una vittoria rimasta in piedi dopo che i vinti hanno smesso di contare. La città italiana è un palinsesto di poteri: il foro romano che silenzia le capanne, il duomo che sovrascrive il tempio, il fascio littorio scrostato sotto l'intonaco di una casa del dopoguerra. La memoria collettiva non è la somma onesta del passato, ma una censura che chiamiamo tradizione. Chi governa decide che cosa resta visibile e che cosa affonda nel silenzio. Eppure, la pietra ha la memoria lunga: basta un restauro, una sbiancatura, perché riaffiori ciò che si voleva seppellire. La cultura, si sa, obbedisce a chi paga i restauri; ma la storia, quella vera, abita nelle crepe."""},
         ],
         "items": [
            {"type": "mc", "prompt": "1. «Monumento è una vittoria rimasta in piedi» significa che i monumenti：", "options": ["A) celebrano i vinti", "B) celebrano i vincitori e cancellano i vinti", "C) sono neutri", "D) sono caduchi"], "answer": 1},
            {"type": "mc", "prompt": "2. «Palinsesto di poteri» indica che la città：", "options": ["A) è nuova", "B) sovrappone strati di potere nel tempo", "C) è povera", "D) è uniforme"], "answer": 1},
            {"type": "mc", "prompt": "3. Il «fascio littorio scrostato» evoca：", "options": ["A) l'età romana", "B) il regime fascista rimosso", "C) il Medioevo", "D) il Rinascimento"], "answer": 1},
            {"type": "mc", "prompt": "4. Per l'autore la memoria collettiva è：", "options": ["A) onesta", "B) una censura chiamata tradizione", "C) completa", "D) scientifica"], "answer": 1},
            {"type": "mc", "prompt": "5. Chi decide che cosa resta visibile?", "options": ["A) gli architetti", "B) chi governa", "C) i turisti", "D) i vinti"], "answer": 1},
            {"type": "mc", "prompt": "6. La «pietra ha la memoria lunga» suggerisce che：", "options": ["A) la pietra non dimentica", "B) i restauri rivelano il nascosto", "C) è dura", "D) è antica"], "answer": 1},
            {"type": "mc", "prompt": "7. Tono del brano：", "options": ["A) celebrativo", "B) ironico e critico", "C) neutro", "D) pubblicitario"], "answer": 1},
            {"type": "mc", "prompt": "8. La «storia vera» abita：", "options": ["A) nei musei ufficiali", "B) nelle crepe / nel nascosto", "C) nei libri di scuola", "D) nei monumenti"], "answer": 1},
         ]},
        {"kind": "writing", "title": "2. Produzione di testi scritti（写作）",
         "tasks": [
            {"title": "Task A — Saggio（论文，约 180 词）",
             "prompt": "\"La memoria collettiva è uno strumento di potere: chi controlla i monumenti e i racconti controlla l'identità di un popolo.\" Sviluppa una tesi argomentata, con esempi storici o contemporanei italiani.",
             "limit": "约 180 词",
             "reference":
"""La tesi che la memoria collettiva sia uno strumento di potere non è retorica, è architettura. Chi innalza un monumento decide non solo che cosa celebrare, ma che cosa dimenticare: il foro che cancella le capanne, il duomo che ricopre il tempio, l'intonaco postbellico che seppellisce il fascio. La Rimini di Fellini e l'Italia repubblicana hanno edificato un racconto di "ricostruzione" che spesso ammutolisce le fratture del Ventennio. Allo stesso modo, l'epurazione dei nomi nelle piazze non cancella la storia, ne riscrive la gerarchia. Il potere, oggi, non alza colonne: compra restauri, finanzia mostre, orienta i curricoli scolastici. Dunque controllare i monumenti e i racconti significa davvero controllare l'identità di un popolo — finché qualcuno non legge le crepe. La vera sovranità democratica sta nel renderle leggibili."""},
            {"title": "Task B — Nota di policy（政策建议，约 80 词）",
             "prompt": "Scrivi una nota di policy per un'amministrazione comunale: come rendere più onesta la memoria di una piazza intitolata a una figura contestata (3 misure concrete).",
             "limit": "约 80 词",
             "reference":
"""Nota per l'Amministrazione — tre misure per una memoria onesta di piazze contestate: 1) Affiancare al nome esistente una targa esplicativa con il contesto storico e le vittime; 2) Istituire un percorso critico cittadino (musealizzazione diffusa) che colleghi i luoghi; 3) Aprire una consultazione pubblica con storici e cittadini prima di ogni modifica, evitando sia l'abbattimento cieco sia l'amnesia. La trasparenza, non la cancellazione, tutela la storia."""},
         ]},
        {"kind": "linguistic", "title": "3. Competenza linguistica（语言能力）",
         "cloze": {"cloze_text":
"""Non _____ (1) saputo, non sarei intervenuto. Pur _____ (2) il valore del monumento, ne criticai l'uso politico. La memoria _____ (3) si fa riferimento è selettiva e, _____ (4) il consiglio deliberasse, i nomi cambierebbero. Non solo cancellarono il passato, ma _____ (5) negano il presente. _____ (6) la pietra silenzi, essa rivela. È il potere _____ (7) detta la narrazione ufficiale; avrebbe dovuto _____ (8) più trasparente. Tanto più la storia è rimossa, _____ (9) riaffiora ciò _____ (10) non si dice. Qualora _____ (11) la legge, muterebbe l'identità collettiva. _____ (12) il regime fosse caduto, altro racconto _____ (13) sorto. Sono fiero _____ (14) questa città che resiste: i suoi monumenti _____ (15) stessi parlano a chi sa ascoltare. Pensavo _____ (16) fosse una memoria condivisa, _____ (17) il restauro rivelò ciò che si celava. Ne discuteremo _____ (18) il consiglio, tema _____ (19) di cui ci si tace volentieri. Chi _____ (20) governa decide che cosa resta; _____ (21) tale silenzio subentra _____ (22) un'altra rimozione. Insomma, la memoria onesta è _____ (23) sì faticosa, ma necessaria.""",
            "answers": ["avessi","riconoscendo","cui","qualora","negano anche","Sebbene","che","essere","tanto più","che","mutasse","Se","sarebbe","di","stessi","ci","mentre","con","di cui","ci","A","a","sì"]},
         "rewrite": [
            {"prompt": "1. Il potere detta la narrazione. La memoria è selettiva. I vinti tacciono.", "ref": "Poiché il potere detta la narrazione e la memoria è selettiva, i vinti tacciono."},
            {"prompt": "2. Il monumento celebra un gerarca. Non è tradizione. È amnesia comoda.", "ref": "Il monumento che celebra un gerarca non è tradizione, bensì amnesia comoda."},
            {"prompt": "3. Rimuoviamo la statua. Non cancelliamo la storia. Ne riscriviamo la gerarchia.", "ref": "Anche se rimuoviamo la statua, non cancelliamo la storia: ne riscriviamo la gerarchia."},
            {"prompt": "4. Il consiglio delibera. I nomi cambiano. La piazza parla d'altro.", "ref": "Se il consiglio delibera, i nomi cambiano e la piazza parla d'altro."},
            {"prompt": "5. La pietra è silenziosa. Rivela comunque. Chi sa ascoltare comprende.", "ref": "Benché la pietra sia silenziosa, rivela comunque a chi sa ascoltare."},
            {"prompt": "6. Contestualizziamo il monumento. Aggiungiamo una targa. La storia resta leggibile.", "ref": "Se contestualizziamo il monumento e vi aggiungiamo una targa, la storia resta leggibile."},
            {"prompt": "7. Il turismo pesa su Venezia. Gli abitanti se ne vanno. Serve una misura concreta.", "ref": "Poiché il turismo pesa su Venezia e gli abitanti se ne vanno, serve una misura concreta."},
         ],
         "wordform": [
            {"text": "1. Da _memoria_ → aggettivo: _____（memorabile / memore / memoria）", "answers": ["memore"]},
            {"text": "2. «Cancellare dalla _____» (collocazione): A) carta　B) memoria　C) pietra", "answers": ["memoria"]},
            {"text": "3. Registro adatto a un saggio accademico: A) figo　B) presupposto　C) bello", "answers": ["presupposto"]},
            {"text": "4. Sinonimo formale di «nascondere» in contesto storico: A) celare　B) mettere via　C) coprire", "answers": ["celare"]},
            {"text": "5. Da _potere_ → sostantivo astratto: _____（potenza / potentato）", "answers": ["potenza"]},
            {"text": "6. «Dettare la _____» (collocazione con _narrazione_): A) legge　B) voce　C) pietra", "answers": ["legge"]},
            {"text": "7. Se il regime _____（cadere, imperf. cong.）, altro racconto sarebbe sorto.", "answers": ["cadesse"]},
            {"text": "8. Pensavo _____（ci / ne / vi）fosse una memoria condivisa, finché il restauro _____（rivelare, pass. rem.）ciò che si celava.", "answers": ["ci","rivelò"]},
         ]},
        {"kind": "listening", "title": "4. Comprensione di testi orali（听力）",
         "items": [
            {"type": "mc", "prompt": "1. La collega A sostiene che rimuovere la statua è：", "options": ["A) giusto", "B) cancel culture", "C) inutile", "D) legge"], "answer": 1},
            {"type": "mc", "prompt": "2. Per l'interlocutore, ogni intitolazione è：", "options": ["A) neutrale", "B) già una cancellazione dei vinti", "C) una vittoria", "D) un errore"], "answer": 1},
            {"type": "mc", "prompt": "3. Il potere sta, secondo lui：", "options": ["A) nel marmo", "B) nel diritto di decidere cosa commemorare", "C) nei turisti", "D) nel denaro"], "answer": 1},
            {"type": "mc", "prompt": "4. Una piazza che onora un gerarca è, per lui：", "options": ["A) tradizione", "B) amnesia comoda", "C) storia", "D) arte"], "answer": 1},
            {"type": "mc", "prompt": "5. La sua soluzione è：", "options": ["A) abbattere tutto", "B) contestualizzare (targhe, percorsi)", "C) ignorare", "D) vietare"], "answer": 1},
            {"type": "mc", "prompt": "6. Sostituiremmo, dice, un silenzio con：", "options": ["A) un libro", "B) un altro silenzio", "C) una statua", "D) una legge"], "answer": 1},
            {"type": "mc", "prompt": "7. Tono dell'intervento：", "options": ["A) celebrativo", "B) polemico / critico", "C) neutrale", "D) pubblicitario"], "answer": 1},
            {"type": "mc", "prompt": "8. La «memoria onesta» è definita：", "options": ["A) facile", "B) faticosa", "C) inutile", "D) comoda"], "answer": 1},
         ]},
        {"kind": "oral", "title": "5. Prova orale（口语）",
         "tasks": [
            {"desc":
"""抽象话题（哲学 / 艺术 / 社会伦理）演讲 + 批判性质疑回应。
Tema: "Il potere di costruire (o abbattere) un monumento è il potere di riscrivere chi siamo."
Task：① Tieni un discorso di 3–4 minuti di tono saggistico；② L'esaminatore ti pone obiezioni (es. "ma la storia è storia, non si cancella"); tu rispondi con argomentazione critica e una proposta (es. musealizzazione contestuale)。""",
             "points": 50,
             "rubric":
"""① 演讲具 saggistica / 哲思语域，善用 metafora, antitesi（palinsesto, censura, monumenti comodi）；② 句法复杂且准确（periodare, congiuntivo, passivo, incisi）；词汇高级（palinsesto, sovranità, epurazione）；③ 承接质疑并以 rigorosa argomentazione 反驳；④ 发音地道、节奏自如。""",
             "dims": [
                ("Pronuncia 发音", "发音精准，学术语域自如"),
                ("Fluenza 流利度", "演讲连贯，抽象概念流转自然"),
                ("Grammatica 语法", "复杂句法准确（虚拟 / 条件 / 被动 / 关系）"),
                ("Contenuto 内容", "抽象概念清晰，词汇精准（palinsesto, sovranità, epurazione）"),
                ("Pensiero critico 思辨", "批判性回应质疑，逻辑自洽有深度"),
             ],
             "ref":
"""Il potere di costruire o abbattere un monumento è il potere di riscrivere chi siamo, perché ogni intitolazione è già una scelta su che cosa commemorare e che cosa dimenticare. La città è un palinsesto di poteri: il foro che cancella le capanne, il duomo che copre il tempio. Non cancello la storia abbattendo una statua, ne riscrivo la gerarchia: la soluzione è contestualizzare, con targhe e percorsi critici, non l'amnesia cieca. La memoria onesta è faticosa, ma necessaria: rendere leggibili le crepe, non sostituire un silenzio con un altro. Il potere, oggi, non alza colonne: compra restauri e orienta i racconti; dunque controllare i monumenti significa davvero controllare l'identità di un popolo."""},
         ]},
    ],
})
